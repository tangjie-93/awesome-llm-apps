# Phase 3/4 Implementation Status

> Updated: 2026-08-18

## Phase 3: Enterprise Capabilities

Completed:

- JWT/OIDC request authentication and configurable identity claims.
- Role-derived API permissions. `admin` bypasses permission checks; `auditor` can read audit data but cannot manage users.
- Separate permissions for ingestion, audit read/manage, user management, and role management.
- Session identity endpoint, audit export/retention, usage counters, ingest replay, user and role administration.

Remaining:

- Production identity-provider onboarding and deployment-specific claim mapping.
- Tenant data model and tenant-level isolation.
- Organization-specific approval rules for destructive audit and administration actions.

## Phase 4: Advanced Capabilities

Completed in this iteration:

- Existing multi-knowledge-base routing is surfaced in the answer tool trace.
- Configurable Web fallback service. It is disabled by default and only calls the configured provider URL.
- Runtime diagnostics for index size, low-confidence answers, Web fallback state, and feedback statistics.
- Human feedback API and question-answer page controls.

Remaining:

- Dedicated knowledge graph storage, graph retrieval, and multi-hop reasoning.
- Image/document multimodal embedding and retrieval pipeline.
- Automated diagnosis actions and feedback-driven ranking/model optimization.

## Verification

- Backend: `python -m unittest discover -s tests`
- Frontend: `npm.cmd run build`
