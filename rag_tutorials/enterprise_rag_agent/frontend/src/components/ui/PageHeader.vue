<template>
    <header class="page-header">
        <div class="page-header__content">
            <h1 class="page-header__title">{{ resolvedTitle }}</h1>
            <p v-if="resolvedSubtitle" class="page-header__subtitle">{{ resolvedSubtitle }}</p>
        </div>
        <div v-if="$slots.actions" class="page-header__actions">
            <slot name="actions" />
        </div>
    </header>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import type { PageHeaderProps } from '@/types/page-header';

const props = defineProps<PageHeaderProps>();
const route = useRoute();

const resolvedTitle = computed(() => props.title ?? String(route.meta.title ?? ''));
const resolvedSubtitle = computed(() => props.subtitle ?? String(route.meta.subtitle ?? ''));
</script>

<style scoped lang="less">
.page-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 16px;
    margin-bottom: 16px;

    &__content {
        min-width: 0;
    }

    &__title {
        margin: 0;
        font-size: 24px;
        line-height: 1.2;
    }

    &__subtitle {
        margin: 8px 0 0;
        color: #64748b;
    }

    &__actions {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-end;
        gap: 10px;
    }

    @media (max-width: 760px) {
        flex-direction: column;
    }
}
</style>
