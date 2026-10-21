# Documentation/Engine/Units/vehicle addon accessory

The **vehicle_addon_accessory** unit class is used to 'attach' addon accessories, their data, and slotted hookups to vehicle and trailer configurations. Units of this type are typically nameless and declared within the same context as the configuration that owns/uses them.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| wear | float | 0.0 | This attribute is used to track damage and wear to the accessory. 0 corresponds to an unworn state and 1 corresponds to a completely worn state. |
| **data_path** | string |  | Full path to the SII file containing a suitable accessory data unit. |
| slot_name | array&lt;token&gt; |  | Name of the model locator in the accessory model for the hookup accessory to be hooked up to. Valid names begin with `slot_`. |
| slot_hookup | array&lt;string&gt; |  | Unit name of the addon hookup to be hooked up in the corresponding **slot_name**. |

> **Note:** The **slot_name** and **slot_hookup** arrays are usually defined as ordered arrays to ensure that their indices correspond. They must always be the same length.

## Slot Usage Example

Here is an example of how marker lights are hooked up to slots on a *cabflares* accessory in a truck configuration:

```
vehicle: .tdealer.peterbilt_4
{
    // ...
    accessories[]: .peterbilt_4.lights
    // ...
}
// ...
vehicle_addon_accessory : .peterbilt_4.lights {
    slot_name: 5
    slot_name[0]: slot_0
    slot_name[1]: slot_2
    slot_name[2]: slot_3
    slot_name[3]: slot_4
    slot_name[4]: slot_6
    slot_hookup: 5
    slot_hookup[0]: "light2.addon_hookup"
    slot_hookup[1]: "light2.addon_hookup"
    slot_hookup[2]: "light2.addon_hookup"
    slot_hookup[3]: "light2.addon_hookup"
    slot_hookup[4]: "light2.addon_hookup"

    wear: 0
    data_path: "/def/vehicle/truck/peterbilt.579/accessory/cabflares/shape01.sii"
}
// ...
```

## Suitable Accessory Data Types

These accessory data types can be used by **vehicle_addon_accessory** in the **data_path** attribute:

- [accessory_addon_data](accessory%20addon%20data.md)
- [accessory_addon_int_data](accessory%20addon%20int%20data.md)
- [accessory_addon_patch_data](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/accessory_addon_patch_data&action=edit&redlink=1)

These accessory data types can be hooked up to the accessory's slots:

- [accessory_hookup_data](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/accessory_hookup_data&action=edit&redlink=1)
- [accessory_hookup_int_data](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/accessory_hookup_int_data&action=edit&redlink=1)
- [accessory_horn_hookup_data](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/accessory_horn_hookup_data&action=edit&redlink=1)

## Related Units

- [traffic_trailer](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_trailer&action=edit&redlink=1)
- [traffic_vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_vehicle&action=edit&redlink=1)
- [trailer](trailer.md)
- [vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle&action=edit&redlink=1)
- [vehicle_accessory](vehicle%20accessory.md)
- [vehicle_paint_job_accessory](vehicle%20paint%20job%20accessory.md)
- [vehicle_sound_accessory](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle_sound_accessory&action=edit&redlink=1)
- [vehicle_wheel_accessory](vehicle%20wheel%20accessory.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/vehicle_addon_accessory | revision: 3320 | captured: 2026-10-21 23:56:14 -->
