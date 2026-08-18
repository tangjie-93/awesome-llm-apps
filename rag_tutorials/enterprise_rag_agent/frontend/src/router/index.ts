import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    {
        path: '/',
        redirect: '/dashboard'
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: () => import('@/views/dashboard/index.vue')
    },
    {
        path: '/knowledge-bases',
        name: 'KnowledgeBases',
        component: () => import('@/views/knowledge-bases/index.vue')
    },
    {
        path: '/documents',
        name: 'Documents',
        component: () => import('@/views/documents/index.vue')
    },
    {
        path: '/ingest',
        name: 'Ingest',
        component: () => import('@/views/ingest/index.vue')
    },
    {
        path: '/ask',
        name: 'Ask',
        component: () => import('@/views/ask/index.vue')
    },
    {
        path: '/search',
        name: 'Search',
        component: () => import('@/views/search/index.vue')
    },
    {
        path: '/evaluate',
        name: 'Evaluate',
        component: () => import('@/views/evaluate/index.vue')
    },
    {
        path: '/logs',
        name: 'Logs',
        component: () => import('@/views/logs/index.vue')
    },
    {
        path: '/scope',
        name: 'Scope',
        component: () => import('@/views/scope/index.vue')
    },
    {
        path: '/admin',
        name: 'Admin',
        component: () => import('@/views/admin/index.vue')
    },
    {
        path: '/users',
        name: 'Users',
        component: () => import('@/views/users/index.vue')
    },
    {
        path: '/roles',
        name: 'Roles',
        component: () => import('@/views/roles/index.vue')
    },
    {
        path: '/diagnostics',
        name: 'Diagnostics',
        component: () => import('@/views/diagnostics/index.vue')
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
