<template>
    <section class="search-page">
        <PageHeader />

        <el-card shadow="never" class="search-page__card">
            <el-row :gutter="12" align="bottom">
                <el-col :xs="24" :md="10">
                    <div class="search-page__label">问题</div>
                    <el-input v-model="question" type="textarea" :rows="3" resize="none" placeholder="请输入检索问题" />
                </el-col>
                <el-col :xs="24" :md="4">
                    <div class="search-page__label">知识库</div>
                    <el-input v-model="knowledgeBase" placeholder="general" />
                </el-col>
                <el-col :xs="24" :md="4">
                    <div class="search-page__label">权限组</div>
                    <el-input v-model="userGroupsText" placeholder="public,security" />
                </el-col>
                <el-col :xs="24" :md="3">
                    <div class="search-page__label">Top K</div>
                    <el-input-number v-model="topK" :min="1" :max="20" controls-position="right" class="search-page__number" />
                </el-col>
                <el-col :xs="24" :md="3" class="search-page__actions">
                    <el-button type="primary" :loading="submitting" class="search-page__submit" @click="submitSearch">
                        检索
                    </el-button>
                </el-col>
            </el-row>
        </el-card>

        <el-alert v-if="message" :title="message" :type="hasError ? 'error' : 'info'" show-icon class="search-page__alert" />
        <el-empty
            v-if="hasSearched && !submitting && !results.length && !hasError"
            description="未检索到候选片段。请确认知识库、权限组或问题关键词。"
            class="search-page__empty"
        />

        <el-space v-if="results.length" fill direction="vertical" class="search-page__results">
            <el-card v-for="item in results" :key="item.chunk.chunk_id" shadow="never" class="search-page__result">
                <div class="search-page__result-header">
                    <div>
                        <div class="search-page__result-title">{{ item.chunk.knowledge_base }} / {{ item.chunk.title }}</div>
                        <div class="search-page__result-meta">
                            {{ item.chunk.section_path }} · chunk {{ item.chunk.chunk_index }} · {{ item.chunk.risk_level }} · {{ item.chunk.path }}
                        </div>
                    </div>
                    <div class="search-page__result-score">{{ item.score.toFixed(3) }}</div>
                </div>
                <p class="search-page__result-text">{{ item.chunk.text }}</p>
                <div class="search-page__result-footer">
                    <span>词元 {{ item.chunk.token_count }}</span>
                    <span>lexical {{ item.lexical_score.toFixed(3) }}</span>
                    <span>rerank {{ item.rerank_score.toFixed(3) }}</span>
                    <span v-if="item.matched_terms.length">{{ item.matched_terms.join(', ') }}</span>
                </div>
            </el-card>
        </el-space>
    </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
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
.search-page {
    min-width: 0;

    &__card {
        margin-bottom: 12px;
    }

    &__label {
        margin-bottom: 6px;
        color: #64748b;
        font-size: 13px;
    }

    &__number,
    &__submit {
        width: 100%;
    }

    &__actions {
        display: flex;
        align-items: flex-end;
    }

    &__alert,
    &__empty {
        margin-bottom: 12px;
    }

    &__results {
        width: 100%;
    }

    &__result {
        margin-bottom: 10px;
    }

    &__result-header,
    &__result-footer {
        display: flex;
        justify-content: space-between;
        gap: 12px;
    }

    &__result-title {
        font-weight: 600;
    }

    &__result-meta,
    &__result-footer {
        margin-top: 6px;
        color: #64748b;
        font-size: 13px;
    }

    &__result-text {
        margin: 12px 0 0;
        line-height: 1.6;
        white-space: pre-wrap;
    }

    &__result-score {
        color: #1d4ed8;
        font-size: 18px;
        font-weight: 700;
    }
}
</style>
