# Documentation/Engine/Units/accessory truck data

The **accessory_truck_data** unit class defines basic information, cameras, fallback rules, and required accessories for the [player's truck](../Game%20data/Player%20trucks%20definitions.md). Units of this type are defined in **/def/vehicle/truck/<brand.model>/data.sii**.

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md). Required attributes are **bolded**.

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| **info** | array&lt;string&gt; |  | This member is attribute of accessory data. Theese items are typically defined for **accessory_truck_data**: info[]: "@@brand_peterbilt@@" // The truck brand info[]: "@@series_peterbilt_579@@" // The truck model info[]: "" // Optional description (used by cars) info[]: "" // Optional short brand name (used eg by Mercedes) info[]: "" // Optional series/cabin name (used eg by Iveco Hiway) *Tweaked in 1.61, added description as 3rd element and two alernative names moved from 3rd and 4th to 4th and 5th elements respectively.* |
| require | array&lt;token&gt; |  | Accessory types which should be required, regardless of the vehicle configuration, should be defined in **accessory_truck_data**. For more information, see [accessory_data](accessory%20data.md). |
| **behind_camera** | link_ptr |  | The unit name of the camera to use for the orbit (2) view. Typically `camera.behind.basic`. |
| **interior_camera** | link_ptr |  | The unit name of the camera to use for the interior (1) view. Typically `camera.interior.<brand>.<model>`. |
| **interior_camera_oculus** | link_ptr |  | The unit name of the camera to use for the interior (1) view when using a head-mounted display. Typically `camera.interior.<brand>.<model>.oculus`. |
| **window_camera** | link_ptr |  | The unit name of the camera to use in the lean-out (5) view. Typically `camera.window.basic`. |
| **bumper_camera** | link_ptr |  | The unit name of the camera to use in the bumper (6) view. Typically `camera.bumper.basic`. |
| **cabin_camera** | link_ptr |  | The unit name of the camera to use for the cabin-top (4) view. Typically `camera.cabin.basic`, placed at the *cam_cabin** locator of the active cabin accessory variant. |
| **wheel_camera** | link_ptr |  | The unit name of the camera to use in the wheel (7) view. Typically `camera.wheel.basic`. |
| **top_camera** | link_ptr |  | The unit name of the camera to use for the overhead (3) view. Typically `camera.top.basic`. |
| top_fixed_camera | link_ptr |  | Typically unused. |
| **tv_camera** | link_ptr |  | The unit name of the camera to use in TV (8) view. Typically `camera.tv.basic`. |
| predefined_tv_camera | link_ptr |  | Typically unused. |
| side_camera | link_ptr |  | Typically unused. |
| wander_camera | link_ptr |  | The unit name of the camera to use in wander mode. Typically `camera.wander`. The player typically won't encounter this mode as it is primarily used for testing. |
| **debug_camera** | link_ptr |  | The unit name of the camera to use for the developer/fly camera (0). Typically `camera.debug`. |
| **fallback** | array&lt;string&gt; |  | Each member contains a specially-formatted string which defines an accessory type (token) and the relative path to an SII file with a safe fallback accessory defined. So a fallback rule for `chassis` may look like `fallback[]: "chassis\|4x2.sii"` which would call on */def/vehicle/truck/<make.model>/chassis/4x2.sii* if there is ever a problem with the vehicle's currently assigned chassis accessory that makes it invalid or unloadable. Accessories in the accessory folder are handled somewhat specially. For example, a rule for `steering_w` looks like `fallback[]: "accessory\|steering_w/shape1.sii"`. **Note:** There are 15 *required* fallback rules: chassis, cabin, engine, transmission, f_tire, f_disc, f_hub, f_nuts, r_tire, r_disc, r_hub, r_nuts, head_light, paint_job, interior. It is generally advisable to include a rule for steering_w if the truck has interchangeable steering wheels. |
| use_non_wheel_pin_placement_from_model | bool |  | If true, then all pins (except wheel pins) will take their position and orientation directly from their locators in vehicle models. Only the **double_sided** flag is always taken from ui_truck_scene_config. *Added in 1.61.* |
| trims | array<owner_ptr> |  | List of rules (*trim_rule* unit) for optional part of vehicle name. Each element defines set of accessories (by file name) that are required for given name part. First matched element defines the name part. *Added in 1.61.* |

### Pin Overrides *(Added in 1.40)*

The following array attributes are used to override the location, appearance, and orientation of accessory pins in the truck configuration scene or in vehicle models (defined via use_non_wheel_pin_placement_from_model). Their usage is the same as the identically named attributes in the ui_truck_scene_config unit, such that one member of each array is used to override the behavior of each pin. Pin overrides defined in accessory_truck_data will supersede the data in ui_truck_scene_config for the associated truck.

| Name | [Type](../Units.md#Attribute_types) | Description |
| --- | --- | --- |
| pin_group | array&lt;token&gt; | The name of the accessory group for each pin override |
| pin_look | array&lt;token&gt; | The appearance of the accessory pin to use – typically `custom_acc` |
| pin_offset | array&lt;float3&gt; | Vector to offset the accessory pin from the locator |
| pin_dir | array&lt;float3&gt; | Vector to set the direction of the pin (independent of locator orientation) |
| pin_dir_uk | array&lt;float3&gt; | Vector to set the direction of the pin for right-hand drive (independent of locator orientation). This attribute is typically omitted in ATS. |
| double_sided | array&lt;bool&gt; | When true, the pin will be duplicated and mirrored across the truck's X-axis. |

In this first example, the pin for the *sideskirt* accessory is offset 1 m to the left of the locator (-X), and pointed to the left as well (-X). It will also be drawn 1 m to the right of the locator, pointed to the right.

```
	pin_group[]: 	sideskirt
	pin_look[]: 	custom_acc
	pin_offset[]: 	(-1, 0, 0)
	pin_dir[]: 	(-1, 0, 0)
	pin_dir_uk[]: 	(-1, 0, 0)
	double_sided[]:	true
```

In this example, the pin for the *exhaust* accessory will be drawn at the locator (no offset), and will be pointed 45° to the rear left of the truck. It will also be drawn 45° to the rear right of the truck. This has the effect of making the pin completely visible from both sides and the rear of the vehicle.

```
	pin_group[]: 	exhaust
	pin_look[]: 	custom_acc
	pin_offset[]: 	(0, 0, 0)
	pin_dir[]: 	(-1, 0, 1)
	pin_dir_uk[]: 	(-1, 0, 1)
	double_sided[]:	true
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_truck_data | revision: 5783 | captured: 2026-10-21 23:56:14 -->
