<template>
    <section class="page">
        <header class="page__header">
            <div>
                <h1 class="page__title">导入文档</h1>
                <p class="page__subtitle">对应后端 ingest 命令，将本地路径内容导入知识库</p>
            </div>
        </header>

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

        <div v-if="message" class="alert">{{ message }}</div>
    </section>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();
const path = ref<string>('backend/sample_docs');
const knowledgeBase = ref<string>('general');
const allowedGroupsText = ref<string>('public');
const submitting = ref<boolean>(false);
const message = ref<string>('');

async function submitIngest(): Promise<void> {
    submitting.value = true;
    message.value = '';
    try {
        const allowedGroups = allowedGroupsText.value
            .split(',')
            .map((group) => group.trim())
            .filter((group) => group.length > 0);
        await store.ingestPath(path.value, knowledgeBase.value.trim() || undefined, allowedGroups.length > 0 ? allowedGroups : undefined);
        message.value = '导入已提交';
        await store.syncDashboard();
    } catch (error) {
        message.value = error instanceof Error ? error.message : '导入失败';
    } finally {
        submitting.value = false;
    }
}
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

.form {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
    max-width: 920px;
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
}
</style>
