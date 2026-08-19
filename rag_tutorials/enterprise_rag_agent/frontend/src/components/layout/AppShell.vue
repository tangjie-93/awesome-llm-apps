<template>
    <div class="app-shell">
        <aside class="app-shell__sidebar">
            <div class="app-shell__brand">
                <div class="app-shell__title">企业 RAG</div>
                <div class="app-shell__subtitle">企业知识检索与智能问答平台</div>
            </div>
            <nav class="app-shell__nav" aria-label="主导航">
                <section v-for="section in navigationSections" :key="section.key" class="app-shell__section">
                    <h2 class="app-shell__section-title">{{ section.label }}</h2>
                    <RouterLink
                        v-for="item in section.items"
                        :key="item.path"
                        class="app-shell__link"
                        active-class="app-shell__link--active"
                        :to="item.path"
                    >
                        {{ item.label }}
                    </RouterLink>
                </section>
            </nav>
        </aside>
        <main class="app-shell__main">
            <AppContent>
                <slot />
            </AppContent>
        </main>
    </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { RouterLink } from 'vue-router';
import AppContent from '@/components/layout/AppContent.vue';
import { appRoutes } from '@/router/routes';
import type { NavigationGroup, NavigationSection } from '@/types/navigation';

const navigationGroups: NavigationGroup[] = [
    { key: 'workspace', label: '工作台' },
    { key: 'knowledgeAssets', label: '知识资产' },
    { key: 'governance', label: '治理与运营' },
    { key: 'system', label: '系统管理' }
];

/**
 * 按主题提取可见路由作为左侧导航，避免壳层和路由定义分散维护。
 */
const navigationSections = computed<NavigationSection[]>(() =>
    navigationGroups
        .map((group) => ({
            ...group,
            items: appRoutes
                .filter((route) => route.meta?.navGroup === group.key && Boolean(route.meta?.navLabel))
                .map((route) => ({
                    path: route.path,
                    label: String(route.meta?.navLabel)
                }))
        }))
        .filter((section) => section.items.length > 0)
);
</script>

<style scoped lang="less">
.app-shell {
    display: flex;
    min-height: 100vh;
    background: #f8fafc;

    &__sidebar {
        position: sticky;
        top: 0;
        width: 208px;
        height: 100vh;
        flex: 0 0 208px;
        overflow-y: auto;
        border-right: 1px solid #e2e8f0;
        padding: 14px 10px;
        background: #fff;
    }

    &__brand {
        margin-bottom: 14px;
        padding: 0 6px 10px;
        border-bottom: 1px solid #e2e8f0;
    }

    &__title {
        font-size: 18px;
        font-weight: 700;
        color: #0f172a;
    }

    &__subtitle {
        margin-top: 4px;
        font-size: 12px;
        color: #64748b;
    }

    &__nav {
        display: grid;
        gap: 12px;
    }

    &__section {
        display: grid;
        gap: 4px;
        padding: 8px 0 12px;
        border-bottom: 1px solid #e2e8f0;

        &:last-child {
            padding-bottom: 0;
            border-bottom: 0;
        }
    }

    &__section-title {
        margin: 0;
        padding: 0 10px 2px;
        color: #475569;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 0;
        text-transform: uppercase;
    }

    &__link {
        display: flex;
        align-items: center;
        min-height: 36px;
        padding: 8px 10px 8px 20px;
        border-radius: 8px;
        text-decoration: none;
        color: #0f172a;
        background: transparent;
        font-size: 14px;
        border: 1px solid transparent;

        &--active {
            background: #eff6ff;
            border-color: #bfdbfe;
            box-shadow: inset 3px 0 0 #1d4ed8;
            color: #1d4ed8;
            font-weight: 700;
        }

        &:hover:not(&--active) {
            background: #f1f5f9;
            border-color: #e2e8f0;
        }
    }

    &__main {
        min-width: 0;
        flex: 1;
        height: 100vh;
        overflow-y: auto;
    }

    @media (max-width: 860px) {
        display: block;

        &__sidebar {
            position: static;
            width: 100%;
            height: auto;
            border-right: 0;
            border-bottom: 1px solid #e2e8f0;
        }

        &__nav {
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 12px;
        }

        &__main {
            height: auto;
            overflow: visible;
        }
    }
}
</style>
