# 文档/引擎/单元/配件附加内部 UI 数据

> **注意：** 本文仍在编写中，尚未经过 SCS 员工审阅。部分信息可能不完整或不准确。

**accessory_addon_int_ui_data** 单元类用于为车辆添加可见组件、且带有动态 UI 屏幕组件的车辆配件。它用于[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)的定制，最常见于额外的 GPS 导航屏幕或带时钟的手机等。

此配件的 UI 脚本可以访问与仪表盘或 gps 内饰脚本相同的 ID 元素，更多信息：[文档/引擎/卡车内饰动画与 ID#仪表盘 ID](../Truck%20Interior%20Animations%20and%20IDs.md#Dashboards_IDs)。

## 属性

许多通用属性继承自 [**accessory_addon_data**](accessory%20addon%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| ui_path | string | &lt;empty&gt; | 此配件的 UI 脚本路径，该脚本应绘制到可绘制对象中。 |
| ui_drawable_texture_path | string | &lt;empty&gt; | UI 将绘制到的纹理 TOBJ 路径，该纹理随后应在模型中使用并用作显示屏。 |
| ui_drawable_size | int2 | (0, 0) | 可绘制纹理的尺寸，必须是介于 [4, 4096] 之间的 2 的幂。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_addon_int_ui_data | revision: 5116 | captured: 2026-10-21 23:56:14 -->
