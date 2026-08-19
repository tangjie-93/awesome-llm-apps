<template>
    <section class="page">
        <PageHeader />

        <div class="form">
            <label class="field field--full">
                <span class="field__label">路径</span>
                <input v-model="path" class="field__input" type="text" placeholder="例如：backend/sample_docs" />
            </label>
            <label class="field">
                <span class="field__label">知识库</span>
                <input v-model="knowledgeBase" class="field__input" type="text" placeholder="general" />
            </label>
            <label class="field">
                <span class="field__label">权限组</span>
                <input v-model="allowedGroupsText" class="field__input" type="text" placeholder="public,security" />
            </label>
            <div class="actions">
                <button class="button button--primary" :disabled="submitting" @click="submitIngest">导入</button>
            </div>
        </div>

        <div v-if="message" class="alert" :class="{ 'alert--error': hasError }">{{ message }}</div>

        <article v-if="ingestResult" class="summary">
            <h2 class="summary__title">导入结果</h2>
            <dl class="summary__stats">
                <div>
                    <dt>新增文档</dt>
                    <dd>{{ ingestResult.documents_indexed }}</dd>
                </div>
                <div>
                    <dt>新增切块</dt>
                    <dd>{{ ingestResult.chunks_indexed }}</dd>
                </div>
                <div>
                    <dt>跳过文档</dt>
                    <dd>{{ ingestResult.documents_skipped }}</dd>
                </div>
                <div>
                    <dt>清理文档</dt>
                    <dd>{{ ingestResult.documents_removed }}</dd>
                </div>
            </dl>
            <div v-if="ingestResult.knowledge_bases.length" class="summary__section">
                <h3 class="summary__subtitle">知识库</h3>
                <div class="tag-list">
                    <span v-for="kb in ingestResult.knowledge_bases" :key="kb" class="tag">{{ kb }}</span>
                </div>
            </div>
            <div v-if="ingestResult.paths.length" class="summary__section">
                <h3 class="summary__subtitle">已索引路径</h3>
                <ul class="path-list">
                    <li v-for="item in ingestResult.paths" :key="item">{{ item }}</li>
                </ul>
            </div>
            <div v-if="ingestResult.duplicate_paths.length" class="summary__section">
                <h3 class="summary__subtitle">重复内容路径</h3>
                <ul class="path-list">
                    <li v-for="item in ingestResult.duplicate_paths" :key="item">{{ item }}</li>
                </ul>
            </div>
        </article>
    </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';
import type { RagIngestResultView } from '@/types/rag';

const store = useRagStore();
const path = ref<string>('backend/sample_docs');
const knowledgeBase = ref<string>('general');
const allowedGroupsText = ref<string>('public');
const submitting = ref<boolean>(false);
const message = ref<string>('');
const hasError = ref<boolean>(false);
const ingestResult = ref<RagIngestResultView | null>(null);

/**
 * 提交目录或文件导入；成功时展示导入明细并刷新全局数据，失败时展示错误说明。
 */
async function submitIngest(): Promise<void> {
    if (!path.value.trim()) {
        message.value = '请输入要导入的文件或目录路径';
        hasError.value = true;
        ingestResult.value = null;
        return;
    }
    submitting.value = true;
    message.value = '';
    hasError.value = false;
    try {
        const allowedGroups = allowedGroupsText.value
            .split(',')
            .map((group) => group.trim())
            .filter((group) => group.length > 0);
        ingestResult.value = await store.ingestPath(path.value.trim(), knowledgeBase.value.trim() || undefined, allowedGroups.length > 0 ? allowedGroups : undefined);
        message.value = '导入完成';
        await store.syncDashboard();
    } catch (error) {
        message.value = error instanceof Error ? error.message : '导入失败';
        hasError.value = true;
        ingestResult.value = null;
    } finally {
        submitting.value = false;
    }
}
</script>

<style scoped lang="less">
.page {
    min-width: 0;
}

.form {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
}

.field {
    display: grid;
    gap: 8px;

    &--full {
        grid-column: 1 / -1;
    }

    &__label {
        font-size: 13px;
        color: #64748b;
    }

    &__input {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 10px 12px;
        font: inherit;
    }
}

.actions {
    grid-column: 1 / -1;
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
    background: #eff6ff;
    color: #1d4ed8;

    &--error {
        background: #fef2f2;
        color: #b91c1c;
    }
}

.summary {
    margin-top: 14px;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 14px;
    background: #fff;

    &__title {
        margin: 0 0 14px;
        font-size: 18px;
    }

    &__stats {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 10px;

        div {
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 12px;
            background: #f8fafc;
        }

        dt {
            color: #64748b;
            font-size: 13px;
        }

        dd {
            margin: 6px 0 0;
            font-size: 22px;
            font-weight: 700;
        }
    }

    &__section {
        margin-top: 16px;
    }

    &__subtitle {
        margin: 0 0 8px;
        font-size: 15px;
    }
}

.tag-list {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.tag {
    border-radius: 999px;
    padding: 6px 10px;
    background: #eff6ff;
    color: #1d4ed8;
    font-size: 13px;
}

.path-list {
    margin: 0;
    padding-left: 18px;
    color: #0f172a;

    li {
        overflow-wrap: anywhere;
    }
}
</style>
