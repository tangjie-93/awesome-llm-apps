<template>
    <div class="empty-state" :class="{ 'empty-state--fill': fill }">
        <el-empty :description="description">
            <el-button v-if="actionLabel" type="primary" @click="emit('action')">
                {{ actionLabel }}
            </el-button>
        </el-empty>
    </div>
</template>

<script setup lang="ts">
import type { EmptyStateEmits, EmptyStateProps } from '@/types/ui';

withDefaults(defineProps<EmptyStateProps>(), {
    fill: false
});
const emit = defineEmits<EmptyStateEmits>();
</script>

<style scoped lang="less">
.empty-state {
    border: 1px dashed #d8e0ea;
    border-radius: 8px;
    background: #fbfdff;

    // 铺满模式：占位块撑满父容器剩余高度，空态垂直居中
    &--fill {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;

        :deep(.el-empty) {
            padding: 24px 0;
        }
    }
}
</style>
