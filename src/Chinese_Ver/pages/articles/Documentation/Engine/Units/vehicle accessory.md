# 文档/引擎/单元/车辆配件

**vehicle_accessory** 单元类用于将某些类型的配件及其数据“附加”到车辆和挂车配置上。此类型的单元通常为无名单元，并在拥有/使用它们的配置所在的同一上下文中声明。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| wear | float | 0.0 | 此属性用于跟踪配件的损坏和磨损情况。0 对应未磨损状态，1 对应完全磨损状态。 |
| **data_path** | string |  | 包含合适配件数据单元的 SII 文件的完整路径。 |

## 适用的配件数据类型

以下配件数据类型可用于 **vehicle_accessory**：

- [accessory_cabin_data](accessory%20cabin%20data.md)
- [accessory_cargo_data](accessory%20cargo%20data.md)
- [accessory_chassis_data](accessory%20chassis%20data.md)
- [accessory_engine_data](accessory%20engine%20data.md)
- [accessory_headlight_data](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/accessory_headlight_data&action=edit&redlink=1)
- [accessory_interior_data](accessory%20interior%20data.md)
- [accessory_trailer_data](accessory%20truck%20data.md)
- [accessory_trailer_body_data](accessory%20truck%20data.md)
- [accessory_transmission_data](accessory%20transmission%20data.md)
- [accessory_truck_data](accessory%20truck%20data.md)

## 相关单元

- [traffic_trailer](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_trailer&action=edit&redlink=1)
- [traffic_vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_vehicle&action=edit&redlink=1)
- [trailer](trailer.md)
- [vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle&action=edit&redlink=1)
- [vehicle_addon_accessory](vehicle%20addon%20accessory.md)
- [vehicle_paint_job_accessory](vehicle%20paint%20job%20accessory.md)
- [vehicle_wheel_accessory](vehicle%20wheel%20accessory.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/vehicle_accessory | revision: 4758 | captured: 2026-10-21 23:56:14 -->
