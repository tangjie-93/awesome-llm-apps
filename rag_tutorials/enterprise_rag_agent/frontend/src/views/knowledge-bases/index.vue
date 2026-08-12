<template>
    <section class="page">
        <header class="page__header">
            <div>
                <h1 class="page__title">Knowledge Bases</h1>
                <p class="page__subtitle">路由后的知识库和权限范围</p>
            </div>
        </header>

        <div class="list">
            <article v-for="kb in store.knowledgeBases" :key="kb" class="item">
                <div class="item__title">{{ kb }}</div>
            </article>
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

.list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
}

.item {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 16px;
    background: #fff;

    &__title {
        font-weight: 600;
    }
}

</style>

