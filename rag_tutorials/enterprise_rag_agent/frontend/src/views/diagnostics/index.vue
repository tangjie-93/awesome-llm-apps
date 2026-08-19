<template>
    <section class="diagnostics-page">
        <header class="diagnostics-page__header">
            <h1 class="diagnostics-page__title">运行诊断</h1>
            <p class="diagnostics-page__subtitle">查看知识库健康情况，并在启用后使用外部检索补充信息。</p>
        </header>

        <section class="diagnostics-page__metrics">
            <article v-for="metric in metrics" :key="metric.label" class="diagnostics-page__metric">
                <span>{{ metric.label }}</span>
                <strong>{{ metric.value }}</strong>
            </article>
        </section>

        <section class="diagnostics-page__section">
            <div class="diagnostics-page__section-header">
                <div>
                    <h2 class="diagnostics-page__section-title">诊断建议</h2>
                    <p class="diagnostics-page__hint">建议来自当前租户的运行指标，不会自动修改模型或排序配置。</p>
                </div>
            </div>
            <div class="diagnostics-page__suggestions">
                <article
                    v-for="suggestion in suggestions"
                    :key="suggestion.code"
                    class="diagnostics-page__suggestion"
                    :class="`diagnostics-page__suggestion--${suggestion.severity}`"
                >
                    <div class="diagnostics-page__suggestion-header">
                        <strong>{{ suggestion.title }}</strong>
                        <span>{{ severityLabel(suggestion.severity) }}</span>
                    </div>
                    <p>{{ suggestion.detail }}</p>
                    <p class="diagnostics-page__suggestion-action">建议：{{ suggestion.action }}</p>
                </article>
            </div>
        </section>

        <section class="diagnostics-page__section">
            <div class="diagnostics-page__section-header">
                <div>
                    <h2 class="diagnostics-page__section-title">人工处置</h2>
                    <p class="diagnostics-page__hint">仅支持经过审批令牌确认的失败导入回放，执行结果会写入操作日志和审计日志。</p>
                </div>
            </div>
            <div class="diagnostics-page__action-grid">
                <label>
                    <span>失败导入操作 ID</span>
                    <input v-model.number="operationId" type="number" min="1" placeholder="例如 12" />
                </label>
                <label>
                    <span>审批令牌</span>
                    <input v-model.trim="approvalToken" type="password" autocomplete="off" placeholder="服务端配置的审批令牌" />
                </label>
                <button class="diagnostics-page__button diagnostics-page__button--primary" :disabled="actionLoading" @click="executeAction">
                    {{ actionLoading ? '执行中...' : '回放失败导入' }}
                </button>
            </div>
            <p v-if="actionMessage" class="diagnostics-page__message">{{ actionMessage }}</p>
        </section>

        <section class="diagnostics-page__section">
            <div class="diagnostics-page__section-header">
                <div>
                    <h2 class="diagnostics-page__section-title">外部检索</h2>
                    <p class="diagnostics-page__hint">
                        {{ store.diagnostics?.web_fallback_enabled ? '已启用受控 Web fallback。' : '当前未启用 Web fallback。' }}
                    </p>
                </div>
                <button class="diagnostics-page__button" :disabled="loading" @click="refresh">刷新诊断</button>
            </div>
            <div class="diagnostics-page__search-row">
                <input v-model.trim="question" class="diagnostics-page__input" placeholder="输入需要补充检索的问题" />
                <button class="diagnostics-page__button diagnostics-page__button--primary" :disabled="searching" @click="searchWeb">
                    {{ searching ? '检索中...' : '检索' }}
                </button>
            </div>
            <p v-if="message" class="diagnostics-page__message">{{ message }}</p>
            <div v-for="result in results" :key="result.url" class="diagnostics-page__result">
                <a :href="result.url" target="_blank" rel="noopener noreferrer">{{ result.title }}</a>
                <p>{{ result.snippet }}</p>
            </div>
        </section>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import { useRagStore } from '@/store/rag';
import type { RagDiagnosticSuggestionView, RagWebSearchResultView } from '@/types/rag';

const store = useRagStore();
const question = ref('');
const results = ref<RagWebSearchResultView[]>([]);
const message = ref('');
const loading = ref(false);
const searching = ref(false);
const operationId = ref<number | null>(null);
const approvalToken = ref('');
const actionLoading = ref(false);
const actionMessage = ref('');
const metrics = computed(() => [
    { label: '文档', value: store.diagnostics?.documents ?? 0 },
    { label: '切块', value: store.diagnostics?.chunks ?? 0 },
    { label: '低置信度回答', value: store.diagnostics?.low_confidence_answers ?? 0 },
    { label: '反馈均分', value: store.diagnostics?.feedback.average_rating ?? 0 }
]);
const suggestions = computed(() => store.diagnostics?.suggestions ?? []);

/**
 * 将后端诊断等级转换为页面可读文本。
 * @param severity 后端返回的诊断等级。
 * @returns 中文等级名称。
 */
function severityLabel(severity: RagDiagnosticSuggestionView['severity']): string {
    const labels: Record<RagDiagnosticSuggestionView['severity'], string> = {
        info: '提示',
        warning: '注意',
        critical: '严重'
    };
    return labels[severity];
}

/** 刷新诊断数据；失败时保留最近一次成功结果。 */
async function refresh(): Promise<void> {
    loading.value = true;
    try {
        await store.syncDiagnostics();
    } catch (error) {
        message.value = error instanceof Error ? error.message : '诊断数据加载失败';
    } finally {
        loading.value = false;
    }
}

/** 请求已配置的外部检索服务，并展示标准化结果。 */
async function searchWeb(): Promise<void> {
    if (!question.value) {
        message.value = '请输入检索问题';
        return;
    }
    searching.value = true;
    message.value = '';
    try {
        const response = await store.searchWeb(question.value);
        results.value = response.results;
        message.value = response.enabled ? `返回 ${response.results.length} 条外部结果` : 'Web fallback 未启用';
    } catch (error) {
        message.value = error instanceof Error ? error.message : '外部检索失败';
    } finally {
        searching.value = false;
    }
}

async function executeAction(): Promise<void> {
    if (!operationId.value || !approvalToken.value) {
        actionMessage.value = '请输入失败导入操作 ID 和审批令牌';
        return;
    }
    actionLoading.value = true;
    actionMessage.value = '';
    try {
        const response = await store.executeDiagnosticAction(
            'replay_failed_ingest',
            operationId.value,
            approvalToken.value
        );
        actionMessage.value = `处置完成，新增 ${response.result.documents_indexed} 个文档，跳过 ${response.result.documents_skipped} 个文档`;
        await store.syncDashboard();
    } catch (error) {
        actionMessage.value = error instanceof Error ? error.message : '诊断处置失败';
    } finally {
        actionLoading.value = false;
    }
}

onMounted(() => {
    void refresh();
});
</script>

<style scoped lang="less">
.diagnostics-page {
    max-width: 1200px;
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

    &__metrics {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 12px;
        margin-bottom: 20px;
    }

    &__metric,
    &__section {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        background: #fff;
    }

    &__metric {
        display: grid;
        gap: 8px;
        color: #64748b;

        strong {
            color: #0f172a;
            font-size: 20px;
        }
    }

    &__section-header,
    &__search-row {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    &__section-header {
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 16px;
    }

    &__section-title {
        margin: 0;
        font-size: 16px;
    }

    &__action-grid {
        display: grid;
        grid-template-columns: minmax(180px, 0.5fr) minmax(260px, 1fr) auto;
        gap: 12px;
        align-items: end;

        label {
            display: grid;
            gap: 6px;
            color: #475569;
            font-size: 13px;
        }

        input {
            box-sizing: border-box;
            min-height: 38px;
            width: 100%;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            padding: 8px 10px;
            color: #0f172a;
        }
    }

    &__suggestions {
        display: grid;
        gap: 10px;
    }

    &__suggestion {
        border-left: 4px solid #94a3b8;
        padding: 12px 14px;
        background: #f8fafc;

        p {
            margin: 6px 0 0;
            color: #475569;
            line-height: 1.5;
        }

        &--critical {
            border-left-color: #dc2626;
            background: #fef2f2;
        }

        &--warning {
            border-left-color: #d97706;
            background: #fffbeb;
        }

        &--info {
            border-left-color: #2563eb;
            background: #eff6ff;
        }
    }

    &__suggestion-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;

        span {
            flex: 0 0 auto;
            color: #64748b;
            font-size: 12px;
        }
    }

    &__suggestion-action {
        font-size: 13px;
    }

    &__input {
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
    }

    &__message {
        margin: 12px 0;
        color: #1d4ed8;
    }

    &__result {
        border-top: 1px solid #e2e8f0;
        padding: 12px 0;

        a {
            color: #1d4ed8;
            font-weight: 600;
        }

        p {
            margin: 6px 0 0;
            color: #475569;
            line-height: 1.5;
        }
    }

    @media (max-width: 760px) {
        &__metrics {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }

        &__section-header,
        &__search-row {
            align-items: stretch;
            flex-direction: column;
        }

        &__action-grid {
            grid-template-columns: 1fr;
        }
    }
}
</style>
