<template>
    <div class="app-content">
        <div class="app-content__inner">
            <slot />
        </div>
    </div>
</template>

<style scoped lang="less">
.app-content {
    min-height: 100%;
    padding: 16px 20px 20px;

    &__inner {
        min-width: 0;
    }

    :deep(.page),
    :deep(.admin-page),
    :deep(.users-page),
    :deep(.roles-page),
    :deep(.scope-page),
    :deep(.diagnostics-page),
    :deep(.knowledge-graph-page) {
        margin: 0;
        padding: 0;
        max-width: none;
    }
}
</style>
