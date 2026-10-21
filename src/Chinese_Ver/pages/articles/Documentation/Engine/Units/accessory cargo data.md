# 文档/引擎/单元/配件货物数据

**accessory_cargo_data** 单元类为[挂车](../Game%20data.md#Trailer_definitions)配置可见的货物模型。此类型的单元位于 **/def/vehicle/cargo/<cargo_name>/** 中（自 1.54 起）。

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| detail_model | string |  | 详细网格模型描述符（.pmd）的路径。此模型仅用于玩家使用的车辆。此外，它还用于车辆预览和浏览器窗口。 |
| model | string |  | 模型描述符（.pmd）的路径。如果只使用单个 LOD，则应将其设置为 **model**，并且不应定义其他属性（detail_model、lods）。 |
| lods | array&lt;string&gt; |  | 简化细节层级模型描述符（.pmd）的路径，按观察距离递增（模型复杂度递减）的顺序排列。 |
| collision | string |  | 碰撞描述符（.pmc）的路径。 |
| variant | token |  | 用于此配件所有描述符的 variant 名称。**注意：** 为此 **accessory_cargo_data** 定义的所有模型都必须使用此 variant 名称。 |
| look | token |  | 用于此配件所有描述符的 look 名称。**注意：** 为此 **accessory_cargo_data** 定义的所有模型都必须使用此 look 名称。 |
| dynamic_cargo_data | owner_ptr |  | 指向 [dynamic_cargo_data](dynamic%20cargo%20data.md) 类型的单元，与动态货物装载/卸载相关的数据存储在其中。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_cargo_data | revision: 5733 | captured: 2026-10-21 23:56:14 -->
