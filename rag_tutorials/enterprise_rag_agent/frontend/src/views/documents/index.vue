<template>
    <section class="page">
        <PageHeader>
            <template #actions>
                <button class="button" :disabled="store.loading" @click="refreshDocuments">刷新</button>
            </template>
        </PageHeader>

        <div v-if="store.error" class="alert alert--error">{{ store.error }}</div>

        <div v-if="store.documents.length" class="table">
            <div class="table__row table__row--head">
                <span>知识库</span>
                <span>标题</span>
                <span>路径</span>
                <span>权限组</span>
                <span>风险</span>
                <span>内容哈希</span>
                <span>版本</span>
                <span>导入时间</span>
            </div>
            <div v-for="doc in store.documents" :key="String(doc.source_id)" class="table__row">
                <span>{{ String(doc.knowledge_base) }}</span>
                <span>{{ String(doc.title) }}</span>
                <span class="truncate">{{ String(doc.path) }}</span>
                <span>{{ doc.allowed_groups.join(', ') }}</span>
                <span>{{ doc.risk_level }}</span>
                <span class="truncate">{{ doc.content_hash }}</span>
                <span>{{ String(doc.version) }}</span>
                <span>{{ doc.indexed_at || '-' }}</span>
            </div>
        </div>
        <div v-else-if="!store.loading" class="empty">暂无文档。请先在导入页导入样例目录或业务文档。</div>
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
.page {
    min-width: 0;
}

.button {
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 10px 14px;
    background: #fff;
    cursor: pointer;

    &:disabled {
        cursor: not-allowed;
        opacity: 0.65;
    }
}

.alert,
.empty {
    margin-bottom: 12px;
    border-radius: 8px;
    padding: 11px 12px;
}

.alert {
    background: #eff6ff;
    color: #1d4ed8;

    &--error {
        background: #fef2f2;
        color: #b91c1c;
    }
}

.empty {
    border: 1px dashed #cbd5e1;
    background: #f8fafc;
    color: #64748b;
}

.table {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    overflow-x: auto;
    background: #fff;

    &__row {
        display: grid;
        grid-template-columns: 110px 150px minmax(220px, 1fr) 140px 80px 160px 70px 160px;
        gap: 10px;
        padding: 10px 12px;
        border-top: 1px solid #e2e8f0;
        min-width: 1180px;

        &--head {
            border-top: 0;
            background: #f8fafc;
            font-weight: 600;
        }
    }
}

.truncate {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
</style>
