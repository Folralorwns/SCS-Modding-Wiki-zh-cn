# 文档/引擎/单元/配件挂车车身数据

**accessory_trailer_body_data** 单元类用于定义自购挂车车身配件，包括车身尺寸、容积、质量和视觉数据。此类型的单元通常定义在 **/def/vehicle/trailer_owned/<brand.model>/body/*.sii** 中。

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| size | float3 |  | 车身内部尺寸（货物区域），单位为米。（宽度、高度、长度） |
| total_size | float3 |  | 挂车的整体外部尺寸，单位为米。（宽度、高度、长度） |
| volume | float |  | 货物容积，单位为立方米（m<sup>3</sup>）。 |
| body_type | token |  | 挂车车身类型（例如 flatbed、dryvan 等）。 |
| mass | float |  | 车身配件的质量，单位为千克（空载，不含货物）。 |
| detail_model | string |  | 详细网格模型描述符（.pmd）的路径。此模型仅用于玩家使用的车辆。此外，它还用于车辆预览和浏览器窗口。 |
| model | string |  | 模型描述符（.pmd）的路径。如果只使用单个 LOD，则应将其设置为 **model**，并且不应定义其他属性（detail_model、lods）。目前，自购挂车通常只使用此项。 |
| lods | array&lt;string&gt; |  | 简化细节层级模型描述符（.pmd）的路径，按观察距离递增（模型复杂度递减）的顺序排列。 |
| collision | string |  | 碰撞描述符（.pmc）的路径。 |
| variant | token |  | 用于 **detail_model**、**model** 和 **lods** 的 variant。 |
| look | token |  | 用于 **detail_model**、**model** 和 **lods** 的 look。 |
| empty_cargo_model | string |  | 挂车为空时挂接的 [accessory_cargo_data](accessory%20cargo%20data.md) 定义的路径。*在 1.39 中添加* |
| animation | array<owner_ptr> |  | 每个成员指向一个 [vehicle_animation_data](vehicle%20animation%20data.md) 单元的单元名称。*在 1.61 中添加* |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_trailer_body_data | revision: 5804 | captured: 2026-10-21 23:56:14 -->
