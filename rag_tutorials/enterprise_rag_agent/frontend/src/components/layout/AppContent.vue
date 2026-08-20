<template>
    <div class="app-content">
        <slot />
    </div>
</template>

<style scoped lang="less">
// 内容区滚动兜底：页面内容不超过一屏时不出现滚动条；
// 表格类页面通过自身 min-height/flex 布局把滚动收敛到表格体内部。
.app-content {
    height: 100%;
    min-width: 0;
    padding: 16px 20px 20px;
    overflow-y: auto;
}
</style>
