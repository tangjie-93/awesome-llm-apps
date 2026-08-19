<template>
    <section class="roles-page">
        <PageHeader />

        <section class="roles-page__section">
            <div class="roles-page__form">
                <label class="roles-page__field">
                    <span>角色名称</span>
                    <input v-model.trim="name" :disabled="editingSystemRole" />
                </label>
                <label class="roles-page__field">
                    <span>角色说明</span>
                    <input v-model.trim="description" />
                </label>
                <label class="roles-page__field">
                    <span>权限项</span>
                    <MultiSelectDropdown
                        v-model="selectedPermissions"
                        :options="permissionOptions"
                        placeholder="选择权限项"
                    />
                </label>
                <div class="roles-page__form-actions">
                    <button class="roles-page__button roles-page__button--primary" :disabled="saving" @click="saveRole">
                        {{ editingId ? '保存修改' : '创建角色' }}
                    </button>
                    <button v-if="editingId" class="roles-page__button" :disabled="saving" @click="resetForm">取消编辑</button>
                    <button class="roles-page__button" :disabled="saving" @click="refresh">刷新</button>
                </div>
            </div>
            <p v-if="message" class="roles-page__message">{{ message }}</p>
        </section>

        <section class="roles-page__section">
            <div class="roles-page__section-header">
                <span class="roles-page__section-label">角色列表</span>
            </div>
            <div v-if="!store.roles.length" class="roles-page__empty">暂无角色。</div>
            <div v-else class="roles-page__table-header">
                <span>角色</span>
                <span>说明</span>
                <span>权限项</span>
                <span>类型</span>
                <span>操作</span>
            </div>
            <div v-for="role in store.roles" :key="role.id" class="roles-page__row">
                <div>
                    <strong>{{ role.name }}</strong>
                    <span>{{ role.description || '暂无说明' }}</span>
                </div>
                <div class="roles-page__permissions">{{ role.permissions.join(', ') || '暂无权限项' }}</div>
                <div class="roles-page__type">
                    <span v-if="role.is_system" class="roles-page__system">系统角色</span>
                    <span v-else>自定义</span>
                </div>
                <div class="roles-page__row-actions">
                    <button class="roles-page__button" @click="editRole(role.id)">编辑</button>
                    <button class="roles-page__button roles-page__button--danger" :disabled="role.is_system" @click="removeRole(role.id)">
                        删除
                    </button>
                </div>
            </div>
        </section>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import MultiSelectDropdown from '@/components/form/MultiSelectDropdown.vue';
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
    &__section {
        margin-bottom: 14px;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px;
        background: #fff;
    }

    &__section-header,
    &__row-actions {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    &__section-header {
        justify-content: space-between;
        margin-bottom: 14px;
    }

    &__section-label {
        color: #475569;
        font-size: 12px;
        font-weight: 700;
    }

    &__section-title {
        margin: 0;
        font-size: 16px;
    }

    &__form {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 10px;
        align-items: end;

        label {
            display: grid;
            gap: 6px;
        }

        span {
            color: #64748b;
            font-size: 13px;
        }

        input {
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            padding: 9px 10px;
        }
    }

    &__field {
        min-width: 0;
    }

    &__form-actions {
        display: flex;
        justify-self: stretch;
        align-items: center;
        gap: 8px;
        white-space: nowrap;
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
        grid-template-columns: minmax(180px, 1fr) minmax(180px, 1fr) minmax(240px, 1.4fr) minmax(90px, 0.6fr) auto;
        gap: 12px;
        align-items: center;
        border-top: 1px solid #e2e8f0;
        padding: 10px 0;

        div:first-child {
            display: grid;
            gap: 4px;
        }

        span {
            color: #64748b;
            font-size: 13px;
        }
    }

    &__table-header {
        display: grid;
        grid-template-columns: minmax(180px, 1fr) minmax(180px, 1fr) minmax(240px, 1.4fr) minmax(90px, 0.6fr) auto;
        gap: 12px;
        border-top: 1px solid #e2e8f0;
        padding: 10px 0 8px;
        color: #64748b;
        font-size: 12px;
        font-weight: 700;
    }

    &__permissions {
        color: #475569;
        font-size: 13px;
    }

    &__type {
        color: #475569;
        font-size: 13px;
    }

    &__system {
        color: #1d4ed8 !important;
    }

    @media (max-width: 820px) {
        &__form,
        &__row {
            grid-template-columns: 1fr;
        }

        &__form-actions {
            justify-self: start;
            flex-wrap: wrap;
        }

        &__row-actions {
            justify-content: flex-start;
            flex-wrap: wrap;
        }
    }
}
</style>
