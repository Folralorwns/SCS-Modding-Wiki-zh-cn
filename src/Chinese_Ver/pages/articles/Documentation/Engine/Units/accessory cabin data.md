# Documentation/Engine/Units/accessory cabin data

The **accessory_cabin_data** unit class configures the models for the cabin of the [player's vehicle](../Game%20data/Player%20trucks%20definitions.md). Units of this type are found in **/def/vehicle/truck/<brand.model>/cabin/**.

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md).

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| detail_model | string |  | Path to the detailed mesh model descriptor (.pmd). This is used only for vehicles used by player. Additionally they are used in vehicle previews & browser windows. |
| model | string |  | Path to the model descriptor (.pmd). If only a single LOD is used, it should be set up as **model**, and the other attributes (detail_model, lods) should not be defined. |
| lods | array&lt;string&gt; |  | Paths to the reduced level-of-detail model descriptors (.pmd), in order of increasing viewing distance (decreasing model complexity). |
| collision | string |  | Path to the collision descriptor (.pmc). |
| variant | token |  | Selects the variant to be used for all models/collisions defined. This is required if the cabin and chassis share a model as is currently the standard practice in ETS2 and ATS. Default value is *default*. **Note:** All models defined for this **accessory_cabin_data** must have this variant name. |
| variant_uk | token |  | Selects the variant to be used for all models/collisions for right-hand-drive (RHD) vehicles. If unset, defaults to the same value as **variant**. **Note:** All models defined for this **accessory_cabin_data** must have this variant name. |
| look | token |  | Selects the look to be used for all models defined. Default value is *default*. **Note:** All models defined for this **accessory_cabin_data** must have this look name. |
| wiper_model | string |  | Path to the animated wiper model (.pmg). |
| wiper_anim | resource_tie |  | Path to the wiper animation (.pma). |
| rear_wiper_anim | resource_tie |  | Path to the rear wiper animation (.pma). *Added in 1.61* |
| wiper_model_uk | string |  | Path to the animated wiper model (.pmg) for RHD vehicles. If unset, defaults to the value of **wiper_model**. |
| wiper_anim_uk | resource_tie |  | Path to the wiper animation (.pma) for RHD vehicles. If unset, defaults to the value of **wiper_anim**. |
| drl_with_headlights | float | 0.0 | Sets the relative strength of the daytime running lights when the headlights are on. For the DRL to be *off* when the headlights are on, a value of 0 is used. If the DRL should stay on and not dim when the headlights are on, a value of 1 is used. An intermediate value will dim the DRL when the headlights are on, and a value greater than 1 will intensify the DRL when the headlights are on. The typical value in ETS2 is 0.4. |
| suspension | bool | true | When true, physical simulation of cabin air suspension is enabled. |
| suspension_type | token | 4air | Defines type of cabin suspension if suspension is enabled. possible values are *4air* (EU type) and *hinge2air*(US type). *Added in 1.47* |
| sounds | array&lt;string&gt; |  | Each item assigns an FMOD event to a function, using the "*sound_name\|sound_path*" [format](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories). *Added in 1.39* Expected sound event names are: horn, aero_noise, and rain_noise. |
| animation | array<owner_ptr> |  | Each member points to the unit name of a [vehicle_animation_data](vehicle%20animation%20data.md) unit. *Added in 1.61* |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_cabin_data | revision: 5809 | captured: 2026-10-21 23:56:14 -->
