<template>
    <section class="page">
        <header class="page__header">
            <div>
                <h1 class="page__title">日志</h1>
                <p class="page__subtitle">问答与评估记录</p>
            </div>
        </header>

        <div class="logs">
            <article class="panel">
                <h2 class="panel__title">回答日志</h2>
                <div v-for="log in store.answerLogs" :key="String(log.id)" class="log">
                    <div class="log__title">{{ String(log.question) }}</div>
                    <div class="log__meta">
                        置信度 {{ String(log.confidence) }} · {{ log.created_at }} ·
                        {{ String(log.metadata.knowledge_base ?? '全部知识库') }}
                    </div>
                </div>
                <div v-if="!store.answerLogs.length" class="empty">暂无回答日志。</div>
            </article>
            <article class="panel">
                <h2 class="panel__title">评估日志</h2>
                <div v-for="log in store.evaluationLogs" :key="String(log.id)" class="log">
                    <div class="log__title">{{ String(log.question) }}</div>
                    <div class="log__meta">得分 {{ String(log.score) }} · {{ log.created_at }}</div>
                </div>
                <div v-if="!store.evaluationLogs.length" class="empty">暂无评估日志。</div>
            </article>
            <article class="panel">
                <h2 class="panel__title">导入日志</h2>
                <div v-for="log in store.operationLogs" :key="String(log.id)" class="log">
                    <div class="log__title">{{ log.status === 'succeeded' ? '导入完成' : '导入失败' }}</div>
                    <div class="log__meta">{{ log.path || '-' }} · {{ log.created_at }}</div>
                    <div class="log__meta">
                        新增 {{ String(log.detail.documents_indexed ?? 0) }} ·
                        跳过 {{ String(log.detail.documents_skipped ?? 0) }} ·
                        清理 {{ String(log.detail.documents_removed ?? 0) }}
                    </div>
                </div>
                <div v-if="!store.operationLogs.length" class="empty">暂无导入日志。</div>
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
    grid-template-columns: repeat(3, minmax(0, 1fr));
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

.empty {
    margin: 0;
    color: #64748b;
    font-size: 14px;
}
</style>
