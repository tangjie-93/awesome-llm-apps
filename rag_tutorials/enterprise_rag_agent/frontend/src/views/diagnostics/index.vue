<template>
    <section class="diagnostics-page">
        <PageHeader />

        <el-row :gutter="12" class="diagnostics-page__metrics">
            <el-col v-for="metric in metrics" :key="metric.label" :xs="12" :sm="12" :md="6">
                <el-card shadow="never" class="diagnostics-page__metric">
                    <div class="diagnostics-page__metric-label">{{ metric.label }}</div>
                    <div class="diagnostics-page__metric-value">{{ metric.value }}</div>
                </el-card>
            </el-col>
        </el-row>

        <el-card shadow="never" class="diagnostics-page__card">
            <div class="diagnostics-page__section-header">
                <div>
                    <div class="diagnostics-page__section-title">诊断建议</div>
                    <div class="diagnostics-page__hint">建议来自当前租户的运行指标，不会自动修改模型或排序配置。</div>
                </div>
            </div>
            <el-row :gutter="12">
                <el-col v-for="suggestion in suggestions" :key="suggestion.code" :xs="24" :md="8">
                    <el-card shadow="never" class="diagnostics-page__suggestion" :class="`diagnostics-page__suggestion--${suggestion.severity}`">
                        <div class="diagnostics-page__suggestion-header">
                            <strong>{{ suggestion.title }}</strong>
                            <el-tag size="small">{{ severityLabel(suggestion.severity) }}</el-tag>
                        </div>
                        <p>{{ suggestion.detail }}</p>
                        <p class="diagnostics-page__suggestion-action">建议：{{ suggestion.action }}</p>
                    </el-card>
                </el-col>
            </el-row>
        </el-card>

        <el-card shadow="never" class="diagnostics-page__card">
            <div class="diagnostics-page__section-header">
                <div>
                    <div class="diagnostics-page__section-title">人工处置</div>
                    <div class="diagnostics-page__hint">仅支持经过审批令牌确认的失败导入回放，执行结果会写入操作日志和审计日志。</div>
                </div>
            </div>
            <el-row :gutter="12" align="bottom">
                <el-col :xs="24" :md="8">
                    <div class="diagnostics-page__label">失败导入操作 ID</div>
                    <el-input v-model.number="operationId" type="number" min="1" placeholder="例如 12" />
                </el-col>
                <el-col :xs="24" :md="12">
                    <div class="diagnostics-page__label">审批令牌</div>
                    <el-input v-model.trim="approvalToken" type="password" autocomplete="off" placeholder="服务端配置的审批令牌" />
                </el-col>
                <el-col :xs="24" :md="4">
                    <el-button type="primary" :loading="actionLoading" class="diagnostics-page__submit" @click="executeAction">
                        回放失败导入
                    </el-button>
                </el-col>
            </el-row>
            <el-alert v-if="actionMessage" :title="actionMessage" type="info" show-icon class="diagnostics-page__alert" />
        </el-card>

        <el-card shadow="never" class="diagnostics-page__card">
            <div class="diagnostics-page__section-header">
                <div>
                    <div class="diagnostics-page__section-title">外部检索</div>
                    <div class="diagnostics-page__hint">
                        {{ store.diagnostics?.web_fallback_enabled ? '已启用受控 Web fallback。' : '当前未启用 Web fallback。' }}
                    </div>
                </div>
                <el-button :loading="loading" @click="refresh">刷新诊断</el-button>
            </div>
            <el-row :gutter="12" align="bottom">
                <el-col :xs="24" :md="20">
                    <div class="diagnostics-page__label">检索问题</div>
                    <el-input v-model.trim="question" placeholder="输入需要补充检索的问题" @keyup.enter="searchWeb" />
                </el-col>
                <el-col :xs="24" :md="4">
                    <el-button type="primary" :loading="searching" class="diagnostics-page__submit" @click="searchWeb">
                        检索
                    </el-button>
                </el-col>
            </el-row>
            <el-alert v-if="message" :title="message" type="info" show-icon class="diagnostics-page__alert" />
            <el-space v-if="results.length" fill direction="vertical" class="diagnostics-page__stack">
                <el-card v-for="result in results" :key="result.url" shadow="never">
                    <el-link :href="result.url" target="_blank" rel="noopener noreferrer">{{ result.title }}</el-link>
                    <p class="diagnostics-page__snippet">{{ result.snippet }}</p>
                </el-card>
            </el-space>
        </el-card>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
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
    min-width: 0;

    &__metrics,
    &__card {
        margin-bottom: 12px;
    }

    &__metric {
        height: 100%;
    }

    &__metric-label,
    &__hint,
    &__label,
    &__snippet,
    &__suggestion-action {
        color: #64748b;
        font-size: 13px;
    }

    &__metric-value {
        margin-top: 10px;
        font-size: 22px;
        font-weight: 700;
        color: #0f172a;
    }

    &__section-header,
    &__suggestion-header {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 12px;
    }

    &__section-title {
        font-size: 16px;
        font-weight: 600;
        color: #0f172a;
    }

    &__suggestion {
        height: 100%;
        margin-bottom: 12px;
        border-left: 3px solid #94a3b8;

        &--critical {
            border-left-color: #dc2626;
        }

        &--warning {
            border-left-color: #d97706;
        }

        &--info {
            border-left-color: #2563eb;
        }
    }

    &__submit {
        width: 100%;
    }

    &__alert {
        margin-top: 12px;
    }

    &__stack {
        width: 100%;
        margin-top: 12px;
    }
}
</style>
