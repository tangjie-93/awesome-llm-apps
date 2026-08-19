export interface RetrievedChunkView {
    knowledge_base: string;
    source: string;
    title: string;
    section_path: string;
    chunk_index: number;
    risk_level: string;
    score: number;
    matched_terms: string[];
}

export interface AnswerView {
    question: string;
    answer: string;
    confidence: number;
    knowledge_bases: string[];
    citations: RetrievedChunkView[];
    evidence_snippets: AnswerEvidenceSnippet[];
    external_sources: RagWebSearchResultView[];
    tool_trace: string[];
    clarifying_question: string | null;
    sources_consulted: number;
}

export interface AnswerEvidenceSnippet {
    knowledge_base: string;
    source: string;
    section_path: string;
    risk_level: string;
    snippet: string;
}

export interface RagChunkView {
    chunk_id: string;
    source_id: string;
    knowledge_base: string;
    path: string;
    title: string;
    section_path: string;
    chunk_index: number;
    text: string;
    token_count: number;
    allowed_groups: string[];
    risk_level: string;
    metadata: Record<string, unknown>;
}

export interface RagSearchItemView {
    chunk: RagChunkView;
    score: number;
    lexical_score: number;
    rerank_score: number;
    matched_terms: string[];
}

export interface RagStatsView {
    documents?: number;
    chunks?: number;
    answer_logs?: number;
    evaluation_logs?: number;
    company_name?: string;
    db_path?: string;
    knowledge_bases?: string[];
    usage?: RagUsageView;
}

export interface RagUsageView {
    requests: number;
    tokens: number;
    model_calls: number;
}

export interface RagConfigView {
    company_name?: string;
    default_knowledge_base?: string;
    default_groups?: string[];
    default_risk_levels?: string[];
    risk_by_group?: Record<string, string>;
    chunk_size?: number;
    chunk_overlap?: number;
    top_k?: number;
    rerank_top_k?: number;
    enable_llm?: boolean;
    llm_provider?: string;
    llm_model?: string;
    auth_mode?: string;
    jwt_tenant_claim?: string;
    web_fallback_enabled?: boolean;
}

export interface RagWebSearchResultView {
    title: string;
    url: string;
    snippet: string;
}

export interface RagWebSearchView {
    results: RagWebSearchResultView[];
    enabled: boolean;
}

export interface RagKnowledgeGraphEntityView {
    name: string;
    chunk_count: number;
}

export interface RagKnowledgeGraphRelationView {
    source: string;
    target: string;
    type: string;
    weight: number;
}

export interface RagKnowledgeGraphView {
    entities: RagKnowledgeGraphEntityView[];
    relations: RagKnowledgeGraphRelationView[];
    entity_count: number;
    relation_count: number;
}

export interface RagKnowledgeGraphQueryEntityView {
    name: string;
    key: string;
    seed: boolean;
}

export interface RagKnowledgeGraphQueryRelationView {
    source: string;
    target: string;
    type: string;
    chunk_id: string;
}

export interface RagKnowledgeGraphPathView {
    entities: string[];
    relations: string[];
    hops: number;
    chunk_ids: string[];
}

export interface RagKnowledgeGraphQueryView {
    query: string;
    max_hops: number;
    entities: RagKnowledgeGraphQueryEntityView[];
    relations: RagKnowledgeGraphQueryRelationView[];
    paths: RagKnowledgeGraphPathView[];
    chunks: Array<{ chunk_id: string }>;
}

export interface RagFeedbackView {
    id: number;
    actor_id: string;
    answer_log_id: number | null;
    rating: number;
    comment: string;
    created_at: string;
}

export interface RagDiagnosticsView {
    documents: number;
    chunks: number;
    knowledge_bases: string[];
    low_confidence_answers: number;
    feedback: {
        count: number;
        average_rating: number;
        negative_count: number;
    };
    web_fallback_enabled: boolean;
    suggestions: RagDiagnosticSuggestionView[];
}

export interface RagDiagnosticSuggestionView {
    code: string;
    severity: 'info' | 'warning' | 'critical';
    title: string;
    detail: string;
    action: string;
}

export interface RagBusinessDomainView {
    code: string;
    description: string;
}

export interface RagScopeView {
    business_domains: RagBusinessDomainView[];
    supported_document_types: string[];
    excluded_scopes: string[];
    permission_summary: string[];
    risk_by_group: Record<string, string>;
    high_risk_policy: string;
}

export interface RagDocumentsView {
    documents: RagDocumentSummary[];
}

export interface RagIngestResultView {
    documents_indexed: number;
    chunks_indexed: number;
    documents_skipped: number;
    documents_removed: number;
    duplicate_paths: string[];
    knowledge_bases: string[];
    paths: string[];
}

export interface RagKnowledgeBasesView {
    knowledge_bases: string[];
}

export interface RagLogsView {
    answer_logs?: RagAnswerLog[];
    evaluation_logs?: RagEvaluationLog[];
    operation_logs?: RagOperationLog[];
}

export interface RagSearchView {
    results: RagSearchItemView[];
}

export interface RagDocumentSummary {
    source_id: string;
    knowledge_base: string;
    path: string;
    title: string;
    content_type: string;
    content_hash: string;
    version: string;
    allowed_groups: string[];
    risk_level: string;
    metadata: Record<string, unknown>;
    indexed_at: string;
}

export interface RagAnswerLog {
    id: number;
    question: string;
    answer: string;
    confidence: number;
    citations: Array<Record<string, unknown>>;
    metadata: Record<string, unknown>;
    created_at: string;
}

export interface RagEvaluationLog {
    id: number;
    question: string;
    expected_answer: string | null;
    actual_answer: string;
    score: number;
    notes: string;
    created_at: string;
}

export interface RagOperationLog {
    id: number;
    operation: string;
    status: string;
    path: string | null;
    knowledge_base: string | null;
    allowed_groups: string[];
    detail: Record<string, unknown>;
    created_at: string;
}

export interface RagOperationReplayView {
    documents_indexed: number;
    chunks_indexed: number;
    documents_skipped: number;
    documents_removed: number;
    duplicate_paths: string[];
    knowledge_bases: string[];
    paths: string[];
}

export interface RagEvaluationResultView {
    question: string;
    expected_answer: string | null;
    actual_answer: string;
    score: number;
    notes: string;
}

export interface RagRetrievalEvaluationView {
    total: number;
    hit_rate: number;
    mrr: number;
    results: RagRetrievalEvaluationCaseView[];
}

export interface RagRetrievalEvaluationCaseView {
    question: string;
    expected_terms: string[];
    expected_sources: string[];
    hit: boolean;
    rank: number;
    results: RagSearchItemView[];
}

export interface RagAuditLogView {
    id: number;
    actor_id: string;
    action: string;
    resource: string;
    detail: Record<string, unknown>;
    created_at: string;
}

export interface RagAuditLogsView {
    audit_logs: RagAuditLogView[];
}

export interface RagAuditDeleteView {
    deleted: number;
    retention_days?: number;
}

export interface RagDiagnosticActionResultView {
    action: string;
    operation_id: number;
    result: RagOperationReplayView;
}

export interface RagUserView {
    id: number;
    external_id: string;
    display_name: string;
    email: string | null;
    groups: string[];
    roles: string[];
    is_active: boolean;
    metadata: Record<string, unknown>;
    created_at: string;
    updated_at: string;
    last_seen_at: string;
}

export interface RagRoleView {
    id: number;
    name: string;
    description: string;
    permissions: string[];
    is_system: boolean;
    created_at: string;
    updated_at: string;
}
