<template>
    <section class="page">
        <header class="page__header">
            <div>
                <h1 class="page__title">检索</h1>
                <p class="page__subtitle">对应后端 search 命令，展示候选片段与打分</p>
            </div>
        </header>

        <div class="form">
            <label class="field field--full">
                <span class="field__label">问题</span>
                <textarea v-model="question" class="field__textarea" rows="4"></textarea>
            </label>
            <label class="field">
                <span class="field__label">知识库</span>
                <input v-model="knowledgeBase" class="field__input" type="text" placeholder="general" />
            </label>
            <label class="field">
                <span class="field__label">权限组</span>
                <input v-model="userGroupsText" class="field__input" type="text" placeholder="public,security" />
            </label>
            <label class="field">
                <span class="field__label">Top K</span>
                <input v-model.number="topK" class="field__input" type="number" min="1" max="20" />
            </label>
            <div class="actions">
                <button class="button button--primary" :disabled="submitting" @click="submitSearch">检索</button>
            </div>
        </div>

        <div v-if="message" class="alert">{{ message }}</div>

        <div v-if="results.length" class="results">
            <article v-for="item in results" :key="item.chunk.chunk_id" class="result-card">
                <div class="result-card__header">
                    <div>
                        <div class="result-card__title">{{ item.chunk.knowledge_base }} / {{ item.chunk.title }}</div>
                        <div class="result-card__meta">{{ item.chunk.section_path }} · chunk {{ item.chunk.chunk_index }} · {{ item.chunk.path }}</div>
                    </div>
                    <div class="result-card__score">{{ item.score.toFixed(3) }}</div>
                </div>
                <p class="result-card__text">{{ item.chunk.text }}</p>
                <div class="result-card__footer">
                    <span>词元 {{ item.chunk.token_count }}</span>
                    <span>lexical {{ item.lexical_score.toFixed(3) }}</span>
                    <span>rerank {{ item.rerank_score.toFixed(3) }}</span>
                    <span v-if="item.matched_terms.length">{{ item.matched_terms.join(', ') }}</span>
                </div>
            </article>
        </div>
    </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRagStore } from '@/store/rag';
import type { RagSearchItemView } from '@/types/rag';

const store = useRagStore();
const question = ref<string>('How fast should we acknowledge the incident?');
const knowledgeBase = ref<string>('');
const userGroupsText = ref<string>('public');
const topK = ref<number>(5);
const submitting = ref<boolean>(false);
const message = ref<string>('');
const results = ref<RagSearchItemView[]>([]);

async function submitSearch(): Promise<void> {
    submitting.value = true;
    message.value = '';
    try {
        const userGroups = userGroupsText.value
            .split(',')
            .map((group) => group.trim())
            .filter((group) => group.length > 0);
        const response = await store.searchQuestion(
            question.value,
            knowledgeBase.value.trim() || undefined,
            userGroups.length > 0 ? userGroups : undefined,
            topK.value
        );
        results.value = response.results;
        message.value = `返回 ${response.results.length} 条结果`;
    } catch (error) {
        message.value = error instanceof Error ? error.message : '检索失败';
        results.value = [];
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

    &__input,
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

.results {
    display: grid;
    gap: 12px;
    max-width: 1080px;
}

.result-card {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 16px;
    background: #fff;

    &__header {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        margin-bottom: 10px;
    }

    &__title {
        font-weight: 600;
    }

    &__meta,
    &__footer {
        margin-top: 4px;
        color: #64748b;
        font-size: 13px;
    }

    &__text {
        margin: 0;
        line-height: 1.6;
        white-space: pre-wrap;
    }

    &__footer {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 12px;
    }

    &__score {
        font-size: 18px;
        font-weight: 700;
        color: #1d4ed8;
    }
}
</style>
