# 文档/引擎/单元/配件附加内部数据

> **注意：** 本文仍在编写中，尚未经过 SCS 员工审阅。部分信息可能不完整或不准确。

**accessory_addon_int_data** 单元类用于为车辆添加可见组件、且其运动模拟依赖实际物理的车辆配件。它用于[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)的定制，最常见于一些悬挂部件或摇头娃娃。

## 属性

许多通用属性继承自 [**accessory_addon_data**](accessory%20addon%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| data | array<owner_ptr> | &lt;empty&gt; | 车辆物理玩具数据的数组。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_addon_int_data | revision: 5115 | captured: 2026-10-21 23:56:14 -->
