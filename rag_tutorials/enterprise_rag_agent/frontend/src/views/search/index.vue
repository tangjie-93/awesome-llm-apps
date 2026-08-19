<template>
    <section class="page">
        <PageHeader />

        <div class="form">
            <label class="field field--full field--question">
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
                <button
                    class="button button--primary"
                    :aria-busy="submitting"
                    :disabled="submitting"
                    @click="submitSearch"
                >
                    <LoaderCircle v-if="submitting" class="button__spinner" :size="16" aria-hidden="true" />
                    {{ submitting ? '检索中...' : '检索' }}
                </button>
            </div>
        </div>

        <div v-if="message" class="alert" :class="{ 'alert--error': hasError }">{{ message }}</div>
        <div v-if="hasSearched && !submitting && !results.length && !hasError" class="empty">
            未检索到候选片段。请确认知识库、权限组或问题关键词。
        </div>

        <div v-if="results.length" class="results">
            <article v-for="item in results" :key="item.chunk.chunk_id" class="result-card">
                <div class="result-card__header">
                    <div>
                        <div class="result-card__title">{{ item.chunk.knowledge_base }} / {{ item.chunk.title }}</div>
                        <div class="result-card__meta">{{ item.chunk.section_path }} · chunk {{ item.chunk.chunk_index }} · {{ item.chunk.risk_level }} · {{ item.chunk.path }}</div>
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
import { LoaderCircle } from 'lucide-vue-next';
import PageHeader from '@/components/ui/PageHeader.vue';
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
const hasSearched = ref<boolean>(false);
const hasError = ref<boolean>(false);

/**
 * 提交检索请求；成功时展示候选片段和打分，失败或无输入时展示明确提示。
 */
async function submitSearch(): Promise<void> {
    if (!question.value.trim()) {
        message.value = '请输入检索问题';
        hasError.value = true;
        hasSearched.value = true;
        results.value = [];
        return;
    }
    submitting.value = true;
    message.value = '';
    hasError.value = false;
    try {
        const userGroups = userGroupsText.value
            .split(',')
            .map((group) => group.trim())
            .filter((group) => group.length > 0);
        const response = await store.searchQuestion(
            question.value.trim(),
            knowledgeBase.value.trim() || undefined,
            userGroups.length > 0 ? userGroups : undefined,
            topK.value
        );
        results.value = response.results;
        message.value = `返回 ${response.results.length} 条结果`;
    } catch (error) {
        message.value = error instanceof Error ? error.message : '检索失败';
        hasError.value = true;
        results.value = [];
    } finally {
        hasSearched.value = true;
        submitting.value = false;
    }
}
</script>

<style scoped lang="less">
.page {
    min-width: 0;
}

.form {
    display: grid;
    grid-template-columns: minmax(0, 1.15fr) minmax(160px, 0.7fr) minmax(160px, 0.7fr) auto;
    gap: 12px;
    align-items: end;
    margin-bottom: 14px;
}

.field {
    display: grid;
    gap: 8px;

    &--full {
        grid-column: 1 / -1;
    }

    &--question {
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
    grid-column: 4;
    display: flex;
    justify-content: flex-end;
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

    &__spinner {
        margin-right: 6px;
        vertical-align: -3px;
        animation: spin 0.8s linear infinite;
    }
}

.alert {
    margin-bottom: 12px;
    padding: 12px 14px;
    border-radius: 8px;
    background: #eff6ff;
    color: #1d4ed8;

    &--error {
        background: #fef2f2;
        color: #b91c1c;
    }
}

.empty {
    margin-bottom: 12px;
    border: 1px dashed #cbd5e1;
    border-radius: 8px;
    padding: 12px 14px;
    background: #f8fafc;
    color: #64748b;
}

.results {
    display: grid;
    gap: 10px;
}

.result-card {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px;
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

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}

@media (max-width: 1100px) {
    .form {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .actions {
        grid-column: 1 / -1;
        justify-content: flex-start;
    }
}

@media (max-width: 720px) {
    .form {
        grid-template-columns: 1fr;
    }

    .actions {
        grid-column: 1;
    }
}
</style>
