# Documentation/Engine/Units/accessory addon int ui data

> **Note:** This article is a work in progress and has yet to be reviewed by SCS staff. Some information may be incomplete or inaccurate.

The **accessory_addon_int_ui_data** unit class is used for vehicle accessories which add a visible component to a vehicle with dynamic UI screen components. This is used for customization of the [player's vehicle](../Game%20data/Player%20trucks%20definitions.md), most commonly for additional GPS navigation screens or phones with clocks etc.

UI script of this accessory can access the same ID elements as dashboard or gps interior scripts, more info: [Documentation/Engine/Truck_Interior_Animations_and_IDs#Dashboards_IDs](../Truck%20Interior%20Animations%20and%20IDs.md#Dashboards_IDs).

## Attributes

Many common attributes are inherited from [**accessory_addon_data**](accessory%20addon%20data.md).

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| ui_path | string | &lt;empty&gt; | Path to the UI script of this accessory that should be drawn into drawable. |
| ui_drawable_texture_path | string | &lt;empty&gt; | Path to the texture TOBJ that UI will drawn into and should be then used in the model and serve as a display. |
| ui_drawable_size | int2 | (0, 0) | Size of the drawable texture, needs to be a power of two between [4, 4096]. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_addon_int_ui_data | revision: 5116 | captured: 2026-10-21 23:56:14 -->
