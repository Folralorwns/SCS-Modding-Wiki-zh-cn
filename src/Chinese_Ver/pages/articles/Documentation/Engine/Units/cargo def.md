# Documentation/Engine/Units/cargo def

The **cargo_def** unit class is used to assign a cargo to be produced or accepted by a company. Units of this type are usually defined in **/def/company/<company_name>/in/<cargo_name>.sii** to mark a cargo the company accepts and **/def/company/<company_name>/out/<cargo_name>.sii** to mark a cargo the company produces.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| **cargo** | string |  | The unit name of the cargo, corresponding to a [cargo_data](cargo%20data.md) unit. For example: `cargo: "cargo.stolen_ducks"` |

## Related Units

- [cargo_data](cargo%20data.md)
- [company_permanent](company%20permanent.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/cargo_def | revision: 3300 | captured: 2026-10-21 23:56:14 -->
