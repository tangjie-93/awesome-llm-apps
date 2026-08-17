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

export interface RagEvaluationResultView {
    question: string;
    expected_answer: string | null;
    actual_answer: string;
    score: number;
    notes: string;
}
