<template>
    <section class="logs-page">
        <PageHeader />

        <el-row :gutter="12">
            <el-col :xs="24" :lg="8">
                <el-card shadow="never" class="logs-page__card">
                    <div class="logs-page__title">回答日志</div>
                    <el-table :data="store.answerLogs" border stripe size="small">
                        <el-table-column label="问题" prop="question" min-width="180" />
                        <el-table-column label="置信度" width="100">
                            <template #default="{ row }">
                                {{ Number(row.confidence).toFixed(2) }}
                            </template>
                        </el-table-column>
                        <el-table-column label="时间" prop="created_at" width="170" />
                    </el-table>
                    <el-empty v-if="!store.answerLogs.length" description="暂无回答日志。" />
                </el-card>
            </el-col>

            <el-col :xs="24" :lg="8">
                <el-card shadow="never" class="logs-page__card">
                    <div class="logs-page__title">评估日志</div>
                    <el-table :data="store.evaluationLogs" border stripe size="small">
                        <el-table-column label="问题" prop="question" min-width="180" />
                        <el-table-column label="得分" width="90">
                            <template #default="{ row }">
                                {{ Number(row.score).toFixed(2) }}
                            </template>
                        </el-table-column>
                        <el-table-column label="时间" prop="created_at" width="170" />
                    </el-table>
                    <el-empty v-if="!store.evaluationLogs.length" description="暂无评估日志。" />
                </el-card>
            </el-col>

            <el-col :xs="24" :lg="8">
                <el-card shadow="never" class="logs-page__card">
                    <div class="logs-page__title">导入日志</div>
                    <el-table :data="store.operationLogs" border stripe size="small">
                        <el-table-column label="状态" width="100">
                            <template #default="{ row }">
                                {{ row.status === 'succeeded' ? '导入完成' : '导入失败' }}
                            </template>
                        </el-table-column>
                        <el-table-column label="路径" prop="path" min-width="180" />
                        <el-table-column label="时间" prop="created_at" width="170" />
                        <el-table-column label="操作" width="100">
                            <template #default="{ row }">
                                <el-button
                                    v-if="row.operation === 'ingest' && row.path"
                                    size="small"
                                    :loading="replayingId === row.id"
                                    @click="replay(row.id)"
                                >
                                    回放
                                </el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                    <el-empty v-if="!store.operationLogs.length" description="暂无导入日志。" />
                </el-card>
            </el-col>
        </el-row>

        <el-alert v-if="message" :title="message" type="info" show-icon class="logs-page__alert" />
    </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();
const replayingId = ref<number | null>(null);
const message = ref('');

onMounted(() => {
    void store.syncDashboard();
});

/** 回放一次已记录的导入操作，并向用户反馈结果或失败原因。 */
async function replay(operationId: number): Promise<void> {
    replayingId.value = operationId;
    message.value = '';
    try {
        const result = await store.replayOperation(operationId);
        message.value = `回放完成：新增 ${result.documents_indexed}，跳过 ${result.documents_skipped}`;
    } catch (error) {
        message.value = error instanceof Error ? error.message : '回放失败';
    } finally {
        replayingId.value = null;
    }
}
</script>

<style scoped lang="less">
.logs-page {
    min-width: 0;

    &__card,
    &__alert {
        margin-bottom: 12px;
    }

    &__title {
        margin-bottom: 12px;
        font-size: 16px;
        font-weight: 600;
        color: #0f172a;
    }
}
</style>
