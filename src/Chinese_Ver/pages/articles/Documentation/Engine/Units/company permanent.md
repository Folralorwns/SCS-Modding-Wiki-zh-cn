# Documentation/Engine/Units/company permanent

**company_permanent** 单元类用于定义公司货场的非实例专属数据。此类型的单元通常定义在 **/def/company/<company_name>.sii** 中。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| name | string |  | 用于 UI 显示的公司名称。 |
| sort_name | string |  | 公司名称的简化版本，用于在列表中排序。 |
| trailer_look | token |  | 生成任务时，如果挂车配置带有涂装配件，将尝试把此 token 与 **/def/vehicle/trailer/<trailer_name>/company_paint_job/<trailer_look>.sii** 中的涂装配件匹配，以显示公司专属外观。此文件名（不含 **.sii** 扩展名）必须小于或等于 12 个字符，否则该名称无法映射到单元 token 中。 |
| out_cargo | array<link_ptr> |  | 请勿在定义中使用此属性。它会根据 **/def/company/<company_name>/out/** 中的任何 cargo_def 单元即时生成。 |
| in_cargo | array<link_ptr> |  | 请勿在定义中使用此属性。它会根据 **/def/company/<company_name>/in/** 中的任何 cargo_def 单元即时生成。 |
| city_names | array&lt;token&gt; |  | 请勿在定义中使用此属性。它会根据 **/def/company/<company_name>/editor/** 中的任何 company_def 单元即时生成。 |
| prefab_names | array&lt;token&gt; |  | 请勿在定义中使用此属性。它会根据 **/def/company/<company_name>/editor/** 中的任何 company_def 单元即时生成。 |

## 相关单元

- [cargo_def](cargo%20def.md)
- [company_def](company%20def.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/company_permanent | revision: 5755 | captured: 2026-10-21 23:56:14 -->
