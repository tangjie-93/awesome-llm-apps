<template>
    <section class="users-page">
        <header class="users-page__header">
            <h1 class="users-page__title">用户管理</h1>
            <p class="users-page__subtitle">管理外部身份映射、权限组和本地角色。</p>
        </header>

        <section class="users-page__section">
            <h2 class="users-page__section-title">{{ editingId ? '编辑用户' : '新增用户' }}</h2>
            <div class="users-page__form">
                <label>
                    <span>外部身份 ID</span>
                    <input v-model.trim="externalId" :disabled="Boolean(editingId)" />
                </label>
                <label>
                    <span>显示名称</span>
                    <input v-model.trim="displayName" />
                </label>
                <label>
                    <span>邮箱</span>
                    <input v-model.trim="email" type="email" />
                </label>
                <label>
                    <span>权限组</span>
                    <input v-model="groupsInput" placeholder="public,security" />
                </label>
                <label>
                    <span>角色</span>
                    <select v-model="selectedRoleIds" multiple>
                        <option v-for="role in store.roles" :key="role.id" :value="role.id">{{ role.name }}</option>
                    </select>
                </label>
                <label v-if="editingId" class="users-page__checkbox">
                    <input v-model="isActive" type="checkbox" />
                    <span>启用用户</span>
                </label>
            </div>
            <div class="users-page__actions">
                <button class="users-page__button users-page__button--primary" :disabled="saving" @click="saveUser">
                    {{ editingId ? '保存修改' : '创建用户' }}
                </button>
                <button v-if="editingId" class="users-page__button" :disabled="saving" @click="resetForm">取消编辑</button>
            </div>
            <p v-if="message" class="users-page__message">{{ message }}</p>
        </section>

        <section class="users-page__section">
            <div class="users-page__section-header">
                <h2 class="users-page__section-title">用户列表</h2>
                <button class="users-page__button" :disabled="saving" @click="refresh">刷新</button>
            </div>
            <div v-if="!store.users.length" class="users-page__empty">暂无用户。用户首次通过身份源访问后会自动同步。</div>
            <div v-for="user in store.users" :key="user.id" class="users-page__row">
                <div class="users-page__identity">
                    <strong>{{ user.display_name }}</strong>
                    <span>{{ user.external_id }}</span>
                    <span>{{ user.email || '未设置邮箱' }}</span>
                </div>
                <div class="users-page__meta">
                    <span>组：{{ user.groups.join(', ') || '-' }}</span>
                    <span>角色：{{ user.roles.join(', ') || '-' }}</span>
                    <span :class="{ 'users-page__status--disabled': !user.is_active }">
                        {{ user.is_active ? '启用' : '停用' }}
                    </span>
                </div>
                <div class="users-page__row-actions">
                    <button class="users-page__button" @click="editUser(user.id)">编辑</button>
                    <button class="users-page__button users-page__button--danger" @click="removeUser(user.id)">删除</button>
                </div>
            </div>
        </section>
    </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
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
    max-width: 1280px;
    margin: 0 auto;
    padding: 24px;

    &__header {
        margin-bottom: 24px;
    }

    &__title {
        margin: 0;
        font-size: 24px;
    }

    &__subtitle {
        margin: 6px 0 0;
        color: #64748b;
        font-size: 13px;
    }

    &__section {
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 16px;
        background: #fff;
    }

    &__section-header,
    &__actions,
    &__row-actions {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    &__section-header {
        justify-content: space-between;
        margin-bottom: 14px;
    }

    &__section-title {
        margin: 0;
        font-size: 16px;
    }

    &__form {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 14px;

        label {
            display: grid;
            gap: 6px;
        }

        span {
            color: #64748b;
            font-size: 13px;
        }

        input,
        select {
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            padding: 9px 10px;
            background: #fff;
        }

        select {
            min-height: 92px;
        }
    }

    &__checkbox {
        display: flex !important;
        align-items: center;
        gap: 8px;
    }

    &__button {
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 8px 11px;
        background: #fff;
        cursor: pointer;

        &:disabled {
            cursor: not-allowed;
            opacity: 0.55;
        }

        &--primary {
            border-color: #1d4ed8;
            background: #1d4ed8;
            color: #fff;
        }

        &--danger {
            border-color: #fecaca;
            color: #b91c1c;
        }
    }

    &__message {
        margin: 12px 0 0;
        color: #1d4ed8;
    }

    &__empty {
        color: #64748b;
    }

    &__row {
        display: grid;
        grid-template-columns: minmax(220px, 1fr) minmax(300px, 1fr) auto;
        gap: 16px;
        align-items: center;
        border-top: 1px solid #e2e8f0;
        padding: 12px 0;
    }

    &__identity,
    &__meta {
        display: grid;
        gap: 4px;
    }

    &__identity span,
    &__meta span {
        color: #64748b;
        font-size: 13px;
    }

    &__status--disabled {
        color: #b91c1c !important;
    }

    @media (max-width: 820px) {
        &__form,
        &__row {
            grid-template-columns: 1fr;
        }

        &__row-actions {
            justify-content: flex-start;
        }
    }
}
</style>
