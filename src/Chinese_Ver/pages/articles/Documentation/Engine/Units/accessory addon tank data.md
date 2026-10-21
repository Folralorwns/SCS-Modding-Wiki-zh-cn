# 文档/引擎/单元/配件附加罐体数据

> **注意：** 本文仍在编写中，尚未经过 SCS 员工审阅。部分信息可能不完整或不准确。

**accessory_addon_tank_data** 单元类用于添加基于配件的罐体数据容器。对于玩家卡车，此类型的单元通常定义在 **/def/vehicle/truck/<brand.model>/accessory/tank/*.sii** 中，有效的单元名称以 `.tank` 结尾。*此单元类型在 1.41 中添加。*

## 属性

许多通用属性继承自 [**accessory_addon_data**](accessory%20addon%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| fuel_tank_size | float | 0.0 | 燃油箱容量，单位为升。若为正值，则覆盖[底盘](accessory%20chassis%20data.md)中关于燃油箱容量的信息。 |
| adblue_tank_size | float | 0.0 | AdBlue/DEF 罐容量，单位为升。若为正值，则覆盖[底盘](accessory%20chassis%20data.md)中关于 AdBlue 罐容量的信息。 |

> **注意：** 在任何给定的卡车上，此配件类型最多应出现一次。虽然技术上可以在不同的定位器/配件类型名称下拥有多个罐体类型配件，但只有最先找到的一个会用于覆盖数值。多次出现会导致未定义行为。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_addon_tank_data | revision: 4968 | captured: 2026-10-21 23:56:14 -->
