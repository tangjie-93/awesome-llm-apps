# OpenAI Self-Improving Backend Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an OpenAI-powered implementation of the self-improving agent skills backend and let the existing frontend switch between Gemini and OpenAI.

**Architecture:** Create a sibling `backend-openai/` FastAPI service that preserves the existing API contract while replacing Google ADK agents with OpenAI Responses API calls. Update frontend state to carry `provider`, `apiKey`, and `model`, and route requests to either the original Gemini backend or the new OpenAI backend without deleting existing Gemini code.

**Tech Stack:** Python 3.10+, FastAPI, Pydantic, OpenAI Python SDK, Next.js, React, TypeScript.

---

### Task 1: OpenAI Optimizer Core

**Files:**
- Create: `agent_skills/self-improving-agent-skills/backend-openai/openai_optimizer.py`
- Create: `agent_skills/self-improving-agent-skills/backend-openai/tests/test_openai_optimizer.py`
- Create: `agent_skills/self-improving-agent-skills/backend-openai/requirements.txt`

- [ ] **Step 1: Write failing tests**

Create tests that insert `backend-openai/` into `sys.path`, inject a fake OpenAI client, and verify JSON extraction, scenario generation, scoring, mutation acceptance, and mutation rejection.

- [ ] **Step 2: Verify RED**

Run: `python3 -m unittest discover agent_skills/self-improving-agent-skills/backend-openai/tests -v`

Expected: import failure because `openai_optimizer.py` does not exist.

- [ ] **Step 3: Implement optimizer**

Implement `OpenAISkillOptimizer` with async methods matching the existing `SkillOptimizer` shape:

- `analyze_skill(skill_files) -> {"scenarios": [...], "evals": [...]}`
- `optimize(skill_files, scenarios, evals, max_rounds, callback) -> final result`
- `_score_skill`, `_analyze_failures`, `_mutate_skill`

Use `client.responses.create(model=model, input=prompt)` through `asyncio.to_thread(...)`, parse `response.output_text`, and accept injected fake clients for tests.

- [ ] **Step 4: Verify GREEN**

Run: `python3 -m unittest discover agent_skills/self-improving-agent-skills/backend-openai/tests -v`

Expected: optimizer tests pass.

### Task 2: OpenAI FastAPI Compatibility Service

**Files:**
- Create: `agent_skills/self-improving-agent-skills/backend-openai/app.py`
- Create: `agent_skills/self-improving-agent-skills/backend-openai/tests/test_app_contract.py`

- [ ] **Step 1: Write failing API contract tests**

Test `create_session_from_files`, `/health`, `/api/update-config`, `/api/status/{session_id}`, and request parsing for both `api_key` and legacy `gemini_api_key` fields.

- [ ] **Step 2: Verify RED**

Run: `python3 -m unittest discover agent_skills/self-improving-agent-skills/backend-openai/tests -v`

Expected: API tests fail because `app.py` does not exist.

- [ ] **Step 3: Implement FastAPI service**

Port safe upload/session/download/example/status behavior from the original backend. Replace `SkillOptimizer` with `OpenAISkillOptimizer`. Use request models that accept:

- `api_key`
- `openai_api_key`
- legacy `gemini_api_key`
- `model`, defaulting to `gpt-5-mini`

Serve OpenAI backend on port `8892` in `if __name__ == "__main__"`.

- [ ] **Step 4: Verify GREEN**

Run: `python3 -m unittest discover agent_skills/self-improving-agent-skills/backend-openai/tests -v`

Expected: all backend-openai tests pass.

### Task 3: Frontend Provider Switching

**Files:**
- Modify: `agent_skills/self-improving-agent-skills/frontend/src/app/page.tsx`
- Modify: `agent_skills/self-improving-agent-skills/frontend/src/components/UploadStep.tsx`
- Modify: `agent_skills/self-improving-agent-skills/frontend/src/components/ConfigStep.tsx`
- Modify: `agent_skills/self-improving-agent-skills/frontend/src/components/RunningStep.tsx`

- [ ] **Step 1: Write type/build failure check**

Run: `cd agent_skills/self-improving-agent-skills/frontend && npm run build`

Expected before changes: establishes baseline; if dependencies are missing, run `npm install` only if required.

- [ ] **Step 2: Implement provider state**

Add `provider: "openai" | "gemini"` and `model` state in `page.tsx`, pass them through step components, and store them from `UploadStep`.

- [ ] **Step 3: Update upload/config/running requests**

Add helper logic in frontend components:

- Gemini API base: `NEXT_PUBLIC_GEMINI_API_URL || NEXT_PUBLIC_API_URL || "http://localhost:8891"`
- OpenAI API base: `NEXT_PUBLIC_OPENAI_API_URL || "http://localhost:8892"`
- Request body includes `{ provider, api_key: apiKey, model, gemini_api_key: apiKey }`

- [ ] **Step 4: Verify frontend**

Run: `cd agent_skills/self-improving-agent-skills/frontend && npm run build`

Expected: build completes without TypeScript errors.

### Task 4: Documentation and Smoke Checks

**Files:**
- Create: `agent_skills/self-improving-agent-skills/backend-openai/README.md`
- Modify: `agent_skills/self-improving-agent-skills/README.md`

- [ ] **Step 1: Document OpenAI backend**

Document `backend-openai` setup, `OPENAI_API_KEY`, optional UI key entry, default port `8892`, default model `gpt-5-mini`, and frontend environment variables.

- [ ] **Step 2: Run final verification**

Run:

```bash
python3 -m unittest discover agent_skills/self-improving-agent-skills/backend-openai/tests -v
cd agent_skills/self-improving-agent-skills/frontend && npm run build
git diff --check -- agent_skills/self-improving-agent-skills docs/superpowers/plans/2026-08-09-openai-self-improving-backend.md
```

Expected: tests pass, frontend builds, and diff check reports no whitespace errors.
