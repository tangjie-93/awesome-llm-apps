<template>
    <div class="empty-state">
        <el-empty :description="description">
            <el-button v-if="actionLabel" type="primary" @click="emit('action')">
                {{ actionLabel }}
            </el-button>
        </el-empty>
    </div>
</template>

<script setup lang="ts">
import type { EmptyStateEmits, EmptyStateProps } from '@/types/ui';

defineProps<EmptyStateProps>();
const emit = defineEmits<EmptyStateEmits>();
</script>

<style scoped lang="less">
.empty-state {
    border: 1px dashed #d8e0ea;
    border-radius: 8px;
    background: #fbfdff;
}
</style>
