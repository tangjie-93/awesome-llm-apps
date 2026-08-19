export type NavigationGroupKey = 'workspace' | 'knowledgeAssets' | 'governance' | 'system';

export interface NavigationGroup {
    key: NavigationGroupKey;
    label: string;
}

export interface NavigationItem {
    path: string;
    label: string;
}

export interface NavigationSection extends NavigationGroup {
    items: NavigationItem[];
}
