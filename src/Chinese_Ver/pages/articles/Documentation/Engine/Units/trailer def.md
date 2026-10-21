# Documentation/Engine/Units/trailer def

The **trailer_def** unit class acts as an intermediary between [cargo_data](cargo%20data.md) and [trailer](trailer.md) units. Units of this type are usually defined in **/def/cargo/<cargo_name>/<trailer_name>.sii**, corresponding to **def/cargo/<cargo_name>.sii**. They define which trailer configuration to enable for the cargo, the cargo's mass for that trailer configuration, how that mass is distributed/placed on the trailer and its slave units, and where the configuration is permitted.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| trailer | string |  | The unit name of the **trailer** unit to be enabled for the cargo. This attribute can safely refer to units which aren't present. (Only for legacy usage when defined in /def/cargo/<cargo_name>/) |
| gross_trailer_weight_limit | float |  | The maximum technical or logical combined weight of the trailer and its cargo (take into account bridge formula, and other similar rules). |
| chassis_mass | float |  | The mass of the trailer chassis in kg. |
| body_mass | float |  | The mass of the trailer body in kg. |
| length | float | 0 | The length of the trailer combination in meters. When generating a job this is compared against the **allowed_trailer_length** of the source and destination depot [prefabs](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/prefab_data&action=edit&redlink=1) to determine whether this trailer_def is suitable for the job. |
| axles | uint |  | The number of axles in the trailer combination, which is checked against country_data→mass_limit_per_axle_count to determine the allowable gross weight. |
| volume | float |  | The interior volume of the trailer body in m<sup>3</sup>. |
| body_type | token |  | Sets the body type of the trailer configuration, which determines which cargoes are allowed to be carried. |
| chain_type | token |  | Sets the trailer chain type of the trailer configuration. |
| country_validity | array&lt;token&gt; |  | Each member is a country (or a state in ATS) where this trailer_def will be suitable for generated jobs. Both the origin and destination of a job must be in the *country* array for the trailer_def to be suitable for it. If unset, then the trailer_def is suitable in all countries. For example, the following would be limited to only Nevada and Arizona: country[]: arizona country[]: nevada |
| **mass_ratio** | array&lt;float&gt; |  | Each member defines how much of the cargo mass and forces are borne by each trailer in the trailer configuration, starting with the *master* trailer and iterating through the *slave* trailers. These must add up to 1. |

## World of Trucks Compatibility

World of Trucks jobs will make use of mod trailers if the following conditions are satisfied:

- The **mass** is equal to, or greater than the job's cargo mass.
- The **length** is compatible with the source and destination prefabs.
- The configuration is valid for the source and destination **country**.
- The trailer count is equal to the trailer count of the job (i.e. A multipivot trailer configuration won't be selected for a single-trailer job).

## Related Units

- [cargo_data](cargo%20data.md)
- [trailer](trailer.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/trailer_def | revision: 4209 | captured: 2026-10-21 23:56:14 -->
