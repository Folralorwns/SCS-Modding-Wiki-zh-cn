# Documentation/Engine/Units/glass pane data

**glass_pane_data** 单元类用于定义玻璃“窗格”，这些窗格用于在驾驶室内视角中模拟雨滴的积聚、移动和清除。每个窗格使用一个单独的单元。它们被定义为无名单元，通过 *glass_panes* 属性归属于 [accessory_interior_data](accessory%20interior%20data.md)，通常通过 **/def/vehicle/truck/<brand.model>/interior/glass.sui** 引入。

> **注意：** 由于历史原因，ETS2 中的部分卡车使用 **glass.dat** 而非 **glass.sui**。但是在你创建自己的定义时，应使用 SUI 扩展名。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| locator | string |  | 内饰模型中与此玻璃窗格对应的定位器名称。定位器的 Y 轴从玻璃表面“向外”指向，其 XZ 平面构成该表面。 |
| size | float2 |  | 玻璃窗格的尺寸（宽度、高度），单位为米。 |
| drop_size_minimum | float | 0.006 | 雨滴的最小尺寸，单位为米。 |
| drop_size_maximum | float | 0.024 | 雨滴的最大尺寸，单位为米。 |
| edge_angle | float | 0 | 定位器朝向与平面左右两侧法线朝向之间的偏航角（单位为度）。用于模拟虚假曲面。 |
| wipers | array<owner_ptr> |  | 每个成员指向一个 [wiper_data](wiper%20data.md) 单元，用于定义会影响此玻璃窗格的雨刷。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/glass_pane_data | revision: 3246 | captured: 2026-10-21 23:56:14 -->
