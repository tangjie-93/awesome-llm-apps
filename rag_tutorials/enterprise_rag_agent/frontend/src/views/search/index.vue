<template>
    <section class="search-page">
        <PageHeader />

        <el-card shadow="never" class="search-page__card">
            <div class="search-page__form">
                <FormField label="问题">
                    <el-input v-model="question" type="textarea" :rows="3" resize="none" placeholder="请输入检索问题" />
                </FormField>
                <el-row :gutter="12" align="bottom">
                    <el-col :xs="24" :md="7">
                        <FormField label="知识库">
                            <el-input v-model="knowledgeBase" placeholder="general" />
                        </FormField>
                    </el-col>
                    <el-col :xs="24" :md="7">
                        <FormField label="权限组">
                            <el-input v-model="userGroupsText" placeholder="public,security" />
                        </FormField>
                    </el-col>
                    <el-col :xs="24" :md="4">
                        <FormField label="Top K">
                            <el-input-number v-model="topK" :min="1" :max="20" controls-position="right" class="search-page__number" />
                        </FormField>
                    </el-col>
                    <el-col :xs="24" :md="6" class="search-page__actions">
                        <el-button type="primary" :loading="submitting" class="search-page__submit" @click="submitSearch">
                            检索
                        </el-button>
                    </el-col>
                </el-row>
            </div>
        </el-card>

        <div class="search-page__results">
            <el-skeleton v-if="submitting" :rows="6" animated />

            <EmptyState
                v-else-if="!hasSearched"
                fill
                description="输入问题并点击检索，候选片段和混合检索打分会展示在这里。"
            />

            <EmptyState
                v-else-if="!results.length && !hasError"
                fill
                description="未检索到候选片段。请确认知识库、权限组或问题关键词。"
            />

            <el-space v-if="!submitting && results.length" fill direction="vertical" class="search-page__result-list">
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
        </div>
    </section>
</template>

<script setup lang="ts">
import { ElMessage } from 'element-plus';
import { ref } from 'vue';
import EmptyState from '@/components/ui/EmptyState.vue';
import FormField from '@/components/ui/FormField.vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';
import type { RagSearchItemView } from '@/types/rag';

const store = useRagStore();
const question = ref<string>('How fast should we acknowledge the incident?');
const knowledgeBase = ref<string>('');
const userGroupsText = ref<string>('public');
const topK = ref<number>(5);
const submitting = ref<boolean>(false);
const results = ref<RagSearchItemView[]>([]);
const hasSearched = ref<boolean>(false);
const hasError = ref<boolean>(false);

/**
 * 提交检索请求；成功时展示候选片段和打分，失败或无输入时展示明确提示。
 */
async function submitSearch(): Promise<void> {
    if (!question.value.trim()) {
        hasError.value = true;
        hasSearched.value = true;
        results.value = [];
        ElMessage.warning('请输入检索问题');
        return;
    }
    submitting.value = true;
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
        ElMessage.success(`返回 ${response.results.length} 条结果`);
    } catch (error) {
        hasError.value = true;
        results.value = [];
        ElMessage.error(error instanceof Error ? error.message : '检索失败');
    } finally {
        hasSearched.value = true;
        submitting.value = false;
    }
}
</script>

<style scoped lang="less">
.search-page {
    min-width: 0;
    height: 100%;
    display: flex;
    flex-direction: column;

    &__card {
        flex-shrink: 0;
        margin-bottom: 12px;
    }

    &__form {
        display: grid;
        gap: 12px;
    }

    &__number {
        width: 100%;
    }

    &__actions {
        display: flex;
        align-items: flex-end;
    }

    &__submit {
        min-width: 112px;
    }

    // 结果区铺满剩余高度，结果多时在内部滚动，页面不出现滚动条
    &__results {
        flex: 1;
        min-height: 0;
        overflow-y: auto;
    }

    &__result-list {
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
