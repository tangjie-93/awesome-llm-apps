<template>
    <el-tabs class="fill-tabs">
        <slot />
    </el-tabs>
</template>

<style scoped lang="less">
// 铺满父容器剩余高度的页签容器：页签头固定，内容区自适应，滚动发生在内容内部
.fill-tabs {
    flex: 1;
    min-height: 0;
    display: flex;
    flex-direction: column;

    :deep(.el-tabs__header) {
        margin-bottom: 12px;
    }

    :deep(.el-tabs__content) {
        flex: 1;
        min-height: 0;
    }

    :deep(.el-tab-pane) {
        height: 100%;
    }
}
</style>
