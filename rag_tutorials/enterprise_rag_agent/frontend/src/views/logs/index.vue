<template>
    <section class="page">
        <header class="page__header">
            <div>
                <h1 class="page__title">Logs</h1>
                <p class="page__subtitle">问答与评估记录</p>
            </div>
        </header>

        <div class="logs">
            <article class="panel">
                <h2 class="panel__title">Answers</h2>
                <div v-for="log in store.answerLogs" :key="String(log.id)" class="log">
                    <div class="log__title">{{ String(log.question) }}</div>
                    <div class="log__meta">confidence {{ String(log.confidence) }}</div>
                </div>
            </article>
            <article class="panel">
                <h2 class="panel__title">Evaluations</h2>
                <div v-for="log in store.evaluationLogs" :key="String(log.id)" class="log">
                    <div class="log__title">{{ String(log.question) }}</div>
                    <div class="log__meta">score {{ String(log.score) }}</div>
                </div>
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

.logs {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
}

.panel {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 16px;
    background: #fff;

    &__title {
        margin: 0 0 12px;
        font-size: 16px;
    }
}

.log {
    padding: 12px 0;
    border-top: 1px solid #e2e8f0;

    &__title {
        font-weight: 600;
    }

    &__meta {
        margin-top: 4px;
        color: #64748b;
        font-size: 13px;
    }
}

</style>

