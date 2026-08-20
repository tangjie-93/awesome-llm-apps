export interface PageSectionProps {
    title?: string;
    subtitle?: string;
}

export interface EmptyStateProps {
    description: string;
    actionLabel?: string;
}

export interface MetricCardProps {
    label: string;
    value: string | number;
    hint?: string;
    type?: 'default' | 'success' | 'warning' | 'danger';
}

export interface EmptyStateEmits {
    action: [];
}
