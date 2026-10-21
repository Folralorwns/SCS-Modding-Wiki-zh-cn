# 文档/引擎/单元/货物数据

**cargo_data** 单元类用于定义货物的物流、语义和经济属性。此类型的单元通常定义在 **/def/cargo/<cargo_name>.sii** 中，并通过 [包含](../Units.md#Includes) 引入到 **/def/cargo.<mod_name>.sii** 中，因此**不得**使用 SiiNunit 魔术标记。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| name | string |  | 用于 UI 显示的货物名称。支持 @@localization@@。 |
| body_types | array&lt;token&gt; |  | 可装载该货物的车体类型列表。 |
| volume | float |  | 一单位货物的体积，单位为 m<sup>3</sup>。 |
| mass | float |  | 一单位货物的质量，单位为 kg。 |
| unit_reward_per_km | float |  | 将一单位货物运输一公里所获得的奖励，以基础货币计。 |
| unit_load_time | float |  | 装载一单位货物所需的时间，单位为秒。 |
| fragility | float |  | 定义货物对损坏的敏感程度。 |
| valuable | bool | false | 为 true 时，玩家需要具备“贵重货物”技能才能承接该货物，并获得相应的经验值和收入技能加成。 |
| overweight | bool | false |  |
| adr_class | uint |  | 为货物指定 ADR/危险品分类。玩家需要具备相应技能才能承接该货物。 |
| minimum_distance | float | 0 | 使用此货物生成任务的最小距离，单位为公里（km）。 |
| maximum_distance | float | ∞ | 使用此货物生成任务的最大距离，单位为公里（km）。 |
| prob_coef | float | 1.0 | 生成使用此货物的任务的相对概率。 |
| group | array&lt;token&gt; |  | 每个成员将货物标记为属于某个预定义的货物分组，用于货物排序。有效值为：machinery adr containers refrigerated liquid fragile construction bulk oversize。通常，*fragile* 类别保留给 **fragility** 为 0.7 或更高的货物。 |

## 相关单元

- [cargo_def](cargo%20def.md)（用于将货物标记为公司生产或接收的货物）
- [trailer_def](trailer%20def.md)（用于为货物分配挂车配置并设置相关质量属性）

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/cargo_data | revision: 4061 | captured: 2026-10-21 23:56:14 -->
