<template>
    <section class="page">
        <header class="page__header">
            <div>
                <h1 class="page__title">文档</h1>
                <p class="page__subtitle">已撰入文档与版本信息</p>
            </div>
        </header>

        <div class="table">
            <div class="table__row table__row--head">
                <span>知识库</span>
                <span>标题</span>
                <span>路径</span>
                <span>版本</span>
            </div>
            <div v-for="doc in store.documents" :key="String(doc.source_id)" class="table__row">
                <span>{{ String(doc.knowledge_base) }}</span>
                <span>{{ String(doc.title) }}</span>
                <span class="truncate">{{ String(doc.path) }}</span>
                <span>{{ String(doc.version) }}</span>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();

onMounted(() => {
    void store.syncDashboard();
});
</script>

<style scoped lang="less">
.page {
    padding: 24px;

    &__header {
        margin-bottom: 24px;
    }

    &__title {
        margin: 0;
        font-size: 24px;
    }

    &__subtitle {
        margin: 8px 0 0;
        color: #64748b;
    }
}

.table {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    overflow: hidden;
    background: #fff;

    &__row {
        display: grid;
        grid-template-columns: 120px 180px 1fr 80px;
        gap: 12px;
        padding: 12px 16px;
        border-top: 1px solid #e2e8f0;

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
