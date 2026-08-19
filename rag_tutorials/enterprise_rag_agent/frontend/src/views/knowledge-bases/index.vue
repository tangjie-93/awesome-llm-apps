<template>
    <section class="page">
        <PageHeader />

        <div class="list">
            <article v-for="kb in store.knowledgeBases" :key="kb" class="item">
                <div class="item__title">{{ kb }}</div>
            </article>
        </div>
    </section>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();

onMounted(() => {
    void store.syncDashboard();
});
</script>

<style scoped lang="less">
.page {
    min-width: 0;
}

.list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 12px;
}

.item {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px;
    background: #fff;

    &__title {
        font-weight: 600;
    }
}
</style>
