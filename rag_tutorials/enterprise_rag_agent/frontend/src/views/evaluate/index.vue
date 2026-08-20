<template>
    <section class="evaluate-page">
        <PageHeader />

        <el-card shadow="never" class="evaluate-page__card">
            <el-row :gutter="12">
                <el-col :xs="24" class="evaluate-page__field">
                    <div class="evaluate-page__label">问题</div>
                    <el-input v-model="question" :rows="3" type="textarea" resize="none" />
                </el-col>
                <el-col :xs="24" class="evaluate-page__field">
                    <div class="evaluate-page__label">预期答案</div>
                    <el-input v-model="expectedAnswer" :rows="4" type="textarea" resize="none" />
                </el-col>
                <el-col :xs="24" class="evaluate-page__field">
                    <div class="evaluate-page__label">实际答案</div>
                    <el-input v-model="actualAnswer" :rows="4" type="textarea" resize="none" />
                </el-col>
                <el-col :xs="24" class="evaluate-page__actions">
                    <el-button type="primary" :loading="submitting" @click="submitEvaluation">提交评估</el-button>
                </el-col>
            </el-row>
        </el-card>

        <el-alert v-if="message" :title="message" type="info" show-icon class="evaluate-page__alert" />

        <el-card v-if="result" shadow="never" class="evaluate-page__card">
            <div class="evaluate-page__result-header">
                <el-tag type="success">得分 {{ result.score.toFixed(2) }}</el-tag>
            </div>
            <el-descriptions :column="1" border>
                <el-descriptions-item label="问题">{{ result.question }}</el-descriptions-item>
                <el-descriptions-item label="说明">{{ result.notes }}</el-descriptions-item>
            </el-descriptions>
        </el-card>

        <el-card shadow="never" class="evaluate-page__card">
            <div class="evaluate-page__result-header">
                <div>
                    <div class="evaluate-page__title">召回基准</div>
                    <div class="evaluate-page__hint">运行内置样例，比较命中率和 MRR。</div>
                </div>
                <el-button :loading="retrievalSubmitting" @click="runRetrievalEvaluation">
                    运行召回评估
                </el-button>
            </div>

            <el-empty
                v-if="!retrievalResult"
                description="当前还没有运行召回评估。"
                class="evaluate-page__empty"
            />

            <div v-else class="evaluate-page__metrics">
                <el-tag>样例 {{ retrievalResult.total }}</el-tag>
                <el-tag type="success">命中率 {{ (retrievalResult.hit_rate * 100).toFixed(1) }}%</el-tag>
                <el-tag type="warning">MRR {{ retrievalResult.mrr.toFixed(3) }}</el-tag>
            </div>

            <el-table v-if="retrievalResult" :data="retrievalResult.results" border stripe>
                <el-table-column label="结果" width="90">
                    <template #default="{ row }">
                        {{ row.hit ? '命中' : '未命中' }}
                    </template>
                </el-table-column>
                <el-table-column label="问题" prop="question" min-width="280" />
                <el-table-column label="排名" width="100">
                    <template #default="{ row }">
                        {{ row.rank || '-' }}
                    </template>
                </el-table-column>
            </el-table>
        </el-card>
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
.evaluate-page {
    min-width: 0;

    &__card,
    &__alert {
        margin-bottom: 12px;
    }

    &__field {
        margin-bottom: 12px;
    }

    &__label,
    &__hint {
        margin-bottom: 6px;
        color: #64748b;
        font-size: 13px;
    }

    &__actions {
        display: flex;
        justify-content: flex-end;
    }

    &__result-header {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 12px;
    }

    &__title {
        font-size: 16px;
        font-weight: 600;
        color: #0f172a;
    }

    &__metrics {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 12px;
    }
}
</style>
