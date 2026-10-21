# Documentation/Engine/Units/accessory interior data

The **accessory_interior_data** unit class is used to define the interior and its animations for the [player's vehicle](../Game%20data/Player%20trucks%20definitions.md). Units of this type are usually defined in **/def/vehicle/truck/<brand.model>/interior/*.sii**, making heavy use of [includes](../Units.md#Includes) via:

- **/def/vehicle/truck/<brand.model>/interior/animations.sui** (animation-related attributes; **animations_uk.sii** for RHD vehicles in ETS2)
- **/def/vehicle/truck/<brand.model>/interior/dashboard_color.sii** (dashboard_color array attribute)
- **/def/vehicle/truck/<brand.model>/interior/seat.sui** (seat adjustment limits; **seat_uk.sui** for RHD vehicles in ETS2)

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md).

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| model | string |  | Path to the model descriptor (.pmd) for the rigid interior model. |
| animated_model | string |  | Path to the model descriptor (.pmd) for the animated interior model. |
| collision | string |  | Path to the collision descriptor (.pmc). This is used for toy physics. |
| variant | token |  | Name of the variant to be used for the interior models and collision. |
| look | token |  | Name of the look to be used for the interior models. |
| ext_model | string |  | Path to the model descriptor (.pmd) for the exterior model (the interior visible from outside cameras). |
| ext_variant | token |  | Name of the variant to be used on the exterior model. |
| ext_look | token |  | Name of the look to be used on the exterior model. |
| *animation attributes* | string / float |  | There are currently nearly 70 [interior animation](../Truck%20Interior%20Animations%20and%20IDs.md#Interior_Animations) attributes, plus _min and _max attributes for some with adjustable ranges. Interior animations are typically defined externally in **animations.sui** and [included](../Units.md#Includes) into the interior definition. |
| wiper_delay | array&lt;float&gt; |  | Each member defines a delay in seconds between wipe cycles for intermittent wipers. They should generally be in decreasing order because the last wiper mode is continuous. If empty then only continuous mode is available. *Removed in 1.35.* |
| wiper_duration_and_delay | array&lt;float2&gt; | (2.0, 0.0) | Each member defines the duration of the wipe cycle in seconds, and the delay between wipe cycles in seconds. They should generally be in decreasing order of delay, and decreasing order of speed. *Added in 1.35.* |
| wiper_main_cycle | float2 | (0.0, 1.0) | Defines the working range of the wiper within the animation. 0.0 to the first value - animation of the wiper start sequence that plays once before the main cycle begins between the two values - animation of the main wiper cycle that is repeated second value to 1.0 - animation of the wiper end sequence that is played once after the wipers are turned off. *Added in 1.61.* |
| blinker_delay | float | 0.5 | The length of half of the blinker cycle in seconds. The blinker is on for this length of time, and then off for this length of time, etc. Typically included via **animations.sui**. |
| show_chassis_rear | bool | false | It should be set true in interiors where you can see part of chassis or chassis accessory (eg ATS daycabs). It renders prebaked model of chassis and all its accessories in interior, so you might have issues with items that are mounted on chassis, but still have their own visualization in interior - you can see them twice and/or z-fighting. To be properly visible both inside and outside, either the accessory locator should be in chassis model ONLY, or it should be in interior AND in cabin model both. *Added in 1.44.* |
| dashboard_path | string |  | Path to the UI definition for the dashboard display. |
| gps_path | string |  | Path to the UI definition for the GPS display. |
| use_mile_units | bool | false | When true, distances and speeds on the dashboard will use mile units instead of kilometers. |
| left_hand_traffic | bool | false | When true, the vehicle uses right-hand drive (UK) conventions. |
| backlight_with_lights | bool | true | When false, the dashboard backlight is always on with the ignition. Otherwise, the backlight is activated with the headlights as normal. |
| air_brake_safeguard | bool | false | When true, the parking brake is automatically applied when the supply air drops below a certain threshold (typical US behavior). |
| panel_intensity_min | float | 0.01 | The minimum backlight intensity. |
| panel_intensity_max | float | 0.3 | The maximum backlight intensity. |
| glass_panes | array<owner_ptr> |  | Each member points to the unit name of a [glass_pane_data](glass%20pane%20data.md) unit. |
| dashboard_color | array&lt;float3&gt; |  | An array of 16 colors which define the illumination color of dashboard and other dif.lum surfaces in the interior based on the tile they are UV mapped to. Typically included via **dashboard_color.sui**. |
| seat_left_limit | float | -0.15 | Maximum distance the interior camera can be moved left. Typically included via **seat.sui**. |
| seat_right_limit | float | 0.15 | Maximum distance the interior camera can be moved right. Typically included via **seat.sui**. |
| seat_up_limit | float | 0.15 | Maximum distance the interior camera can be moved up. Typically included via **seat.sui**. |
| seat_down_limit | float | -0.15 | Maximum distance the interior camera can be moved down. Typically included via **seat.sui**. |
| seat_front_limit | float | -0.1 | Maximum distance the interior camera can be moved forward. Typically included via **seat.sui**. |
| seat_back_limit | float | 0.2 | Maximum distance the interior camera can be moved backward. Typically included via **seat.sui**. |
| sounds | array&lt;string&gt; |  | Each item assigns an FMOD event to a function, using the "*sound_name\|sound_path*" [format](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories). *Added in 1.39* Expected sound event names are: air_warning, blinker_off, blinker_on, noise, stick_blinker, stick_blinker_off, stick_engine_brake, stick_hazard_warning, stick_high_beam, stick_light_horn, stick_lights, stick_park_brake, stick_park_brake_off, stick_retarder, stick_wipers, weigh_green, weigh_red, window_click, window_move, wipers_down, and wipers_up. |

## Glass Panes and Wipers

Related units, **glass_pane_data** and **wiper_data** are defined within the same `SiiNunit` scope as accessory_interior_data, included via **/def/vehicle/truck/<brand.model>/interior/glass.sui** (or **glass.dat** in some legacy cases):

- [glass_pane_data](glass%20pane%20data.md) (Used to define surfaces for raindrop accumulation and wiper simulation)
- [wiper_data](wiper%20data.md) (Used to define wipers that wipe drops from glass panes)

For example:

```
SiiNunit
{	// start of SiiNunit global scope

accessory_interior_data : something.brand.truck.interior
{	// start of accessory_interior_data unit

	// various attributes belonging to accessory_interior_data

	// each member refers to a unit included via glass.sui
	glass_panes[]: .brand.truck.pane.front
	glass_panes[]: .brand.truck.pane.close
	glass_panes[]: .brand.truck.pane.far
	// etc...

}	// end of accessory_interior_data scope

@include "glass.sui"	// file containing glass_pane_data and wiper_data units

}	// end of SiiNunit global scope
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_interior_data | revision: 5795 | captured: 2026-10-21 23:56:14 -->
