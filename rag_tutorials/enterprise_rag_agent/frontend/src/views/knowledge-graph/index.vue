<template>
    <section class="knowledge-graph-page">
        <PageHeader>
            <template #actions>
                <el-button :loading="loading" @click="refresh">{{ loading ? '加载中...' : '刷新' }}</el-button>
            </template>
        </PageHeader>

        <el-alert v-if="message" :title="message" type="info" show-icon class="knowledge-graph-page__alert" />

        <el-row :gutter="12" class="knowledge-graph-page__metrics">
            <el-col :xs="12" :md="6">
                <MetricCard label="实体" :value="graph?.entity_count ?? 0" />
            </el-col>
            <el-col :xs="12" :md="6">
                <MetricCard label="关系" :value="graph?.relation_count ?? 0" />
            </el-col>
            <el-col :xs="12" :md="6">
                <MetricCard label="平均共现权重" :value="averageWeight" />
            </el-col>
            <el-col :xs="12" :md="6">
                <MetricCard label="关系类型" :value="relationTypeCount" />
            </el-col>
        </el-row>

        <PageSection title="多跳查询">
            <el-row :gutter="12" align="bottom">
                <el-col :xs="24" :md="16">
                    <FormField label="查询问题">
                        <el-input
                            v-model.trim="question"
                            placeholder="输入实体或关系问题"
                            @keyup.enter="queryGraph"
                        />
                    </FormField>
                </el-col>
                <el-col :xs="12" :md="4">
                    <FormField label="最大跳数">
                        <el-select v-model="maxHops">
                            <el-option :value="1" label="1 跳" />
                            <el-option :value="2" label="2 跳" />
                            <el-option :value="3" label="3 跳" />
                        </el-select>
                    </FormField>
                </el-col>
                <el-col :xs="12" :md="4">
                    <el-button type="primary" :loading="queryLoading" class="knowledge-graph-page__submit" @click="queryGraph">
                        查询
                    </el-button>
                </el-col>
            </el-row>

            <el-alert v-if="queryMessage" :title="queryMessage" type="info" show-icon class="knowledge-graph-page__alert" />

            <el-descriptions v-if="queryResult" :column="3" border class="knowledge-graph-page__summary">
                <el-descriptions-item label="实体">{{ queryResult.entities.length }}</el-descriptions-item>
                <el-descriptions-item label="关系">{{ queryResult.relations.length }}</el-descriptions-item>
                <el-descriptions-item label="路径">{{ queryResult.paths.length }}</el-descriptions-item>
            </el-descriptions>

            <el-empty v-if="queryResult && !queryResult.paths.length" description="没有找到当前权限范围内的关联路径。" />

            <el-space v-if="queryResult?.paths.length" fill direction="vertical" class="knowledge-graph-page__stack">
                <el-card v-for="(path, index) in queryResult.paths" :key="`${index}-${path.entities.join('-')}`" shadow="never">
                    <strong>{{ path.hops }} 跳</strong>
                    <span class="knowledge-graph-page__path">{{ path.entities.join(' -> ') }}</span>
                </el-card>
            </el-space>
        </PageSection>

        <el-row :gutter="12" class="knowledge-graph-page__tables">
            <el-col :xs="24" :md="12">
                <PageSection fill title="实体">
                    <DataTable :data="graph?.entities ?? []" size="small" empty-description="暂无可见实体，请先导入文档。">
                        <el-table-column label="名称" prop="name" min-width="180" />
                        <el-table-column label="切块数" prop="chunk_count" width="100" />
                    </DataTable>
                </PageSection>
            </el-col>
            <el-col :xs="24" :md="12">
                <PageSection fill title="共现关系">
                    <DataTable :data="graph?.relations ?? []" size="small" empty-description="暂无可见关系。">
                        <el-table-column label="来源" prop="source" min-width="140" />
                        <el-table-column label="目标" prop="target" min-width="140" />
                        <el-table-column label="类型" prop="type" width="120" />
                        <el-table-column label="权重" prop="weight" width="80" />
                    </DataTable>
                </PageSection>
            </el-col>
        </el-row>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import DataTable from '@/components/ui/DataTable.vue';
import FormField from '@/components/ui/FormField.vue';
import MetricCard from '@/components/ui/MetricCard.vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import PageSection from '@/components/ui/PageSection.vue';
import { ragApi } from '@/services/ragApi';
import type { RagKnowledgeGraphView } from '@/types/rag';

const graph = ref<RagKnowledgeGraphView | null>(null);
const loading = ref(false);
const message = ref('');
const question = ref('');
const maxHops = ref(2);
const queryLoading = ref(false);
const queryMessage = ref('');
const queryResult = ref<Awaited<ReturnType<typeof ragApi.queryKnowledgeGraph>> | null>(null);
const averageWeight = computed(() => {
    const relations = graph.value?.relations ?? [];
    if (!relations.length) return '0.00';
    return (relations.reduce((sum, relation) => sum + relation.weight, 0) / relations.length).toFixed(2);
});
const relationTypeCount = computed(() => new Set((graph.value?.relations ?? []).map((relation) => relation.type)).size);

/**
 * 加载当前用户权限范围内的图谱数据；请求失败时保留已有结果并显示错误。
 */
async function refresh(): Promise<void> {
    loading.value = true;
    message.value = '';
    try {
        graph.value = await ragApi.getKnowledgeGraph();
    } catch (error) {
        message.value = error instanceof Error ? error.message : '知识图谱加载失败';
    } finally {
        loading.value = false;
    }
}

onMounted(() => {
    void refresh();
});

async function queryGraph(): Promise<void> {
    if (!question.value) return;
    queryLoading.value = true;
    queryMessage.value = '';
    try {
        queryResult.value = await ragApi.queryKnowledgeGraph(question.value, undefined, maxHops.value);
    } catch (error) {
        queryMessage.value = error instanceof Error ? error.message : '图谱查询失败';
    } finally {
        queryLoading.value = false;
    }
}
</script>

<style scoped lang="less">
.knowledge-graph-page {
    min-width: 0;
    height: 100%;
    display: flex;
    flex-direction: column;

    &__alert {
        flex-shrink: 0;
        margin-bottom: 12px;
    }

    &__metrics {
        flex-shrink: 0;
        margin-bottom: 12px;
    }

    &__path {
        color: #64748b;
        font-size: 13px;
    }

    &__submit {
        width: 100%;
    }

    // 查询结果较多时限高内部滚动，查询区不抢占表格高度
    &__stack {
        width: 100%;
        margin-top: 12px;
        max-height: 200px;
        overflow-y: auto;
    }

    // 底部两列表格铺满剩余高度：列内卡片各自填满列高
    &__tables {
        flex: 1;
        min-height: 0;

        :deep(> .el-col) {
            height: 100%;
            display: flex;
            flex-direction: column;
        }
    }

    // 窄屏单列：表格恢复自然高度，由内容区整体滚动
    @media (max-width: 991px) {
        &__tables {
            display: block;

            :deep(> .el-col) {
                height: auto;
                margin-bottom: 12px;
            }

            :deep(.page-section--fill) {
                flex: none;
                min-height: 240px;
            }
        }
    }
}
</style>
