<template>
    <div class="app-shell">
        <header class="app-shell__header">
            <div class="app-shell__brand">
                <div class="app-shell__title">Enterprise RAG</div>
                <div class="app-shell__subtitle">Stage 0 scope and knowledge workspace</div>
            </div>
            <nav class="app-shell__nav" aria-label="Primary">
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/dashboard">Dashboard</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/knowledge-bases">Knowledge Bases</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/documents">Documents</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/ask">Ask</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/logs">Logs</RouterLink>
                <RouterLink class="app-shell__link" active-class="app-shell__link--active" to="/scope">Scope</RouterLink>
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
