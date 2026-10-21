# Documentation/Engine/Units/vehicle wheel accessory

> **Note:** WIP — [Smarty](../../../../users/Smarty.md) ([talk](../../../../user_talk/Smarty.md)) 04:25, 23 June 2017 (CEST)

The **vehicle_wheel_accessory** unit class is used to 'attach' wheel/rim accessories and their data to vehicle and trailer configurations. Units of this type are typically nameless and declared within the same context as the configuration that owns/uses them.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| wear | float | 0.0 | This attribute is used to track damage and wear to the accessory. 0 corresponds to an unworn state and 1 corresponds to a completely worn state. |
| **data_path** | string |  | Full path to the SII file containing a suitable accessory data unit. |
| offset | uint | 0 | The axle index to which this accessory applies. "Front" (steering) axles are enumerated from the front of the vehicle to its rear and "rear" axles are enumerated from the rear of the vehicle to its front. Front and rear axles are enumerated independently. |
| paint_color | float3 | **default_color** from data unit | The color to be used for .paint materials on the accessory model. |

## Suitable Accessory Data Types

These accessory data types can be used by **vehicle_wheel_accessory**:

- [accessory_rim_data](accessory%20rim%20data.md)
- [accessory_wheel_data](accessory%20wheel%20data.md)

## Related Units

- [traffic_trailer](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_trailer&action=edit&redlink=1)
- [traffic_vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_vehicle&action=edit&redlink=1)
- [trailer](trailer.md)
- [vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle&action=edit&redlink=1)
- [vehicle_accessory](vehicle%20accessory.md)
- [vehicle_addon_accessory](vehicle%20addon%20accessory.md)
- [vehicle_paint_job_accessory](vehicle%20paint%20job%20accessory.md)
- [vehicle_sound_accessory](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle_sound_accessory&action=edit&redlink=1)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/vehicle_wheel_accessory | revision: 3322 | captured: 2026-10-21 23:56:14 -->
