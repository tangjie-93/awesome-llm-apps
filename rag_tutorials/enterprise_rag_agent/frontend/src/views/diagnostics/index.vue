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
import type { RagWebSearchResultView } from '@/types/rag';

const store = useRagStore();
const question = ref('');
const results = ref<RagWebSearchResultView[]>([]);
const message = ref('');
const loading = ref(false);
const searching = ref(false);
const metrics = computed(() => [
    { label: '文档', value: store.diagnostics?.documents ?? 0 },
    { label: '切块', value: store.diagnostics?.chunks ?? 0 },
    { label: '低置信度回答', value: store.diagnostics?.low_confidence_answers ?? 0 },
    { label: '反馈均分', value: store.diagnostics?.feedback.average_rating ?? 0 }
]);

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
    }
}
</style>
