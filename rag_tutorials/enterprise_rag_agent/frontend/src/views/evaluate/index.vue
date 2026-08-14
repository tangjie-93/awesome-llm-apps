<template>
    <section class="page">
        <header class="page__header">
            <div>
                <h1 class="page__title">评估</h1>
                <p class="page__subtitle">对应后端 evaluate 命令，用于记录答案评分</p>
            </div>
        </header>

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
    </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRagStore } from '@/store/rag';
import type { RagEvaluationResultView } from '@/types/rag';

const store = useRagStore();
const question = ref<string>('How fast should we acknowledge the incident?');
const expectedAnswer = ref<string>('Within 15 minutes.');
const actualAnswer = ref<string>('Respond as quickly as possible.');
const submitting = ref<boolean>(false);
const message = ref<string>('');
const result = ref<RagEvaluationResultView | null>(null);

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
</script>

<style scoped lang="less">
.page {
    padding: 24px;

    &__header {
        margin-bottom: 24px;
    }

    &__title {
        margin: 0;
        font-size: 24px;
    }

    &__subtitle {
        margin: 8px 0 0;
        color: #64748b;
    }
}

.form {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
    margin-bottom: 20px;
    max-width: 1080px;
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
    margin-bottom: 16px;
    padding: 12px 14px;
    border-radius: 8px;
    background: #eff6ff;
    color: #1d4ed8;
}

.result {
    max-width: 1080px;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 16px;
    background: #fff;

    &__header {
        margin-bottom: 12px;
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
