<template>
    <section class="admin-page">
        <header class="admin-page__header">
            <h1 class="admin-page__title">管理后台</h1>
            <p class="admin-page__subtitle">身份、审计、用量与检索策略</p>
        </header>

        <section class="admin-page__section">
            <h2 class="admin-page__section-title">当前会话</h2>
            <div class="admin-page__token-row">
                <input
                    v-model="tokenInput"
                    class="admin-page__token-input"
                    type="password"
                    autocomplete="off"
                    placeholder="粘贴 OIDC/JWT access token"
                />
                <button class="admin-page__button admin-page__button--primary" @click="applyToken">应用 token</button>
                <button class="admin-page__button" @click="clearToken">清除</button>
            </div>
            <p class="admin-page__hint">token 仅保存在当前浏览器内存中，刷新页面后需要重新输入。</p>
        </section>

        <section class="admin-page__metrics">
            <article v-for="metric in metrics" :key="metric.label" class="admin-page__metric">
                <span>{{ metric.label }}</span>
                <strong>{{ metric.value }}</strong>
            </article>
        </section>

        <section class="admin-page__section">
            <div class="admin-page__section-header">
                <div>
                    <h2 class="admin-page__section-title">审计日志</h2>
                    <p class="admin-page__hint">默认保留 30 天，支持管理员导出与清理。</p>
                </div>
                <div class="admin-page__actions">
                    <button class="admin-page__button" :disabled="loading" @click="refresh">刷新</button>
                    <button class="admin-page__button" :disabled="loading" @click="exportLogs">导出 CSV</button>
                    <button class="admin-page__button admin-page__button--danger" :disabled="loading" @click="purgeLogs">
                        清理 30 天前日志
                    </button>
                </div>
            </div>
            <div v-if="message" class="admin-page__message">{{ message }}</div>
            <div v-if="!store.auditLogs.length" class="admin-page__empty">暂无审计记录。</div>
            <div v-for="log in store.auditLogs" :key="log.id" class="admin-page__audit-row">
                <div>
                    <strong>{{ log.action }}</strong>
                    <span>{{ log.resource }}</span>
                </div>
                <div>
                    <span>{{ log.actor_id }}</span>
                    <time>{{ log.created_at }}</time>
                </div>
            </div>
        </section>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();
const tokenInput = ref('');
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
    try {
        const result = await store.purgeAuditLogs();
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
    max-width: 1280px;
    margin: 0 auto;
    padding: 24px;

    &__header {
        margin-bottom: 24px;
    }

    &__title {
        margin: 0;
        font-size: 24px;
    }

    &__subtitle,
    &__hint {
        margin: 6px 0 0;
        color: #64748b;
        font-size: 13px;
    }

    &__section {
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        background: #fff;
    }

    &__section-header,
    &__token-row,
    &__actions {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    &__section-header {
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 14px;
    }

    &__section-title {
        margin: 0;
        font-size: 16px;
    }

    &__token-input {
        min-width: 0;
        flex: 1;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 9px 10px;
    }

    &__button {
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 8px 11px;
        background: #fff;
        color: #0f172a;
        cursor: pointer;

        &:disabled {
            cursor: not-allowed;
            opacity: 0.55;
        }

        &--primary {
            border-color: #1d4ed8;
            background: #1d4ed8;
            color: #fff;
        }

        &--danger {
            border-color: #fecaca;
            color: #b91c1c;
        }
    }

    &__metrics {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 12px;
        margin-bottom: 20px;
    }

    &__metric {
        display: grid;
        gap: 8px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px;
        background: #fff;
        color: #64748b;

        strong {
            color: #0f172a;
            font-size: 20px;
        }
    }

    &__message {
        margin-bottom: 12px;
        color: #1d4ed8;
    }

    &__empty {
        color: #64748b;
    }

    &__audit-row {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        border-top: 1px solid #e2e8f0;
        padding: 12px 0;

        div {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        span,
        time {
            color: #64748b;
            font-size: 13px;
        }
    }

    @media (max-width: 760px) {
        &__metrics {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }

        &__section-header,
        &__token-row,
        &__audit-row {
            align-items: stretch;
            flex-direction: column;
        }

        &__actions {
            flex-wrap: wrap;
        }
    }
}
</style>
