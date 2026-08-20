/** Element Plus 标签可用的展示类型。 */
export type TagType = 'primary' | 'success' | 'warning' | 'danger' | 'info';

export interface PageSectionProps {
    title?: string;
    subtitle?: string;
    /** 开启后区块铺满页面剩余高度，内容区自适应。 */
    fill?: boolean;
}

export interface EmptyStateProps {
    description: string;
    actionLabel?: string;
    /** 开启后占位块铺满父容器高度并垂直居中。 */
    fill?: boolean;
}

export interface MetricCardProps {
    label: string;
    value: string | number;
    hint?: string;
    type?: 'default' | 'success' | 'warning' | 'danger';
}

export interface DataTableProps {
    data: unknown[];
    /** 表格加载中状态。 */
    loading?: boolean;
    /** 是否显示斑马纹（默认开启，表体无边框时用于区分行）。 */
    stripe?: boolean;
    /** 开启后表格铺满父容器高度，表体独立滚动、表头固定（默认开启）。 */
    fill?: boolean;
    size?: 'large' | 'default' | 'small';
    /** 无数据时的默认占位文案。 */
    emptyDescription?: string;
}

export interface TagListProps {
    items: string[];
    /** 统一的标签类型。 */
    type?: TagType;
    /** 按条目动态计算标签类型，优先于 type。 */
    typeFor?: (item: string) => TagType;
    /** 列表为空时的占位文案。 */
    emptyText?: string;
}

export interface FormFieldProps {
    label: string;
}

export interface EmptyStateEmits {
    action: [];
}
