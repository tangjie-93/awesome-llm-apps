<template>
    <section class="logs-page">
        <PageHeader>
            <template #actions>
                <el-button @click="refreshLogs">刷新</el-button>
            </template>
        </PageHeader>

        <PageSection fill title="运行日志" subtitle="集中查看问答、评估和导入任务记录">
            <FillTabs v-model="activeTab">
                <el-tab-pane label="回答日志" name="answers">
                    <DataTable :data="store.answerLogs" empty-description="暂无回答日志。">
                        <el-table-column label="问题" prop="question" min-width="280" show-overflow-tooltip />
                        <el-table-column label="置信度" width="110">
                            <template #default="{ row }">
                                <el-tag :type="row.confidence < 0.5 ? 'warning' : 'success'">
                                    {{ Number(row.confidence).toFixed(2) }}
                                </el-tag>
                            </template>
                        </el-table-column>
                        <el-table-column label="知识库" width="150">
                            <template #default="{ row }">
                                {{ String(row.metadata.knowledge_base ?? '全部知识库') }}
                            </template>
                        </el-table-column>
                        <el-table-column label="时间" prop="created_at" width="180" />
                    </DataTable>
                </el-tab-pane>

                <el-tab-pane label="评估日志" name="evaluations">
                    <DataTable :data="store.evaluationLogs" empty-description="暂无评估日志。">
                        <el-table-column label="问题" prop="question" min-width="260" show-overflow-tooltip />
                        <el-table-column label="实际答案" prop="actual_answer" min-width="260" show-overflow-tooltip />
                        <el-table-column label="得分" width="100">
                            <template #default="{ row }">
                                <el-tag :type="row.score < 0.6 ? 'warning' : 'success'">
                                    {{ Number(row.score).toFixed(2) }}
                                </el-tag>
                            </template>
                        </el-table-column>
                        <el-table-column label="时间" prop="created_at" width="180" />
                    </DataTable>
                </el-tab-pane>

                <el-tab-pane label="导入日志" name="operations">
                    <DataTable :data="store.operationLogs" empty-description="暂无导入日志。">
                        <el-table-column label="状态" width="110">
                            <template #default="{ row }">
                                <el-tag :type="row.status === 'succeeded' ? 'success' : 'danger'">
                                    {{ row.status === 'succeeded' ? '导入完成' : '导入失败' }}
                                </el-tag>
                            </template>
                        </el-table-column>
                        <el-table-column label="路径" prop="path" min-width="280" show-overflow-tooltip />
                        <el-table-column label="知识库" prop="knowledge_base" width="140" />
                        <el-table-column label="时间" prop="created_at" width="180" />
                        <el-table-column label="操作" width="100" fixed="right">
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
                    </DataTable>
                </el-tab-pane>
            </FillTabs>
        </PageSection>

        <el-alert v-if="message" :title="message" type="info" show-icon class="logs-page__alert" />
    </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import DataTable from '@/components/ui/DataTable.vue';
import FillTabs from '@/components/ui/FillTabs.vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import PageSection from '@/components/ui/PageSection.vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();
const replayingId = ref<number | null>(null);
const message = ref('');
const activeTab = ref('answers');

/** 刷新所有运行日志数据。 */
async function refreshLogs(): Promise<void> {
    await store.syncDashboard();
}

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

onMounted(() => {
    void refreshLogs();
});
</script>

<style scoped lang="less">
.logs-page {
    min-width: 0;
    height: 100%;
    display: flex;
    flex-direction: column;

    &__alert {
        flex-shrink: 0;
        margin-top: 12px;
    }
}
</style>
