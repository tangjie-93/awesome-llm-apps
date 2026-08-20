<template>
    <section class="users-page">
        <PageHeader />

        <el-card shadow="never" class="users-page__card">
            <div class="users-page__section-title">{{ editingId ? '编辑用户' : '新建用户' }}</div>
            <el-row :gutter="12" align="bottom">
                <el-col :xs="24" :md="4">
                    <div class="users-page__label">外部身份 ID</div>
                    <el-input v-model.trim="externalId" :disabled="Boolean(editingId)" />
                </el-col>
                <el-col :xs="24" :md="4">
                    <div class="users-page__label">显示名称</div>
                    <el-input v-model.trim="displayName" />
                </el-col>
                <el-col :xs="24" :md="4">
                    <div class="users-page__label">邮箱</div>
                    <el-input v-model.trim="email" type="email" />
                </el-col>
                <el-col :xs="24" :md="4">
                    <div class="users-page__label">权限组</div>
                    <el-input v-model="groupsInput" placeholder="public,security" />
                </el-col>
                <el-col :xs="24" :md="4">
                    <div class="users-page__label">角色</div>
                    <el-select v-model="selectedRoleIds" multiple collapse-tags collapse-tags-tooltip placeholder="选择角色">
                        <el-option v-for="role in roleOptions" :key="role.value" :label="role.label" :value="role.value" />
                    </el-select>
                </el-col>
                <el-col v-if="editingId" :xs="24" :md="2">
                    <el-checkbox v-model="isActive" class="users-page__checkbox">启用用户</el-checkbox>
                </el-col>
                <el-col :xs="24" :md="2" class="users-page__actions">
                    <el-button type="primary" :loading="saving" @click="saveUser">
                        {{ editingId ? '保存修改' : '创建用户' }}
                    </el-button>
                </el-col>
                <el-col v-if="editingId" :xs="24" :md="2" class="users-page__actions">
                    <el-button :loading="saving" @click="resetForm">取消编辑</el-button>
                </el-col>
            </el-row>
            <el-alert v-if="message" :title="message" type="info" show-icon class="users-page__alert" />
        </el-card>

        <el-card shadow="never" class="users-page__card">
            <div class="users-page__header">
                <div class="users-page__section-title">用户列表</div>
                <el-button :loading="saving" @click="refresh">刷新</el-button>
            </div>
            <el-empty v-if="!store.users.length" description="暂无用户。用户首次通过身份源访问后会自动同步。" />
            <el-table v-else :data="store.users" border stripe>
                <el-table-column label="用户" min-width="220">
                    <template #default="{ row }">
                        <div class="users-page__identity">
                            <strong>{{ row.display_name }}</strong>
                            <span>{{ row.external_id }}</span>
                            <span>{{ row.email || '未设置邮箱' }}</span>
                        </div>
                    </template>
                </el-table-column>
                <el-table-column label="组" min-width="150">
                    <template #default="{ row }">
                        {{ row.groups.join(', ') || '-' }}
                    </template>
                </el-table-column>
                <el-table-column label="角色" min-width="180">
                    <template #default="{ row }">
                        {{ row.roles.join(', ') || '-' }}
                    </template>
                </el-table-column>
                <el-table-column label="状态" width="90">
                    <template #default="{ row }">
                        <span :class="{ 'users-page__status--disabled': !row.is_active }">
                            {{ row.is_active ? '启用' : '停用' }}
                        </span>
                    </template>
                </el-table-column>
                <el-table-column label="操作" width="170" fixed="right">
                    <template #default="{ row }">
                        <div class="users-page__row-actions">
                            <el-button size="small" @click="editUser(row.id)">编辑</el-button>
                            <el-button size="small" type="danger" plain @click="removeUser(row.id)">删除</el-button>
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
const externalId = ref('');
const displayName = ref('');
const email = ref('');
const groupsInput = ref('');
const selectedRoleIds = ref<number[]>([]);
const isActive = ref(true);
const saving = ref(false);
const message = ref('');
const roleOptions = computed(() => store.roles.map((role) => ({ label: role.name, value: role.id })));

/** 刷新用户和角色目录。 */
async function refresh(): Promise<void> {
    try {
        await store.syncUserDirectory();
    } catch (error) {
        message.value = error instanceof Error ? error.message : '用户目录加载失败';
    }
}

/** 清空用户编辑表单。 */
function resetForm(): void {
    editingId.value = null;
    externalId.value = '';
    displayName.value = '';
    email.value = '';
    groupsInput.value = '';
    selectedRoleIds.value = [];
    isActive.value = true;
}

/** 将列表用户加载到编辑表单。 */
function editUser(userId: number): void {
    const user = store.users.find((item) => item.id === userId);
    if (!user) return;
    editingId.value = user.id;
    externalId.value = user.external_id;
    displayName.value = user.display_name;
    email.value = user.email ?? '';
    groupsInput.value = user.groups.join(',');
    selectedRoleIds.value = store.roles.filter((role) => user.roles.includes(role.name)).map((role) => role.id);
    isActive.value = user.is_active;
}

/** 保存新增或编辑后的用户。 */
async function saveUser(): Promise<void> {
    const normalizedExternalId = externalId.value.trim();
    const normalizedDisplayName = displayName.value.trim();
    if ((!editingId.value && !normalizedExternalId) || !normalizedDisplayName) {
        message.value = '请填写身份 ID 和显示名称';
        return;
    }
    const groups = groupsInput.value.split(',').map((item) => item.trim()).filter(Boolean);
    saving.value = true;
    message.value = '';
    try {
        if (editingId.value) {
            await store.updateUser(editingId.value, {
                display_name: normalizedDisplayName,
                email: email.value.trim() || null,
                groups,
                is_active: isActive.value,
                role_ids: selectedRoleIds.value
            });
            message.value = '用户已更新';
        } else {
            await store.createUser({
                external_id: normalizedExternalId,
                display_name: normalizedDisplayName,
                email: email.value.trim() || null,
                groups,
                is_active: true,
                role_ids: selectedRoleIds.value
            });
            message.value = '用户已创建';
        }
        resetForm();
    } catch (error) {
        message.value = error instanceof Error ? error.message : '用户保存失败';
    } finally {
        saving.value = false;
    }
}

/** 删除用户并刷新目录。 */
async function removeUser(userId: number): Promise<void> {
    if (!window.confirm('确定删除这个用户吗？')) return;
    saving.value = true;
    try {
        await store.deleteUser(userId);
        message.value = '用户已删除';
    } catch (error) {
        message.value = error instanceof Error ? error.message : '用户删除失败';
    } finally {
        saving.value = false;
    }
}

onMounted(() => {
    void refresh();
});
</script>

<style scoped lang="less">
.users-page {
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
        align-items: flex-end;
    }

    &__alert {
        margin-top: 12px;
    }

    &__header {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 12px;
    }

    &__identity {
        display: grid;
        gap: 4px;
    }

    &__status--disabled {
        color: #dc2626;
    }

    &__row-actions {
        display: flex;
        gap: 8px;
    }
}
</style>
