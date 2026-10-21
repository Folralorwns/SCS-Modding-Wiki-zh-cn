# Documentation/Engine/Units/company def

The **company_def** unit class is used to assign a prefab to a [company_permanent](company%20permanent.md) unit. Units of this type are usually defined in **/def/company/<company_name>/editor/<city_name>.sii**.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| **city** | token |  | The tokenized name of the city in which the prefab is located. In the case of *city.san_francisc*, this would appear as `city: san_francisc` |
| **prefab** | token |  | The tokenized name of the prefab to be linked. In the case of *prefab.d_port_sf*, this would appear as `prefab: d_port_sf` **Note:** This implementation requires that each depot prefab may only appear once per city. |

## Related Units

- [company_permanent](company%20permanent.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/company_def | revision: 3308 | captured: 2026-10-21 23:56:14 -->
