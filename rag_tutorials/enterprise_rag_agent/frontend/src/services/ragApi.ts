import axios, { type AxiosInstance } from 'axios';
import type {
    AnswerView,
    RagDocumentsView,
    RagKnowledgeBasesView,
    RagLogsView,
    RagSearchView,
    RagStatsView
} from '@/types/rag';

class RagApi {
    private client: AxiosInstance;

    public constructor(baseUrl: string) {
        this.client = axios.create({
            baseURL: baseUrl,
            timeout: 30000
        });
    }

    public setBaseUrl(baseUrl: string): void {
        this.client = axios.create({
            baseURL: baseUrl,
            timeout: 30000
        });
    }

    public async getStats(): Promise<RagStatsView> {
        return this.request('/stats');
    }

    public async getKnowledgeBases(): Promise<RagKnowledgeBasesView> {
        return this.request('/knowledge-bases');
    }

    public async getDocuments(): Promise<RagDocumentsView> {
        return this.request('/documents');
    }

    public async getAnswerLogs(): Promise<RagLogsView> {
        return this.request('/answer-logs');
    }

    public async getEvaluationLogs(): Promise<RagLogsView> {
        return this.request('/evaluation-logs');
    }

    public async ingest(path: string, knowledgeBase?: string, allowedGroups?: string[]): Promise<Record<string, unknown>> {
        return this.request('/ingest', {
            method: 'POST',
            data: {
                path,
                knowledge_base: knowledgeBase,
                allowed_groups: allowedGroups
            }
        });
    }

    public async search(question: string, knowledgeBase?: string, userGroups?: string[], topK?: number): Promise<RagSearchView> {
        return this.request('/search', {
            method: 'POST',
            data: {
                question,
                knowledge_base: knowledgeBase,
                user_groups: userGroups,
                top_k: topK
            }
        });
    }

    public async ask(question: string, knowledgeBase?: string, userGroups?: string[], topK?: number): Promise<AnswerView> {
        return this.request('/ask', {
            method: 'POST',
            data: {
                question,
                knowledge_base: knowledgeBase,
                user_groups: userGroups,
                top_k: topK
            }
        });
    }

    public async evaluate(question: string, expectedAnswer: string | null, actualAnswer: string): Promise<Record<string, unknown>> {
        return this.request('/evaluate', {
            method: 'POST',
            data: {
                question,
                expected_answer: expectedAnswer,
                actual_answer: actualAnswer
            }
        });
    }

    private async request<T>(path: string, config?: Parameters<AxiosInstance['request']>[0]): Promise<T> {
        const response = await this.client.request({
            url: path,
            ...config
        });
        return response.data as T;
    }
}

export const ragApi = new RagApi('http://127.0.0.1:8000');
