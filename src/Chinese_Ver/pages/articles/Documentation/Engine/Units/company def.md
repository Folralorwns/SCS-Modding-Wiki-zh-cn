# Documentation/Engine/Units/company def

**company_def** 单元类用于将预制件分配给 [company_permanent](company%20permanent.md) 单元。此类型的单元通常定义在 **/def/company/<company_name>/editor/<city_name>.sii** 中。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| **city** | token |  | 预制件所在城市的 token 名称。以 *city.san_francisc* 为例，它应写作 `city: san_francisc` |
| **prefab** | token |  | 要链接的预制件的 token 名称。以 *prefab.d_port_sf* 为例，它应写作 `prefab: d_port_sf` **注意：** 此实现要求每个货场预制件在每个城市中只能出现一次。 |

## 相关单元

- [company_permanent](company%20permanent.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/company_def | revision: 3308 | captured: 2026-10-21 23:56:14 -->
