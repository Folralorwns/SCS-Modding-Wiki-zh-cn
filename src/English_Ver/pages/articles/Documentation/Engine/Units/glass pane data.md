# Documentation/Engine/Units/glass pane data

The **glass_pane_data** unit class is used to define glass 'panes' which are used to simulate raindrop accumulation, movement, and clearing in the interior view. A separate unit is used for each pane. They are defined as nameless units, belonging to [accessory_interior_data](accessory%20interior%20data.md) via the *glass_panes* attribute and are typically included via **/def/vehicle/truck/<brand.model>/interior/glass.sui**.

> **Note:** Because of historical reasons some trucks in ETS2 are using **glass.dat** instead of **glass.sui**. However when you are creating your own definitions SUI extension shall be used.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| locator | string |  | The name of the locator in the interior model that corresponds to this glass pane. The locator's Y axis points 'out' from the glass surface, and its XZ plane forms the surface. |
| size | float2 |  | The size (width, height) of the glass pane in meters. |
| drop_size_minimum | float | 0.006 | Minimum raindrop size in meters. |
| drop_size_maximum | float | 0.024 | Maximum raindrop size in meters. |
| edge_angle | float | 0 | Yaw angle (in degrees) between locator orientation and orientation of normals at left and right sides of the plane. Used to simulate fake curved surface. |
| wipers | array<owner_ptr> |  | Each member points to a [wiper_data](wiper%20data.md) unit defining a wiper that will affect this glass pane. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/glass_pane_data | revision: 3246 | captured: 2026-10-21 23:56:14 -->
