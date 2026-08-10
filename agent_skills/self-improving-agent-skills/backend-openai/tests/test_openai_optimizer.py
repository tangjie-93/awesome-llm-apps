import asyncio
import os
import sys
import unittest
from types import SimpleNamespace


BACKEND_DIR = os.path.dirname(os.path.dirname(__file__))
if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from openai_optimizer import OpenAISkillOptimizer


class FakeResponses:
    def __init__(self, outputs):
        self.outputs = list(outputs)
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if not self.outputs:
            raise AssertionError("No fake OpenAI responses left")
        return SimpleNamespace(output_text=self.outputs.pop(0))


class FakeClient:
    def __init__(self, outputs):
        self.responses = FakeResponses(outputs)


class OpenAIOptimizerTests(unittest.IsolatedAsyncioTestCase):
    async def test_analyze_skill_extracts_json_from_fenced_response(self):
        client = FakeClient([
            """Here is the config:
```json
{
  "scenarios": [
    {"id": 1, "name": "Use skill", "description": "Use skill", "input": "Run it"}
  ],
  "evals": [
    {
      "id": 1,
      "name": "Useful",
      "criterion": "Useful",
      "question": "Is it useful?",
      "pass_condition": "yes",
      "fail_condition": "no"
    }
  ]
}
```"""
        ])
        optimizer = OpenAISkillOptimizer(api_key="test-key", client=client)

        result = await optimizer.analyze_skill({"SKILL.md": "# Skill\nDo work"})

        self.assertEqual(result["scenarios"][0]["input"], "Run it")
        self.assertEqual(result["evals"][0]["question"], "Is it useful?")
        self.assertEqual(client.responses.calls[0]["model"], "gpt-5-mini")

    async def test_optimize_keeps_mutation_when_score_improves(self):
        client = FakeClient([
            "baseline execution",
            '{"results": [{"eval_id": 1, "passed": false, "reason": "missing detail"}]}',
            '{"diagnosis": "The skill is vague", "mutation_strategy": "add_example", "target_section": "Usage", "suggested_change": "Add an example"}',
            '{"description": "Added example", "reasoning": "Examples reduce ambiguity", "new_skill_md": "# Skill\\nUse this example."}',
            "improved execution",
            '{"results": [{"eval_id": 1, "passed": true, "reason": "clear"}]}',
        ])
        optimizer = OpenAISkillOptimizer(api_key="test-key", client=client)
        events = []

        async def callback(event):
            events.append(event)

        result = await optimizer.optimize(
            skill_files={"SKILL.md": "# Skill\nUse it."},
            scenarios=[{"id": 1, "input": "Help me"}],
            evals=[{"id": 1, "question": "Is the output clear?"}],
            max_rounds=1,
            callback=callback,
        )

        self.assertEqual(result["baseline_score"], 0.0)
        self.assertEqual(result["final_score"], 100.0)
        self.assertEqual(result["improved_skill_md"], "# Skill\nUse this example.")
        self.assertTrue(result["mutation_log"][0]["kept"])
        self.assertEqual([event["type"] for event in events], ["baseline", "experiment_start", "experiment_result", "complete"])

    async def test_optimize_discards_mutation_when_score_drops(self):
        client = FakeClient([
            "baseline execution",
            '{"results": [{"eval_id": 1, "passed": true, "reason": "clear"}]}',
            '{"diagnosis": "No real failure", "mutation_strategy": "restructure", "target_section": "Body", "suggested_change": "Rewrite"}',
            '{"description": "Rewrote body", "reasoning": "Attempted simplification", "new_skill_md": "# Skill\\nDifferent."}',
            "worse execution",
            '{"results": [{"eval_id": 1, "passed": false, "reason": "unclear"}]}',
        ])
        optimizer = OpenAISkillOptimizer(api_key="test-key", client=client)

        result = await optimizer.optimize(
            skill_files={"SKILL.md": "# Skill\nOriginal."},
            scenarios=[{"id": 1, "input": "Help me"}],
            evals=[{"id": 1, "question": "Is the output clear?"}],
            max_rounds=1,
        )

        self.assertEqual(result["baseline_score"], 100.0)
        self.assertEqual(result["final_score"], 100.0)
        self.assertEqual(result["improved_skill_md"], "# Skill\nOriginal.")
        self.assertFalse(result["mutation_log"][0]["kept"])


if __name__ == "__main__":
    unittest.main()
