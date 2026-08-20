<template>
    <el-space v-if="items.length" wrap>
        <el-tag v-for="item in items" :key="item" :type="resolveType(item)" size="small">
            {{ item }}
        </el-tag>
    </el-space>
    <span v-else class="tag-list__empty">{{ emptyText }}</span>
</template>

<script setup lang="ts">
import type { TagListProps, TagType } from '@/types/ui';

const props = withDefaults(defineProps<TagListProps>(), {
    type: undefined,
    typeFor: undefined,
    emptyText: '-'
});

/**
 * 解析单个标签的展示类型：优先按条目动态计算，其次使用统一类型。
 * @param item 标签文本。
 * @returns 标签展示类型；未配置时使用 Element Plus 默认样式。
 */
function resolveType(item: string): TagType | undefined {
    return props.typeFor ? props.typeFor(item) : props.type;
}
</script>

<style scoped lang="less">
.tag-list {
    &__empty {
        color: #94a3b8;
        font-size: 13px;
    }
}
</style>
