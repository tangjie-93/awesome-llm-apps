<template>
    <div class="form-field">
        <div class="form-field__label">{{ label }}</div>
        <slot />
    </div>
</template>

<script setup lang="ts">
import type { FormFieldProps } from '@/types/ui';

defineProps<FormFieldProps>();
</script>

<style scoped lang="less">
.form-field {
    &__label {
        margin-bottom: 6px;
        color: #64748b;
        font-size: 13px;
    }
}
</style>
