<template>
    <section class="page">
        <header class="page__header">
            <div>
                <h1 class="page__title">提问</h1>
                <p class="page__subtitle">按知识库提问并查看引用</p>
            </div>
        </header>

        <div class="form">
            <label class="field field--full">
                <span class="field__label">问题</span>
                <textarea v-model="question" class="field__textarea" rows="4"></textarea>
            </label>
            <div class="actions">
                <button class="button button--primary" :disabled="submitting" @click="submitQuestion">提问</button>
                <button class="button" :disabled="submitting" @click="searchQuestion">检索</button>
            </div>
        </div>

        <article v-if="answer" class="result">
            <div class="result__header">
                <div class="result__score">置信度 {{ answer.confidence.toFixed(2) }}</div>
            </div>
            <pre class="result__text">{{ answer.answer }}</pre>
            <div v-if="answer.citations.length" class="citations">
                <h2 class="section-title">引用来源</h2>
                <div v-for="citation in answer.citations" :key="citation.source + String(citation.chunk_index)" class="citation">
                    <div class="citation__title">{{ citation.knowledge_base }} / {{ citation.title }}</div>
                    <div class="citation__meta">{{ citation.section_path }} 段 chunk {{ citation.chunk_index }}</div>
                    <div class="citation__terms">{{ citation.matched_terms.join(', ') }}</div>
                </div>
            </div>
        </article>
    </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRagStore } from '@/store/rag';
import type { AnswerView } from '@/types/rag';

const store = useRagStore();
const question = ref<string>('How fast should we acknowledge the incident?');
const answer = ref<AnswerView | null>(null);
const submitting = ref<boolean>(false);

async function submitQuestion(): Promise<void> {
    submitting.value = true;
    try {
        answer.value = await store.askQuestion(question.value);
    } finally {
        submitting.value = false;
    }
}

async function searchQuestion(): Promise<void> {
    submitting.value = true;
    try {
        const result = await store.searchQuestion(question.value);
        answer.value = {
            question: question.value,
            answer: JSON.stringify(result.results, null, 2),
            confidence: 0,
            knowledge_bases: [],
            citations: [],
            evidence_snippets: [],
            clarifying_question: null,
            sources_consulted: 0
        };
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

    &__input,
    &__textarea {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 10px 12px;
        font: inherit;
    }
}

.actions {
    display: flex;
    gap: 12px;
    align-items: end;
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

.result {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 16px;
    background: #fff;

    &__header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 12px;
    }

    &__score {
        font-weight: 600;
    }

    &__text {
        margin: 0;
        white-space: pre-wrap;
        font-family: inherit;
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
</style>
