# Documentation/Engine/Units/accessory trailer body data

The **accessory_trailer_body_data** unit class is used to define ownable trailer body accessories, including body dimensions, volume, mass, and visual data. Units of this type are usually defined in **/def/vehicle/trailer_owned/<brand.model>/body/*.sii**.

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md).

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| size | float3 |  | Interior dimensions (cargo area) of the body in meters. (width, height, length) |
| total_size | float3 |  | Overall exterior dimensions of the trailer in meters. (width, height, length) |
| volume | float |  | The cargo volume in meters cubed (m<sup>3</sup>). |
| body_type | token |  | The trailer body type (e.g. flatbed, dryvan, etc). |
| mass | float |  | The mass of the body accessory in kilograms (empty, without cargo). |
| detail_model | string |  | Path to the detailed mesh model descriptor (.pmd). This is used only for vehicles used by player. Additionally they are used in vehicle previews & browser windows. |
| model | string |  | Path to the model descriptor (.pmd). If only a single LOD is used, it should be set up as **model**, and the other attributes (detail_model, lods) should not be defined. Presently it is typical to use only this for owned trailers. |
| lods | array&lt;string&gt; |  | Paths to the reduced level-of-detail model descriptors (.pmd), in order of increasing viewing distance (decreasing model complexity). |
| collision | string |  | Path to the collision descriptor (.pmc). |
| variant | token |  | Variant to be used from **detail_model**, **model**, and **lods**. |
| look | token |  | Look to be used from **detail_model**, **model**, and **lods**. |
| empty_cargo_model | string |  | Path to an [accessory_cargo_data](accessory%20cargo%20data.md) definition to be hooked up when the trailer is empty. *(Added in 1.39)* |
| animation | array<owner_ptr> |  | Each member points to the unit name of a [vehicle_animation_data](vehicle%20animation%20data.md) unit. *Added in 1.61* |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_trailer_body_data | revision: 5804 | captured: 2026-10-21 23:56:14 -->
