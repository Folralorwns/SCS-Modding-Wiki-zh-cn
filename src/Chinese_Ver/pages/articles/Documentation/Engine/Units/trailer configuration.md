# Documentation/Engine/Units/trailer configuration

The **trailer_configuration** unit class is used to collect the chassis of a given configuration for an ownable trailer, define which body set(s) are valid for that configuration, and define which configurations are “equivalent” for the purposes of trailer configuration. Units of this type are usually found in **/def/vehicle/trailer_owned/<brand.model>/configurations/**

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| **name** | string |  | Full name of the configuration for UI display. |
| icon | string |  | Path relative to `/material/ui/accessory/` to the icon for the accessory, omitting the file extension. For example, `icon: "truck_name/fancy_doodad"` would point to `/material/ui/accessory/truck_name/fancy_doodad.mat`. |
| **chain_type** | token |  | Defines the chain type (e.g. single, double, rmdouble, etc) |
| equivalency | token |  | Trailer configurations with matching **equivalency** tokens can be switched during gameplay using the Trailer Configuration menu. This must be set explicitly — Configurations with blank equivalency attributes will not match. |
| **chassis** | array&lt;string&gt; |  | Array of paths to chassis definitions for the trailer configuration (e.g. `chassis[]: "/def/vehicle/trailer_owned/scs.box/chassis/ch_45_f.sii"`). The expected unit type is [accessory_chassis_data](accessory%20chassis%20data.md). |
| **body_sets** | array<owner_ptr> ([trailer_body_set](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/trailer_body_set&action=edit&redlink=1)) |  | Array of compatible **trailer_body_set**s with this configuration. This array is usually automatically gathered from a sub-folder with the same name as the base configuration file (name of the file to first dot, so configuration "single3.sii" or "single3.mymod.sii" should have body sets in folder "/def/vehicle/trailer_owned/<brand.model>/configurations/single3"). Body sets can also be defined and linked explicitly within the configuration definition. Each trailer configuration must have at least one valid body set. |

## Related Units

- [trailer_body_set](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/trailer_body_set&action=edit&redlink=1)
- [accessory_chassis_data](accessory%20chassis%20data.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/trailer_configuration | revision: 4067 | captured: 2026-10-21 23:56:14 -->
