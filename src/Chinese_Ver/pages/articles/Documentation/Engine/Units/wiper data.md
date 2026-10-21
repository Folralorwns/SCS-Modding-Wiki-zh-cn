# Documentation/Engine/Units/wiper data

The **wiper_data** unit class is used to define wipers which clear raindrops from the simulated glass panes in the interior view. A separate unit is used for each wiper. They are defined as nameless units, belonging to [glass_pane_data](glass%20pane%20data.md) via the *wipers* attribute and are typically included via **/def/vehicle/truck/<brand.model>/interior/glass.sui**.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| center_bone | string |  | The name of the bone in the animated interior model's skeleton to use as the wiper's centroid. The bone's Z axis should point 'into' the glass pane (roughly opposite the glass locator's Y axis). |
| length | float | 0.0 | The length of the wiper 'blade' in meters, along the center_bone's X axis. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/wiper_data | revision: 3276 | captured: 2026-10-21 23:56:14 -->
