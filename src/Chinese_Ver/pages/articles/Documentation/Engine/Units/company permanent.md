# Documentation/Engine/Units/company permanent

The **company_permanent** unit class is used to define non-instance-specific data for company depots. Units of this type are usually defined in **/def/company/<company_name>.sii**.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| name | string |  | The name of the company for UI display. |
| sort_name | string |  | A simplified version of the company name for sorting in lists. |
| trailer_look | token |  | When generating a job, if the trailer configuration has a paint job accessory, an attempt will be made to match this token with a paint job accessory in **/def/vehicle/trailer/<trailer_name>/company_paint_job/<trailer_look>.sii** to display a company-specific look. This file name (without the **.sii** extension) must be shorter than or equal to 12 characters, or the name won't map into the unit token. |
| out_cargo | array<link_ptr> |  | Do not use this attribute in definitions. It is generated "on the fly" from any cargo_def units in **/def/company/<company_name>/out/**. |
| in_cargo | array<link_ptr> |  | Do not use this attribute in definitions. It is generated "on the fly" from any cargo_def units in **/def/company/<company_name>/in/**. |
| city_names | array&lt;token&gt; |  | Do not use this attribute in definitions. It is generated "on the fly" from any company_def units in **/def/company/<company_name>/editor/**. |
| prefab_names | array&lt;token&gt; |  | Do not use this attribute in definitions. It is generated "on the fly" from any company_def units in **/def/company/<company_name>/editor/**. |

## Related Units

- [cargo_def](cargo%20def.md)
- [company_def](company%20def.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/company_permanent | revision: 5755 | captured: 2026-10-21 23:56:14 -->
