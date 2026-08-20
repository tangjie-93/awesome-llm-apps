import type { RouteRecordRaw } from 'vue-router';

export const appRoutes: RouteRecordRaw[] = [
    {
        path: '/',
        redirect: '/dashboard'
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: () => import('@/views/dashboard/index.vue'),
        meta: {
            navGroup: 'workspace',
            navLabel: '仪表盘',
            title: '仪表盘',
            subtitle: '企业知识检索与问答总览'
        }
    },
    {
        path: '/knowledge-bases',
        name: 'KnowledgeBases',
        component: () => import('@/views/knowledge-bases/index.vue'),
        meta: {
            navGroup: 'knowledgeAssets',
            navLabel: '知识库概览',
            title: '知识库概览',
            subtitle: '查看知识库分布、文档规模和权限覆盖'
        }
    },
    {
        path: '/documents',
        name: 'Documents',
        component: () => import('@/views/documents/index.vue'),
        meta: {
            navGroup: 'knowledgeAssets',
            navLabel: '文档索引',
            title: '文档索引',
            subtitle: '已导入文档、权限、风险和索引信息'
        }
    },
    {
        path: '/ingest',
        name: 'Ingest',
        component: () => import('@/views/ingest/index.vue'),
        meta: {
            title: '导入文档',
            subtitle: '对应后端 ingest 命令，将本地路径内容导入知识库'
        }
    },
    {
        path: '/ask',
        name: 'Ask',
        component: () => import('@/views/ask/index.vue'),
        meta: {
            navGroup: 'workspace',
            navLabel: '智能问答',
            title: '提问',
            subtitle: '按知识库提问并查看回答与引用'
        }
    },
    {
        path: '/search',
        name: 'Search',
        component: () => import('@/views/search/index.vue'),
        meta: {
            navGroup: 'workspace',
            navLabel: '知识检索',
            title: '检索',
            subtitle: '对应后端 search 命令，展示候选片段与打分'
        }
    },
    {
        path: '/evaluate',
        name: 'Evaluate',
        component: () => import('@/views/evaluate/index.vue'),
        meta: {
            navGroup: 'governance',
            navLabel: '效果评估',
            title: '评估',
            subtitle: '对应后端 evaluate 命令，用于记录答案评分'
        }
    },
    {
        path: '/logs',
        name: 'Logs',
        component: () => import('@/views/logs/index.vue'),
        meta: {
            navGroup: 'governance',
            navLabel: '运行日志',
            title: '日志',
            subtitle: '问答与评估记录'
        }
    },
    {
        path: '/scope',
        name: 'Scope',
        component: () => import('@/views/scope/index.vue'),
        meta: {
            navGroup: 'system',
            navLabel: '范围配置',
            title: '范围',
            subtitle: '阶段 0 范围、配置和权限总览'
        }
    },
    {
        path: '/admin',
        name: 'Admin',
        component: () => import('@/views/admin/index.vue'),
        meta: {
            navGroup: 'system',
            navLabel: '系统管理',
            title: '管理后台',
            subtitle: '身份、审计、用量与检索策略'
        }
    },
    {
        path: '/users',
        name: 'Users',
        component: () => import('@/views/users/index.vue'),
        meta: {
            navGroup: 'system',
            navLabel: '用户管理',
            title: '用户管理',
            subtitle: '管理外部身份映射、权限组和本地角色'
        }
    },
    {
        path: '/roles',
        name: 'Roles',
        component: () => import('@/views/roles/index.vue'),
        meta: {
            navGroup: 'system',
            navLabel: '角色管理',
            title: '角色管理',
            subtitle: '维护角色名称、说明和权限项'
        }
    },
    {
        path: '/diagnostics',
        name: 'Diagnostics',
        component: () => import('@/views/diagnostics/index.vue'),
        meta: {
            navGroup: 'governance',
            navLabel: '运行诊断',
            title: '运行诊断',
            subtitle: '查看知识库健康情况，并在启用后使用外部检索补充信息。'
        }
    },
    {
        path: '/knowledge-graph',
        name: 'KnowledgeGraph',
        component: () => import('@/views/knowledge-graph/index.vue'),
        meta: {
            navGroup: 'knowledgeAssets',
            navLabel: '知识图谱',
            title: '知识图谱',
            subtitle: '查看当前用户有权限访问的实体和一跳关联。'
        }
    }
];
