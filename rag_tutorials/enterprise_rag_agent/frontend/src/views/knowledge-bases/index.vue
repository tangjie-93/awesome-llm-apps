<template>
    <section class="knowledge-bases-page">
        <PageHeader>
            <template #actions>
                <el-button type="primary" @click="goToIngest">导入文档</el-button>
            </template>
        </PageHeader>

        <PageSection fill title="知识库概览" subtitle="按库级维度查看文档规模、权限覆盖和风险分布">
            <DataTable :data="knowledgeBaseRows">
                <template #empty>
                    <EmptyState
                        description="暂无知识库。导入文档后会自动创建或更新知识库。"
                        action-label="导入文档"
                        @action="goToIngest"
                    />
                </template>
                <el-table-column label="知识库" min-width="180">
                    <template #default="{ row }">
                        <div class="knowledge-bases-page__name">{{ row.name }}</div>
                    </template>
                </el-table-column>
                <el-table-column label="文档数" prop="documentCount" width="110" />
                <el-table-column label="权限组覆盖" min-width="220">
                    <template #default="{ row }">
                        <TagList :items="row.groups" empty-text="暂无权限组" />
                    </template>
                </el-table-column>
                <el-table-column label="风险等级" min-width="160">
                    <template #default="{ row }">
                        <TagList :items="row.risks" :type-for="riskTagType" empty-text="暂无风险信息" />
                    </template>
                </el-table-column>
                <el-table-column label="最近索引时间" prop="latestIndexedAt" min-width="180" />
            </DataTable>
        </PageSection>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import DataTable from '@/components/ui/DataTable.vue';
import EmptyState from '@/components/ui/EmptyState.vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import PageSection from '@/components/ui/PageSection.vue';
import TagList from '@/components/ui/TagList.vue';
import { useRagStore } from '@/store/rag';
import type { RagDocumentSummary } from '@/types/rag';
import { riskTagType } from '@/utils/tag';

const store = useRagStore();
const router = useRouter();

const knowledgeBaseRows = computed(() =>
    store.knowledgeBases.map((knowledgeBase) => ({
        name: knowledgeBase,
        documentCount: documentsByKnowledgeBase(knowledgeBase).length,
        groups: groupsByKnowledgeBase(knowledgeBase),
        risks: risksByKnowledgeBase(knowledgeBase),
        latestIndexedAt: latestIndexedAtByKnowledgeBase(knowledgeBase)
    }))
);

/**
 * 获取指定知识库下的文档列表。
 * @param knowledgeBase 知识库名称。
 * @returns 当前 store 中该知识库的文档列表。
 */
function documentsByKnowledgeBase(knowledgeBase: string): RagDocumentSummary[] {
    return store.documents.filter((document) => document.knowledge_base === knowledgeBase);
}

/**
 * 获取指定知识库覆盖的权限组。
 * @param knowledgeBase 知识库名称。
 * @returns 去重后的权限组列表。
 */
function groupsByKnowledgeBase(knowledgeBase: string): string[] {
    return Array.from(new Set(documentsByKnowledgeBase(knowledgeBase).flatMap((document) => document.allowed_groups)));
}

/**
 * 获取指定知识库覆盖的风险等级。
 * @param knowledgeBase 知识库名称。
 * @returns 去重后的风险等级列表。
 */
function risksByKnowledgeBase(knowledgeBase: string): string[] {
    return Array.from(new Set(documentsByKnowledgeBase(knowledgeBase).map((document) => document.risk_level)));
}

/**
 * 获取指定知识库最近一次索引时间。
 * @param knowledgeBase 知识库名称。
 * @returns 最近索引时间；没有文档时返回占位符。
 */
function latestIndexedAtByKnowledgeBase(knowledgeBase: string): string {
    const indexedTimes = documentsByKnowledgeBase(knowledgeBase)
        .map((document) => document.indexed_at)
        .filter(Boolean)
        .sort()
        .reverse();
    return indexedTimes[0] ?? '-';
}

/** 跳转到文档导入页面。 */
function goToIngest(): void {
    void router.push('/ingest');
}

onMounted(() => {
    void store.syncDashboard();
});
</script>

<style scoped lang="less">
.knowledge-bases-page {
    min-width: 0;
    height: 100%;
    display: flex;
    flex-direction: column;

    &__name {
        color: #0f172a;
        font-weight: 600;
    }
}
</style>
