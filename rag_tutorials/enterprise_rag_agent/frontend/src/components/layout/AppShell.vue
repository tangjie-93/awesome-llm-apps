<template>
    <el-container class="app-shell">
        <el-aside class="app-shell__sidebar" width="208px">
            <div class="app-shell__brand">
                <div class="app-shell__title">企业 RAG</div>
                <div class="app-shell__subtitle">企业知识检索与智能问答平台</div>
            </div>
            <el-menu
                class="app-shell__menu"
                :default-active="activePath"
                :default-openeds="openedSections"
                router
                unique-opened
            >
                <el-sub-menu v-for="section in navigationSections" :key="section.key" :index="section.key">
                    <template #title>
                        <span class="app-shell__section-title">{{ section.label }}</span>
                    </template>
                    <el-menu-item v-for="item in section.items" :key="item.path" :index="item.path">
                        {{ item.label }}
                    </el-menu-item>
                </el-sub-menu>
            </el-menu>
        </el-aside>
        <el-main class="app-shell__main">
            <AppContent>
                <slot />
            </AppContent>
        </el-main>
    </el-container>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import AppContent from '@/components/layout/AppContent.vue';
import { appRoutes } from '@/router/routes';
import type { NavigationGroup, NavigationSection } from '@/types/navigation';

const navigationGroups: NavigationGroup[] = [
    { key: 'workspace', label: '工作台' },
    { key: 'knowledgeAssets', label: '知识资产' },
    { key: 'governance', label: '治理与运营' },
    { key: 'system', label: '系统管理' }
];
const route = useRoute();
const activePath = computed(() => route.path);

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

const openedSections = computed(() => navigationSections.value.map((section) => section.key));
</script>

<style scoped lang="less">
.app-shell {
    min-height: 100vh;
    background: #f8fafc;

    &__sidebar {
        height: 100vh;
        overflow: hidden;
        border-right: 1px solid #e2e8f0;
        padding: 14px 12px;
        background: #fff;
    }

    &__brand {
        margin-bottom: 14px;
        padding: 0 4px 10px;
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

    &__section-title {
        margin: 0;
        color: #64748b;
        font-size: 13px;
        font-weight: 700;
    }

    &__menu {
        border-right: 0;
        background: transparent;
    }

    &__main {
        min-width: 0;
        height: 100vh;
        overflow-y: auto;
    }

    @media (max-width: 860px) {
        &__sidebar {
            width: 100%;
            height: auto;
            border-right: 0;
            border-bottom: 1px solid #e2e8f0;
        }

        &__main {
            height: auto;
            overflow: visible;
        }
    }
}

:deep(.el-menu) {
    border-right: 0;
    background: transparent;
}

:deep(.el-sub-menu__title) {
    padding-left: 4px;
    height: 40px;
    line-height: 40px;
    font-weight: 600;
}

:deep(.el-menu-item) {
    margin: 0 0 4px 12px;
    height: 36px;
    line-height: 36px;
    border-radius: 8px;
}

:deep(.el-menu-item.is-active) {
    background: #eff6ff;
    color: #1d4ed8;
    font-weight: 700;
}
</style>
