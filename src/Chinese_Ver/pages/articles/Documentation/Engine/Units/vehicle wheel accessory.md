# 文档/引擎/单元/车辆车轮配件

> **注意：** 编写中——[Smarty](../../../../users/Smarty.md)（[讨论](../../../../user_talk/Smarty.md)）04:25, 23 June 2017 (CEST)

**vehicle_wheel_accessory** 单元类用于将车轮/轮辋配件及其数据“附加”到车辆和挂车配置上。此类型的单元通常为无名单元，并在拥有/使用它们的配置所在的同一上下文中声明。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| wear | float | 0.0 | 此属性用于跟踪配件的损坏和磨损情况。0 对应未磨损状态，1 对应完全磨损状态。 |
| **data_path** | string |  | 包含合适配件数据单元的 SII 文件的完整路径。 |
| offset | uint | 0 | 此配件所适用的车轴索引。“前”（转向）轴从车辆前部向尾部枚举，“后”轴从车辆尾部向前部枚举。前轴和后轴分别独立枚举。 |
| paint_color | float3 | 数据单元中的 **default_color** | 用于配件模型上 .paint 材质的颜色。 |

## 适用的配件数据类型

以下配件数据类型可用于 **vehicle_wheel_accessory**：

- [accessory_rim_data](accessory%20rim%20data.md)
- [accessory_wheel_data](accessory%20wheel%20data.md)

## 相关单元

- [traffic_trailer](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_trailer&action=edit&redlink=1)
- [traffic_vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_vehicle&action=edit&redlink=1)
- [trailer](trailer.md)
- [vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle&action=edit&redlink=1)
- [vehicle_accessory](vehicle%20accessory.md)
- [vehicle_addon_accessory](vehicle%20addon%20accessory.md)
- [vehicle_paint_job_accessory](vehicle%20paint%20job%20accessory.md)
- [vehicle_sound_accessory](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle_sound_accessory&action=edit&redlink=1)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/vehicle_wheel_accessory | revision: 3322 | captured: 2026-10-21 23:56:14 -->
