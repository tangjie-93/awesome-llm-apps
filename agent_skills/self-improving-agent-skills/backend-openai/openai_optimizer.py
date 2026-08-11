import asyncio
import json
from typing import Callable, Optional


DEFAULT_MODEL = "gpt-5-mini"


class OpenAISkillOptimizer:
    """基于 OpenAI Responses API 的 Agent Skill 自动分析、评测与优化器。"""

    def __init__(self, api_key: str, model: str = DEFAULT_MODEL, client=None):
        """初始化优化器，并在未传入客户端时创建默认 OpenAI 客户端。"""
        self.api_key = api_key
        self.model = model or DEFAULT_MODEL
        self.client = client or self._create_client(api_key)

    def _create_client(self, api_key: str):
        """使用指定 API Key 创建 OpenAI 同步客户端。"""
        from openai import OpenAI

        return OpenAI(api_key=api_key)

    async def _ask(self, prompt: str) -> str:
        """异步调用模型并返回响应文本。"""
        # OpenAI Python SDK 是同步调用，这里放到线程中避免阻塞事件循环。
        response = await asyncio.to_thread(
            self.client.responses.create,
            model=self.model,
            input=prompt,
        )
        return self._response_text(response)

    def _response_text(self, response) -> str:
        """从 Responses API 返回对象中提取纯文本内容。"""
        if hasattr(response, "output_text") and response.output_text:
            return response.output_text

        # 兼容没有 output_text 快捷字段的响应结构，逐层收集 content.text。
        chunks = []
        for item in getattr(response, "output", []) or []:
            for content in getattr(item, "content", []) or []:
                text = getattr(content, "text", None)
                if text:
                    chunks.append(text)
        return "\n".join(chunks)

    def _parse_json_text(self, text: str, fallback=None):
        """从模型输出中解析 JSON，支持去除 Markdown 代码块包裹。"""
        cleaned = text.strip()
        if cleaned.startswith("```"):
            # 模型有时会用 ```json 包裹结果，解析前先剥离代码围栏。
            lines = cleaned.splitlines()
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            cleaned = "\n".join(lines).strip()

        decoder = json.JSONDecoder()
        # 找到第一个 JSON 对象或数组的起始位置，容忍前面混入少量说明文字。
        candidates = [idx for idx in (cleaned.find("{"), cleaned.find("[")) if idx != -1]
        if not candidates:
            if fallback is not None:
                return fallback
            raise json.JSONDecodeError("No JSON object found", cleaned, 0)

        start = min(candidates)
        try:
            result, _ = decoder.raw_decode(cleaned, start)
            return result
        except json.JSONDecodeError:
            if fallback is not None:
                return fallback
            raise

    async def _ask_json(self, prompt: str, fallback=None):
        """调用模型并将返回内容解析成 JSON，失败时可返回 fallback。"""
        text = await self._ask(prompt)
        return self._parse_json_text(text, fallback=fallback)

    async def analyze_skill(self, skill_files: dict) -> dict:
        """分析 Skill 文件并生成测试场景与二元评测标准。"""
        skill_md = next((v for k, v in skill_files.items() if k.endswith("SKILL.md")), "")
        refs = {k: v for k, v in skill_files.items() if "references/" in k}
        ref_text = ""
        if refs:
            # 将 references/ 下的辅助文件拼入提示词，帮助模型理解完整技能上下文。
            ref_text = "\n\nReference files:\n" + "\n---\n".join(
                f"## {k}\n{v}" for k, v in refs.items()
            )

        prompt = (
            "Analyze this agent skill and generate test scenarios with evaluation criteria.\n\n"
            f"# SKILL.md\n{skill_md}\n{ref_text}\n\n"
            "Generate exactly this JSON shape and no prose:\n"
            "{"
            '"scenarios": [{"id": 1, "name": "short name", "description": "short name", "input": "the user request to test"}], '
            '"evals": [{"id": 1, "name": "what to check", "criterion": "what to check", '
            '"question": "yes/no question about the output", "pass_condition": "what yes looks like", '
            '"fail_condition": "what no looks like"}]'
            "}\n"
            "Create 3-4 diverse realistic scenarios and 4-6 binary evaluation criteria."
        )
        result = await self._ask_json(prompt, fallback={"scenarios": [], "evals": []})
        return {
            "scenarios": result.get("scenarios", []),
            "evals": result.get("evals", []),
        }

    async def optimize(
        self,
        skill_files: dict,
        scenarios: list,
        evals: list,
        max_rounds: int = 5,
        callback: Optional[Callable] = None,
    ) -> dict:
        """按评测结果迭代优化 Skill，并返回最佳版本和优化过程记录。"""
        async def emit(event):
            """向外部回调发送优化进度事件。"""
            if callback:
                await callback(event)

        current_md = next((v for k, v in skill_files.items() if k.endswith("SKILL.md")), "")
        # 先评估原始版本，后续每轮优化都与当前最佳基线比较。
        baseline = await self._score_skill(current_md, scenarios, evals)
        baseline_pct = self._pct(baseline["passed"], baseline["total"])
        score_history = [baseline_pct]
        mutation_log = []

        await emit({
            "type": "baseline",
            "data": {
                "score": baseline_pct,
                "passed": baseline["passed"],
                "total": baseline["total"],
                "per_eval": baseline["per_eval"],
            },
        })

        for rnd in range(1, max_rounds + 1):
            await emit({"type": "experiment_start", "data": {"round": rnd}})

            # 基于失败详情生成诊断，再让模型提出一个针对性的 Skill 修改。
            analysis = await self._analyze_failures(current_md, scenarios, evals, baseline["details"])
            mutation = await self._mutate_skill(current_md, analysis)
            new_md = mutation.get("new_skill_md") or current_md

            result = await self._score_skill(new_md, scenarios, evals)
            new_pct = self._pct(result["passed"], result["total"])
            # 只保留分数严格提升的变更，避免劣化或无效修改覆盖当前最佳版本。
            kept = new_pct > baseline_pct

            entry = {
                "round": rnd,
                "strategy_type": analysis.get("mutation_strategy", "unknown"),
                "diagnosis": analysis.get("diagnosis", ""),
                "description": mutation.get("description", ""),
                "score_before": baseline_pct,
                "score_after": new_pct,
                "kept": kept,
            }
            mutation_log.append(entry)

            if kept:
                current_md = new_md
                baseline = result
                baseline_pct = new_pct

            score_history.append(baseline_pct)

            await emit({
                "type": "experiment_result",
                "data": {
                    "round": rnd,
                    "score": new_pct,
                    "kept": kept,
                    "status": "kept" if kept else "discarded",
                    "description": mutation.get("description", ""),
                    "strategy": analysis.get("mutation_strategy", ""),
                    "per_eval": result["per_eval"],
                },
            })

        final = {
            "baseline_score": score_history[0],
            "final_score": baseline_pct,
            "improved_skill_md": current_md,
            "score_history": score_history,
            "mutation_log": mutation_log,
            "strategy_stats": self._strategy_stats(mutation_log),
        }
        await emit({"type": "complete", "data": final})
        return final

    async def _score_skill(self, skill_md: str, scenarios: list, evals: list) -> dict:
        """针对一组场景和评测项计算 Skill 的通过率与明细。"""
        total_passed = 0
        total_checks = 0
        per_eval = {e["id"]: {"eval_id": e["id"], "passed": 0, "total": 0, "pass_rate": 0} for e in evals}
        details = []

        for scenario in scenarios:
            # 先模拟用户请求执行 Skill，得到待评测的用户可见输出。
            output = await self._ask(
                "Execute this skill. Follow the instructions exactly and produce only the user-facing output.\n\n"
                f"# SKILL.md\n{skill_md}\n\n"
                f"User request:\n{scenario.get('input', '')}"
            )
            # 再让模型按二元标准打分，统一解析成 results 列表。
            scoring = await self._ask_json(
                "Evaluate this output against the criteria. Return JSON only in this shape: "
                '{"results": [{"eval_id": 1, "passed": true, "reason": "..."}]}\n\n'
                f"Input: {scenario.get('input', '')}\n\n"
                f"Output: {output}\n\n"
                f"Criteria:\n{json.dumps(evals, ensure_ascii=False, indent=2)}",
                fallback={"results": []},
            )
            scores = scoring.get("results", []) if isinstance(scoring, dict) else scoring
            by_eval = {score.get("eval_id"): score for score in scores if isinstance(score, dict)}

            scenario_results = []
            for eval_item in evals:
                eval_id = eval_item["id"]
                # 缺失评分按失败处理，避免模型漏打分导致通过率虚高。
                score = by_eval.get(eval_id, {"eval_id": eval_id, "passed": False, "reason": "Missing score"})
                passed = bool(score.get("passed", False))
                total_checks += 1
                per_eval[eval_id]["total"] += 1
                if passed:
                    total_passed += 1
                    per_eval[eval_id]["passed"] += 1
                scenario_results.append(score)

            details.append({
                "scenario": scenario,
                "output": output,
                "results": scenario_results,
            })

        for stats in per_eval.values():
            stats["pass_rate"] = self._pct(stats["passed"], stats["total"])

        return {
            "passed": total_passed,
            "total": total_checks,
            "per_eval": list(per_eval.values()),
            "details": details,
        }

    async def _analyze_failures(self, skill_md: str, scenarios: list, evals: list, details: list) -> dict:
        """根据评测失败详情诊断问题，并给出下一轮变更策略。"""
        return await self._ask_json(
            "Diagnose why this skill failed its evals. Return JSON only with keys "
            "diagnosis, mutation_strategy, target_section, suggested_change. "
            "mutation_strategy must be one of add_example, add_constraint, restructure, add_edge_case.\n\n"
            f"# SKILL.md\n{skill_md}\n\n"
            f"Scenarios:\n{json.dumps(scenarios, ensure_ascii=False, indent=2)}\n\n"
            f"Evals:\n{json.dumps(evals, ensure_ascii=False, indent=2)}\n\n"
            f"Results:\n{json.dumps(details, ensure_ascii=False, indent=2)}",
            fallback={
                "diagnosis": "Unable to diagnose automatically",
                "mutation_strategy": "add_constraint",
                "target_section": "Instructions",
                "suggested_change": "Clarify the expected behavior",
            },
        )

    async def _mutate_skill(self, skill_md: str, analysis: dict) -> dict:
        """根据诊断结果生成一个新的 Skill Markdown 版本。"""
        return await self._ask_json(
            "Edit this agent skill. Make exactly one targeted change based on the diagnosis. "
            "Keep YAML frontmatter valid and return JSON only with keys description, reasoning, new_skill_md.\n\n"
            f"Diagnosis:\n{json.dumps(analysis, ensure_ascii=False, indent=2)}\n\n"
            f"# Current SKILL.md\n{skill_md}",
            fallback={
                "description": "No change generated",
                "reasoning": "The model did not return a usable mutation",
                "new_skill_md": skill_md,
            },
        )

    def _strategy_stats(self, mutation_log: list) -> dict:
        """统计各类变更策略的尝试次数和被保留次数。"""
        stats = {}
        for mutation in mutation_log:
            strategy = mutation.get("strategy_type", "unknown")
            current = stats.setdefault(strategy, {"attempted": 0, "kept": 0})
            current["attempted"] += 1
            if mutation.get("kept"):
                current["kept"] += 1
        return stats

    def _pct(self, passed: int, total: int) -> float:
        """计算通过率百分比，total 为 0 时按 1 兜底避免除零。"""
        return round(100 * passed / max(total, 1), 1)
