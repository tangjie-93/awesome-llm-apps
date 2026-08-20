<template>
    <section class="knowledge-bases-page">
        <PageHeader />

        <el-empty v-if="!store.knowledgeBases.length" description="暂无知识库" class="knowledge-bases-page__empty" />

        <el-row v-else :gutter="12">
            <el-col v-for="kb in store.knowledgeBases" :key="kb" :xs="24" :sm="12" :md="8" :lg="6">
                <el-card shadow="never" class="knowledge-bases-page__card">
                    <div class="knowledge-bases-page__title">{{ kb }}</div>
                </el-card>
            </el-col>
        </el-row>
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
.knowledge-bases-page {
    min-width: 0;

    &__card,
    &__empty {
        margin-bottom: 12px;
    }

    &__title {
        font-weight: 600;
        color: #0f172a;
    }
}
</style>
