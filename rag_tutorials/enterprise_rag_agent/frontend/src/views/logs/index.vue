<template>
    <section class="page">
        <PageHeader />

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
                    <button
                        v-if="log.operation === 'ingest' && log.path"
                        class="log__replay"
                        :disabled="replayingId === log.id"
                        @click="replay(log.id)"
                    >
                        {{ replayingId === log.id ? '回放中...' : '回放' }}
                    </button>
                </div>
                <div v-if="!store.operationLogs.length" class="empty">暂无导入日志。</div>
            </article>
        </div>
        <div v-if="message" class="alert">{{ message }}</div>
    </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();
const replayingId = ref<number | null>(null);
const message = ref<string>('');

onMounted(() => {
    void store.syncDashboard();
});

/** 回放一次已记录的导入操作，并向用户反馈结果或失败原因。 */
async function replay(operationId: number): Promise<void> {
    replayingId.value = operationId;
    message.value = '';
    try {
        const result = await store.replayOperation(operationId);
        message.value = `回放完成：新增 ${result.documents_indexed}，跳过 ${result.documents_skipped}`;
    } catch (error) {
        message.value = error instanceof Error ? error.message : '回放失败';
    } finally {
        replayingId.value = null;
    }
}
</script>

<style scoped lang="less">
.page {
    min-width: 0;
}

.logs {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
}

.panel {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px;
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

    &__replay {
        margin-top: 8px;
        border: 1px solid #93c5fd;
        border-radius: 6px;
        padding: 5px 8px;
        background: #eff6ff;
        color: #1d4ed8;
        cursor: pointer;

        &:disabled {
            cursor: wait;
            opacity: 0.65;
        }
    }
}

.alert {
    margin-top: 12px;
    padding: 11px 12px;
    border: 1px solid #bfdbfe;
    border-radius: 6px;
    background: #eff6ff;
    color: #1d4ed8;
}

.empty {
    margin: 0;
    color: #64748b;
    font-size: 14px;
}
</style>
