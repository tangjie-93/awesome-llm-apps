<template>
    <div ref="rootRef" class="multi-select">
        <button
            class="multi-select__button"
            type="button"
            :disabled="disabled"
            @click="toggleOpen"
        >
            <span class="multi-select__label">{{ triggerLabel }}</span>
            <ChevronDown :size="14" aria-hidden="true" />
        </button>
        <div v-if="open" class="multi-select__menu">
            <label v-for="option in options" :key="option.value" class="multi-select__option">
                <input
                    type="checkbox"
                    :checked="selectedSet.has(option.value)"
                    :disabled="disabled"
                    @change="toggleValue(option.value)"
                />
                <span>{{ option.label }}</span>
            </label>
        </div>
    </div>
</template>

<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue';
import { ChevronDown } from 'lucide-vue-next';
import type { MultiSelectDropdownEmits, MultiSelectDropdownProps } from '@/types/form-controls';

const props = defineProps<MultiSelectDropdownProps>();
const emit = defineEmits<MultiSelectDropdownEmits>();
const open = ref(false);
const rootRef = ref<HTMLElement | null>(null);

const selectedSet = computed(() => new Set(props.modelValue));

const triggerLabel = computed(() => {
    if (!props.modelValue.length) {
        return props.placeholder ?? '请选择';
    }
    const labels = props.options
        .filter((option) => selectedSet.value.has(option.value))
        .map((option) => option.label);
    return labels.length <= 2 ? labels.join('、') : `${labels.slice(0, 2).join('、')} 等 ${labels.length} 项`;
});

/**
 * 切换下拉菜单显示状态。
 */
function toggleOpen(): void {
    open.value = !open.value;
}

/**
 * 更新当前多选值并保留菜单打开状态，方便连续勾选。
 *
 * @param value 要切换的选项值。
 */
function toggleValue(value: string | number): void {
    const nextValues = new Set(props.modelValue);
    if (nextValues.has(value)) {
        nextValues.delete(value);
    } else {
        nextValues.add(value);
    }
    emit('update:modelValue', Array.from(nextValues));
}

/**
 * 点击外部区域时关闭下拉菜单。
 */
function handleDocumentClick(event: MouseEvent): void {
    if (!open.value) return;
    const target = event.target as Node | null;
    if (rootRef.value && target && !rootRef.value.contains(target)) {
        open.value = false;
    }
}

onMounted(() => {
    document.addEventListener('click', handleDocumentClick);
});

onBeforeUnmount(() => {
    document.removeEventListener('click', handleDocumentClick);
});
</script>

<style scoped lang="less">
.multi-select {
    position: relative;

    &__button {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        min-height: 38px;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 8px 10px;
        background: #fff;
        color: #0f172a;
        cursor: pointer;
    }

    &__label {
        min-width: 0;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        text-align: left;
    }

    &__menu {
        position: absolute;
        z-index: 20;
        top: calc(100% + 6px);
        left: 0;
        width: 100%;
        max-height: 240px;
        overflow: auto;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 8px;
        background: #fff;
        box-shadow: 0 12px 24px rgba(15, 23, 42, 0.12);
    }

    &__option {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 6px 4px;
        color: #0f172a;
        cursor: pointer;

        input {
            margin: 0;
        }
    }
}
</style>
