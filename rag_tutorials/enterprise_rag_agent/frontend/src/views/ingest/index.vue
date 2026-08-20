<template>
    <section class="ingest-page">
        <PageHeader />

        <el-card shadow="never" class="ingest-page__card">
            <el-row :gutter="12" align="bottom">
                <el-col :xs="24" :md="10">
                    <div class="ingest-page__label">路径</div>
                    <el-select
                        v-model="path"
                        allow-create
                        filterable
                        default-first-option
                        placeholder="选择或输入导入路径"
                    >
                        <el-option v-for="item in pathOptions" :key="item" :label="item" :value="item" />
                    </el-select>
                </el-col>
                <el-col :xs="24" :md="4">
                    <div class="ingest-page__label">知识库</div>
                    <el-select
                        v-model="knowledgeBase"
                        allow-create
                        filterable
                        default-first-option
                        placeholder="选择或输入知识库"
                    >
                        <el-option v-for="item in knowledgeBaseOptions" :key="item" :label="item" :value="item" />
                    </el-select>
                </el-col>
                <el-col :xs="24" :md="6">
                    <div class="ingest-page__label">权限组</div>
                    <el-select
                        v-model="allowedGroups"
                        allow-create
                        filterable
                        multiple
                        collapse-tags
                        collapse-tags-tooltip
                        default-first-option
                        placeholder="选择或输入权限组"
                    >
                        <el-option v-for="item in groupOptions" :key="item" :label="item" :value="item" />
                    </el-select>
                </el-col>
                <el-col :xs="24" :md="4" class="ingest-page__actions">
                    <el-button type="primary" :loading="submitting" class="ingest-page__submit" @click="submitIngest">
                        导入
                    </el-button>
                </el-col>
            </el-row>
        </el-card>

        <el-card v-if="ingestResult" shadow="never" class="ingest-page__card">
            <div class="ingest-page__section-title">导入结果</div>
            <el-row :gutter="12" class="ingest-page__stats">
                <el-col v-for="stat in stats" :key="stat.label" :xs="12" :md="6">
                    <div class="ingest-page__stat">
                        <div class="ingest-page__stat-label">{{ stat.label }}</div>
                        <div class="ingest-page__stat-value">{{ stat.value }}</div>
                    </div>
                </el-col>
            </el-row>

            <div v-if="ingestResult.knowledge_bases.length" class="ingest-page__section">
                <div class="ingest-page__section-subtitle">知识库</div>
                <el-space wrap>
                    <el-tag v-for="kb in ingestResult.knowledge_bases" :key="kb">{{ kb }}</el-tag>
                </el-space>
            </div>

            <div v-if="ingestResult.paths.length" class="ingest-page__section">
                <div class="ingest-page__section-subtitle">已索引路径</div>
                <el-space fill direction="vertical" class="ingest-page__stack">
                    <div v-for="item in ingestResult.paths" :key="item" class="ingest-page__path">{{ item }}</div>
                </el-space>
            </div>

            <div v-if="ingestResult.duplicate_paths.length" class="ingest-page__section">
                <div class="ingest-page__section-subtitle">重复内容路径</div>
                <el-space fill direction="vertical" class="ingest-page__stack">
                    <div v-for="item in ingestResult.duplicate_paths" :key="item" class="ingest-page__path">
                        {{ item }}
                    </div>
                </el-space>
            </div>
        </el-card>
    </section>
</template>

<script setup lang="ts">
import { ElMessage } from 'element-plus';
import { computed, ref } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';
import type { RagIngestResultView } from '@/types/rag';

const store = useRagStore();
const path = ref<string>('backend/sample_docs');
const knowledgeBase = ref<string>('general');
const allowedGroups = ref<string[]>(['public']);
const submitting = ref<boolean>(false);
const ingestResult = ref<RagIngestResultView | null>(null);

const pathOptions = ['backend/sample_docs', 'backend/sample_docs/onboarding.md', 'backend/sample_docs/security.md'];
const knowledgeBaseOptions = computed(() =>
    Array.from(new Set([store.config.default_knowledge_base ?? 'general', ...store.knowledgeBases]))
);
const groupOptions = computed(() => {
    const groups = new Set([...(store.config.default_groups ?? []), ...store.documents.flatMap((document) => document.allowed_groups)]);
    if (!groups.size) {
        ['public', 'security', 'hr', 'it', 'ops'].forEach((group) => groups.add(group));
    }
    return Array.from(groups);
});

const stats = computed(() => [
    { label: '新增文档', value: ingestResult.value?.documents_indexed ?? 0 },
    { label: '新增切块', value: ingestResult.value?.chunks_indexed ?? 0 },
    { label: '跳过文档', value: ingestResult.value?.documents_skipped ?? 0 },
    { label: '清理文档', value: ingestResult.value?.documents_removed ?? 0 }
]);

/**
 * 提交目录或文件导入；成功时展示导入明细并刷新全局数据，失败时展示错误说明。
 */
async function submitIngest(): Promise<void> {
    if (!path.value.trim()) {
        ingestResult.value = null;
        ElMessage.warning('请输入要导入的文件或目录路径');
        return;
    }
    submitting.value = true;
    try {
        const normalizedAllowedGroups = allowedGroups.value.map((group) => group.trim()).filter((group) => group.length > 0);
        ingestResult.value = await store.ingestPath(
            path.value.trim(),
            knowledgeBase.value.trim() || undefined,
            normalizedAllowedGroups.length > 0 ? normalizedAllowedGroups : undefined
        );
        ElMessage.success('导入完成');
        await store.syncDashboard();
    } catch (error) {
        ingestResult.value = null;
        ElMessage.error(error instanceof Error ? error.message : '导入失败');
    } finally {
        submitting.value = false;
    }
}
</script>

<style scoped lang="less">
.ingest-page {
    min-width: 0;

    &__card {
        margin-bottom: 12px;
    }

    &__label {
        margin-bottom: 6px;
        color: #64748b;
        font-size: 13px;
    }

    :deep(.el-select) {
        width: 100%;
    }

    &__actions {
        display: flex;
        align-items: flex-end;
    }

    &__submit {
        width: 100%;
    }

    &__section-title {
        margin-bottom: 12px;
        font-size: 16px;
        font-weight: 600;
    }

    &__section-subtitle {
        margin-bottom: 8px;
        font-size: 14px;
        font-weight: 600;
        color: #0f172a;
    }

    &__stats {
        margin-bottom: 14px;
    }

    &__stat {
        padding: 12px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        background: #f8fafc;
    }

    &__stat-label {
        color: #64748b;
        font-size: 13px;
    }

    &__stat-value {
        margin-top: 8px;
        font-size: 22px;
        font-weight: 700;
        color: #0f172a;
    }

    &__section {
        margin-top: 14px;
    }

    &__stack {
        width: 100%;
    }

    &__path {
        overflow-wrap: anywhere;
        padding: 10px 12px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        background: #fff;
    }
}
</style>
