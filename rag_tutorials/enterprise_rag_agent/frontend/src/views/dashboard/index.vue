<template>
    <section class="dashboard-page">
        <PageHeader>
            <template #actions>
                <el-button type="primary" :loading="refreshing" @click="refreshDashboard">刷新</el-button>
            </template>
        </PageHeader>

        <el-row :gutter="12" class="dashboard-page__metrics">
            <el-col v-for="metric in metrics" :key="metric.label" :xs="12" :sm="12" :md="6">
                <el-card shadow="never" class="dashboard-page__metric">
                    <div class="dashboard-page__metric-label">{{ metric.label }}</div>
                    <div class="dashboard-page__metric-value">{{ metric.value }}</div>
                </el-card>
            </el-col>
        </el-row>

        <el-alert v-if="store.error" :title="store.error" type="error" show-icon class="dashboard-page__alert" />
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();
const refreshing = ref(false);

const metrics = computed(() => [
    { label: '知识库', value: store.knowledgeBases.length },
    { label: '文档', value: store.documents.length },
    { label: '回答日志', value: store.answerLogs.length },
    { label: '评估日志', value: store.evaluationLogs.length }
]);

/**
 * 刷新仪表盘统计和最近数据。
 * 成功时更新全局 store，失败时由 store 自身记录错误状态。
 */
async function refreshDashboard(): Promise<void> {
    refreshing.value = true;
    try {
        await store.syncDashboard();
    } finally {
        refreshing.value = false;
    }
}

onMounted(() => {
    void refreshDashboard();
});
</script>

<style scoped lang="less">
.dashboard-page {
    min-width: 0;

    &__metrics {
        margin-bottom: 8px;
    }

    &__metric {
        height: 100%;
    }

    &__metric-label {
        color: #64748b;
        font-size: 13px;
    }

    &__metric-value {
        margin-top: 10px;
        font-size: 28px;
        font-weight: 700;
        color: #0f172a;
    }

    &__alert {
        margin-top: 12px;
    }
}
</style>
