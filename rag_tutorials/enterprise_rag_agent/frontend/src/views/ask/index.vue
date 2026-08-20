<template>
    <section class="ask-page">
        <PageHeader />

        <el-row :gutter="12" class="ask-page__columns">
            <el-col :xs="24" :md="14">
                <el-card shadow="never" class="ask-page__panel">
                    <div class="ask-page__form">
                        <FormField label="问题">
                            <el-input
                                v-model="question"
                                :autosize="{ minRows: 3, maxRows: 8 }"
                                type="textarea"
                                resize="none"
                                placeholder="请输入问题"
                                @keyup.ctrl.enter="submitQuestion"
                            />
                        </FormField>
                        <div class="ask-page__actions">
                            <span class="ask-page__shortcut">Ctrl + Enter 快速提问</span>
                            <el-button type="primary" :loading="submitting" class="ask-page__submit" @click="submitQuestion">
                                提问
                            </el-button>
                        </div>
                    </div>

                    <el-divider />

                    <div class="ask-page__answer-area">
                        <el-skeleton v-if="submitting" :rows="5" animated />
                        <EmptyState
                            v-else-if="!answer"
                            fill
                            description="输入问题后点击提问，回答会展示在这里。"
                        />
                        <div v-else class="ask-page__answer">
                            <div class="ask-page__result-header">
                                <el-tag :type="answer.confidence < 0.5 ? 'warning' : 'success'">
                                    置信度 {{ answer.confidence.toFixed(2) }}
                                </el-tag>
                                <span v-if="answer.clarifying_question" class="ask-page__clarifying">
                                    {{ answer.clarifying_question }}
                                </span>
                            </div>
                            <pre class="ask-page__answer-text">{{ answer.answer }}</pre>
                            <div class="ask-page__feedback">
                                <span>这次回答是否有帮助？</span>
                                <el-button size="small" :loading="feedbackSubmitting" @click="submitFeedback(5)">有帮助</el-button>
                                <el-button size="small" :loading="feedbackSubmitting" @click="submitFeedback(1)">需改进</el-button>
                            </div>
                        </div>
                    </div>
                </el-card>
            </el-col>

            <el-col :xs="24" :md="10">
                <el-card shadow="never" class="ask-page__panel">
                    <template #header>
                        <span class="ask-page__panel-title">引用与证据</span>
                    </template>
                    <div class="ask-page__sources">
                        <EmptyState
                            v-if="!answer"
                            fill
                            description="提交问题后展示引用来源、证据片段和外部补充。"
                        />
                        <el-empty
                            v-else-if="!answer.citations.length && !answer.evidence_snippets.length"
                            description="未返回引用来源，当前回答不能作为已验证结论。"
                        />

                        <template v-if="answer">
                            <div v-if="answer.citations.length" class="ask-page__section">
                                <div class="ask-page__section-title">引用来源</div>
                                <el-space fill direction="vertical" class="ask-page__stack">
                                    <el-card
                                        v-for="citation in answer.citations"
                                        :key="citation.source + String(citation.chunk_index)"
                                        shadow="never"
                                        class="ask-page__citation"
                                    >
                                        <div class="ask-page__citation-title">{{ citation.knowledge_base }} / {{ citation.title }}</div>
                                        <div class="ask-page__citation-meta">
                                            {{ citation.section_path }} · chunk {{ citation.chunk_index }} · {{ citation.risk_level }}
                                        </div>
                                        <div class="ask-page__citation-terms">{{ citation.matched_terms.join(', ') }}</div>
                                    </el-card>
                                </el-space>
                            </div>

                            <div v-if="answer.evidence_snippets.length" class="ask-page__section">
                                <div class="ask-page__section-title">证据片段</div>
                                <el-space fill direction="vertical" class="ask-page__stack">
                                    <el-card
                                        v-for="snippet in answer.evidence_snippets"
                                        :key="snippet.source + snippet.section_path"
                                        shadow="never"
                                    >
                                        <div class="ask-page__citation-meta">
                                            {{ snippet.knowledge_base }} / {{ snippet.section_path }} / {{ snippet.risk_level }}
                                        </div>
                                        <p class="ask-page__snippet-text">{{ snippet.snippet }}</p>
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
                        </template>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </section>
</template>

<script setup lang="ts">
import { ElMessage } from 'element-plus';
import { ref } from 'vue';
import EmptyState from '@/components/ui/EmptyState.vue';
import FormField from '@/components/ui/FormField.vue';
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
    height: 100%;
    display: flex;
    flex-direction: column;

    // 双栏铺满剩余高度：窄屏堆叠时恢复自然高度并允许页面内滚动
    &__columns {
        flex: 1;
        min-height: 0;

        :deep(> .el-col) {
            height: 100%;
        }
    }

    &__panel {
        height: 100%;
        display: flex;
        flex-direction: column;
        overflow: hidden;

        :deep(.el-card__body) {
            flex: 1;
            min-height: 0;
            display: flex;
            flex-direction: column;
        }
    }

    &__panel-title {
        font-weight: 600;
    }

    &__form {
        flex-shrink: 0;
        display: grid;
        gap: 10px;
    }

    &__actions {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
    }

    &__shortcut {
        color: #94a3b8;
        font-size: 12px;
    }

    &__submit {
        min-width: 112px;
    }

    // 答案区占满左栏剩余高度，内容多时内部滚动
    &__answer-area {
        flex: 1;
        min-height: 0;
        display: flex;
        flex-direction: column;
        overflow-y: auto;
    }

    &__answer {
        display: flex;
        flex-direction: column;
    }

    &__result-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
        margin-bottom: 12px;
    }

    &__clarifying {
        color: #92400e;
        font-size: 13px;
    }

    &__answer-text,
    &__snippet-text {
        margin: 0;
        white-space: pre-wrap;
        font-family: inherit;
        line-height: 1.6;
    }

    &__feedback {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-top: 16px;
        padding-top: 12px;
        border-top: 1px solid #eef2f7;
    }

    // 引用区占满右栏剩余高度，内容多时内部滚动
    &__sources {
        flex: 1;
        min-height: 0;
        overflow-y: auto;
    }

    &__section {
        margin-bottom: 16px;
    }

    &__section-title {
        margin-bottom: 10px;
        font-weight: 600;
        color: #0f172a;
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

    // 窄屏单列：双栏卡片恢复自然高度，由内容撑开
    @media (max-width: 991px) {
        &__columns {
            display: block;
            overflow-y: auto;

            :deep(> .el-col) {
                height: auto;
            }
        }

        &__panel {
            height: auto;
            margin-bottom: 12px;

            :deep(.el-card__body) {
                overflow: visible;
            }
        }

        &__answer-area,
        &__sources {
            overflow: visible;
        }
    }
}
</style>
