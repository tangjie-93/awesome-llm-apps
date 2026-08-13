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
        path: '/ask',
        name: 'Ask',
        component: () => import('@/views/ask/index.vue')
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
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;
