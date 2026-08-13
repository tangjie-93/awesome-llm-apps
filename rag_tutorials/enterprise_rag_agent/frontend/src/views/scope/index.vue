<template>
    <section class="scope-page">
        <header class="scope-page__header">
            <div>
                <h1 class="scope-page__title">Scope</h1>
                <p class="scope-page__subtitle">Stage 0 scope, config and access overview</p>
            </div>
            <button class="scope-page__button" @click="refreshScope">Refresh</button>
        </header>

        <div class="scope-grid">
            <article class="scope-card">
                <h2 class="scope-card__title">Base Config</h2>
                <dl class="scope-list">
                    <div>
                        <dt>Company</dt>
                        <dd>{{ store.config.company_name ?? store.companyName }}</dd>
                    </div>
                    <div>
                        <dt>Default KB</dt>
                        <dd>{{ store.config.default_knowledge_base ?? 'general' }}</dd>
                    </div>
                    <div>
                        <dt>LLM</dt>
                        <dd>{{ store.config.enable_llm ? 'enabled' : 'disabled' }}</dd>
                    </div>
                    <div>
                        <dt>Provider</dt>
                        <dd>{{ store.config.llm_provider ?? '-' }}</dd>
                    </div>
                    <div>
                        <dt>Model</dt>
                        <dd>{{ store.config.llm_model ?? '-' }}</dd>
                    </div>
                </dl>
            </article>

            <article class="scope-card">
                <h2 class="scope-card__title">Access Groups</h2>
                <div class="tag-list">
                    <span v-for="group in store.config.default_groups ?? []" :key="group" class="tag">
                        {{ group }}
                    </span>
                </div>
            </article>

            <article class="scope-card">
                <h2 class="scope-card__title">Risk Levels</h2>
                <div class="tag-list">
                    <span v-for="risk in store.config.default_risk_levels ?? []" :key="risk" class="tag tag--risk">
                        {{ risk }}
                    </span>
                </div>
            </article>

            <article class="scope-card">
                <h2 class="scope-card__title">Retrieval Defaults</h2>
                <dl class="scope-list">
                    <div>
                        <dt>Chunk Size</dt>
                        <dd>{{ store.config.chunk_size ?? '-' }}</dd>
                    </div>
                    <div>
                        <dt>Chunk Overlap</dt>
                        <dd>{{ store.config.chunk_overlap ?? '-' }}</dd>
                    </div>
                    <div>
                        <dt>Top K</dt>
                        <dd>{{ store.config.top_k ?? '-' }}</dd>
                    </div>
                    <div>
                        <dt>Rerank Top K</dt>
                        <dd>{{ store.config.rerank_top_k ?? '-' }}</dd>
                    </div>
                </dl>
            </article>

            <article class="scope-card">
                <h2 class="scope-card__title">Knowledge Bases</h2>
                <div class="tag-list">
                    <span v-for="kb in store.knowledgeBases" :key="kb" class="tag">
                        {{ kb }}
                    </span>
                </div>
            </article>

            <article class="scope-card">
                <h2 class="scope-card__title">Sample Docs</h2>
                <ul class="scope-bullets">
                    <li v-for="doc in store.documents" :key="String(doc.source_id)">
                        {{ doc.knowledge_base }} / {{ doc.title }} / {{ doc.allowed_groups.join(', ') }}
                    </li>
                </ul>
            </article>

            <article class="scope-card scope-card--wide">
                <h2 class="scope-card__title">Business Scope</h2>
                <ul class="scope-bullets">
                    <li>security: security policy, incident response, access control</li>
                    <li>hr: onboarding, training, employee handbook</li>
                    <li>it: backup, operations, core IT standards</li>
                </ul>
            </article>

            <article class="scope-card scope-card--wide">
                <h2 class="scope-card__title">Out of Scope</h2>
                <ul class="scope-bullets">
                    <li>multi-tenant isolation</li>
                    <li>segment-level permission</li>
                    <li>automatic action execution</li>
                    <li>multimodal input</li>
                    <li>knowledge graph</li>
                </ul>
            </article>

            <article class="scope-card scope-card--wide">
                <h2 class="scope-card__title">Permission Notes</h2>
                <p class="scope-copy">
                    Documents default to <strong>public</strong>. Sensitive documents must be assigned explicitly.
                    Search results are filtered before answering. <strong>high</strong> risk content can produce a
                    candidate answer, but it must be reviewed and approved.
                </p>
            </article>
        </div>
    </section>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();

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
