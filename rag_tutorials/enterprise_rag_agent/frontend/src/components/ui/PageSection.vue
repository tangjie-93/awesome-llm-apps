<template>
    <el-card shadow="never" class="page-section" :class="{ 'page-section--fill': fill }">
        <div v-if="title || $slots.actions" class="page-section__header">
            <div class="page-section__heading">
                <div v-if="title" class="page-section__title">{{ title }}</div>
                <div v-if="subtitle" class="page-section__subtitle">{{ subtitle }}</div>
            </div>
            <div v-if="$slots.actions" class="page-section__actions">
                <slot name="actions" />
            </div>
        </div>
        <div class="page-section__body">
            <slot />
        </div>
    </el-card>
</template>

<script setup lang="ts">
import type { PageSectionProps } from '@/types/ui';

defineProps<PageSectionProps>();
</script>

<style scoped lang="less">
.page-section {
    margin-bottom: 12px;

    &__header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 12px;
    }

    &__heading {
        min-width: 0;
    }

    &__title {
        color: #0f172a;
        font-size: 16px;
        font-weight: 600;
    }

    &__subtitle {
        margin-top: 4px;
        color: #64748b;
        font-size: 13px;
    }

    &__actions {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-end;
        gap: 8px;
    }

    // 铺满模式：卡片占满页面剩余高度，内容区自适应，滚动交给内部（如表格体）
    &--fill {
        flex: 1;
        min-height: 0;
        display: flex;
        flex-direction: column;
        overflow: hidden;

        :deep(.el-card__body) {
            flex: 1;
            min-height: 0;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        .page-section__body {
            flex: 1;
            min-height: 0;
            display: flex;
            flex-direction: column;
        }
    }
}
</style>
