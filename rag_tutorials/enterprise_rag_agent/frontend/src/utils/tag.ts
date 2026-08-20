import type { TagType } from '@/types/ui';

/**
 * 将文档风险等级映射为 Element Plus 标签展示类型。
 * @param riskLevel 风险等级（high / medium / low 或其他）。
 * @returns 标签展示类型。
 */
export function riskTagType(riskLevel: string): TagType {
    if (riskLevel === 'high') return 'danger';
    if (riskLevel === 'medium') return 'warning';
    if (riskLevel === 'low') return 'success';
    return 'info';
}
