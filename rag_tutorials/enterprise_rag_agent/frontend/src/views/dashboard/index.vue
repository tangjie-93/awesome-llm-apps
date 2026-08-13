<template>
    <section class="page">
        <header class="page__header">
            <div>
                <h1 class="page__title">仪表盘</h1>
                <p class="page__subtitle">企业知识检索与问答总览</p>
            </div>
            <button class="button button--primary" @click="refreshDashboard">刷新</button>
        </header>

        <div class="grid">
            <article class="panel">
                <div class="panel__label">知识库</div>
                <div class="panel__value">{{ store.knowledgeBases.length }}</div>
            </article>
            <article class="panel">
                <div class="panel__label">文档</div>
                <div class="panel__value">{{ store.documents.length }}</div>
            </article>
            <article class="panel">
                <div class="panel__label">回答日志</div>
                <div class="panel__value">{{ store.answerLogs.length }}</div>
            </article>
            <article class="panel">
                <div class="panel__label">评估日志</div>
                <div class="panel__value">{{ store.evaluationLogs.length }}</div>
            </article>
        </div>

        <div v-if="store.error" class="alert">{{ store.error }}</div>
    </section>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();

async function refreshDashboard(): Promise<void> {
    await store.syncDashboard();
}

onMounted(() => {
    void refreshDashboard();
});
</script>

<style scoped lang="less">
.page {
    padding: 24px;

    &__header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 16px;
        margin-bottom: 24px;
    }

    &__title {
        margin: 0;
        font-size: 28px;
        line-height: 1.2;
    }

    &__subtitle {
        margin: 8px 0 0;
        color: #64748b;
    }
}

.grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 16px;
}

.panel {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 16px;
    background: #fff;

    &__label {
        color: #64748b;
        font-size: 13px;
    }

    &__value {
        margin-top: 12px;
        font-size: 28px;
        font-weight: 600;
    }
}

.button {
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 10px 14px;
    background: #fff;
    cursor: pointer;

    &--primary {
        border-color: #1d4ed8;
        background: #1d4ed8;
        color: #fff;
    }
}

.alert {
    margin-top: 16px;
    padding: 12px 14px;
    border-radius: 8px;
    background: #fef2f2;
    color: #b91c1c;
}
</style>
