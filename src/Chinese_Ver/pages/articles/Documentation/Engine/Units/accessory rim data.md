# Documentation/Engine/Units/accessory rim data

The **accessory_rim_data** unit class is used to define wheels (rims), hubs, nuts and covers for the [player's vehicle](../Game%20data/Player%20trucks%20definitions.md). It defines the path to the visible model, the look used, whether it is paintable, and horizontal offset of the tire from its default position. Units of this type are typically found in:

- **/def/vehicle/f_cover/*.sii** (front hub covers for playable trucks) → Valid unit names are `*.fcover`
- **/def/vehicle/f_disc/*.sii** (front wheels for playable trucks) → Valid unit names are `*.fdisc`
- **/def/vehicle/f_hub/*.sii** (front hubs for playable trucks) → Valid unit names are `*.fhub`
- **/def/vehicle/f_nuts/*.sii** (front nuts for playable trucks) → Valid unit names are `*.fnuts`
- **/def/vehicle/r_cover/*.sii** (rear hub covers for playable trucks) → Valid unit names are `*.rcover`
- **/def/vehicle/r_disc/*.sii** (rear wheels for playable trucks) → Valid unit names are `*.rdisc`
- **/def/vehicle/r_hub/*.sii** (rear hubs for playable trucks) → Valid unit names are `*.rhub`
- **/def/vehicle/r_nuts/*.sii** (rear nuts for playable trucks) → Valid unit names are `*.rnuts`

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md). Required attributes are **bolded**.

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| **model** | string |  | Path to the model descriptor (.pmd) of a valid rim model. Valid rim models have *left* and *right* variants. |
| look | token | default | Name of the look to be used. |
| tire_shift | float | 0.0 | The distance in meters the tire model is shifted toward the vehicle centerline. This should only be defined for accessories of the **fdisc** and **rdisc** type. |
| paintable | boolean | false | When true, enables the color picker on the garage, truck browser, etc screens. The paint color is applied to pieces of the **model** whose materials use the [paint](../../Tools/SCS%20Blender%20Tools/Supported%20shaders.md#paint) flavor. **Note:** Unlike other accessories, rim accessories do not inherit the paint color(s) of the vehicle they belong to. Each instance may have its own paint color. |
| default_color | float3 | (1.0, 1.0, 1.0) | Sets the default color for the rim accessory. |

## Related Classes

- [accessory_wheel_data](accessory%20wheel%20data.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_rim_data | revision: 3266 | captured: 2026-10-21 23:56:14 -->
