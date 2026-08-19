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
    RagEvaluationResultView,
    RagRetrievalEvaluationView,
    RagOperationReplayView,
    RagAuditLogsView,
    RagAuditDeleteView,
    RagUsageView,
    RagUserView,
    RagRoleView
    ,RagDiagnosticsView
    ,RagFeedbackView
    ,RagWebSearchView
} from '@/types/rag';

class RagApi {
    private client: AxiosInstance;
    private accessToken = '';

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

    /** 设置当前会话 access token；token 仅保存在内存中。 */
    public setAccessToken(token: string): void {
        this.accessToken = token.trim();
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

    /** 回放指定的导入操作；成功时返回本次重新索引结果，失败时抛出请求错误。 */
    public async replayOperation(operationId: number): Promise<RagOperationReplayView> {
        return this.request(`/operation-logs/${operationId}/replay`, { method: 'POST' });
    }

    public async getAuditLogs(): Promise<RagAuditLogsView> {
        return this.request('/admin/audit-logs');
    }

    public async exportAuditLogs(): Promise<Blob> {
        const response = await this.client.request<Blob>({
            url: '/admin/audit-logs/export',
            responseType: 'blob',
            headers: this.accessToken ? { Authorization: `Bearer ${this.accessToken}` } : undefined
        });
        return response.data;
    }

    public async deleteAuditLogs(approvalToken: string, before?: string): Promise<RagAuditDeleteView> {
        return this.request('/admin/audit-logs', {
            method: 'DELETE',
            params: before ? { before } : undefined,
            data: { approval_token: approvalToken }
        });
    }

    public async purgeAuditLogs(approvalToken: string): Promise<RagAuditDeleteView> {
        return this.request('/admin/audit-logs/purge', { method: 'POST', data: { approval_token: approvalToken } });
    }

    public async getUsage(): Promise<{ usage: RagUsageView; rerank_provider: string }> {
        return this.request('/admin/usage');
    }

    public async getDiagnostics(): Promise<RagDiagnosticsView> {
        return this.request('/diagnostics');
    }

    public async webSearch(question: string, limit: number = 3): Promise<RagWebSearchView> {
        return this.request('/web-search', { method: 'POST', data: { question, limit } });
    }

    public async submitFeedback(rating: number, comment: string = ''): Promise<{ feedback: RagFeedbackView }> {
        return this.request('/feedback', { method: 'POST', data: { rating, comment } });
    }

    public async getUsers(): Promise<{ users: RagUserView[] }> {
        return this.request('/admin/users');
    }

    public async createUser(payload: Omit<RagUserView, 'id' | 'roles' | 'metadata' | 'created_at' | 'updated_at' | 'last_seen_at'> & { role_ids: number[] }): Promise<{ user: RagUserView }> {
        return this.request('/admin/users', { method: 'POST', data: payload });
    }

    public async updateUser(userId: number, payload: Omit<RagUserView, 'id' | 'external_id' | 'roles' | 'metadata' | 'created_at' | 'updated_at' | 'last_seen_at'> & { role_ids: number[] }): Promise<{ user: RagUserView }> {
        return this.request(`/admin/users/${userId}`, { method: 'PUT', data: payload });
    }

    public async deleteUser(userId: number): Promise<{ deleted: boolean }> {
        return this.request(`/admin/users/${userId}`, { method: 'DELETE' });
    }

    public async getRoles(): Promise<{ roles: RagRoleView[] }> {
        return this.request('/admin/roles');
    }

    public async createRole(payload: Pick<RagRoleView, 'name' | 'description' | 'permissions'>): Promise<{ role: RagRoleView }> {
        return this.request('/admin/roles', { method: 'POST', data: payload });
    }

    public async updateRole(roleId: number, payload: Pick<RagRoleView, 'name' | 'description' | 'permissions'>): Promise<{ role: RagRoleView }> {
        return this.request(`/admin/roles/${roleId}`, { method: 'PUT', data: payload });
    }

    public async deleteRole(roleId: number): Promise<{ deleted: boolean }> {
        return this.request(`/admin/roles/${roleId}`, { method: 'DELETE' });
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

    /** 运行内置离线召回样例，成功时返回可比较的命中率和 MRR。 */
    public async evaluateRetrieval(): Promise<RagRetrievalEvaluationView> {
        return this.request('/evaluate-retrieval', { method: 'POST', data: {} });
    }

    private async request<T>(path: string, config?: Parameters<AxiosInstance['request']>[0]): Promise<T> {
        const response = await this.client.request({
            url: path,
            ...config,
            headers: {
                ...(config?.headers ?? {}),
                ...(this.accessToken ? { Authorization: `Bearer ${this.accessToken}` } : {})
            }
        });
        return response.data as T;
    }
}

export const ragApi = new RagApi('/api');
