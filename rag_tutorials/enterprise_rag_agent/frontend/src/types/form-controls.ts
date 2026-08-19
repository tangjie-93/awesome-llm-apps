export interface MultiSelectOption {
    label: string;
    value: string | number;
}

export interface MultiSelectDropdownProps {
    modelValue: Array<string | number>;
    options: MultiSelectOption[];
    placeholder?: string;
    disabled?: boolean;
}

export interface MultiSelectDropdownEmits {
    'update:modelValue': [value: Array<string | number>];
}
