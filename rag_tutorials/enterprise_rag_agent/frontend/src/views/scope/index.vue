<template>
    <section class="scope-page">
        <PageHeader>
            <template #actions>
                <el-button @click="refreshScope">刷新</el-button>
            </template>
        </PageHeader>

        <PageSection title="基础信息" subtitle="企业范围、默认权限和检索参数">
            <div class="scope-page__overview">
                <section class="scope-page__panel">
                    <div class="scope-page__panel-title">基础配置</div>
                    <el-descriptions :column="1" border>
                        <el-descriptions-item label="公司">{{ store.config.company_name ?? store.companyName }}</el-descriptions-item>
                        <el-descriptions-item label="默认知识库">{{ store.config.default_knowledge_base ?? 'general' }}</el-descriptions-item>
                        <el-descriptions-item label="LLM">{{ store.config.enable_llm ? '已启用' : '未启用' }}</el-descriptions-item>
                        <el-descriptions-item label="供应商">{{ store.config.llm_provider ?? '-' }}</el-descriptions-item>
                        <el-descriptions-item label="模型">{{ store.config.llm_model ?? '-' }}</el-descriptions-item>
                    </el-descriptions>
                </section>

                <section class="scope-page__panel">
                    <div class="scope-page__panel-title">访问与风险</div>
                    <div class="scope-page__field">
                        <div class="scope-page__label">访问组</div>
                        <el-space wrap>
                            <el-tag v-for="group in store.config.default_groups ?? []" :key="group">{{ group }}</el-tag>
                        </el-space>
                    </div>
                    <div class="scope-page__field">
                        <div class="scope-page__label">风险等级</div>
                        <el-space wrap>
                            <el-tag v-for="risk in store.config.default_risk_levels ?? []" :key="risk" type="warning">
                                {{ risk }}
                            </el-tag>
                        </el-space>
                    </div>
                    <div class="scope-page__field">
                        <div class="scope-page__label">知识库</div>
                        <el-space wrap>
                            <el-tag v-for="kb in store.knowledgeBases" :key="kb">{{ kb }}</el-tag>
                        </el-space>
                    </div>
                </section>

                <section class="scope-page__panel">
                    <div class="scope-page__panel-title">检索默认值</div>
                    <div class="scope-page__stat-grid">
                        <div class="scope-page__stat">
                            <span>分块大小</span>
                            <strong>{{ store.config.chunk_size ?? '-' }}</strong>
                        </div>
                        <div class="scope-page__stat">
                            <span>分块重叠</span>
                            <strong>{{ store.config.chunk_overlap ?? '-' }}</strong>
                        </div>
                        <div class="scope-page__stat">
                            <span>Top K</span>
                            <strong>{{ store.config.top_k ?? '-' }}</strong>
                        </div>
                        <div class="scope-page__stat">
                            <span>重排 Top K</span>
                            <strong>{{ store.config.rerank_top_k ?? '-' }}</strong>
                        </div>
                    </div>
                </section>
            </div>
        </PageSection>

        <PageSection title="范围内容" subtitle="业务覆盖范围、样本文档和明确排除项">
            <div class="scope-page__content-grid">
                <section class="scope-page__panel">
                    <div class="scope-page__panel-title">业务范围</div>
                    <el-space fill direction="vertical" class="scope-page__stack">
                        <div v-for="domain in businessDomains" :key="domain.code" class="scope-page__item">
                            {{ domain.code }}：{{ domain.description }}
                        </div>
                    </el-space>
                </section>

                <section class="scope-page__panel">
                    <div class="scope-page__panel-title">样本文档</div>
                    <el-space fill direction="vertical" class="scope-page__stack">
                        <div v-for="doc in store.documents" :key="String(doc.source_id)" class="scope-page__item">
                            {{ doc.knowledge_base }} / {{ doc.title }} / {{ doc.allowed_groups.join(', ') }} / {{ doc.risk_level }}
                        </div>
                    </el-space>
                </section>

                <section class="scope-page__panel">
                    <div class="scope-page__panel-title">不在范围内</div>
                    <el-space fill direction="vertical" class="scope-page__stack">
                        <div v-for="item in excludedScopes" :key="item" class="scope-page__item">{{ item }}</div>
                    </el-space>
                </section>

                <section class="scope-page__panel">
                    <div class="scope-page__panel-title">权限说明</div>
                    <el-space fill direction="vertical" class="scope-page__stack">
                        <div v-for="rule in permissionSummary" :key="rule" class="scope-page__item">{{ rule }}</div>
                    </el-space>
                </section>
            </div>
        </PageSection>

        <PageSection title="风险映射" subtitle="访问组与默认风险等级的关系">
            <el-descriptions :column="2" border>
                <el-descriptions-item v-for="[group, riskLevel] in riskEntries" :key="group" :label="group">
                    {{ riskLevel }}
                </el-descriptions-item>
            </el-descriptions>
            <p class="scope-page__copy">{{ store.scope?.high_risk_policy }}</p>
        </PageSection>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import PageSection from '@/components/ui/PageSection.vue';
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

    &__overview,
    &__content-grid {
        display: grid;
        gap: 12px;
    }

    &__overview {
        grid-template-columns: repeat(3, minmax(0, 1fr));
    }

    &__content-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    &__panel {
        min-height: 100%;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px;
        background: #fbfdff;
    }

    &__panel-title {
        margin-bottom: 12px;
        font-size: 16px;
        font-weight: 600;
        color: #0f172a;
    }

    &__stack {
        width: 100%;
    }

    &__field + &__field {
        margin-top: 18px;
    }

    &__label {
        margin-bottom: 8px;
        color: #64748b;
        font-size: 13px;
        font-weight: 600;
    }

    &__stat-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 10px;
    }

    &__stat {
        min-height: 82px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 12px;
        background: #fff;

        span {
            color: #64748b;
            font-size: 13px;
        }

        strong {
            display: block;
            margin-top: 10px;
            color: #0f172a;
            font-size: 22px;
        }
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

    @media (max-width: 1180px) {
        &__overview {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 860px) {
        &__content-grid {
            grid-template-columns: 1fr;
        }
    }
}
</style>
