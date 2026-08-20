<template>
    <section class="documents-page">
        <PageHeader>
            <template #actions>
                <el-button type="primary" @click="goToIngest">导入文档</el-button>
                <el-button :loading="store.loading" @click="refreshDocuments">刷新</el-button>
            </template>
        </PageHeader>

        <el-alert v-if="store.error" :title="store.error" type="error" show-icon class="documents-page__alert" />

        <PageSection title="文档索引" subtitle="按知识库、权限组和风险等级查看已导入文档">
            <EmptyState
                v-if="!store.loading && !store.documents.length"
                description="暂无文档。请先导入样例目录或业务文档。"
                action-label="导入文档"
                @action="goToIngest"
            />

            <el-table v-else :data="store.documents" border stripe class="documents-page__table">
                <el-table-column label="知识库" prop="knowledge_base" min-width="120" />
                <el-table-column label="标题" prop="title" min-width="160" show-overflow-tooltip />
                <el-table-column label="路径" min-width="240" show-overflow-tooltip>
                    <template #default="{ row }">
                        {{ row.path }}
                    </template>
                </el-table-column>
                <el-table-column label="权限组" min-width="180">
                    <template #default="{ row }">
                        <el-space wrap>
                            <el-tag v-for="group in row.allowed_groups" :key="group" size="small">
                                {{ group }}
                            </el-tag>
                        </el-space>
                    </template>
                </el-table-column>
                <el-table-column label="风险" width="100">
                    <template #default="{ row }">
                        <el-tag :type="riskTagType(row.risk_level)" size="small">
                            {{ row.risk_level }}
                        </el-tag>
                    </template>
                </el-table-column>
                <el-table-column label="版本" prop="version" width="90" />
                <el-table-column label="导入时间" prop="indexed_at" min-width="170" />
            </el-table>
        </PageSection>
    </section>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import EmptyState from '@/components/ui/EmptyState.vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import PageSection from '@/components/ui/PageSection.vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();
const router = useRouter();

/**
 * 刷新文档列表；成功时更新 store 文档数据，失败时由 store.error 展示。
 */
async function refreshDocuments(): Promise<void> {
    await store.syncDashboard();
}

/** 跳转到文档导入页面。 */
function goToIngest(): void {
    void router.push('/ingest');
}

/**
 * 将风险等级映射为 Element Plus 标签类型。
 * @param riskLevel 文档风险等级。
 * @returns 标签展示类型。
 */
function riskTagType(riskLevel: string): 'success' | 'warning' | 'danger' | 'info' {
    if (riskLevel === 'high') return 'danger';
    if (riskLevel === 'medium') return 'warning';
    if (riskLevel === 'low') return 'success';
    return 'info';
}

onMounted(() => {
    void refreshDocuments();
});
</script>

<style scoped lang="less">
.documents-page {
    min-width: 0;

    &__alert {
        margin-bottom: 12px;
    }
}
</style>
