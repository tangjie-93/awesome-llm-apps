<template>
    <section class="admin-page">
        <PageHeader />

        <el-card shadow="never" class="admin-page__card">
            <div class="admin-page__section-title">当前会话</div>
            <el-row :gutter="12">
                <el-col :xs="24" :md="12" class="admin-page__field">
                    <div class="admin-page__label">Access Token</div>
                    <el-input
                        v-model="tokenInput"
                        type="password"
                        autocomplete="off"
                        placeholder="粘贴 OIDC/JWT access token"
                    />
                </el-col>
                <el-col :xs="24" :md="12" class="admin-page__field">
                    <div class="admin-page__label">审计清理审批令牌</div>
                    <el-input
                        v-model="approvalToken"
                        type="password"
                        autocomplete="off"
                        placeholder="服务端配置的审批令牌"
                    />
                </el-col>
                <el-col :xs="24" class="admin-page__actions">
                    <el-button type="primary" @click="applyToken">应用 token</el-button>
                    <el-button @click="clearToken">清除</el-button>
                </el-col>
            </el-row>
            <div class="admin-page__hint">token 仅保存在当前浏览器内存中，刷新页面后需要重新输入。</div>
            <div class="admin-page__hint">清理或删除审计日志需要服务端配置的审批令牌。</div>
        </el-card>

        <el-row :gutter="12" class="admin-page__metrics">
            <el-col v-for="metric in metrics" :key="metric.label" :xs="12" :sm="12" :md="6">
                <el-card shadow="never" class="admin-page__metric">
                    <div class="admin-page__metric-label">{{ metric.label }}</div>
                    <div class="admin-page__metric-value">{{ metric.value }}</div>
                </el-card>
            </el-col>
        </el-row>

        <el-card shadow="never" class="admin-page__card">
            <div class="admin-page__section-header">
                <div>
                    <div class="admin-page__section-title">审计日志</div>
                    <div class="admin-page__hint">默认保留 30 天，支持管理员导出与清理。</div>
                </div>
                <div class="admin-page__actions">
                    <el-button :loading="loading" @click="refresh">刷新</el-button>
                    <el-button :loading="loading" @click="exportLogs">导出 CSV</el-button>
                    <el-button :loading="loading" type="danger" plain @click="purgeLogs">清理 30 天前日志</el-button>
                </div>
            </div>
            <el-alert v-if="message" :title="message" type="info" show-icon class="admin-page__message" />
            <el-empty v-if="!store.auditLogs.length" description="暂无审计记录。" />
            <el-table v-else :data="store.auditLogs" border stripe>
                <el-table-column label="动作" prop="action" min-width="180" />
                <el-table-column label="资源" prop="resource" min-width="200" />
                <el-table-column label="操作者" prop="actor_id" width="140" />
                <el-table-column label="时间" prop="created_at" width="180" />
            </el-table>
        </el-card>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();
const tokenInput = ref('');
const approvalToken = ref('');
const rerankProvider = ref('heuristic');
const message = ref('');
const loading = ref(false);

const metrics = computed(() => [
    { label: '请求数', value: store.usage.requests },
    { label: '估算 token', value: store.usage.tokens },
    { label: '模型调用', value: store.usage.model_calls },
    { label: 'Rerank provider', value: rerankProvider.value }
]);

/** 应用当前会话 token 并加载管理员数据。 */
async function applyToken(): Promise<void> {
    store.setAccessToken(tokenInput.value);
    await refresh();
}

/** 清除内存中的 access token 和当前页面数据。 */
function clearToken(): void {
    tokenInput.value = '';
    store.setAccessToken('');
    store.auditLogs.splice(0);
}

/** 刷新用量和审计日志，并将请求状态反馈给页面。 */
async function refresh(): Promise<void> {
    loading.value = true;
    message.value = '';
    try {
        await store.syncDashboard();
        await store.syncAuditLogs();
        rerankProvider.value = (await store.getUsage()).rerank_provider;
    } catch (error) {
        message.value = error instanceof Error ? error.message : '管理数据加载失败';
    } finally {
        loading.value = false;
    }
}

/** 下载后端生成的审计 CSV 文件。 */
async function exportLogs(): Promise<void> {
    try {
        const blob = await store.exportAuditLogs();
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'audit-logs.csv';
        link.click();
        URL.revokeObjectURL(url);
        message.value = '审计日志已导出';
    } catch (error) {
        message.value = error instanceof Error ? error.message : '导出失败';
    }
}

/** 触发后端按 30 天保留策略清理审计日志。 */
async function purgeLogs(): Promise<void> {
    if (!approvalToken.value.trim()) {
        message.value = '请输入审计清理审批令牌';
        return;
    }
    try {
        const result = await store.purgeAuditLogs(approvalToken.value.trim());
        message.value = `已清理 ${result.deleted} 条审计日志`;
        await store.syncAuditLogs();
    } catch (error) {
        message.value = error instanceof Error ? error.message : '清理失败';
    }
}

onMounted(() => {
    void refresh();
});
</script>

<style scoped lang="less">
.admin-page {
    min-width: 0;

    &__card,
    &__metrics {
        margin-bottom: 12px;
    }

    &__field,
    &__message {
        margin-bottom: 12px;
    }

    &__label,
    &__hint {
        margin-bottom: 6px;
        color: #64748b;
        font-size: 13px;
    }

    &__section-title {
        margin-bottom: 10px;
        font-size: 16px;
        font-weight: 600;
        color: #0f172a;
    }

    &__section-header {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 12px;
    }

    &__actions {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: flex-end;
    }

    &__metric {
        height: 100%;
    }

    &__metric-label {
        color: #64748b;
        font-size: 13px;
    }

    &__metric-value {
        margin-top: 10px;
        font-size: 24px;
        font-weight: 700;
        color: #0f172a;
    }
}
</style>
