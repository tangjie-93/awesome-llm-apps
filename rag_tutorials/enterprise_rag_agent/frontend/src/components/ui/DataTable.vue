<template>
    <el-table
        :data="data"
        v-loading="loading"
        :stripe="stripe"
        :size="size"
        :height="fill ? '100%' : undefined"
        class="data-table"
        :class="{ 'data-table--fill': fill }"
        v-bind="$attrs"
    >
        <slot />
        <template #empty>
            <slot name="empty">
                <el-empty :description="emptyDescription ?? '暂无数据'" />
            </slot>
        </template>
        <template v-if="$slots.append" #append>
            <slot name="append" />
        </template>
    </el-table>
</template>

<script setup lang="ts">
import type { DataTableProps } from '@/types/ui';

withDefaults(defineProps<DataTableProps>(), {
    loading: false,
    stripe: true,
    fill: true,
    size: 'default',
    emptyDescription: undefined
});

// row-key、selection-change 等未声明的属性和事件透传给 el-table。
defineOptions({ inheritAttrs: false });
</script>

<style scoped lang="less">
.data-table {
    width: 100%;

    // 铺满模式下作为弹性子项占据父容器剩余高度
    &--fill {
        flex: 1;
        min-height: 0;
    }

    // 表头：与表体不同的底色，保留底部分隔 border
    :deep(.el-table__header-wrapper th.el-table__cell) {
        background: #f1f5f9;
        color: #334155;
        font-weight: 600;
        border-bottom: 1px solid #dbe3ec;
    }

    // 表头列之间的竖向 border（最后一列除外）
    :deep(.el-table__header-wrapper th.el-table__cell:not(:last-child)) {
        border-right: 1px solid #e2e8f0;
    }

    // 表体：不显示任何 border，仅靠斑马纹与悬停高亮区分行
    :deep(.el-table__body-wrapper td.el-table__cell) {
        border-bottom: none;
    }
}
</style>
