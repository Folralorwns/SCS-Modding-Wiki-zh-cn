# Documentation/Engine/Units/accessory chassis data

The **accessory_chassis_data** unit class is used to define the chassis characteristics for the [player's vehicle](../Game%20data/Player%20trucks%20definitions.md) including axle weights, extended shadow parameters, and fluid capacities. It is also used to define chassis characteristics of trailers and AI vehicles. Units of this type are usually defined in **/def/vehicle/truck/<brand.model>/chassis/*.sii**, **/def/vehicle/trailer/<trailer_name>/*.sii**, and **/def/vehicle/ai/<vehicle_name>/chassis.sii.**

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md).

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| detail_model | string |  | Path to the detailed mesh model descriptor (.pmd). This is used only for vehicles used by player. Additionally they are used in vehicle previews & browser windows. |
| model | string |  | Path to the model descriptor (.pmd). If only a single LOD is used, it should be set up as **model**, and the other attributes (detail_model, lods) should not be defined. |
| lods | array&lt;string&gt; |  | Paths to the reduced level-of-detail model descriptors (.pmd), in order of increasing viewing distance (decreasing model complexity). |
| collision | string |  | Path to the collision descriptor (.pmc). |
| pendle_axle_model | array&lt;string&gt; |  | Paths to the model descriptors (.pmd) of pendle (self-steering, lazy) axle models, paired left/right per axle. |
| brake_caliper_model | array&lt;string&gt; |  | Paths to the animated brake caliper model descriptors (.pmd), one per axle. Must match the number of axles (size of **residual_travel**) when set. |
| brake_rotor_model | array&lt;string&gt; |  | Paths to the animated brake rotor (disc) model descriptors (.pmd), one per axle. Must match the number of axles (size of **residual_travel**) when set. |
| trailer_brace_model | string |  | *For trailer usage only.* Path to the animated landing gear model. |
| trailer_brace_anim | string |  | *For trailer usage only.* Path to the landing gear animation. |
| trailer_brace_up_sound | string |  | *For trailer usage only.* Path to the sound to be played when retracting landing gear. *Default value changed to blank (no sound) in 1.35.* |
| trailer_brace_down_sound | string |  | *For trailer usage only.* Path to the sound to be played when extending landing gear. *Default value changed to blank (no sound) in 1.35.* |
| variant | token |  | Variant to be used from **detail_model**, **model**, and **lods**. |
| variant_uk | token |  | Variant to be used in countries which drive on the left. If unspecified, defaults to the value of **variant**. |
| look | token |  | Look to be used from **detail_model**, **model**, and **lods**. |
| shadow_texture | string |  | Texture to be used for basic shadow. |
| shadow_intensity | float | 1.0 | Relative intensity of basic shadow. |
| extended_shadow_texture | string |  | Texture to be used for the extended (volumetric) shadow. |
| extended_shadow_intensity | float | 1.0 | Relative intensity of the extended (volumetric) shadow. |
| extended_shadow_fadeout_start | float | 0.0 | Sets the distance in meters from the fakeshadow surface to begin fading the extended shadow. |
| extended_shadow_fadeout_length | float | 1.0 | Sets the length in meters over which to fade out the extended shadow. |
| extended_shadow_shared_model_variant | token |  | If provided, specified variant of model will be used to draw the shared shadows. |
| ui_shadow | string |  | Path to the model descriptor (.pmd) for the UI shadow (used for the truck/trailer browser, thumbnail generation, etc). |
| tank_size | float | 0.0 | Fuel tank size in liters. |
| adblue_tank_size | float | 80.0 | AdBlue/DEF tank size in liters. |
| air_tank_pressure | float | 10.0 | Nominal air brake reservoir pressure in bar. *Added in ETS2 1.27/ATS 1.6.* |
| nominal_voltage | float | 24.0 | Nominal battery voltage. *Added in 1.36* |
| air_resistance | float | -1.0 | Overrides the air resistance coefficient from [physics_data](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/physics_data&action=edit&redlink=1) for this specific chassis. When unset (negative), the global value is used. |
| residual_travel | array&lt;float&gt; |  | *For trucks and trailers.* The limit of upwards and downwards travel in meters for each axle. Each array member corresponds to an axle, from front to back. |
| trailer_mass | float | 7000.0 | *For trailer usage only.* Sets the unladen mass of the trailer. |
| powered_axle | array&lt;bool&gt; |  | *For truck usage only.* When true, motive torque will be applied on the axle. Each array member corresponds to an axle, from front to back. |
| kerb_weight | array&lt;float&gt; |  | *For truck usage only.* Assigns the static weight on each axle. Each array member corresponds to an axle, from front to back. |
| brake_rotor_diameter | array&lt;float&gt; |  | Brake rotor diameter in meters. Valid range is above 0.0 and up to 0.6. Each array member corresponds to an axle, from front to back. |
| disc_brake | array&lt;bool&gt; | false | When true, the axle uses disc brakes. Each array member corresponds to an axle, from front to back. |
| caster_angle | float | 3.0 | Caster angle of the front axle(s), in degrees. Valid range is -20 to 20. |
| sway_bar_stiffness | float | 1.0 | Relative stiffness of the anti-roll (sway) bar. Valid range is 0 to 10. |
| axle_suspension_type | array&lt;token&gt; | solidaxle | Suspension type per axle, from front to back. Possible values are: simple wishbone (double wishbone) macpherson solidaxle Each array member corresponds to an axle, from front to back. |
| solid_axle_suspension_model | array&lt;string&gt; |  | Paths to the visual model descriptors (.pmd) for solid axle beams, one entry per axle using **solidaxle** in **axle_suspension_type** that has a visible model. |
| suspension_damping_factor | array&lt;float&gt; |  | Relative suspension damping factor per axle. Valid range is 0 to 2. Each array member corresponds to an axle, from front to back. |
| suspension_class | token | heavy | Suspension class, used for suspension physics tuning and audio selection. Acceptable values are **heavy**, **bus**, or **standard**; any other value defaults to **heavy**. |
| liftable_axle | array&lt;bool&gt; |  | *For truck and trailers.* When true, the axle can be lifted. Each array member corresponds to an axle, from front to back. *Trailer functionality is added in ETS2 1.27/ATS 1.6.* |
| steerable_axle | array&lt;token&gt; | *See description* | *For truck and trailers.* Each array member corresponds to an axle, from front to back. By default, first axles on trucks are *true*, while all others are *false*. Possible values are: false (non-steerable axle) true (steerable wheels on given axle) axle (whole axle is rotated when steering, *axle_model* must be correctly defined, valid only for trailers). *Added in 1.31. Value "axle" was added in 1.50* |
| steerable_lifted_axles | bool | false | *For truck and trailers.* When true, lifted steerable axles will react to steering. Otherwise they line themselves with chassis once lifted. *Added in 1.44.* |
| max_steering_angle | uint | *See description* | Maximum steering angle, in degrees, for wheel-steered axles. If unset, defaults to 40 for trucks and 50 for trailers. Valid range is up to 70 for trucks and up to 85 for trailers. |
| steering_pivot_point_offset | float | 0.0 | Longitudinal offset of the steering pivot point, used for steering geometry calculations. |
| powered_trailer | bool | false | *For trailer usage only.* When true together with **powered_axle**, identifies the vehicle as a powered dolly/trailer rather than a truck for weight distribution purposes. |
| weight_distribution | enum | semitrailer | Determines how forces are transferred between the vehicle and its connected vehicle(s). Possible values are: truck (any standalone, self-sufficient vehicle; auto-detected when **powered_axle** is set and **powered_trailer** is false) semitrailer (fifth wheel, part of trailer weight transferred) trailer (hook, no weight transfer) spreader (removes the pitch degree of freedom, typical of a spreader/booster/stinger on a lowboy configuration) perimeter (special-purpose vehicles with no wheel-based physics, e.g. cranes) *Added in ATS 1.6.2.* |
| cog_height | float | *See description* | Height of the center of gravity above the chassis. If unset (negative), a default value is used based on whether the chassis belongs to a truck or a trailer. |
| joint_yaw_limit | float | -1.0 | Custom yaw limit, in degrees, of the joint between this vehicle and its master vehicle. Valid range is 0 to 90; negative (default) means no custom limit. |
| joint_pitch_limit | float | -1.0 | Custom pitch limit, in degrees, of the joint between this vehicle and its master vehicle. Valid range is 0 to 90; negative (default) means no custom limit. |
| joint_roll_limit | float | -1.0 | Custom roll limit, in degrees, of the joint between this vehicle and its master vehicle. Valid range is 0 to 90; negative (default) means no custom limit. |
| master_collision_angle | float | 90.0 | Angle, in degrees, at which collisions between this vehicle and its master vehicle are switched on. Valid range is 0 to 180. |
| axle_model | array&lt;string&gt; |  | *For trailer usage only.* Path to the axle model descriptors (.pmd). *Added in 1.50.* |
| axle_model_collision | array&lt;string&gt; |  | *For trailer usage only.* Path to the axle model collision descriptors (.pmc). *Added in 1.50.* |
| axle_model_extended_shadow_texture | array&lt;string&gt; |  | *For trailer usage only.* Texture to be used for the extended (volumetric) shadow underneath each axle. *Added in 1.50.* |
| axle_model_steer_angle | unsigned int |  | *For trailer usage only.* Overwrites the maximum steering angle of the last steerable axle model. *Added in 1.50.* |
| axle_model_sliding_limits | float2 | (0,0) | *For trailer usage only.* Minimum and maximum Z (longitudinal) sliding limits for movable **axle_model** models, relative to the axle locator. Requires **axle_model** to be set. |
| cog_cargo_mass_min | float | 0 | Lowest cargo mass at which to offset the center of gravity. *Added in 1.35.* |
| cog_cargo_mass_max | float | 20000 | Highest cargo mass at which to offset the center of gravity. *Added in 1.35.* |
| cog_cargo_offset_min | float3 | (0,0,0) | Distance to offset the center of gravity at **cog_cargo_mass_min**. *Added in 1.35.* |
| cog_cargo_offset_max | float3 | (0,0.6,0) | Distance to offset the center of gravity at **cog_cargo_mass_max**. *Added in 1.35.* |
| sounds | array&lt;string&gt; |  | Each item assigns an FMOD event to a chassis function, using the "*sound_name\|sound_path*" [format](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories). *Added in 1.39* Expected sound event names are: air_brake, air_cutoff, reverse, lift_axle, hook_attach, hook_detach, and trailer_cables. |
| lamp_setup | string |  | Paths to the special headlight setup if default is not good enough. *Added in 1.40* **Content of vehicle_lamp_setup unit is an experimental feature and will most probably change in the future!** |
| animation | array<owner_ptr> |  | Each member points to the unit name of a [vehicle_animation_data](vehicle%20animation%20data.md) unit. *Added in 1.61* |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_chassis_data | revision: 5810 | captured: 2026-10-21 23:56:14 -->
