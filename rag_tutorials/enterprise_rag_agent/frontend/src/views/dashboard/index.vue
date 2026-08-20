<template>
    <section class="dashboard-page">
        <PageHeader>
            <template #actions>
                <el-button type="primary" :loading="refreshing" @click="refreshDashboard">刷新</el-button>
            </template>
        </PageHeader>

        <el-row :gutter="12" class="dashboard-page__metrics">
            <el-col v-for="metric in metrics" :key="metric.label" :xs="12" :sm="12" :md="6">
                <MetricCard :label="metric.label" :value="metric.value" :hint="metric.hint" :type="metric.type" />
            </el-col>
        </el-row>

        <PageSection title="近期动态" subtitle="最近产生的问答记录、导入任务和索引结果">
            <template #actions>
                <el-button @click="goTo('/ask')">去提问</el-button>
                <el-button @click="goTo('/documents')">查看文档</el-button>
            </template>

            <el-tabs v-model="activeRecentTab" class="dashboard-page__tabs">
                <el-tab-pane label="近期回答" name="answers">
                    <EmptyState
                        v-if="!recentAnswerLogs.length"
                        description="暂无回答日志。可以先发起一次智能问答。"
                        action-label="去提问"
                        @action="goTo('/ask')"
                    />
                    <el-table v-else :data="recentAnswerLogs" border stripe class="dashboard-page__table">
                        <el-table-column label="问题" prop="question" min-width="420" show-overflow-tooltip />
                        <el-table-column label="置信度" width="110">
                            <template #default="{ row }">
                                <el-tag :type="row.confidence < 0.5 ? 'warning' : 'success'">
                                    {{ Number(row.confidence).toFixed(2) }}
                                </el-tag>
                            </template>
                        </el-table-column>
                        <el-table-column label="知识库" width="140">
                            <template #default="{ row }">
                                {{ String(row.metadata.knowledge_base ?? '全部知识库') }}
                            </template>
                        </el-table-column>
                        <el-table-column label="时间" prop="created_at" width="180" />
                    </el-table>
                </el-tab-pane>
                <el-tab-pane label="导入动态" name="operations">
                    <EmptyState
                        v-if="!recentOperationLogs.length"
                        description="暂无导入日志。导入文档后这里会显示最近任务。"
                        action-label="导入文档"
                        @action="goTo('/ingest')"
                    />
                    <el-table v-else :data="recentOperationLogs" border stripe class="dashboard-page__table">
                        <el-table-column label="状态" width="120">
                            <template #default="{ row }">
                                <el-tag :type="row.status === 'succeeded' ? 'success' : 'danger'">
                                    {{ row.status === 'succeeded' ? '导入完成' : '导入失败' }}
                                </el-tag>
                            </template>
                        </el-table-column>
                        <el-table-column label="路径" prop="path" min-width="420" show-overflow-tooltip />
                        <el-table-column label="时间" prop="created_at" width="180" />
                    </el-table>
                </el-tab-pane>
            </el-tabs>
        </PageSection>

        <PageSection title="待关注问题" subtitle="低置信度回答和评估记录会影响知识库质量">
            <el-tabs v-model="activeAttentionTab" class="dashboard-page__tabs">
                <el-tab-pane :label="`低置信度回答 ${lowConfidenceCount}`" name="lowConfidence">
                    <EmptyState
                        v-if="!lowConfidenceLogs.length"
                        description="暂无低置信度回答。"
                    />
                    <el-table v-else :data="lowConfidenceLogs" border stripe class="dashboard-page__table">
                        <el-table-column label="问题" prop="question" min-width="420" show-overflow-tooltip />
                        <el-table-column label="置信度" width="110">
                            <template #default="{ row }">
                                <el-tag type="warning">{{ Number(row.confidence).toFixed(2) }}</el-tag>
                            </template>
                        </el-table-column>
                        <el-table-column label="时间" prop="created_at" width="180" />
                    </el-table>
                </el-tab-pane>
                <el-tab-pane :label="`评估记录 ${recentEvaluationLogs.length}`" name="evaluations">
                    <EmptyState
                        v-if="!recentEvaluationLogs.length"
                        description="暂无评估记录。"
                    />
                    <el-table v-else :data="recentEvaluationLogs" border stripe class="dashboard-page__table">
                        <el-table-column label="问题" prop="question" min-width="420" show-overflow-tooltip />
                        <el-table-column label="得分" width="100">
                            <template #default="{ row }">
                                <el-tag :type="row.score < 0.6 ? 'warning' : 'success'">
                                    {{ Number(row.score).toFixed(2) }}
                                </el-tag>
                            </template>
                        </el-table-column>
                        <el-table-column label="时间" prop="created_at" width="180" />
                    </el-table>
                </el-tab-pane>
            </el-tabs>
        </PageSection>
    </section>
</template>

<script setup lang="ts">
import { ElMessage } from 'element-plus';
import { computed, onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import EmptyState from '@/components/ui/EmptyState.vue';
import MetricCard from '@/components/ui/MetricCard.vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import PageSection from '@/components/ui/PageSection.vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();
const router = useRouter();
const refreshing = ref(false);
const activeRecentTab = ref('answers');
const activeAttentionTab = ref('lowConfidence');

const metrics = computed(() => [
    { label: '知识库', value: store.knowledgeBases.length, hint: '当前可路由知识库', type: 'default' as const },
    { label: '文档', value: store.documents.length, hint: '已完成索引文档', type: 'success' as const },
    { label: '回答日志', value: store.answerLogs.length, hint: '累计问答记录', type: 'default' as const },
    { label: '低置信度', value: lowConfidenceCount.value, hint: '需要人工关注', type: lowConfidenceCount.value ? 'warning' as const : 'default' as const }
]);
const recentAnswerLogs = computed(() => store.answerLogs.slice(0, 5));
const recentEvaluationLogs = computed(() => store.evaluationLogs.slice(0, 5));
const recentOperationLogs = computed(() => store.operationLogs.slice(0, 5));
const lowConfidenceCount = computed(() => store.answerLogs.filter((log) => log.confidence < 0.5).length);
const lowConfidenceLogs = computed(() => store.answerLogs.filter((log) => log.confidence < 0.5).slice(0, 5));

/**
 * 刷新仪表盘统计和最近数据。
 * 成功时更新全局 store，失败时由 store 自身记录错误状态。
 */
async function refreshDashboard(): Promise<void> {
    refreshing.value = true;
    try {
        await store.syncDashboard();
        if (store.error) {
            ElMessage.error(store.error);
        }
    } finally {
        refreshing.value = false;
    }
}

/**
 * 跳转到指定功能页面。
 * @param path 目标路由路径。
 */
function goTo(path: string): void {
    void router.push(path);
}

onMounted(() => {
    void refreshDashboard();
});
</script>

<style scoped lang="less">
.dashboard-page {
    min-width: 0;

    &__metrics {
        margin-bottom: 12px;
    }

    &__tabs {
        --el-tabs-header-height: 40px;
    }

    &__table {
        width: 100%;
    }

    :deep(.el-tabs__header) {
        margin-bottom: 12px;
    }

    :deep(.el-tabs__nav-wrap::after) {
        height: 1px;
    }
}
</style>
