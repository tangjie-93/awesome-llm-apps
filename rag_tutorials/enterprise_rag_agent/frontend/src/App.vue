<template>
    <div class="app-shell">
        <header class="app-shell__header">
            <div class="app-shell__brand">
                <div class="app-shell__title">企业 RAG</div>
                <div class="app-shell__subtitle">阶段 0 范围与知识工作区</div>
            </div>
            <nav class="app-shell__nav" aria-label="主导航">
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/dashboard">仪表盘</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/knowledge-bases">知识库</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/documents">文档</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/ingest">导入</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/ask">问答</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/search">检索</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/evaluate">评估</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/logs">日志</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/scope">范围</RouterLink>
            </nav>
        </header>
        <main class="app-shell__main">
            <router-view />
        </main>
    </div>
</template>

<style scoped lang="less">
.app-shell {
    min-height: 100vh;
    background: #f8fafc;

    &__header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 24px;
        padding: 16px 24px;
        border-bottom: 1px solid #e2e8f0;
        background: #fff;
    }

    &__brand {
        min-width: 220px;
    }

    &__title {
        font-size: 18px;
        font-weight: 700;
        color: #0f172a;
    }

    &__subtitle {
        margin-top: 4px;
        font-size: 12px;
        color: #64748b;
    }

    &__nav {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-end;
        gap: 8px;
    }

    &__link {
        padding: 8px 12px;
        border-radius: 8px;
        text-decoration: none;
        color: #0f172a;
        background: #f8fafc;

        &--active {
            background: #1d4ed8;
            color: #fff;
        }
    }

    &__main {
        min-width: 0;
    }
}
</style>
