<template>
    <section class="ask-page">
        <PageHeader />

        <el-card shadow="never" class="ask-page__card ask-page__card--form">
            <div class="ask-page__form">
                <div class="ask-page__label">问题</div>
                <el-input
                    v-model="question"
                    :rows="3"
                    type="textarea"
                    resize="none"
                    placeholder="请输入问题"
                />
                <div class="ask-page__actions">
                    <el-button
                        type="primary"
                        :loading="submitting"
                        class="ask-page__submit"
                        @click="submitQuestion"
                    >
                        提问
                    </el-button>
                </div>
            </div>
        </el-card>

        <el-card v-if="answer" shadow="never" class="ask-page__card">
            <div class="ask-page__result-header">
                <el-tag type="success">置信度 {{ answer.confidence.toFixed(2) }}</el-tag>
                <span v-if="answer.clarifying_question" class="ask-page__clarifying">{{ answer.clarifying_question }}</span>
            </div>
            <pre class="ask-page__answer">{{ answer.answer }}</pre>

            <el-empty
                v-if="!answer.citations.length"
                description="未返回引用来源，当前回答不能作为已验证结论。"
                class="ask-page__empty"
            />

            <div v-if="answer.citations.length" class="ask-page__section">
                <div class="ask-page__section-title">引用来源</div>
                <el-row :gutter="12">
                    <el-col v-for="citation in answer.citations" :key="citation.source + String(citation.chunk_index)" :xs="24" :md="12">
                        <el-card shadow="never" class="ask-page__citation">
                            <div class="ask-page__citation-title">{{ citation.knowledge_base }} / {{ citation.title }}</div>
                            <div class="ask-page__citation-meta">{{ citation.section_path }} 段 chunk {{ citation.chunk_index }} / {{ citation.risk_level }}</div>
                            <div class="ask-page__citation-terms">{{ citation.matched_terms.join(', ') }}</div>
                        </el-card>
                    </el-col>
                </el-row>
            </div>

            <div v-if="answer.evidence_snippets.length" class="ask-page__section">
                <div class="ask-page__section-title">证据片段</div>
                <el-space fill direction="vertical" class="ask-page__stack">
                    <el-card
                        v-for="snippet in answer.evidence_snippets"
                        :key="snippet.source + snippet.section_path"
                        shadow="never"
                        class="ask-page__evidence"
                    >
                        <div class="ask-page__citation-meta">
                            {{ snippet.knowledge_base }} / {{ snippet.section_path }} / {{ snippet.risk_level }}
                        </div>
                        <p class="ask-page__answer-text">{{ snippet.snippet }}</p>
                    </el-card>
                </el-space>
            </div>

            <div v-if="answer.external_sources.length" class="ask-page__section">
                <div class="ask-page__section-title">外部补充来源</div>
                <el-space fill direction="vertical" class="ask-page__stack">
                    <el-link
                        v-for="source in answer.external_sources"
                        :key="source.url"
                        :href="source.url"
                        target="_blank"
                        rel="noopener noreferrer"
                        class="ask-page__source"
                    >
                        <strong>{{ source.title }}</strong>
                        <span>{{ source.snippet }}</span>
                    </el-link>
                </el-space>
            </div>

            <div v-if="answer.tool_trace.length" class="ask-page__trace">
                调用链：{{ answer.tool_trace.join(' → ') }}
            </div>

            <div class="ask-page__feedback">
                <span>这次回答是否有帮助？</span>
                <el-button :loading="feedbackSubmitting" @click="submitFeedback(5)">有帮助</el-button>
                <el-button :loading="feedbackSubmitting" @click="submitFeedback(1)">需改进</el-button>
            </div>
        </el-card>
    </section>
</template>

<script setup lang="ts">
import { ElMessage } from 'element-plus';
import { ref } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';
import type { AnswerView } from '@/types/rag';

const store = useRagStore();
const question = ref<string>('How fast should we acknowledge the incident?');
const answer = ref<AnswerView | null>(null);
const submitting = ref<boolean>(false);
const feedbackSubmitting = ref<boolean>(false);

/**
 * 提交问答请求；成功时展示答案和引用，失败或空问题时展示明确提示。
 */
async function submitQuestion(): Promise<void> {
    if (!question.value.trim()) {
        answer.value = null;
        ElMessage.warning('请输入问题');
        return;
    }
    submitting.value = true;
    try {
        answer.value = await store.askQuestion(question.value.trim());
        if (!answer.value.citations.length) {
            ElMessage.info('未检索到可引用证据');
        }
    } catch (error) {
        answer.value = null;
        ElMessage.error(error instanceof Error ? error.message : '提问失败');
    } finally {
        submitting.value = false;
    }
}

/** 提交当前回答的简化人工反馈，并将状态反馈给用户。 */
async function submitFeedback(rating: number): Promise<void> {
    feedbackSubmitting.value = true;
    try {
        await store.submitFeedback(rating);
        ElMessage.success('感谢反馈，已记录到质量改进闭环。');
    } catch (error) {
        ElMessage.error(error instanceof Error ? error.message : '反馈提交失败');
    } finally {
        feedbackSubmitting.value = false;
    }
}
</script>

<style scoped lang="less">
.ask-page {
    min-width: 0;

    &__card {
        margin-bottom: 12px;
    }

    &__form {
        display: grid;
        gap: 10px;
    }

    &__label {
        color: #475569;
        font-size: 14px;
        font-weight: 600;
    }

    &__actions {
        display: flex;
        justify-content: flex-end;
    }

    &__submit {
        min-width: 112px;
    }

    &__result-header,
    &__feedback {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    &__result-header {
        justify-content: space-between;
        margin-bottom: 12px;
    }

    &__clarifying {
        color: #92400e;
    }

    &__answer,
    &__answer-text {
        margin: 0;
        white-space: pre-wrap;
        font-family: inherit;
        line-height: 1.6;
    }

    &__section {
        margin-top: 16px;
    }

    &__section-title {
        margin-bottom: 10px;
        font-weight: 600;
        color: #0f172a;
    }

    &__citation {
        height: 100%;
        margin-bottom: 12px;
    }

    &__citation-title {
        font-weight: 600;
    }

    &__citation-meta,
    &__citation-terms,
    &__trace {
        margin-top: 6px;
        color: #64748b;
        font-size: 13px;
    }

    &__source {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 4px;
        width: 100%;
        padding: 12px 14px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        text-decoration: none;
        color: inherit;
    }

    &__stack {
        width: 100%;
    }

    &__empty {
        margin-top: 10px;
    }
}
</style>
