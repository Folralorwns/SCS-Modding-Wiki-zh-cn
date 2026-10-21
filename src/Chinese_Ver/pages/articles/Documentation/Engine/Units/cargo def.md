# 文档/引擎/单元/货物定义

**cargo_def** 单元类用于指定某货物由某公司生产或接收。此类型的单元通常定义在 **/def/company/<company_name>/in/<cargo_name>.sii** 中，用于标记公司接收的货物；并定义在 **/def/company/<company_name>/out/<cargo_name>.sii** 中，用于标记公司生产的货物。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| **cargo** | string |  | 货物的单元名称，对应一个 [cargo_data](cargo%20data.md) 单元。例如：`cargo: "cargo.stolen_ducks"` |

## 相关单元

- [cargo_data](cargo%20data.md)
- [company_permanent](company%20permanent.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/cargo_def | revision: 3300 | captured: 2026-10-21 23:56:14 -->
