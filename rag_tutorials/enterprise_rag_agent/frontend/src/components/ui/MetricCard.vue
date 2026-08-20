<template>
    <el-card shadow="never" class="metric-card" :class="`metric-card--${type ?? 'default'}`">
        <div class="metric-card__label">{{ label }}</div>
        <div class="metric-card__value">{{ value }}</div>
        <div v-if="hint" class="metric-card__hint">{{ hint }}</div>
    </el-card>
</template>

<script setup lang="ts">
import type { MetricCardProps } from '@/types/ui';

defineProps<MetricCardProps>();
</script>

<style scoped lang="less">
.metric-card {
    height: 100%;

    &__label {
        color: #64748b;
        font-size: 13px;
    }

    &__value {
        margin-top: 8px;
        color: #0f172a;
        font-size: 28px;
        font-weight: 700;
        line-height: 1.2;
    }

    &__hint {
        margin-top: 8px;
        color: #64748b;
        font-size: 12px;
    }

    &--success {
        border-color: #bbf7d0;
        background: #f0fdf4;
    }

    &--warning {
        border-color: #fed7aa;
        background: #fff7ed;
    }

    &--danger {
        border-color: #fecaca;
        background: #fef2f2;
    }
}
</style>
