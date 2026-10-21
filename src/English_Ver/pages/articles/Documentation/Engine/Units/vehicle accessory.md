# Documentation/Engine/Units/vehicle accessory

The **vehicle_accessory** unit class is used to 'attach' certain types of accessories and their data to vehicle and trailer configurations. Units of this type are typically nameless and declared within the same context as the configuration that owns/uses them.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| wear | float | 0.0 | This attribute is used to track damage and wear to the accessory. 0 corresponds to an unworn state and 1 corresponds to a completely worn state. |
| **data_path** | string |  | Full path to the SII file containing a suitable accessory data unit. |

## Suitable Accessory Data Types

These accessory data types can be used by **vehicle_accessory**:

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

## Related Units

- [traffic_trailer](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_trailer&action=edit&redlink=1)
- [traffic_vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_vehicle&action=edit&redlink=1)
- [trailer](trailer.md)
- [vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle&action=edit&redlink=1)
- [vehicle_addon_accessory](vehicle%20addon%20accessory.md)
- [vehicle_paint_job_accessory](vehicle%20paint%20job%20accessory.md)
- [vehicle_wheel_accessory](vehicle%20wheel%20accessory.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/vehicle_accessory | revision: 4758 | captured: 2026-10-21 23:56:14 -->
