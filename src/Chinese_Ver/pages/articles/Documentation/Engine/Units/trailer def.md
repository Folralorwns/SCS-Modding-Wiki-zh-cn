# 文档/引擎/单元/挂车 def

**trailer_def** 单元类充当 [cargo_data](cargo%20data.md) 与 [trailer](trailer.md) 单元之间的中介。此类型的单元通常定义在 **/def/cargo/<cargo_name>/<trailer_name>.sii** 中，对应 **def/cargo/<cargo_name>.sii**。它们定义为该货物启用哪个挂车配置、该挂车配置下货物的质量、该质量如何分布/放置到挂车及其从属单元上，以及该配置在何处被允许。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| trailer | string |  | 为该货物启用的 **trailer** 单元的单元名称。此属性可以安全地引用不存在的单元。（仅用于在 /def/cargo/<cargo_name>/ 中定义时的旧版用法） |
| gross_trailer_weight_limit | float |  | 挂车及其货物的最大技术或逻辑总重量（需考虑桥梁公式及其他类似规则）。 |
| chassis_mass | float |  | 挂车底盘的质量，单位为 kg。 |
| body_mass | float |  | 挂车车身的质量，单位为 kg。 |
| length | float | 0 | 挂车组合的长度，单位为米。生成任务时，会将此值与起点和终点车库 [预制件](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/prefab_data&action=edit&redlink=1) 的 **allowed_trailer_length** 进行比较，以确定该 trailer_def 是否适合该任务。 |
| axles | uint |  | 挂车组合中的车轴数量，会与 country_data→mass_limit_per_axle_count 进行比较，以确定允许的总重量。 |
| volume | float |  | 挂车车身的内部容积，单位为 m<sup>3</sup>。 |
| body_type | token |  | 设置挂车配置的车身类型，决定允许运输哪些货物。 |
| chain_type | token |  | 设置挂车配置的挂车链类型。 |
| country_validity | array&lt;token&gt; |  | 每个成员都是该 trailer_def 适合用于生成任务的国家（或在 ATS 中为州）。任务的起点和终点都必须位于 *country* 数组中，该 trailer_def 才适合该任务。如果未设置，则该 trailer_def 适合所有国家。例如，以下配置将仅限内华达州和亚利桑那州：country[]: arizona country[]: nevada |
| **mass_ratio** | array&lt;float&gt; |  | 每个成员定义挂车配置中各挂车分别承担多少货物质量和作用力，从 *master* 挂车开始，依次遍历 *slave* 挂车。这些值之和必须为 1。 |

## World of Trucks 兼容性

如果满足以下条件，World of Trucks 任务将使用模组挂车：

- **mass** 等于或大于任务的货物质量。
- **length** 与起点和终点的预制件兼容。
- 该配置对于起点和终点的 **country** 有效。
- 挂车数量等于任务的挂车数量（即，多铰接挂车配置不会被选用于单挂车任务）。

## 相关单元

- [cargo_data](cargo%20data.md)
- [trailer](trailer.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/trailer_def | revision: 4209 | captured: 2026-10-21 23:56:14 -->
