import { defineStore } from 'pinia';
import { computed, ref } from 'vue';
import { ragApi } from '@/services/ragApi';
import type {
    RagAnswerLog,
    RagConfigView,
    RagDocumentSummary,
    RagEvaluationLog,
    RagEvaluationResultView,
    RagIngestResultView,
    RagOperationLog,
    RagOperationReplayView,
    RagScopeView,
    RagSearchView,
    RagStatsView,
    RagRetrievalEvaluationView,
    RagAuditLogView,
    RagAuditDeleteView,
    RagUsageView
    ,RagUserView
    ,RagRoleView
    ,RagDiagnosticsView
    ,RagWebSearchView
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
    const scope = ref<RagScopeView | null>(null);
    const answerLogs = ref<RagAnswerLog[]>([]);
    const evaluationLogs = ref<RagEvaluationLog[]>([]);
    const operationLogs = ref<RagOperationLog[]>([]);
    const stats = ref<RagStatsView>({});
    const loading = ref<boolean>(false);
    const error = ref<string>('');
    const accessToken = ref<string>('');
    const auditLogs = ref<RagAuditLogView[]>([]);
    const usage = ref<RagUsageView>({ requests: 0, tokens: 0, model_calls: 0 });
    const users = ref<RagUserView[]>([]);
    const roles = ref<RagRoleView[]>([]);
    const diagnostics = ref<RagDiagnosticsView | null>(null);

    const hasKnowledgeBases = computed<boolean>(() => knowledgeBases.value.length > 0);

    /**
     * 同步仪表盘和阶段 0 范围数据；成功时刷新本地状态，失败时写入 error。
     */
    async function syncDashboard(): Promise<void> {
        loading.value = true;
        error.value = '';
        try {
            baseUrl.value = baseUrl.value.trim() || DEFAULT_BASE_URL;
            ragApi.setBaseUrl(baseUrl.value);
            ragApi.setAccessToken(accessToken.value);
            const [statsData, configData, scopeData, kbData, docsData, answerData, evalData, operationData] = await Promise.all([
                ragApi.getStats(),
                ragApi.getConfig(),
                ragApi.getScope(),
                ragApi.getKnowledgeBases(),
                ragApi.getDocuments(),
                ragApi.getAnswerLogs(),
                ragApi.getEvaluationLogs(),
                ragApi.getOperationLogs()
            ]);
            stats.value = statsData;
            usage.value = statsData.usage ?? usage.value;
            companyName.value = String(statsData.company_name ?? companyName.value);
            config.value = configData;
            scope.value = scopeData;
            knowledgeBases.value = kbData.knowledge_bases ?? [];
            documents.value = docsData.documents ?? [];
            answerLogs.value = answerData.answer_logs ?? [];
            evaluationLogs.value = evalData.evaluation_logs ?? [];
            operationLogs.value = operationData.operation_logs ?? [];
            localStorage.setItem('enterprise-rag-base-url', baseUrl.value);
        } catch (err) {
            error.value = err instanceof Error ? err.message : '加载失败';
        } finally {
            loading.value = false;
        }
    }

    /**
     * 导入本地文件或目录；成功时返回导入明细，失败时向调用方抛出错误。
     */
    async function ingestPath(path: string, knowledgeBase?: string, allowedGroups?: string[]): Promise<RagIngestResultView> {
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

    /** 运行默认召回评估，成功时返回命中率、MRR 和逐题结果。 */
    async function evaluateRetrieval(): Promise<RagRetrievalEvaluationView> {
        return ragApi.evaluateRetrieval();
    }

    /** 回放导入日志并在成功后刷新仪表盘数据。 */
    async function replayOperation(operationId: number): Promise<RagOperationReplayView> {
        const result = await ragApi.replayOperation(operationId);
        await syncDashboard();
        return result;
    }

    /** 设置当前会话 JWT，不写入 localStorage。 */
    function setAccessToken(token: string): void {
        accessToken.value = token.trim();
        ragApi.setAccessToken(accessToken.value);
    }

    /** 加载管理员审计日志。 */
    async function syncAuditLogs(): Promise<void> {
        auditLogs.value = (await ragApi.getAuditLogs()).audit_logs;
    }

    /** 导出管理员审计 CSV。 */
    async function exportAuditLogs(): Promise<Blob> {
        return ragApi.exportAuditLogs();
    }

    /** 删除或清理审计日志。 */
    async function purgeAuditLogs(before?: string): Promise<RagAuditDeleteView> {
        return before ? ragApi.deleteAuditLogs(before) : ragApi.purgeAuditLogs();
    }

    /** 加载管理员用量统计和当前 rerank provider。 */
    async function getUsage(): Promise<{ usage: RagUsageView; rerank_provider: string }> {
        const result = await ragApi.getUsage();
        usage.value = result.usage;
        return result;
    }

    /** 读取运行诊断指标。 */
    async function syncDiagnostics(): Promise<void> {
        diagnostics.value = await ragApi.getDiagnostics();
    }

    /** 调用受控的外部检索 provider。 */
    async function searchWeb(question: string, limit: number = 3): Promise<RagWebSearchView> {
        return ragApi.webSearch(question, limit);
    }

    /** 提交对当前问答质量的人工反馈。 */
    async function submitFeedback(rating: number, comment: string = ''): Promise<void> {
        await ragApi.submitFeedback(rating, comment);
    }

    /** 加载用户和角色目录。 */
    async function syncUserDirectory(): Promise<void> {
        const [userData, roleData] = await Promise.all([ragApi.getUsers(), ragApi.getRoles()]);
        users.value = userData.users;
        roles.value = roleData.roles;
    }

    /** 创建用户并刷新用户目录。 */
    async function createUser(payload: Parameters<typeof ragApi.createUser>[0]): Promise<void> {
        await ragApi.createUser(payload);
        await syncUserDirectory();
    }

    /** 更新用户并刷新用户目录。 */
    async function updateUser(userId: number, payload: Parameters<typeof ragApi.updateUser>[1]): Promise<void> {
        await ragApi.updateUser(userId, payload);
        await syncUserDirectory();
    }

    /** 删除用户并刷新用户目录。 */
    async function deleteUser(userId: number): Promise<void> {
        await ragApi.deleteUser(userId);
        await syncUserDirectory();
    }

    /** 创建角色并刷新用户目录。 */
    async function createRole(payload: Parameters<typeof ragApi.createRole>[0]): Promise<void> {
        await ragApi.createRole(payload);
        await syncUserDirectory();
    }

    /** 更新角色并刷新用户目录。 */
    async function updateRole(roleId: number, payload: Parameters<typeof ragApi.updateRole>[1]): Promise<void> {
        await ragApi.updateRole(roleId, payload);
        await syncUserDirectory();
    }

    /** 删除角色并刷新用户目录。 */
    async function deleteRole(roleId: number): Promise<void> {
        await ragApi.deleteRole(roleId);
        await syncUserDirectory();
    }

    return {
        baseUrl,
        accessToken,
        companyName,
        knowledgeBases,
        documents,
        answerLogs,
        evaluationLogs,
        operationLogs,
        stats,
        config,
        scope,
        loading,
        error,
        auditLogs,
        usage,
        users,
        roles,
        diagnostics,
        hasKnowledgeBases,
        syncDashboard,
        ingestPath,
        askQuestion,
        searchQuestion,
        evaluateAnswer,
        evaluateRetrieval,
        replayOperation,
        setAccessToken,
        syncAuditLogs,
        exportAuditLogs,
        purgeAuditLogs,
        getUsage,
        syncDiagnostics,
        searchWeb,
        submitFeedback,
        syncUserDirectory,
        createUser,
        updateUser,
        deleteUser,
        createRole,
        updateRole,
        deleteRole
    };
});
