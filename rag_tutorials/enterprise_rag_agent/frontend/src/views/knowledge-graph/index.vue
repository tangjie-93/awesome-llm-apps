<template>
    <section class="knowledge-graph-page">
        <PageHeader>
            <template #actions>
                <el-button :loading="loading" @click="refresh">{{ loading ? '加载中...' : '刷新' }}</el-button>
            </template>
        </PageHeader>

        <el-alert v-if="message" :title="message" type="info" show-icon class="knowledge-graph-page__alert" />

        <el-row :gutter="12" class="knowledge-graph-page__metrics">
            <el-col :xs="12" :md="12">
                <el-card shadow="never" class="knowledge-graph-page__metric">
                    <div class="knowledge-graph-page__metric-label">实体</div>
                    <div class="knowledge-graph-page__metric-value">{{ graph?.entity_count ?? 0 }}</div>
                </el-card>
            </el-col>
            <el-col :xs="12" :md="12">
                <el-card shadow="never" class="knowledge-graph-page__metric">
                    <div class="knowledge-graph-page__metric-label">关系</div>
                    <div class="knowledge-graph-page__metric-value">{{ graph?.relation_count ?? 0 }}</div>
                </el-card>
            </el-col>
        </el-row>

        <el-card shadow="never" class="knowledge-graph-page__card">
            <div class="knowledge-graph-page__section-title">多跳查询</div>
            <el-row :gutter="12" align="bottom">
                <el-col :xs="24" :md="18">
                    <div class="knowledge-graph-page__label">查询问题</div>
                    <el-input
                        v-model.trim="question"
                        placeholder="输入实体或关系问题"
                        @keyup.enter="queryGraph"
                    />
                </el-col>
                <el-col :xs="24" :md="4">
                    <div class="knowledge-graph-page__label">最大跳数</div>
                    <el-select v-model="maxHops" class="knowledge-graph-page__select">
                        <el-option :value="1" label="1 跳" />
                        <el-option :value="2" label="2 跳" />
                        <el-option :value="3" label="3 跳" />
                    </el-select>
                </el-col>
                <el-col :xs="24" :md="2">
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
        </el-card>

        <el-row :gutter="12">
            <el-col :xs="24" :md="12">
                <el-card shadow="never" class="knowledge-graph-page__card">
                    <div class="knowledge-graph-page__section-title">实体</div>
                    <el-empty v-if="!graph?.entities.length" description="暂无可见实体，请先导入文档。" />
                    <el-table v-else :data="graph.entities" border stripe size="small">
                        <el-table-column label="名称" prop="name" min-width="180" />
                        <el-table-column label="切块数" prop="chunk_count" width="100" />
                    </el-table>
                </el-card>
            </el-col>
            <el-col :xs="24" :md="12">
                <el-card shadow="never" class="knowledge-graph-page__card">
                    <div class="knowledge-graph-page__section-title">共现关系</div>
                    <el-empty v-if="!graph?.relations.length" description="暂无可见关系。" />
                    <el-table v-else :data="graph.relations" border stripe size="small">
                        <el-table-column label="来源" prop="source" min-width="140" />
                        <el-table-column label="目标" prop="target" min-width="140" />
                        <el-table-column label="类型" prop="type" width="120" />
                        <el-table-column label="权重" prop="weight" width="80" />
                    </el-table>
                </el-card>
            </el-col>
        </el-row>
    </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
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

    &__alert,
    &__card,
    &__metrics {
        margin-bottom: 12px;
    }

    &__metric {
        height: 100%;
    }

    &__metric-label,
    &__label,
    &__path {
        color: #64748b;
        font-size: 13px;
    }

    &__metric-value {
        margin-top: 10px;
        font-size: 24px;
        font-weight: 700;
        color: #0f172a;
    }

    &__section-title {
        margin-bottom: 12px;
        font-size: 16px;
        font-weight: 600;
        color: #0f172a;
    }

    &__submit,
    &__select {
        width: 100%;
    }

    &__stack {
        width: 100%;
        margin-top: 12px;
    }
}
</style>
