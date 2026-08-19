<template>
    <section class="page">
        <PageHeader />

        <div class="form">
            <label class="field field--full">
                <span class="field__label">问题</span>
                <textarea v-model="question" class="field__textarea" rows="3"></textarea>
            </label>
            <label class="field field--full">
                <span class="field__label">预期答案</span>
                <textarea v-model="expectedAnswer" class="field__textarea" rows="4"></textarea>
            </label>
            <label class="field field--full">
                <span class="field__label">实际答案</span>
                <textarea v-model="actualAnswer" class="field__textarea" rows="4"></textarea>
            </label>
            <div class="actions">
                <button class="button button--primary" :disabled="submitting" @click="submitEvaluation">提交评估</button>
            </div>
        </div>

        <div v-if="message" class="alert">{{ message }}</div>

        <article v-if="result" class="result">
            <div class="result__header">
                <div class="result__score">得分 {{ result.score.toFixed(2) }}</div>
            </div>
            <dl class="result__list">
                <div>
                    <dt>问题</dt>
                    <dd>{{ result.question }}</dd>
                </div>
                <div>
                    <dt>说明</dt>
                    <dd>{{ result.notes }}</dd>
                </div>
            </dl>
        </article>

        <article class="result result--retrieval">
            <div class="result__header">
                <div>
                    <h2 class="result__title">召回基准</h2>
                    <p class="result__hint">运行内置样例，比较命中率和 MRR。</p>
                </div>
                <button class="button" :disabled="retrievalSubmitting" @click="runRetrievalEvaluation">
                    {{ retrievalSubmitting ? '评估中...' : '运行召回评估' }}
                </button>
            </div>
            <div v-if="retrievalResult" class="result__metrics">
                <span>样例 {{ retrievalResult.total }}</span>
                <span>命中率 {{ (retrievalResult.hit_rate * 100).toFixed(1) }}%</span>
                <span>MRR {{ retrievalResult.mrr.toFixed(3) }}</span>
            </div>
            <div v-if="retrievalResult" class="result__cases">
                <div v-for="item in retrievalResult.results" :key="item.question" class="result__case">
                    <strong>{{ item.hit ? '命中' : '未命中' }}</strong>
                    <span>{{ item.question }}</span>
                    <span>排名 {{ item.rank || '-' }}</span>
                </div>
            </div>
        </article>
    </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';
import type { RagEvaluationResultView, RagRetrievalEvaluationView } from '@/types/rag';

const store = useRagStore();
const question = ref<string>('How fast should we acknowledge the incident?');
const expectedAnswer = ref<string>('Within 15 minutes.');
const actualAnswer = ref<string>('Respond as quickly as possible.');
const submitting = ref<boolean>(false);
const message = ref<string>('');
const result = ref<RagEvaluationResultView | null>(null);
const retrievalSubmitting = ref<boolean>(false);
const retrievalResult = ref<RagRetrievalEvaluationView | null>(null);

async function submitEvaluation(): Promise<void> {
    submitting.value = true;
    message.value = '';
    try {
        result.value = await store.evaluateAnswer(question.value, expectedAnswer.value.trim() || null, actualAnswer.value);
        message.value = '评估已提交';
        await store.syncDashboard();
    } catch (error) {
        message.value = error instanceof Error ? error.message : '评估失败';
    } finally {
        submitting.value = false;
    }
}

/** 运行内置召回评估并展示可比较的命中率与 MRR。 */
async function runRetrievalEvaluation(): Promise<void> {
    retrievalSubmitting.value = true;
    message.value = '';
    try {
        retrievalResult.value = await store.evaluateRetrieval();
    } catch (error) {
        message.value = error instanceof Error ? error.message : '召回评估失败';
    } finally {
        retrievalSubmitting.value = false;
    }
}
</script>

<style scoped lang="less">
.page {
    min-width: 0;
}

.form {
    display: grid;
    grid-template-columns: 1fr;
    gap: 12px;
    margin-bottom: 14px;
}

.field {
    display: grid;
    gap: 8px;

    &--full {
        grid-column: 1 / -1;
    }

    &__label {
        font-size: 13px;
        color: #64748b;
    }

    &__textarea {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 10px 12px;
        font: inherit;
    }
}

.actions {
    grid-column: 1 / -1;
}

.button {
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 10px 14px;
    background: #fff;
    cursor: pointer;

    &--primary {
        border-color: #1d4ed8;
        background: #1d4ed8;
        color: #fff;
    }
}

.alert {
    margin-bottom: 12px;
    padding: 11px 12px;
    border-radius: 8px;
    background: #eff6ff;
    color: #1d4ed8;
}

.result {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px;
    background: #fff;

    &__header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 12px;
    }

    &__title {
        margin: 0;
        font-size: 17px;
    }

    &__hint {
        margin: 4px 0 0;
        color: #64748b;
        font-size: 13px;
    }

    &__metrics {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-bottom: 12px;
        color: #1d4ed8;
        font-weight: 600;
    }

    &__cases {
        display: grid;
        gap: 8px;
    }

    &__case {
        display: grid;
        grid-template-columns: 56px minmax(0, 1fr) 64px;
        gap: 10px;
        padding-top: 8px;
        border-top: 1px solid #e2e8f0;
        font-size: 13px;
    }

    &__score {
        font-size: 20px;
        font-weight: 700;
        color: #1d4ed8;
    }

    &__list {
        display: grid;
        gap: 14px;

        dt {
            font-size: 13px;
            color: #64748b;
        }

        dd {
            margin: 4px 0 0;
            white-space: pre-wrap;
            line-height: 1.6;
        }
    }
}
</style>
