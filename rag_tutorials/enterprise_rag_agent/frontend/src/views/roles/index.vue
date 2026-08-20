<template>
    <section class="roles-page">
        <PageHeader />

        <el-card shadow="never" class="roles-page__card">
            <div class="roles-page__section-title">{{ editingId ? '编辑角色' : '新建角色' }}</div>
            <el-row :gutter="12" align="bottom">
                <el-col :xs="24" :md="8">
                    <div class="roles-page__label">角色名称</div>
                    <el-input v-model.trim="name" :disabled="editingSystemRole" />
                </el-col>
                <el-col :xs="24" :md="8">
                    <div class="roles-page__label">角色说明</div>
                    <el-input v-model.trim="description" />
                </el-col>
                <el-col :xs="24" :md="8">
                    <div class="roles-page__label">权限项</div>
                    <el-select v-model="selectedPermissions" multiple collapse-tags collapse-tags-tooltip placeholder="选择权限项">
                        <el-option
                            v-for="permission in permissionOptions"
                            :key="permission.value"
                            :label="permission.label"
                            :value="permission.value"
                        />
                    </el-select>
                </el-col>
                <el-col :xs="24" class="roles-page__actions">
                    <el-button type="primary" :loading="saving" @click="saveRole">
                        {{ editingId ? '保存修改' : '创建角色' }}
                    </el-button>
                    <el-button v-if="editingId" :loading="saving" @click="resetForm">取消编辑</el-button>
                    <el-button :loading="saving" @click="refresh">刷新</el-button>
                </el-col>
            </el-row>
            <el-alert v-if="message" :title="message" type="info" show-icon class="roles-page__alert" />
        </el-card>

        <el-card shadow="never" class="roles-page__card">
            <div class="roles-page__header">
                <div class="roles-page__section-title">角色列表</div>
            </div>
            <el-empty v-if="!store.roles.length" description="暂无角色。" />
            <el-table v-else :data="store.roles" border stripe>
                <el-table-column label="角色" min-width="180">
                    <template #default="{ row }">
                        <strong>{{ row.name }}</strong>
                    </template>
                </el-table-column>
                <el-table-column label="说明" min-width="180">
                    <template #default="{ row }">
                        {{ row.description || '暂无说明' }}
                    </template>
                </el-table-column>
                <el-table-column label="权限项" min-width="240">
                    <template #default="{ row }">
                        {{ row.permissions.join(', ') || '暂无权限项' }}
                    </template>
                </el-table-column>
                <el-table-column label="类型" width="120">
                    <template #default="{ row }">
                        <el-tag v-if="row.is_system" type="success">系统角色</el-tag>
                        <span v-else>自定义</span>
                    </template>
                </el-table-column>
                <el-table-column label="操作" width="170" fixed="right">
                    <template #default="{ row }">
                        <div class="roles-page__row-actions">
                            <el-button size="small" @click="editRole(row.id)">编辑</el-button>
                            <el-button size="small" type="danger" plain :disabled="row.is_system" @click="removeRole(row.id)">
                                删除
                            </el-button>
                        </div>
                    </template>
                </el-table-column>
            </el-table>
        </el-card>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import PageHeader from '@/components/ui/PageHeader.vue';
import { useRagStore } from '@/store/rag';

const store = useRagStore();
const editingId = ref<number | null>(null);
const name = ref('');
const description = ref('');
const selectedPermissions = ref<string[]>([]);
const message = ref('');
const saving = ref(false);
const editingSystemRole = computed(() => store.roles.find((item) => item.id === editingId.value)?.is_system ?? false);
const permissionOptions = [
    { label: 'read_documents', value: 'read_documents' },
    { label: 'ask_questions', value: 'ask_questions' },
    { label: 'run_ingest', value: 'run_ingest' },
    { label: 'manage_documents', value: 'manage_documents' },
    { label: 'read_audit', value: 'read_audit' },
    { label: 'manage_users', value: 'manage_users' },
    { label: 'manage_roles', value: 'manage_roles' },
    { label: 'manage_audit', value: 'manage_audit' }
];

/** 刷新角色和用户目录。 */
async function refresh(): Promise<void> {
    try {
        await store.syncUserDirectory();
    } catch (error) {
        message.value = error instanceof Error ? error.message : '角色目录加载失败';
    }
}

/** 清空角色编辑表单。 */
function resetForm(): void {
    editingId.value = null;
    name.value = '';
    description.value = '';
    selectedPermissions.value = [];
}

/** 将角色加载到编辑表单。 */
function editRole(roleId: number): void {
    const role = store.roles.find((item) => item.id === roleId);
    if (!role) return;
    editingId.value = role.id;
    name.value = role.name;
    description.value = role.description;
    selectedPermissions.value = [...role.permissions];
}

/** 保存新增或编辑后的角色。 */
async function saveRole(): Promise<void> {
    if (!name.value.trim()) {
        message.value = '请填写角色名称';
        return;
    }
    const permissions = selectedPermissions.value;
    saving.value = true;
    message.value = '';
    try {
        if (editingId.value) {
            await store.updateRole(editingId.value, {
                name: name.value.trim(),
                description: description.value.trim(),
                permissions
            });
            message.value = '角色已更新';
        } else {
            await store.createRole({
                name: name.value.trim(),
                description: description.value.trim(),
                permissions
            });
            message.value = '角色已创建';
        }
        resetForm();
    } catch (error) {
        message.value = error instanceof Error ? error.message : '角色保存失败';
    } finally {
        saving.value = false;
    }
}

/** 删除自定义角色并刷新目录。 */
async function removeRole(roleId: number): Promise<void> {
    if (!window.confirm('确定删除这个角色吗？')) return;
    saving.value = true;
    try {
        await store.deleteRole(roleId);
        message.value = '角色已删除';
    } catch (error) {
        message.value = error instanceof Error ? error.message : '角色删除失败';
    } finally {
        saving.value = false;
    }
}

onMounted(() => {
    void refresh();
});
</script>

<style scoped lang="less">
.roles-page {
    min-width: 0;

    &__card {
        margin-bottom: 12px;
    }

    &__section-title {
        margin-bottom: 12px;
        font-size: 16px;
        font-weight: 600;
        color: #0f172a;
    }

    &__label {
        margin-bottom: 6px;
        color: #64748b;
        font-size: 13px;
    }

    &__actions {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }

    &__alert {
        margin-top: 12px;
    }

    &__header {
        margin-bottom: 12px;
    }

    &__row-actions {
        display: flex;
        gap: 8px;
    }
}
</style>
