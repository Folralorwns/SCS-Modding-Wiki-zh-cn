# Documentation/Engine/Units/vehicle paint job accessory

> **Note:** WIP — [Smarty](../../../../users/Smarty.md) ([talk](../../../../user_talk/Smarty.md)) 04:17, 23 June 2017 (CEST)

The **vehicle_paint_job_accessory** unit class is used to 'attach' a paint job accessory and its [data](accessory%20paint%20job%20data.md) to vehicle and trailer configurations. Units of this type are typically nameless and declared within the same context as the configuration that owns/uses them.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| wear | float | 0.0 | This attribute is used to track damage and wear to the accessory. 0 corresponds to an unworn state and 1 corresponds to a completely worn state. |
| **data_path** | string |  | Full path to the SII file containing a suitable accessory data unit. |
| mask_r_color | float3 | From accessory data | The color to apply to the red channel of the paint job (colormask only). |
| mask_g_color | float3 | From accessory data | The color applied to the green channel of the paint job (colormask only). |
| mask_b_color | float3 | From accessory data | The color applied to the blue channel of the paint job (colormask only). |
| flake_color | float3 | From accessory data | The color used for the flake component of the paint job (flipflake only). |
| flip_color | float3 | From accessory data | The color used for the flip component of the paint job (flipflake only). |
| base_color | float3 | From accessory data | The base color of the paint job (all paint job modes). |

## Related Units

- [traffic_trailer](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_trailer&action=edit&redlink=1)
- [traffic_vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_vehicle&action=edit&redlink=1)
- [trailer](trailer.md)
- [vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle&action=edit&redlink=1)
- [vehicle_accessory](vehicle%20accessory.md)
- [vehicle_addon_accessory](vehicle%20addon%20accessory.md)
- [vehicle_sound_accessory](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle_sound_accessory&action=edit&redlink=1)
- [vehicle_wheel_accessory](vehicle%20wheel%20accessory.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/vehicle_paint_job_accessory | revision: 3323 | captured: 2026-10-21 23:56:14 -->
