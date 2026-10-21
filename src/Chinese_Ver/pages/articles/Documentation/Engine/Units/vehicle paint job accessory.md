# 文档/引擎/单元/车辆涂装配件

> **注意：** 编写中——[Smarty](../../../../users/Smarty.md)（[讨论](../../../../user_talk/Smarty.md)）04:17, 23 June 2017 (CEST)

**vehicle_paint_job_accessory** 单元类用于将涂装配件及其[数据](accessory%20paint%20job%20data.md)“附加”到车辆和挂车配置上。此类型的单元通常为无名单元，并在拥有/使用它们的配置所在的同一上下文中声明。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| wear | float | 0.0 | 此属性用于跟踪配件的损坏和磨损情况。0 对应未磨损状态，1 对应完全磨损状态。 |
| **data_path** | string |  | 包含合适配件数据单元的 SII 文件的完整路径。 |
| mask_r_color | float3 | 来自配件数据 | 应用于涂装红色通道的颜色（仅限 colormask）。 |
| mask_g_color | float3 | 来自配件数据 | 应用于涂装绿色通道的颜色（仅限 colormask）。 |
| mask_b_color | float3 | 来自配件数据 | 应用于涂装蓝色通道的颜色（仅限 colormask）。 |
| flake_color | float3 | 来自配件数据 | 用于涂装闪片效果的颜色（仅限 flipflake）。 |
| flip_color | float3 | 来自配件数据 | 用于涂装翻转效果的颜色（仅限 flipflake）。 |
| base_color | float3 | 来自配件数据 | 涂装的基色（所有涂装模式）。 |

## 相关单元

- [traffic_trailer](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_trailer&action=edit&redlink=1)
- [traffic_vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_vehicle&action=edit&redlink=1)
- [trailer](trailer.md)
- [vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle&action=edit&redlink=1)
- [vehicle_accessory](vehicle%20accessory.md)
- [vehicle_addon_accessory](vehicle%20addon%20accessory.md)
- [vehicle_sound_accessory](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle_sound_accessory&action=edit&redlink=1)
- [vehicle_wheel_accessory](vehicle%20wheel%20accessory.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/vehicle_paint_job_accessory | revision: 3323 | captured: 2026-10-21 23:56:14 -->
