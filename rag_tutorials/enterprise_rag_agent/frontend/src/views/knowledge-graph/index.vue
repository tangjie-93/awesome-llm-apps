<template>
    <section class="knowledge-graph-page">
        <PageHeader>
            <template #actions>
                <button class="knowledge-graph-page__button" :disabled="loading" @click="refresh">
                    {{ loading ? '加载中...' : '刷新' }}
                </button>
            </template>
        </PageHeader>

        <p v-if="message" class="knowledge-graph-page__message">{{ message }}</p>

        <section class="knowledge-graph-page__metrics">
            <article class="knowledge-graph-page__metric">
                <span>实体</span>
                <strong>{{ graph?.entity_count ?? 0 }}</strong>
            </article>
            <article class="knowledge-graph-page__metric">
                <span>关系</span>
                <strong>{{ graph?.relation_count ?? 0 }}</strong>
            </article>
        </section>

        <section class="knowledge-graph-page__query">
            <div class="knowledge-graph-page__query-fields">
                <label>
                    <span>多跳查询</span>
                    <input v-model.trim="question" type="search" placeholder="输入实体或关系问题" @keyup.enter="queryGraph" />
                </label>
                <label class="knowledge-graph-page__hop-field">
                    <span>最大跳数</span>
                    <select v-model.number="maxHops">
                        <option :value="1">1 跳</option>
                        <option :value="2">2 跳</option>
                        <option :value="3">3 跳</option>
                    </select>
                </label>
                <button class="knowledge-graph-page__button" :disabled="queryLoading || !question" @click="queryGraph">
                    {{ queryLoading ? '查询中...' : '查询路径' }}
                </button>
            </div>
            <p v-if="queryMessage" class="knowledge-graph-page__message">{{ queryMessage }}</p>
            <div v-if="queryResult" class="knowledge-graph-page__query-result">
                <div class="knowledge-graph-page__query-summary">
                    <span>{{ queryResult.entities.length }} 个实体</span>
                    <span>{{ queryResult.relations.length }} 条关系</span>
                    <span>{{ queryResult.paths.length }} 条路径</span>
                </div>
                <div v-if="queryResult.paths.length" class="knowledge-graph-page__path-list">
                    <div v-for="(path, index) in queryResult.paths" :key="`${index}-${path.entities.join('-')}`" class="knowledge-graph-page__path">
                        <strong>{{ path.hops }} 跳</strong>
                        <span>{{ path.entities.join(' -> ') }}</span>
                    </div>
                </div>
                <p v-else class="knowledge-graph-page__empty">没有找到当前权限范围内的关联路径。</p>
            </div>
        </section>

        <section class="knowledge-graph-page__grid">
            <article class="knowledge-graph-page__section">
                <h2>实体</h2>
                <div v-if="graph?.entities.length" class="knowledge-graph-page__entity-list">
                    <div v-for="entity in graph.entities" :key="entity.name" class="knowledge-graph-page__entity">
                        <span>{{ entity.name }}</span>
                        <strong>{{ entity.chunk_count }} 个切块</strong>
                    </div>
                </div>
                <p v-else class="knowledge-graph-page__empty">暂无可见实体，请先导入文档。</p>
            </article>

            <article class="knowledge-graph-page__section">
                <h2>共现关系</h2>
                <div v-if="graph?.relations.length" class="knowledge-graph-page__relation-list">
                    <div
                        v-for="relation in graph.relations"
                        :key="`${relation.source}-${relation.target}-${relation.type}`"
                        class="knowledge-graph-page__relation"
                    >
                        <span>{{ relation.source }}</span>
                        <span aria-hidden="true">→</span>
                        <span>{{ relation.target }}</span>
                        <strong>{{ relation.weight }}</strong>
                    </div>
                </div>
                <p v-else class="knowledge-graph-page__empty">暂无可见关系。</p>
            </article>
        </section>
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
    &__relation {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    &__button {
        border: 1px solid #1d4ed8;
        border-radius: 6px;
        padding: 8px 12px;
        background: #1d4ed8;
        color: #fff;
        cursor: pointer;

        &:disabled {
            cursor: not-allowed;
            opacity: 0.55;
        }
    }

    &__message {
        margin: 12px 0;
        color: #b91c1c;
    }

    &__metrics,
    &__grid,
    &__query-fields,
    &__query-summary {
        display: grid;
        gap: 12px;
    }

    &__metrics {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        margin-bottom: 10px;
    }

    &__grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    &__query {
        margin: 10px 0;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px;
        background: #fff;
    }

    &__query-fields {
        grid-template-columns: minmax(0, 1fr) 120px auto;
        align-items: end;

        label {
            display: grid;
            gap: 6px;
            color: #334155;
            font-size: 13px;
        }

        input,
        select {
            box-sizing: border-box;
            min-height: 38px;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            padding: 8px 10px;
            background: #fff;
            color: #0f172a;
        }
    }

    &__query-summary {
        grid-template-columns: repeat(3, max-content);
        margin-top: 12px;
        color: #475569;
        font-size: 13px;
    }

    &__path-list {
        display: grid;
        gap: 8px;
        margin-top: 10px;
    }

    &__path {
        display: flex;
        gap: 12px;
        align-items: baseline;
        border-bottom: 1px solid #f1f5f9;
        padding: 7px 0;
        color: #334155;

        strong {
            min-width: 38px;
            color: #1d4ed8;
            font-size: 12px;
        }
    }

    &__metric,
    &__section {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px;
        background: #fff;
    }

    &__metric {
        display: grid;
        gap: 6px;
        color: #64748b;

        strong {
            color: #0f172a;
            font-size: 22px;
        }
    }

    &__section {
        min-width: 0;

        h2 {
            margin: 0 0 12px;
            color: #0f172a;
            font-size: 16px;
        }
    }

    &__entity-list,
    &__relation-list {
        display: grid;
        gap: 8px;
    }

    &__entity,
    &__relation {
        justify-content: space-between;
        min-width: 0;
        border-bottom: 1px solid #f1f5f9;
        padding: 7px 0;
        color: #334155;
    }

    &__entity strong,
    &__relation strong {
        color: #64748b;
        font-size: 12px;
    }

    &__empty {
        color: #64748b;
    }

    @media (max-width: 760px) {
        &__header {
            align-items: stretch;
            flex-direction: column;
        }

        &__grid {
            grid-template-columns: 1fr;
        }

        &__query-fields {
            grid-template-columns: 1fr;
        }

        &__query-summary {
            grid-template-columns: 1fr;
            gap: 6px;
        }
    }
}
</style>
