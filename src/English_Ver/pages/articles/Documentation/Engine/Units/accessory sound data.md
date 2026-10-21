# Documentation/Engine/Units/accessory sound data

The **accessory_sound_data** unit class is used to define sounds for the [player's vehicle](../Game%20data/Player%20trucks%20definitions.md). Units of this type are typically found in **/def/vehicle/truck/<brand.model>/sound/&lt;type&gt;/*.sii**. They are mostly comprised of pointers to [sound_data](sound%20data.md), [sound_engine_data](sound%20engine%20data.md), and [sound_noise_data](sound%20noise%20data.md) units which may be defined in-line or [included](../Units.md#Includes) from other sources. A valid truck configuration will contain two sound accessories: one for exterior sounds and one for interior sounds. The names for these units always end with `.esound` for exterior sounds and `.isound` for interior sounds.

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md). Attributes marked *common* are typically defined by including `/def/vehicle/truck/common_sound_ext.sui` or `common_sound_int.sui` within the accessory_sound_data unit definition, and `/def/vehicle/truck/common_sound_ext_data.sui` or `common_sound_int_data.sui` within the SiiNunit.

| Name | [Type](../Units.md#Attribute_types) | Default Value | Common? | Description |
| --- | --- | --- | --- | --- |
| exterior_sound | bool | false | No | Defines whether the unit contains exterior sounds (true) or interior sounds (false). |
| start | owner_ptr |  | No | Points to a **sound_data** unit which defines the sound to play when the engine is starting. |
| start_no_fuel | owner_ptr |  | No | Points to a **sound_data** unit which defines the sound to play when the player attempts to start the engine with no fuel. |
| stop | owner_ptr |  | No | Points to a **sound_data** unit which defines the sound to play when the engine is stopped. |
| engine | array<owner_ptr> |  | No | Each array member points to a **sound_engine_data** unit which collectively define the engine's sound with no load (e.g. idle, cruising, gentle acceleration, etc). |
| engine_load | array<owner_ptr> |  | No | Each array member points to a **sound_engine_data** unit which collectively define the engine's sound under load (e.g. heavy acceleration, climbing a hill, etc). |
| engine_nofuel | array<owner_ptr> |  | No | Each array member points to a **sound_engine_data** unit which collectively define the engine's sound when fuel has been cut (e.g. coasting in gear, speed limiter, etc). |
| engine_exhaust | array<owner_ptr> |  | No | Each array member points to a **sound_engine_data** unit which collectively define the resonant sound of the truck's exhaust. |
| engine_brake | array<owner_ptr> |  | No | Each array member points to a **sound_engine_data** unit which collectively define the engine's sound while using the engine brake. |
| turbo | owner_ptr |  | No | Points to a **sound_data** unit which defines the sound of the turbocharger. |
| retarder | owner_ptr |  | **Yes** | Points to a **sound_data** unit which defines the sound of the retarder. |
| air_gear | array<owner_ptr> |  | No | Each member points to a **sound_data** unit defining one of the gear change sounds. Sounds are played randomly during gear change. |
| air_brake | array<owner_ptr> |  | No | Each member points to a **sound_data** unit defining one of the air brake sounds. Sounds are played randomly when the service brake is released. |
| air_cutoff | array<owner_ptr> |  | **Yes** | Each member points to a **sound_data** unit defining a sound to be played when the air compressor is unloaded by the governor. |
| wheel_asphalt | array<owner_ptr> |  | **Yes** | Each member points to a **sound_noise_data** unit collectively defining the sound to be played when the truck is driving on asphalt. |
| wheel_rumble | array<owner_ptr> |  | **Yes** | Each member points to a **sound_noise_data** unit collectively defining the sound to be played when the truck is driving on a rumble strip. |
| wheel_gravel | array<owner_ptr> |  | **Yes** | Each member points to a **sound_noise_data** unit collectively defining the sound to be played when the truck is driving on gravel. |
| wheel_grass | array<owner_ptr> |  | **Yes** | Each member points to a **sound_noise_data** unit collectively defining the sound to be played when the truck is driving on grass. |
| aero_noise | owner_ptr |  | **Yes** | Points to a **sound_noise_data** unit defining the aerodynamic sound of the truck. |
| gear_noise | array<owner_ptr> |  | **Yes** | Each member points to a **sound_data** unit defining the sound of the gears when damaged. |
| gear_grind_loop | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the the sound to be looped when the gear the player is trying to activate won't mesh (e.g. input shaft speed doesn't match or the player hasn't used the clutch correctly). |
| seat_noise_threshold | float |  | **Yes** | Defines the minimum acceleration (m/s<sup>2</sup>) to generate noise from the seat suspension. |
| seat_noise | array<owner_ptr> |  | **Yes** |  |
| suspension_noise_threshold | float |  | **Yes** | Defines the minimum acceleration (m/s<sup>2</sup>) to generate noise from the truck's suspension. |
| suspension_noise | array<owner_ptr> |  | **Yes** |  |
| lift_axle | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound to be played when the truck's lift axles (if any) are raised or lowered. |
| horn | owner_ptr |  | No | Points to a **sound_data** unit defining the sound for the truck's electric/city horn. |
| air_horn | owner_ptr |  | No | Points to a **sound_data** unit defining the default sound for the truck's air horn. This is overridden by any hookup accessory horns. If unset, the truck will not have an air horn without the presence of hookup accessory horns. |
| reverse | owner_ptr |  | No | Points to a **sound_data** unit defining the sound for the truck's reverse beeper. |
| air_warning | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound for the truck's audible low air warning. |
| crash_metal | array<owner_ptr> |  | **Yes** | Each member points to a **sound_data** unit collectively defining sounds for collisions at 60-90 km/h. |
| crash_hard | array<owner_ptr> |  | **Yes** | Each member points to a **sound_data** unit collectively defining sounds for collisions at 30-59 km/h. |
| crash_soft | array<owner_ptr> |  | **Yes** | Each member points to a **sound_data** unit collectively defining sounds for collisions at 6-29 km/h. |
| crash_scratch | array<owner_ptr> |  | **Yes** | Each member points to a **sound_data** unit collectively defining looped sounds for scraping collisions. |
| blinker_on | owner_ptr |  | No | Points to a **sound_data** unit defining the sound of the blinker relay closing. |
| blinker_off | owner_ptr |  | No | Points to a **sound_data** unit defining the sound of the blinker relay opening. |
| wipers_up | owner_ptr |  | No | Points to a **sound_data** unit defining the sound of the wiper(s) traveling from the park position to the extended position. |
| wipers_down | owner_ptr |  | No | Points to a **sound_data** unit defining the sound of the wiper(s) traveling from the extended position to the park position. |
| lights_stick | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound of the headlight control being moved. |
| high_beam_stick | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound of the high beam switch being activated. |
| light_horn_stick | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound of the electric/city horn being activated. |
| blinker_stick | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound of the blinker lever being activated. |
| blinker_stick_off | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound of the blinker lever being deactivated. |
| hazard_warning_stick | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound of the hazard/four-way flasher control being activated. |
| wipers_stick | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound of the wiper control being activated. |
| retarder_stick | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound of the retarder control being activated. |
| park_brake_stick | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound of the parking brake being engaged. |
| park_brake_stick_off | owner_ptr |  | **Yes** | Points to a **sound_data** unit defining the sound of the parking brake being disengaged. |

## Related Units

- [sound_data](sound%20data.md)
- [sound_engine_data](sound%20engine%20data.md)
- [sound_noise_data](sound%20noise%20data.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_sound_data | revision: 3325 | captured: 2026-10-21 23:56:14 -->
