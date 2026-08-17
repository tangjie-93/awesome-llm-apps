<template>
    <section class="scope-page">
        <header class="scope-page__header">
            <div>
                <h1 class="scope-page__title">范围</h1>
                <p class="scope-page__subtitle">阶段 0 范围、配置和权限总览</p>
            </div>
            <button class="scope-page__button" @click="refreshScope">刷新</button>
        </header>

        <div class="scope-grid">
            <article class="scope-card">
                <h2 class="scope-card__title">基础配置</h2>
                <dl class="scope-list">
                    <div>
                        <dt>公司</dt>
                        <dd>{{ store.config.company_name ?? store.companyName }}</dd>
                    </div>
                    <div>
                        <dt>默认知识库</dt>
                        <dd>{{ store.config.default_knowledge_base ?? 'general' }}</dd>
                    </div>
                    <div>
                        <dt>LLM</dt>
                        <dd>{{ store.config.enable_llm ? '已启用' : '未启用' }}</dd>
                    </div>
                    <div>
                        <dt>供应商</dt>
                        <dd>{{ store.config.llm_provider ?? '-' }}</dd>
                    </div>
                    <div>
                        <dt>模型</dt>
                        <dd>{{ store.config.llm_model ?? '-' }}</dd>
                    </div>
                </dl>
            </article>

            <article class="scope-card">
                <h2 class="scope-card__title">访问组</h2>
                <div class="tag-list">
                    <span v-for="group in store.config.default_groups ?? []" :key="group" class="tag">
                        {{ group }}
                    </span>
                </div>
            </article>

            <article class="scope-card">
                <h2 class="scope-card__title">风险等级</h2>
                <div class="tag-list">
                    <span v-for="risk in store.config.default_risk_levels ?? []" :key="risk" class="tag tag--risk">
                        {{ risk }}
                    </span>
                </div>
            </article>

            <article class="scope-card">
                <h2 class="scope-card__title">检索默认值</h2>
                <dl class="scope-list">
                    <div>
                        <dt>分块大小</dt>
                        <dd>{{ store.config.chunk_size ?? '-' }}</dd>
                    </div>
                    <div>
                        <dt>分块重叠</dt>
                        <dd>{{ store.config.chunk_overlap ?? '-' }}</dd>
                    </div>
                    <div>
                        <dt>Top K</dt>
                        <dd>{{ store.config.top_k ?? '-' }}</dd>
                    </div>
                    <div>
                        <dt>重排 Top K</dt>
                        <dd>{{ store.config.rerank_top_k ?? '-' }}</dd>
                    </div>
                </dl>
            </article>

            <article class="scope-card">
                <h2 class="scope-card__title">知识库</h2>
                <div class="tag-list">
                    <span v-for="kb in store.knowledgeBases" :key="kb" class="tag">
                        {{ kb }}
                    </span>
                </div>
            </article>

            <article class="scope-card">
                <h2 class="scope-card__title">样本文档</h2>
                <ul class="scope-bullets">
                    <li v-for="doc in store.documents" :key="String(doc.source_id)">
                        {{ doc.knowledge_base }} / {{ doc.title }} / {{ doc.allowed_groups.join(', ') }} / {{ doc.risk_level }}
                    </li>
                </ul>
            </article>

            <article class="scope-card scope-card--wide">
                <h2 class="scope-card__title">业务范围</h2>
                <ul class="scope-bullets">
                    <li v-for="domain in businessDomains" :key="domain.code">
                        {{ domain.code }}：{{ domain.description }}
                    </li>
                </ul>
            </article>

            <article class="scope-card scope-card--wide">
                <h2 class="scope-card__title">不在范围内</h2>
                <ul class="scope-bullets">
                    <li v-for="item in excludedScopes" :key="item">{{ item }}</li>
                </ul>
            </article>

            <article class="scope-card scope-card--wide">
                <h2 class="scope-card__title">权限说明</h2>
                <ul class="scope-bullets">
                    <li v-for="rule in permissionSummary" :key="rule">{{ rule }}</li>
                </ul>
            </article>

            <article class="scope-card scope-card--wide">
                <h2 class="scope-card__title">风险映射</h2>
                <dl class="scope-list">
                    <div v-for="[group, riskLevel] in riskEntries" :key="group">
                        <dt>{{ group }}</dt>
                        <dd>{{ riskLevel }}</dd>
                    </div>
                </dl>
                <p class="scope-copy">{{ store.scope?.high_risk_policy }}</p>
            </article>
        </div>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted } from 'vue';
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
        font-size: 24px;
    }

    &__subtitle {
        margin: 8px 0 0;
        color: #64748b;
    }

    &__button {
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 10px 14px;
        background: #fff;
        cursor: pointer;
    }
}

.scope-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
}

.scope-card {
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 16px;
    background: #fff;

    &--wide {
        grid-column: 1 / -1;
    }

    &__title {
        margin: 0 0 12px;
        font-size: 16px;
    }
}

.scope-list {
    display: grid;
    gap: 12px;

    dt {
        font-size: 13px;
        color: #64748b;
    }

    dd {
        margin: 4px 0 0;
        font-weight: 600;
    }
}

.tag-list {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.tag {
    padding: 6px 10px;
    border-radius: 999px;
    background: #eff6ff;
    color: #1d4ed8;
    font-size: 13px;

    &--risk {
        background: #fef3c7;
        color: #92400e;
    }
}

.scope-bullets {
    margin: 0;
    padding-left: 18px;
    color: #0f172a;

    li + li {
        margin-top: 8px;
    }
}

.scope-copy {
    margin: 0;
    color: #0f172a;
    line-height: 1.6;
}
</style>
