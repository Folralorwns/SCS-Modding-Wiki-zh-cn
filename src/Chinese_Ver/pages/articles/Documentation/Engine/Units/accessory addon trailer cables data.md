# 文档/引擎/单元/配件附加挂车线缆数据

> **注意：** 本文仍在编写中，尚未经过 SCS 员工审阅。部分信息可能不完整或不准确。

**accessory_addon_trailer_cables_data** 单元类用于在车辆与其挂车之间添加动态挂车线缆。对于玩家卡车，此类型的单元通常定义在 **/def/vehicle/truck/<brand.model>/accessory/trlr_cables/*.sii** 中，有效的单元名称以 `.trlr_cables` 结尾。对于玩家挂车，此类型的单元通常定义在 **/def/vehicle/trailer/<trailer_name>/accessory/trlr_cables/*.sii** 中，有效的单元名称以 `.trlr_cables` 结尾。*此单元类型在 1.31 中添加。*

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| exterior_model | string |  | 要在外部视图中显示的模型对应的模型描述符（.pmd）路径（如果适用）。 |
| exterior_model_uk | string |  | 右舵车辆要在外部视图中显示的模型对应的模型描述符（.pmd）路径（如果适用）。如果未设置，则默认为 **exterior_model**。 |
| coll | string |  | 配件的碰撞描述符（.pmc）路径（如果适用）。 |
| look | token | default | 用于此配件所有描述符的 look 名称。**注意：** 一个配件的所有模型必须具有相同的 look 集合。 |
| variant | token | default | 用于此配件所有描述符的 variant 名称。**注意：** 一个配件的所有模型必须具有相同的 variant 集合。 |
| cables | array<owner_ptr> |  | 每个成员指向一个 [trailer_cable_data](trailer%20cable%20data.md) 单元 |

## 模型

有效的挂车线缆配件模型必须包含以下内容：

- 一些可见几何体（模型不能只包含定位器）
- 为 *cables* 数组中定义的每个成员提供连接定位器，卡车插头模型将放置在这些定位器处。定位器名称由每个 **trailer_cable_data** 单元的 *locator_prefix* 属性定义。

它还可以使用以下内容：

- 为每根已定义的线缆提供静置定位器，在未连接挂车时，挂车插头模型将放置在这些定位器处（否则未连接挂车时线缆将不会被绘制/模拟）。定位器名称由每个 **trailer_cable_data** 单元的 *rest_locator_prefix* 属性定义。
- 特殊部件名称仅在特定状态下显示：
  - `cables_off` 仅在未连接挂车时显示
  - `cables_on` 仅在连接挂车时显示

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_addon_trailer_cables_data | revision: 5348 | captured: 2026-10-21 23:56:14 -->
