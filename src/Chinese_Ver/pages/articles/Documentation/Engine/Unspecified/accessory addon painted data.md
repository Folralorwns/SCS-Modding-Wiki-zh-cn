# Documentation/Engine/Unspecified/accessory addon painted data

The **accessory_addon_painted_data** unit class is used for painted vehicle accessories which add a visible component to a vehicle. This is most commonly used for customization of the [player's vehicle](../Game%20data/Player%20trucks%20definitions.md). It defines the paths to the visible models and their configuration (variant, look, excluded views), and the path to the collision mesh if applicable. Units of this type are found in **/def/vehicle/truck/<brand.model>/accessory/&lt;type&gt;/*.sii**.

This SII data set allows the Color Picker UI in the vehicle shop to be utilized for players to color their accessory.

> **Note:** Painted parts must be assigned the 'truckpaint' rfx in blender or the .paint flavor for appropriate rfx in order to be painted.

> **Note:** Some legacy accessories which don't directly interact with the player (eg. badges) may also be found in **def/vehicle/truck/<brand.model>/&lt;type&gt;/*.sii** because of legacy. So when creating new types always create them inside **accessory** subfolder.

## Attributes

Many common attributes are inherited from [**accessory_data**](../Units/accessory%20data.md).

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| exterior_model | string |  | Path to the model descriptor (.pmd) for the model to be displayed in the exterior view (if applicable). |
| exterior_model_uk | string |  | Path to the model descriptor (.pmd) for the model to be displayed in the exterior view for right-hand drive vehicles (if applicable). If unset, defaults to **exterior_model**. |
| interior_model | string |  | Path to the model descriptor (.pmd) for the model to be displayed in the interior view (if applicable). |
| interior_model_uk | string |  | Path to the model descriptor (.pmd) for the model to be displayed in the interior view for right-hand drive vehicles (if applicable). If unset, defaults to **interior_model**. |
| coll | string |  | Path to the collision descriptor (.pmc) for the accessory (if applicable). |
| look | token | default | Name of the look to be used on all descriptors of this accessory. **Note:** All models for an accessory must have the same set of looks. |
| variant | token | default | Name of the variant to be used on all descriptors of this accessory. **Note:** All models for an accessory must have the same set of variants. |
| hide_in | u32 | 0 | Flag for “hiding“ accessory from being drawn in specific views. Valid values can be calculated [here](http://eurotrucksimulator2.com/modding_changes_114.php#Hide%20following%20views). **Note:** Accessories whose model references textures containing the mirror reflection (e.g. the mirror itself) **MUST** be marked as not visible in the mirrors. Previously there was a special mechanism to handle this however the now game exclusively relies on hide_in attribute to handle that. |
| default_color | (R, G, B) | (0, 0, 0) | The default color value of the accessory IE. (0, 0, 0) for pure black item. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Unspecified/accessory_addon_painted_data | revision: 5617 | captured: 2026-10-21 23:56:14 -->
