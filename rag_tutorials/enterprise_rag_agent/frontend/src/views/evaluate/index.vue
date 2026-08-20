<template>
    <section class="evaluate-page">
        <PageHeader />

        <PageSection title="答案评估">
            <el-row :gutter="12">
                <el-col :xs="24" class="evaluate-page__field">
                    <FormField label="问题">
                        <el-input v-model="question" :rows="3" type="textarea" resize="none" />
                    </FormField>
                </el-col>
                <el-col :xs="24" class="evaluate-page__field">
                    <FormField label="预期答案">
                        <el-input v-model="expectedAnswer" :rows="4" type="textarea" resize="none" />
                    </FormField>
                </el-col>
                <el-col :xs="24" class="evaluate-page__field">
                    <FormField label="实际答案">
                        <el-input v-model="actualAnswer" :rows="4" type="textarea" resize="none" />
                    </FormField>
                </el-col>
                <el-col :xs="24" class="evaluate-page__actions">
                    <el-button type="primary" :loading="submitting" @click="submitEvaluation">提交评估</el-button>
                </el-col>
            </el-row>
        </PageSection>

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

        <PageSection fill title="召回基准" subtitle="运行内置样例，比较命中率和 MRR。">
            <template #actions>
                <el-button :loading="retrievalSubmitting" @click="runRetrievalEvaluation">
                    运行召回评估
                </el-button>
            </template>

            <div v-if="retrievalResult" class="evaluate-page__metrics">
                <el-tag>样例 {{ retrievalResult.total }}</el-tag>
                <el-tag type="success">命中率 {{ (retrievalResult.hit_rate * 100).toFixed(1) }}%</el-tag>
                <el-tag type="warning">MRR {{ retrievalResult.mrr.toFixed(3) }}</el-tag>
            </div>

            <DataTable :data="retrievalResult?.results ?? []" empty-description="当前还没有运行召回评估。">
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
            </DataTable>
        </PageSection>
    </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import DataTable from '@/components/ui/DataTable.vue';
import FormField from '@/components/ui/FormField.vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import PageSection from '@/components/ui/PageSection.vue';
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
    height: 100%;
    display: flex;
    flex-direction: column;

    &__card,
    &__alert {
        flex-shrink: 0;
        margin-bottom: 12px;
    }

    &__field {
        margin-bottom: 12px;
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

    &__metrics {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 12px;
    }
}
</style>
