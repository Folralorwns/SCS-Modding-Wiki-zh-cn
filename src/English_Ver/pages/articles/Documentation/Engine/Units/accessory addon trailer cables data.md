# Documentation/Engine/Units/accessory addon trailer cables data

> **Note:** This article is a work in progress and has yet to be reviewed by SCS staff. Some information may be incomplete or inaccurate.

The **accessory_addon_trailer_cables_data** unit class is used for adding dynamic trailer cables between a vehicle and its trailer. For player trucks, units of this type are usually defined in **/def/vehicle/truck/<brand.model>/accessory/trlr_cables/*.sii** and valid unit names end in `.trlr_cables`. For player trailers, units of this type are usually defined in **/def/vehicle/trailer/<trailer_name>/accessory/trlr_cables/*.sii** and valid unit names end in `.trlr_cables`. *This unit type was added in 1.31.*

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md).

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| exterior_model | string |  | Path to the model descriptor (.pmd) for the model to be displayed in the exterior view (if applicable). |
| exterior_model_uk | string |  | Path to the model descriptor (.pmd) for the model to be displayed in the exterior view for right-hand drive vehicles (if applicable). If unset, defaults to **exterior_model**. |
| coll | string |  | Path to the collision descriptor (.pmc) for the accessory (if applicable). |
| look | token | default | Name of the look to be used on all descriptors of this accessory. **Note:** All models for an accessory must have the same set of looks. |
| variant | token | default | Name of the variant to be used on all descriptors of this accessory. **Note:** All models for an accessory must have the same set of variants. |
| cables | array<owner_ptr> |  | Each member points to a [trailer_cable_data](trailer%20cable%20data.md) unit |

## Model

A valid trailer cables accessory model must have the following:

- Some visible geometry (models cannot contain only locators)
- Attachment locators for each member defined in the *cables* array, where the truck plug model will be placed. The locator names are defined by each **trailer_cable_data** unit's *locator_prefix* attribute.

It may additionally make use of the following:

- Rest locators for each defined cable where the trailer plug model will be placed when there is no trailer connected (otherwise the cable will not be drawn/simulated when there is no trailer connected). The locator names are defined by each **trailer_cable_data** unit's *rest_locator_prefix* attribute.
- Special part names are displayed only during particular states:
  - `cables_off` is displayed only when no trailer is attached
  - `cables_on` is displayed only when a trailer is attached

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_addon_trailer_cables_data | revision: 5348 | captured: 2026-10-21 23:56:14 -->
