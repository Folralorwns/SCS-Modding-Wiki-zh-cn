# 文档/引擎/单元/挂车

> **注意：** 编写中——[Smarty](../../../../users/Smarty.md)（[讨论](../../../../user_talk/Smarty.md)）19:32, 21 June 2017 (CEST)

**trailer** 单元类用于定义可玩的挂车。此类型的单元通常定义在 **/def/vehicle/trailer/<trailer_name>.sii** 中，与其配件单元以及任何“从属”挂车单元一同定义。它们通过 **/def/vehicle/trailer_storage.<mod_name>.sii** 被[包含](../Units.md#Includes)，因此**不得**使用 SiiNunit 魔法标记。

此单元类还用于在内存和存档中存储挂车（例如玩家当前启用的挂车、任务市场等）。因此，有许多属性在手动定义挂车时不会用到。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| accessories | array<owner_ptr> |  | 每个成员指向属于该挂车的一个配件单元。有效的单元类为 vehicle_accessory、vehicle_addon_accessory、vehicle_wheel_accessory 和 vehicle_paint_job_accessory。 |
| odometer | uint |  | 记录车辆里程表的整数部分。不应在定义中设置。 |
| odometer_float_part | float |  | 记录车辆里程表的小数部分。不应在定义中设置。 |
| trip_fuel | float |  | 不应在定义中设置。 |
| trip_distance | float |  | 不应在定义中设置。 |
| license_plate | string |  | 此属性存储车牌号码以及挂车初始化时车牌模板所应用的任何格式。不应在定义中设置。 |
| cargo_mass | float |  | 从为该挂车所生成任务关联的 [trailer_def](trailer%20def.md) 单元的货物质量和质量比例继承而来。不应在定义中设置。 |
| virtual_rear_wheels_offset | float |  | 此属性用于偏移挂车车轮的物理（而非视觉）位置，以调整其转弯半径。通常不应用于可玩的挂车。 |
| slave_trailer | owner_ptr |  | 指向构成多铰接配置中下一辆车的 **trailer** 单元。从属挂车的 *hook* 定位器将挂接到主挂车的 *s_hook* 定位器。 |

## 必需配件

有效的挂车单元必须具有一个底盘配件（通过 vehicle_accessory 的 accessory_chassis_data），并且每个车轴各有一个车轮配件（通过 vehicle_wheel_accessory 的 accessory_wheel_data）。

## 相关单元

- [trailer_def](trailer%20def.md)
- [vehicle_accessory](vehicle%20accessory.md)
- [vehicle_addon_accessory](vehicle%20addon%20accessory.md)
- [vehicle_paint_job_accessory](vehicle%20paint%20job%20accessory.md)
- [vehicle_wheel_accessory](vehicle%20wheel%20accessory.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/trailer | revision: 3296 | captured: 2026-10-21 23:56:14 -->
