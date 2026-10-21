# Documentation/Engine/Units/trailer cable data

> **Note:** This article is a work in progress and has yet to be reviewed by SCS staff. Some information may be incomplete or inaccurate.

The **trailer_cable_data** unit class is used for defining a dynamic trailer cable connection between a vehicle and its trailer. Units of this type are typically nameless, and defined in-line with an **[accessory_addon_trailer_cables_data](accessory%20addon%20trailer%20cables%20data.md)** unit. *This unit type was added in 1.31 and was previously named **physics_trailer_cable_data** until 1.32.*

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| locator_prefix | token |  | The name of the locators on the vehicle and trailer that will be used to connect the cable. |
| rest_locator_prefix | token |  | The name of the locator on the vehicle that will be used as a rest position for the trailer end of the cable when no trailer is connected. If there is no rest locator, the cable will not be drawn unless there is a cable connected. |
| vehicle_plug_model | string |  | Path to the descriptor (.pmd) of the model to be used at the vehicle end of the cable. This model will be hooked up at, and oriented to, the locator defined in **locator_prefix**. If no model is defined, the cable will be hooked up directly to the locator on the vehicle. |
| vehicle_plug_model_variant | token | default | The variant of the **vehicle_plug_model** to be used. |
| vehicle_plug_model_look | token | default | The look of the **vehicle_plug_model** to be used. |
| vehicle_plug_model_offset | float3 | (0.0, 0.0, 0.0) | The offset (in local space) from the **vehicle_plug_model** origin at which the vehicle end of the cable will be attached. |
| trailer_plug_model | string |  | Path to the descriptor (.pmd) of the model to be used at the trailer end of the cable. This model will be hooked up at, and oriented to, the locator defined in **locator_prefix** when there is a trailer attached, or the locator defined in **rest_locator_prefix** when there is not a trailer attached. If no model is defined, the cable will be hooked up directly to the locator on the trailer. |
| trailer_plug_model_variant | token | default | The variant of the **trailer_plug_model** to be used. |
| trailer_plug_model_look | token | default | The look of the **trailer_plug_model** to be used. |
| trailer_plug_model_offset | float3 | (0.0, 0.0, 0.0) | The offset (in local space) from the **trailer_plug_model** origin at which the trailer end of the cable will be attached. |
| ring_count | int |  | The number of rings in the spiral portion of the cable. (Minimum 2) |
| ring_resolution | int |  | The number of sides each ring has. (Minimum 3) |
| diameter | float |  | Diameter of the spiral portion of the cable. (Minimum 0.02) |
| width | float |  | Diameter of the cable itself. (Minimum 0.001, cannot exceed **diameter**) |
| straight_cable_length | float | 0 | Length of straight cable, in meters, if greater than zero. Cables are spiral otherwise. |
| back_faces | boolean | false | When true, the "inside" faces of a straight cable are drawn. This can be useful when using a transparent material on cable, so that inner wall of the cable will also be visible (for example back faces are currently used in the new trailer cables for traffic vehicles). |
| material | string | "/material/ropes/cable_white.mat" | The material used for rendering the cable. |
| color | float3 | (0.5, 0.5, 0.5) | The vertex color (in linear colorspace) applied to the cable model. |
| resolution | int |  | The number of lengthwise segments for the cable simulation. (Minimum 2) |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/trailer_cable_data | revision: 4038 | captured: 2026-10-21 23:56:14 -->
