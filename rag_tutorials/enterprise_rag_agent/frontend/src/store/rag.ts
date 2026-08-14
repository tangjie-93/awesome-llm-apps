import { defineStore } from 'pinia';
import { computed, ref } from 'vue';
import { ragApi } from '@/services/ragApi';
import type {
    RagAnswerLog,
    RagConfigView,
    RagDocumentSummary,
    RagEvaluationLog,
    RagEvaluationResultView,
    RagSearchView,
    RagStatsView
} from '@/types/rag';

const DEFAULT_BASE_URL = '/api';
const LEGACY_BASE_URL = 'http://127.0.0.1:8000';

function resolveBaseUrl(): string {
    const savedBaseUrl = localStorage.getItem('enterprise-rag-base-url');
    if (!savedBaseUrl || savedBaseUrl === LEGACY_BASE_URL) {
        return DEFAULT_BASE_URL;
    }
    return savedBaseUrl;
}

export const useRagStore = defineStore('rag', () => {
    const baseUrl = ref<string>(resolveBaseUrl());
    const companyName = ref<string>('Acme Corp');
    const config = ref<RagConfigView>({});
    const knowledgeBases = ref<string[]>([]);
    const documents = ref<RagDocumentSummary[]>([]);
    const answerLogs = ref<RagAnswerLog[]>([]);
    const evaluationLogs = ref<RagEvaluationLog[]>([]);
    const stats = ref<RagStatsView>({});
    const loading = ref<boolean>(false);
    const error = ref<string>('');

    const hasKnowledgeBases = computed<boolean>(() => knowledgeBases.value.length > 0);

    async function syncDashboard(): Promise<void> {
        loading.value = true;
        error.value = '';
        try {
            baseUrl.value = baseUrl.value.trim() || DEFAULT_BASE_URL;
            ragApi.setBaseUrl(baseUrl.value);
            const [statsData, configData, kbData, docsData, answerData, evalData] = await Promise.all([
                ragApi.getStats(),
                ragApi.getConfig(),
                ragApi.getKnowledgeBases(),
                ragApi.getDocuments(),
                ragApi.getAnswerLogs(),
                ragApi.getEvaluationLogs()
            ]);
            stats.value = statsData;
            companyName.value = String(statsData.company_name ?? companyName.value);
            config.value = configData;
            knowledgeBases.value = kbData.knowledge_bases ?? [];
            documents.value = docsData.documents ?? [];
            answerLogs.value = answerData.answer_logs ?? [];
            evaluationLogs.value = evalData.evaluation_logs ?? [];
            localStorage.setItem('enterprise-rag-base-url', baseUrl.value);
        } catch (err) {
            error.value = err instanceof Error ? err.message : '加载失败';
        } finally {
            loading.value = false;
        }
    }

    async function ingestPath(path: string, knowledgeBase?: string, allowedGroups?: string[]): Promise<Record<string, unknown>> {
        return ragApi.ingest(path, knowledgeBase, allowedGroups);
    }

    async function askQuestion(question: string, knowledgeBase?: string, userGroups?: string[], topK?: number) {
        return ragApi.ask(question, knowledgeBase, userGroups, topK);
    }

    async function searchQuestion(question: string, knowledgeBase?: string, userGroups?: string[], topK?: number): Promise<RagSearchView> {
        return ragApi.search(question, knowledgeBase, userGroups, topK);
    }

    async function evaluateAnswer(question: string, expectedAnswer: string | null, actualAnswer: string): Promise<RagEvaluationResultView> {
        return ragApi.evaluate(question, expectedAnswer, actualAnswer);
    }

    return {
        baseUrl,
        companyName,
        knowledgeBases,
        documents,
        answerLogs,
        evaluationLogs,
        stats,
        config,
        loading,
        error,
        hasKnowledgeBases,
        syncDashboard,
        ingestPath,
        askQuestion,
        searchQuestion,
        evaluateAnswer
    };
});
