# Documentation/Engine/Units/accessory horn addon data

The **accessory_horn_addon_data** unit class is an extension of [**accessory_addon_data**](accessory%20addon%20data.md), used specifically for air horn accessories. If functions the same as **accessory_addon_data**, with the addition of the *sound_path* attribute used to bind a horn sound event to the accessory. This is most commonly used for customization of the [player's vehicle](../Game%20data/Player%20trucks%20definitions.md). This unit type was added in 1.38.

## Attributes

Many common attributes are inherited from parent classes [**accessory_addon_data**](accessory%20addon%20data.md) and [**accessory_data**](accessory%20data.md).

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| sound_path | string |  | Path to the sound bank/event or soundref to be used for the horn accessory. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_horn_addon_data | revision: 4786 | captured: 2026-10-21 23:56:14 -->
