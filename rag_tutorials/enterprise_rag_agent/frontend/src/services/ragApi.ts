import axios, { type AxiosInstance } from 'axios';
import type {
    AnswerView,
    RagConfigView,
    RagDocumentsView,
    RagIngestResultView,
    RagKnowledgeBasesView,
    RagLogsView,
    RagScopeView,
    RagSearchView,
    RagStatsView,
    RagEvaluationResultView
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

    public async getConfig(): Promise<RagConfigView> {
        return this.request('/config');
    }

    /**
     * 获取阶段 0 只读范围配置；成功时返回业务域、权限和风险边界，失败时抛出请求错误。
     */
    public async getScope(): Promise<RagScopeView> {
        return this.request('/scope');
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

    public async getOperationLogs(): Promise<RagLogsView> {
        return this.request('/operation-logs');
    }

    /**
     * 提交文档导入请求；成功时返回索引、跳过、清理和重复路径明细，失败时抛出请求错误。
     */
    public async ingest(path: string, knowledgeBase?: string, allowedGroups?: string[]): Promise<RagIngestResultView> {
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

    public async evaluate(question: string, expectedAnswer: string | null, actualAnswer: string): Promise<RagEvaluationResultView> {
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

export const ragApi = new RagApi('/api');
