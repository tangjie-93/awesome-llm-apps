<template>
    <section class="scope-page">
        <PageHeader>
            <template #actions>
                <el-button @click="refreshScope">刷新</el-button>
            </template>
        </PageHeader>

        <el-row :gutter="12">
            <el-col :xs="24" :md="12" :lg="8">
                <el-card shadow="never" class="scope-page__card">
                    <div class="scope-page__title">基础配置</div>
                    <el-descriptions :column="1" border>
                        <el-descriptions-item label="公司">{{ store.config.company_name ?? store.companyName }}</el-descriptions-item>
                        <el-descriptions-item label="默认知识库">{{ store.config.default_knowledge_base ?? 'general' }}</el-descriptions-item>
                        <el-descriptions-item label="LLM">{{ store.config.enable_llm ? '已启用' : '未启用' }}</el-descriptions-item>
                        <el-descriptions-item label="供应商">{{ store.config.llm_provider ?? '-' }}</el-descriptions-item>
                        <el-descriptions-item label="模型">{{ store.config.llm_model ?? '-' }}</el-descriptions-item>
                    </el-descriptions>
                </el-card>
            </el-col>

            <el-col :xs="24" :md="12" :lg="8">
                <el-card shadow="never" class="scope-page__card">
                    <div class="scope-page__title">访问组</div>
                    <el-space wrap>
                        <el-tag v-for="group in store.config.default_groups ?? []" :key="group">{{ group }}</el-tag>
                    </el-space>
                </el-card>
            </el-col>

            <el-col :xs="24" :md="12" :lg="8">
                <el-card shadow="never" class="scope-page__card">
                    <div class="scope-page__title">风险等级</div>
                    <el-space wrap>
                        <el-tag v-for="risk in store.config.default_risk_levels ?? []" :key="risk" type="warning">{{ risk }}</el-tag>
                    </el-space>
                </el-card>
            </el-col>

            <el-col :xs="24" :md="12" :lg="8">
                <el-card shadow="never" class="scope-page__card">
                    <div class="scope-page__title">检索默认值</div>
                    <el-descriptions :column="1" border>
                        <el-descriptions-item label="分块大小">{{ store.config.chunk_size ?? '-' }}</el-descriptions-item>
                        <el-descriptions-item label="分块重叠">{{ store.config.chunk_overlap ?? '-' }}</el-descriptions-item>
                        <el-descriptions-item label="Top K">{{ store.config.top_k ?? '-' }}</el-descriptions-item>
                        <el-descriptions-item label="重排 Top K">{{ store.config.rerank_top_k ?? '-' }}</el-descriptions-item>
                    </el-descriptions>
                </el-card>
            </el-col>

            <el-col :xs="24" :md="12" :lg="8">
                <el-card shadow="never" class="scope-page__card">
                    <div class="scope-page__title">知识库</div>
                    <el-space wrap>
                        <el-tag v-for="kb in store.knowledgeBases" :key="kb">{{ kb }}</el-tag>
                    </el-space>
                </el-card>
            </el-col>

            <el-col :xs="24" :md="12" :lg="8">
                <el-card shadow="never" class="scope-page__card">
                    <div class="scope-page__title">样本文档</div>
                    <el-space fill direction="vertical" class="scope-page__stack">
                        <div v-for="doc in store.documents" :key="String(doc.source_id)" class="scope-page__item">
                            {{ doc.knowledge_base }} / {{ doc.title }} / {{ doc.allowed_groups.join(', ') }} / {{ doc.risk_level }}
                        </div>
                    </el-space>
                </el-card>
            </el-col>

            <el-col :xs="24">
                <el-card shadow="never" class="scope-page__card">
                    <div class="scope-page__title">业务范围</div>
                    <el-space fill direction="vertical" class="scope-page__stack">
                        <div v-for="domain in businessDomains" :key="domain.code" class="scope-page__item">
                            {{ domain.code }}：{{ domain.description }}
                        </div>
                    </el-space>
                </el-card>
            </el-col>

            <el-col :xs="24" :md="12">
                <el-card shadow="never" class="scope-page__card">
                    <div class="scope-page__title">不在范围内</div>
                    <el-space fill direction="vertical" class="scope-page__stack">
                        <div v-for="item in excludedScopes" :key="item" class="scope-page__item">{{ item }}</div>
                    </el-space>
                </el-card>
            </el-col>

            <el-col :xs="24" :md="12">
                <el-card shadow="never" class="scope-page__card">
                    <div class="scope-page__title">权限说明</div>
                    <el-space fill direction="vertical" class="scope-page__stack">
                        <div v-for="rule in permissionSummary" :key="rule" class="scope-page__item">{{ rule }}</div>
                    </el-space>
                </el-card>
            </el-col>

            <el-col :xs="24">
                <el-card shadow="never" class="scope-page__card">
                    <div class="scope-page__title">风险映射</div>
                    <el-descriptions :column="2" border>
                        <el-descriptions-item v-for="[group, riskLevel] in riskEntries" :key="group" :label="group">
                            {{ riskLevel }}
                        </el-descriptions-item>
                    </el-descriptions>
                    <p class="scope-page__copy">{{ store.scope?.high_risk_policy }}</p>
                </el-card>
            </el-col>
        </el-row>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();

const businessDomains = computed(() => store.scope?.business_domains ?? []);
const excludedScopes = computed(() => store.scope?.excluded_scopes ?? []);
const permissionSummary = computed(() => store.scope?.permission_summary ?? []);
const riskEntries = computed(() => Object.entries(store.scope?.risk_by_group ?? {}));

/**
 * 刷新阶段 0 只读范围数据；成功时同步配置、范围、知识库和文档，失败信息由 store 记录。
 */
async function refreshScope(): Promise<void> {
    await store.syncDashboard();
}

onMounted(() => {
    void refreshScope();
});
</script>

<style scoped lang="less">
.scope-page {
    min-width: 0;

    &__card {
        margin-bottom: 12px;
    }

    &__title {
        margin-bottom: 12px;
        font-size: 16px;
        font-weight: 600;
        color: #0f172a;
    }

    &__stack {
        width: 100%;
    }

    &__item,
    &__copy {
        color: #475569;
        line-height: 1.6;
    }

    &__item {
        padding: 10px 12px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        background: #f8fafc;
    }

    &__copy {
        margin: 12px 0 0;
    }
}
</style>
