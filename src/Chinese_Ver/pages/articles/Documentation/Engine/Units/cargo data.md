# Documentation/Engine/Units/cargo data

The **cargo_data** unit class is used to define the logistical, semantic, and economic properties of a cargo. Units of this type are usually defined in **/def/cargo/<cargo_name>.sii** and [included](../Units.md#Includes) in **/def/cargo.<mod_name>.sii** and therefore **must not** use the SiiNunit magic mark.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| name | string |  | The name of the cargo for ui display. Supports @@localization@@. |
| body_types | array&lt;token&gt; |  | List of body types the cargo can be loaded in. |
| volume | float |  | The volume in m<sup>3</sup> of one unit of cargo. |
| mass | float |  | The mass in kg of one unit of cargo. |
| unit_reward_per_km | float |  | The reward in the base currency to transport one unit of the cargo one kilometer. |
| unit_load_time | float |  | The time in seconds to load one unit of cargo. |
| fragility | float |  | Defines how sensitive to damage the cargo is. |
| valuable | bool | false | When true, the player will require the Valuable Cargo skill to take the cargo and will receive related skill bonuses to XP and income. |
| overweight | bool | false |  |
| adr_class | uint |  | Assigns an ADR/Hazardous Materials classification to the cargo. The player will require the corresponding skill to take the cargo. |
| minimum_distance | float | 0 | The minimum distance in kilometers (km) for which a job may be generated using this cargo. |
| maximum_distance | float | ∞ | The maximum distance in kilometers (km) for which a job may be generated using this cargo. |
| prob_coef | float | 1.0 | The relative probability of spawning a job with this cargo. |
| group | array&lt;token&gt; |  | Each member marks the cargo as belonging to a predefined group for cargo sorting. Valid values are: machinery adr containers refrigerated liquid fragile construction bulk oversize Typically, the *fragile* category is reserved for cargoes with a **fragility** of 0.7 or higher. |

## Related Units

- [cargo_def](cargo%20def.md) (used to mark a cargo as produced or accepted by a company)
- [trailer_def](trailer%20def.md) (used to assign a trailer configuration to a cargo and set related mass properties)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/cargo_data | revision: 4061 | captured: 2026-10-21 23:56:14 -->
