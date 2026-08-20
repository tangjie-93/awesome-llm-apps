<template>
    <section class="documents-page">
        <PageHeader>
            <template #actions>
                <el-button :loading="store.loading" @click="refreshDocuments">刷新</el-button>
            </template>
        </PageHeader>

        <el-alert v-if="store.error" :title="store.error" type="error" show-icon class="documents-page__alert" />

        <el-empty
            v-if="!store.loading && !store.documents.length"
            description="暂无文档。请先在导入页导入样例目录或业务文档。"
            class="documents-page__empty"
        />

        <el-card v-else shadow="never" class="documents-page__card">
            <el-table :data="store.documents" border stripe class="documents-page__table">
                <el-table-column label="知识库" prop="knowledge_base" min-width="120" />
                <el-table-column label="标题" prop="title" min-width="160" />
                <el-table-column label="路径" min-width="220">
                    <template #default="{ row }">
                        <span class="documents-page__truncate">{{ row.path }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="权限组" min-width="140">
                    <template #default="{ row }">
                        {{ row.allowed_groups.join(', ') }}
                    </template>
                </el-table-column>
                <el-table-column label="风险" prop="risk_level" width="100" />
                <el-table-column label="内容哈希" min-width="180">
                    <template #default="{ row }">
                        <span class="documents-page__truncate">{{ row.content_hash }}</span>
                    </template>
                </el-table-column>
                <el-table-column label="版本" prop="version" width="80" />
                <el-table-column label="导入时间" prop="indexed_at" min-width="160" />
            </el-table>
        </el-card>
    </section>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();

/**
 * 刷新文档列表；成功时更新 store 文档数据，失败时由 store.error 展示。
 */
async function refreshDocuments(): Promise<void> {
    await store.syncDashboard();
}

onMounted(() => {
    void refreshDocuments();
});
</script>

<style scoped lang="less">
.documents-page {
    min-width: 0;

    &__alert,
    &__empty {
        margin-bottom: 12px;
    }

    &__truncate {
        display: inline-block;
        max-width: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
}
</style>
