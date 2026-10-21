# Documentation/Engine/Units/accessory addon tank data

> **Note:** This article is a work in progress and has yet to be reviewed by SCS staff. Some information may be incomplete or inaccurate.

The **accessory_addon_tank_data** unit class is used for adding accessory based tank data container. For player trucks, units of this type are usually defined in **/def/vehicle/truck/<brand.model>/accessory/tank/*.sii** and valid unit names end in `.tank`. *This unit type was added in 1.41.*

## Attributes

Many common attributes are inherited from [**accessory_addon_data**](accessory%20addon%20data.md).

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| fuel_tank_size | float | 0.0 | Fuel tank size in liters. Overrides [chassis](accessory%20chassis%20data.md) info about fuel tank size, if positive. |
| adblue_tank_size | float | 0.0 | AdBlue/DEF tank size in liters. Overrides [chassis](accessory%20chassis%20data.md) info about adblue tank size, if positive. |

> **Note:** This accessory type is expected at most once on any given truck. While it is technically possible to have more than one tank type accessory (eg under different locator/accessory type name) only the first found is used for value override. Multiple occurence has undefined behavior.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_addon_tank_data | revision: 4968 | captured: 2026-10-21 23:56:14 -->
