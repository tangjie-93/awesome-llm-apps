export interface RetrievedChunkView {
    knowledge_base: string;
    source: string;
    title: string;
    section_path: string;
    chunk_index: number;
    score: number;
    matched_terms: string[];
}

export interface AnswerView {
    question: string;
    answer: string;
    confidence: number;
    knowledge_bases: string[];
    citations: RetrievedChunkView[];
    evidence_snippets: Array<Record<string, unknown>>;
    clarifying_question: string | null;
    sources_consulted: number;
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

export interface RagDocumentsView {
    documents: RagDocumentSummary[];
}

export interface RagKnowledgeBasesView {
    knowledge_bases: string[];
}

export interface RagLogsView {
    answer_logs?: RagAnswerLog[];
    evaluation_logs?: RagEvaluationLog[];
}

export interface RagSearchView {
    results: Array<Record<string, unknown>>;
}

export interface RagDocumentSummary {
    source_id: string;
    knowledge_base: string;
    path: string;
    title: string;
    content_type: string;
    version: string;
    allowed_groups: string[];
    metadata: Record<string, unknown>;
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
