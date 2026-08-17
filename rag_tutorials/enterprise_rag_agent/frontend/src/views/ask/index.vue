<template>
    <section class="page">
        <header class="page__header">
            <div>
                <h1 class="page__title">提问</h1>
                <p class="page__subtitle">按知识库提问并查看回答与引用</p>
            </div>
        </header>

        <div class="form">
            <label class="field field--full">
                <span class="field__label">问题</span>
                <textarea v-model="question" class="field__textarea" rows="4"></textarea>
            </label>
            <div class="actions">
                <button
                    class="button button--primary"
                    :aria-busy="submitting"
                    :disabled="submitting"
                    @click="submitQuestion"
                >
                    <LoaderCircle v-if="submitting" class="button__spinner" :size="16" aria-hidden="true" />
                    {{ submitting ? '生成中...' : '提问' }}
                </button>
            </div>
        </div>

        <div v-if="message" class="alert" :class="{ 'alert--error': hasError }">{{ message }}</div>

        <article v-if="answer" class="result">
            <div class="result__header">
                <div class="result__score">置信度 {{ answer.confidence.toFixed(2) }}</div>
                <div v-if="answer.clarifying_question" class="result__hint">{{ answer.clarifying_question }}</div>
            </div>
            <pre class="result__text">{{ answer.answer }}</pre>
            <div v-if="!answer.citations.length" class="empty">未返回引用来源，当前回答不能作为已验证结论。</div>
            <div v-if="answer.citations.length" class="citations">
                <h2 class="section-title">引用来源</h2>
                <div v-for="citation in answer.citations" :key="citation.source + String(citation.chunk_index)" class="citation">
                    <div class="citation__title">{{ citation.knowledge_base }} / {{ citation.title }}</div>
                    <div class="citation__meta">{{ citation.section_path }} 段 chunk {{ citation.chunk_index }} / {{ citation.risk_level }}</div>
                    <div class="citation__terms">{{ citation.matched_terms.join(', ') }}</div>
                </div>
            </div>
            <div v-if="answer.evidence_snippets.length" class="evidence">
                <h2 class="section-title">证据片段</h2>
                <article
                    v-for="snippet in answer.evidence_snippets"
                    :key="snippet.source + snippet.section_path"
                    class="evidence__item"
                >
                    <div class="evidence__meta">
                        {{ snippet.knowledge_base }} / {{ snippet.section_path }} / {{ snippet.risk_level }}
                    </div>
                    <p class="evidence__text">{{ snippet.snippet }}</p>
                </article>
            </div>
        </article>
    </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { LoaderCircle } from 'lucide-vue-next';
import { useRagStore } from '@/store/rag';
import type { AnswerView } from '@/types/rag';

const store = useRagStore();
const question = ref<string>('How fast should we acknowledge the incident?');
const answer = ref<AnswerView | null>(null);
const submitting = ref<boolean>(false);
const message = ref<string>('');
const hasError = ref<boolean>(false);

/**
 * 提交问答请求；成功时展示答案和引用，失败或空问题时展示明确提示。
 */
async function submitQuestion(): Promise<void> {
    if (!question.value.trim()) {
        message.value = '请输入问题';
        hasError.value = true;
        answer.value = null;
        return;
    }
    submitting.value = true;
    message.value = '';
    hasError.value = false;
    try {
        answer.value = await store.askQuestion(question.value.trim());
        if (!answer.value.citations.length) {
            message.value = '未检索到可引用证据';
        }
    } catch (error) {
        message.value = error instanceof Error ? error.message : '提问失败';
        hasError.value = true;
        answer.value = null;
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
    margin-bottom: 24px;
    max-width: 960px;
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

    &__spinner {
        margin-right: 6px;
        vertical-align: -3px;
        animation: spin 0.8s linear infinite;
    }
}

.alert,
.empty {
    margin-bottom: 16px;
    border-radius: 8px;
    padding: 12px 14px;
}

.alert {
    max-width: 960px;
    background: #eff6ff;
    color: #1d4ed8;

    &--error {
        background: #fef2f2;
        color: #b91c1c;
    }
}

.empty {
    margin-top: 14px;
    border: 1px dashed #cbd5e1;
    background: #f8fafc;
    color: #64748b;
}

.result {
    max-width: 960px;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 16px;
    background: #fff;

    &__header {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        margin-bottom: 12px;
    }

    &__score {
        font-weight: 600;
    }

    &__hint {
        color: #92400e;
    }

    &__text {
        margin: 0;
        white-space: pre-wrap;
        font-family: inherit;
        line-height: 1.6;
    }
}

.section-title {
    margin: 20px 0 12px;
    font-size: 16px;
}

.citation {
    padding: 12px 0;
    border-top: 1px solid #e2e8f0;

    &__title {
        font-weight: 600;
    }

    &__meta,
    &__terms {
        margin-top: 4px;
        color: #64748b;
        font-size: 13px;
    }
}

.evidence {
    &__item {
        padding: 12px 0;
        border-top: 1px solid #e2e8f0;
    }

    &__meta {
        color: #64748b;
        font-size: 13px;
    }

    &__text {
        margin: 8px 0 0;
        line-height: 1.6;
        white-space: pre-wrap;
    }
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}
</style>
