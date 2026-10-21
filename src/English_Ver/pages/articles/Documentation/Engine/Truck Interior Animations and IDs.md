# Documentation/Engine/Truck Interior Animations and IDs

## Interior Animations

The movement of various things in the truck interior is controlled by program-driven animations ( ***_anim** ). For each animation, the range is set by the ***_anim_min** and ***_anim_max** values. As most animations expect a range from 0 to 1, these are also the default values. If an animation expects any other value range, it will be stated below.

### Special Animations

| Attribute Name | Function | Behavior | Notes |
| --- | --- | --- | --- |
| wheel_anim | Steering wheel | 0 - left full lock<br>0.5 - center<br>1 - right full lock | *(Obsolete in 1.42)*<br><br>For best results, each keyframe should be less than 45°<br>The steering wheel bone should be named **steering_w** for compatibility with [interchangeable steering wheels](../../Games/ETS2/Modding%20guides/1.25.md#Steering_wheel_accessory). |
| wheel_updown_anim | Steering column tilt adjustment | 0 - lowest setting<br>1 - highest setting | The default position is set by **wheel_updown_anim_default** |
| wheel_frontback_anim | Steering column telescope adjustment | 0 - fully retracted<br>1 - fully extended | The default position is set by **wheel_frontback_anim_default** |
| wiper_anim | Windshield wipers | 0→1 is a full wipe cycle<br>(from park to full travel and back to park) | The keyframes at 0 and 1 should match. |
| rear_wiper_anim | Rear windshield wipers | 0→1 is a full wipe cycle<br>(from park to full travel and back to park) | The keyframes at 0 and 1 should match. *Added in 1.61* |
| gadget_anim |  | 0→1 is a full animation cycle<br>(animation will be played as a continuous loop) | This animation is played in a loop while the truck's ignition/electricity is on. |
| left_window_anim | Left window up/down animation | 0 - closed<br>1 - open | Controlled with window up/down controls. |
| right_window_anim | Right window up/down animation | 0 - closed<br>1 - open | Controlled with window up/down controls. |

### Stick Animations

<table class="wikitable">
<tbody><tr>
<th>Attribute Name
</th>
<th>Function
</th>
<th>Behavior
</th>
<th>Notes
</th></tr>
<tr>
<td>blinker_anim
</td>
<td>Turn signal control lever
</td>
<td>0 - left indicator active<br/>0.5 - rest position<br/>1 - right indicator active
</td>
<td>
</td></tr>
<tr>
<td>lights_anim
</td>
<td>Headlight control
</td>
<td>0 - lights off<br/>0.5 - parking/clearance lights on<br/>1 - headlights on
</td>
<td>
</td></tr>
<tr>
<td>high_beam_anim
</td>
<td>High beam headlight control
</td>
<td>0 - rest position<br/>1 - high beams on
</td>
<td>
</td></tr>
<tr>
<td>light_horn_stick_anim
</td>
<td>Light/city horn button
</td>
<td>0 - rest position<br/>1 - light horn being applied
</td>
<td>
</td></tr>
<tr>
<td>wiper_stick_anim
</td>
<td>Windshield wiper control
</td>
<td>0 - off<br/>1 - maximum speed
</td>
<td>This animation is interpolated based on the total number of wiper speeds. For example, if there are two additional wiper speeds (delays), 0.33 would correspond with the first and 0.67 with the second delay definition.
</td></tr>
<tr>
<td rowspan="2">parking_stick_anim
</td>
<td rowspan="2">Parking brake control
</td>
<td rowspan="2">0 - parking brake released<br/>1 - parking brake applied
</td>
<td><b>North America:</b> Whether 'in' or 'out' is the applied state will depend on the truck – make sure that the animation matches the label on the valve or you will look like a goof.
<p>The typical usage is for 'push to release' systems where the 0.0 state is 'in' and the 1.0 state is 'out'.
</p>
</td></tr>
<tr>
<td><b>Europe:</b>
</td></tr>
<tr>
<td>parking_stick_electric_anim
</td>
<td>Parking brake control
</td>
<td>0 - parking brake releasing<br/>0.5 - parking brake mid/neutral/return position<br/>1 - parking brake application
</td>
<td>Electronic version of parking brake. It is clicked to some position and then returns automatically to default position (games handles return procedurally).
</td></tr>
<tr>
<td>parking_stick_handbrake_anim
</td>
<td>Handbrake control
</td>
<td>0 - handbrake disengaged<br/>0.5 - handbrake engaged<br/>1 - handbrake disengaged
</td>
<td>Handbrake version of parking brake. Plays the first half when engaging the handbrake and the second half when disengaging handbrake. Keyframe at time 0.0 and 1.0 should be the same. <i>Added in 1.61</i>
</td></tr>
<tr>
<td>flasher_4way_anim
</td>
<td>Four-way flasher (hazard light) control
</td>
<td>0 - rest position<br/>1 - hazard lights are active
</td>
<td>For a button, the “depressed” state would be 0.5 to make the button press and rebound for both activation and deactivation
</td></tr>
<tr>
<td>engine_start_anim
</td>
<td>Ignition and starting controls
</td>
<td>0 - off<br/>0.33 - electricity on<br/>0.67 - engine on<br/>1 - engine starting
</td>
<td>
</td></tr>
<tr>
<td>beacon_anim
</td>
<td>Beacon on/off switch
</td>
<td>0 - beacon off
<p>1 - beacon on
</p>
</td></tr>
<tr>
<td>trailer_air_stick_anim
</td>
<td>Trailer air supply valve
</td>
<td>0 - trailer disconnected
<p>1 - trailer connected
</p>
</td>
<td>This is directly tied to whether a trailer is connected to the truck or not.
<p>Typical usage is for a 'push to supply' type, so the valve is 'out' in the 0.0 state and 'in' in the 1.0 state
</p>
</td></tr>
<tr>
<td>trailer_air_stick_electric_anim
</td>
<td>Trailer air supply valve
</td>
<td>0 - trailer disconnecting<br/>0.5 - trailer air mid/neutral/return position<br/>1 - trailer connecting
</td>
<td>Electronic version of trailer air supply. It is clicked to some position and then returns automatically to default position (games handles return procedurally).
</td></tr>
<tr>
<td>trailer_brake_stick_anim
</td>
<td>Trailer brake hand valve
<p>(sometimes called the 'spike')
</p>
</td>
<td>0 - rest position
<p>1 - trailer brake hand valve fully applied
</p>
</td>
<td>Do not confuse this with the trailer supply valve - the hand valve is used (rarely) to apply only the trailer brakes in a controlled manner
</td></tr>
<tr>
<td>retarder_stick_anim
</td>
<td>Retarder control
</td>
<td>0 - off
<p>1 - maximum setting
</p>
</td>
<td>
</td></tr>
<tr>
<td>engine_brake_stick_anim
</td>
<td>Engine brake control
</td>
<td>0 - off
<p>1 - maximum setting
</p>
</td>
<td><i>Added in 1.38</i>
</td></tr>
<tr>
<td>auto_transmission_stick_anim
</td>
<td>Automatic transmission gear selector
</td>
<td>0 - reverse<br/>0.5 - neutral<br/>1 - drive
</td>
<td>
</td></tr>
<tr>
<td>lift_axle_stick_anim
</td>
<td>Lift axle switch/control
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td>differential_lock_stick_anim
</td>
<td>Differential lock switch/control
</td>
<td>0 - disengaged<br/>1 - engaged
</td>
<td><i>Added in ETS2 1.27/ATS 1.6</i>
</td></tr>
<tr>
<td>left_window_stick_anim
</td>
<td>Left window switch/control
</td>
<td>0 - closing<br/>0.5 - rest position<br/>1 - opening
</td>
<td>
</td></tr>
<tr>
<td>right_window_stick_anim
</td>
<td>Right window switch/control
</td>
<td>0 - closing<br/>0.5 - rest position<br/>1 - opening
</td>
<td>
</td></tr>
<tr>
<td>left_window_stick_manual_anim
</td>
<td>Left window manual control
</td>
<td>0 - window closed<br/>1 - window opened
</td>
<td>Plays from 0 to 1 while the window anim is playing, allows lowering the windows without engine electrics. <i>Added in 1.61</i>
</td></tr>
<tr>
<td>right_window_stick_manual_anim
</td>
<td>Right window manual control
</td>
<td>0 - window closed<br/>1 - window opened
</td>
<td>Plays from 0 to 1 while the window anim is playing, allows lowering the windows without engine electrics. <i>Added in 1.61</i>
</td></tr></tbody></table>

### Gauge animations

This set of animations handles analog gauges. The related ***_min** and ***_max** attributes set the values that the start and end of the animation correspond to. Where the simulated value exceeds the min/max attribute, the animation is clamped.

> **Note:** All ***_psi_*** attributes have been renamed to ***_pressure_*** as of ETS2 1.27/ATS 1.6. This is to reflect the change to *bar* (atmospheres) as the working pressure unit instead of *psi*.

| Attribute Name | Function | Behavior | Notes |
| --- | --- | --- | --- |
| oil_pressure_anim | Engine oil pressure (bar) | 0 - oil_pressure_anim_min 1 - oil_pressure_anim_max | 3-6 bars (43.5-87 psi) is typical working value |
| water_temp_anim | Engine water/coolant temperature (°C) | 0 - water_temp_anim_min 1 - water_temp_anim_max | working value 90°C |
| battery_anim | Battery potential (V) | 0 - battery_anim_min 1 - battery_anim_max | Nominally 24V. For 12V systems, set the min/max attributes to twice the value the gauge displays and it should appear as if it is indeed a 12V system. |
| oil_temp_anim | Engine oil temperature (°C) | 0 - oil_temp_anim_min 1 - oil_temp_anim_max | working value 90°C |
| exhaust_temp_anim | Exhaust gas temperature (°C) | 0 - exhaust_temp_anim_min 1 - exhaust_temp_anim_max | working range cca to 650°C |
| diff_temp_anim | Differential temperature (°C) | 0 - diff_temp_anim_min 1 - diff_temp_anim_max | working value 90°C |
| tachometer_anim | Tachometer in rpm (revolution per minute) | 0 - tachometer_anim_min 1 - tachometer_anim_max |  |
| speedometer_anim | Speedometer (km/h) | 0 - speedometer_anim_min 1 - speedometer_anim_max | 1mph = 1.60934km/h |
| air_pressure_anim | Air brake reservoir pressure (bar) | 0 - air_pressure_anim_min 1 - air_pressure_anim_max |  |
| brake_pressure_anim | Air brake application (bar) | 0 - brake_pressure_anim_min 1 - brake_pressure_anim_max |  |
| general_air_press_anim | General air supply (bar) | 0 - general_air_press_anim_min 1 - general_air_press_anim_max |  |
| trailer_air_press_anim | Trailer air supply (bar) | 0 - trailer_air_press_anim_min 1 - trailer_air_press_anim_max |  |
| suspension_load_anim | Suspension load (newtons) | 0 - suspension_load_anim_min 1 - suspension_load_anim_max | expects range in newtons (22t trailer creates like 70kN on kingpin) |
| fuel_anim | Fuel gauge (relative to full) | 0 - fuel_anim_min 1 - fuel_anim_max | By default, 0 corresponds to empty state and 1 corresponds to full |
| ad_blue_anim | Ad Blue/DEF gauge (relative to full) | 0 - fuel_anim_min 1 - fuel_anim_max | By default, 0 corresponds to empty state and 1 corresponds to full |
| turbo_anim | Manifold pressure |  |  |
| consumption_anim | Instantaneous fuel consumption in l/100km | 0 - consumption_anim_min 1 - consumption_anim_max | scania gauge has 0 to 120 |
| clock_big_anim | Analog clock, minute hand (0-60) | 0 - clock_big_anim_min (default 0) 1 - clock_big_anim_max (default 60) |  |
| clock_small_anim | Analog clock, hour hand (0-12) | 0 - clock_small_anim_min (default 0) 1 - clock_small_anim_max (default 24) |  |
| generic_anim | Animation for other gauges. | 0 when truck is turned off 1 when truck is turned on |  |
| odometer_digit_0_anim<br> odometer_digit_1_anim<br> odometer_digit_2_anim<br> odometer_digit_3_anim<br> odometer_digit_4_anim<br> odometer_digit_5_anim<br> odometer_digit_6_anim<br> odometer_digit_7_anim | Analog odometer animations | Each anim has 10 keyframes 1 keyframe for each number 0-9 | Digit 0 shows the tenths, digit 1 shows ones, digit 2 shows tens, ..., digit 7 shows millions. Digit 1 is required for the odometer to function, other digits are optional. Distance unit shown (km or m) is controlled by **use_mile_units** in **accessory_interior_data**. *Added in 1.61* |
| trip_counter_digit_0_anim<br> trip_counter_digit_1_anim<br> trip_counter_digit_2_anim<br> trip_counter_digit_3_anim | Analog trip counter animations | Each anim has 10 keyframes 1 keyframe for each number 0-9 | Digit 0 shows the tenths, digit 1 shows ones, digit 2 shows tens, digit 3 shows hundreds. Digit 1 is required for the trip counter to function, other digits are optional. Distance unit shown (km or m) is controlled by **use_mile_units** in **accessory_interior_data**. *Added in 1.61* |

### Indicator animations

These animations are not interpolated from 0 to 1. Instead they have only 2 states: switched off (0) and switched on (1), so these animations should have only 2 key frames. All indicator animations are triggered during the start-up electrical check, as well as for their particular functions.

<table class="wikitable">
<tbody><tr>
<th>Attribute Name
</th>
<th>Function
</th>
<th>Behavior
</th>
<th>Notes
</th></tr>
<tr>
<td>button_left_blinker
</td>
<td>Left turn signal indicator
</td>
<td rowspan="2">Flashes on and off with left/right turn signal
</td>
<td rowspan="2">The related attribute <b>blinker_delay</b> is describing length of the half blinking loop (in seconds)
</td></tr>
<tr>
<td>button_right_blinker
</td>
<td>Right turn signal indicator
</td></tr>
<tr>
<td>button_water_temp
</td>
<td>Water temperature warning light
</td>
<td>On when engine temperature is excessive
</td>
<td>
</td></tr>
<tr>
<td>indicator_oil_temp
</td>
<td>Engine oil temperature warning light
</td>
<td>On when engine oil temperature is excessive
</td>
<td>
</td></tr>
<tr>
<td>indicator_position_lights
</td>
<td>Position light indicator
</td>
<td>On when positional/marker/parking lights are on
</td>
<td>
</td></tr>
<tr>
<td>button_lights
</td>
<td>Headlight indicator
</td>
<td>On when headlights are on
</td>
<td>
</td></tr>
<tr>
<td>button_high_beam_lights
</td>
<td>Highbeam indicator
</td>
<td>On when highbeam headlights are on
</td>
<td>
</td></tr>
<tr>
<td>indicator_aux_lights_front
</td>
<td>Front auxiliary lights indicator
</td>
<td>On when <i>front</i> auxiliary lights are on
</td>
<td>
</td></tr>
<tr>
<td>indicator_aux_lights_roof
</td>
<td>Roof auxiliary lights indicator
</td>
<td>On when <i>roof</i> auxiliary lights are on
</td>
<td>
</td></tr>
<tr>
<td>indicator_aux_lights_any
</td>
<td>Auxiliary lights indicator
</td>
<td>On when any auxiliary lights are on
</td>
<td>
</td></tr>
<tr>
<td>indicator_low_air_pressure
</td>
<td>Low air pressure warning light
</td>
<td>On when air pressure drops below cca 5 bars
</td>
<td>
</td></tr>
<tr>
<td>indicator_low_oil_pressure
</td>
<td>Low oil pressure warning light
</td>
<td>On when engine oil pressure is low
</td>
<td>This will also illuminate when the electrical is on and the engine is off
</td></tr>
<tr>
<td>button_battery_warning
</td>
<td>Low battery voltage warning light
</td>
<td>On when battery voltage is low
</td>
<td>
</td></tr>
<tr>
<td>button_low_fuel
</td>
<td>Low fuel warning light
</td>
<td>On when fuel level is low
</td>
<td>
</td></tr>
<tr>
<td>indicator_low_adblue
</td>
<td>Low AdBlue/DEF warning light
</td>
<td>On when AdBlue/DEF level is low
</td>
<td>
</td></tr>
<tr>
<td>button_jakebrake
</td>
<td>Engine brake indicator light
</td>
<td>On when engine brake (jake brake) is armed or active
</td>
<td>
</td></tr>
<tr>
<td>button_parking_brake
</td>
<td>Parking brake indicator light
</td>
<td>On when parking brake is applied
</td>
<td>
</td></tr>
<tr>
<td>button_4way
</td>
<td>Four-way flasher status light
</td>
<td>On when four-way flasher is on
</td>
<td>Indicator should be placed on hazard warning button for blinking
</td></tr>
<tr>
<td>indicator_retarder
</td>
<td>Retarder status light
</td>
<td>On when the retarder is active
</td>
<td>
</td></tr>
<tr>
<td>indicator_warning
</td>
<td>Damage warning indicator
</td>
<td>On when damage is 15% or more
</td>
<td>
</td></tr>
<tr>
<td>indicator_stop
</td>
<td>Critical damage indicator
</td>
<td>On when damage is 50% or more
</td>
<td>
</td></tr>
<tr>
<td>indicator_axle_lift
</td>
<td>Lift axle indicator
</td>
<td>On when lift axle is up
</td>
<td>
</td></tr>
<tr>
<td>indicator_cruise_control
</td>
<td>Cruise control status light
</td>
<td>On when cruise control is engaged
</td>
<td>
</td></tr>
<tr>
<td>indicator_generic
</td>
<td>Animation for other indicators
</td>
<td>0 most of the time, 1 when truck is making electricity check (after turned on).
</td>
<td>
</td></tr>
<tr>
<td>indicator_differential_lock
</td>
<td>Differential lock status light
</td>
<td>On when differential lock is engaged
</td>
<td><i>Added in ETS2 1.27/ATS 1.6</i>
</td></tr>
<tr>
<td>indicator_trailer_axle_lift
</td>
<td>Trailer lift axle status light
</td>
<td>On when trailer axle(s) are raised.
</td>
<td><i>Added in ETS2 1.27/ATS 1.6</i>
</td></tr>
<tr>
<td>indicator_weigh_green
</td>
<td>(ATS) Weigh pass transponder green (bypass) light
</td>
<td>On when the player may bypass an upcoming weigh station
</td>
<td><i>Added in ETS2 1.27/ATS 1.6</i>
</td></tr>
<tr>
<td>indicator_weigh_red
</td>
<td>(ATS) Weigh pass transponder red (no bypass) light
</td>
<td>On when the player must enter an upcoming weigh station
</td>
<td><i>Added in ETS2 1.27/ATS 1.6</i>
</td></tr>
<tr>
<td>indicator_blind_spot_left
</td>
<td>Left blind spot indicator
</td>
<td>On when some vehicle is near left blind spot of player vehicle
</td>
<td><i>Added in ETS2 1.47/ATS 1.45</i>
</td></tr>
<tr>
<td>indicator_blind_spot_right
</td>
<td>Right blind spot indicator
</td>
<td>On when some vehicle is near right blind spot of player vehicle
</td>
<td><i>Added in ETS2 1.47/ATS 1.45</i>
</td></tr></tbody></table>

## Dashboards IDs

Screen of dashboard computers uses our UI library and shows thus UI elements. Each element has unique ID and can be used only once (due to caching). Most of fields can be used as two parameter template - value and unit, both are used accordingly to current game options. As in different languages can be units and other texts translated ensure that there are enough space for all of them.

### Screen IDs ( **ui::group** type):

- 100 to 800 - basic screens, up to 8 screens
- 900 - warning screen, used when truck is damage and should be repaired, shown alone (without shared screen)
- 910 to 913 - parking cameras screens, up to 4 screens (enabled when driving in R and/or user activates parking cameras)
- 950 - shared screen (used together with all basic screens)

### Element IDs (mostly **ui::text_common** type):

- 1000 - ambient temperature
- 1010 - oil temperature
- 1020 - current speed
- 1030 - odometer, needs space for at least six digits
- 1040 - current gear, uses N, A[number], R or R[number] for automatic and N, [number], R or R[number] for manual or sequential
- 1050 - current clock time in proper format, eg. "12:34" (am/pm is omitted)
- 1060 - remaining fuel in tank
- 1070 - ui_text_bar for fuel bar, the text is cut according to current fuel tank state
- 1075 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of fuel bar (typical data "H~~0~~1", horizontal range 0 to 1)
- 1080 - guessed operating range of vehicle
- 1090 - water temperature
- 1100 - cruise control speed value
- 1110 - ui_text_bar for oil pressure bar, the text is cut according to current oil pressure
- 1115 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of oil pressure bar (typical data "H~~0~~8", horizontal range 0bar to 8bar (116psi))
- 1120 - ui_text_bar for air pressure bar, the text is cut according to current air pressure
- 1125 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of air pressure bar (typical data "H~~0~~12", horizontal range 0bar to 12bar (174psi))
- 1130 - ui_text_bar for turbo pressure bar, the text is cut according to current oil pressure
- 1135 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of turbo pressure bar (typical data "H~~0~~1", horizontal range 0 to 1)
- 1140 - ui_text_bar for adblue bar, the text is cut according to current adblue tank state
- 1145 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of adblue bar (typical data "H~~0~~1", horizontal range 0 to 1)
- 1150 - ui_text_bar for water temperature bar, the text is cut according to current water temperature
- 1155 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of water temperature bar (typical data "H~~0~~130", horizontal range 0°C to 130°C (32°F to 266°F))
- 1160 - instant consumption
- 1170 - average (trip) consumption
- 1180 - ui_text_bar for brake pedal pressure bar, the text is cut according to current pressure
- 1185 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of brake pedal pressure bar (typical data "H~~0~~1", horizontal range 0 to 1)
- 1190 - damage warning icon, can be ui::group or ui::text or any other element that could show/hide
- 1200 - low fuel warning icon, can be ui::group or ui::text or any other element that could show/hide
- 1210 - trip distance
- 1220 - compass, displays strings like "N", "E", "SW".
- 1230 - engine brake icon
- 1240 - cruise control icon, can be ui::group or ui::text or any other element that could show/hide. Cruise control speed (id 1100) explicitly CAN be child of this group.
- 1250 - cruise control memory icon, can be ui::group or ui::text or any other element that could show/hide.
- 1260 - low air pressure warning icon
- 1270 - parking brake indicator icon
- 1280 - engine running time
- 1290 - retarder icon
- 1300 - transmission gear (raw, without mode info)
- 1310 - transmission mode (without gear info, A/M)
- 1320 - battery voltage
- 1330 - battery voltage gauge, expected to be ui_gauge element type
- 1340 - oil temperature gauge, expected to be ui_gauge element type
- 1350 - ui_text_bar for instant fuel economy bar, the text is cut according to current value
- 1355 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of instant fuel economy bar (typical data "H~~0~~5", horizontal range 0 to 5 km/l (11.8mpg))
- 1360 - ui_text_bar for average fuel economy bar, the text is cut according to current value
- 1365 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of average fuel economy bar (typical data "H~~0~~5", horizontal range 0 to 5 km/l (11.8mpg))
- 1370 - air pressure value (psi only)
- 1380 - transmission mode, detailed (D/N/R/M)
- 1390 - trip time
- 1400 - trip average speed (trip distance / trip time)
- 1410 - smart cruise control tolerance if CC is engaged, otherwise hides the element
- 1420 - damage stop icon, can be ui::group or ui::text or any other element that could show/hide
- 1430 - speed gauge, expected to be ui_gauge element type
- 1440 - revolutions per minute (rpm) gauge, expected to be ui_gauge element type
- 1450 - cruise control speed gauge, expected to be ui_gauge element type
- 1460 - water temperature gauge, expected to be ui_gauge element type
- 1470 - parking lights icon, can be ui::group or ui::text or any other element that could show/hide
- 1480 - low beam lights icon, can be ui::group or ui::text or any other element that could show/hide
- 1490 - differential lock icon, can be ui::group or ui::text or any other element that could show/hide
- 1500 - fuel consumed since last trip computer reset
- 1510 - remaining fuel in tank percent (range 0-100)
- 1520 - remaining adblue in tank percent (range 0-100)
- 1530 - ETA (estimated time to arrival), hidden when time is not available (no delivery, no navigation etc.)
- 1540 - time until rest is needed, hidden when g_fatigue is 0 (fatigue option is disabled)
- 1550 - ui_text_bar for differential temperature bar, the text is cut according to current value
- 1555 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of differential temperature bar (typical data "H~~0~~130", horizontal range 0°C to 130°C (32°F to 266°F))
- 1560 - ui_text_bar for suspension load bar, the text is cut according to current value
- 1565 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of suspension load bar (typical data "H~~0~~100000", horizontal range 0 to 100kN)
- 1570 - left blinker icon
- 1580 - right blinker icon
- 1590 - high beam icon
- 1600 - ui_text_bar for oil temperature bar, the text is cut according to current value
- 1605 - *(obsolete in 1.49)* ui::text that defines size, orientation and range of oil temperature bar (typical data "H~~0~~130", horizontal range 0°C to 130°C (32°F to 266°F))
- 1610 - speed limit
- 1620 - digital main mirrors, can be any element that can show/hide (shown when digital main mirrors are detected by the main mirrors using camera unit prefix)
- 1630 - digital side mirror, can be any element that can show/hide (shown when digital side mirror is detected by the side mirror using camera unit prefix)
- 1640 - digital front mirror, can be any element that can show/hide (shown when digital front mirror is detected by the front mirror using camera unit prefix)
- 1650 - digital hood mirrors, can be any element that can show/hide (shown when digital hood mirror is detected by the hood mirror using camera unit prefix)
- 1660 - close blind spot indicator (side depends on `left_hand_traffic` interior data attribute), can be any element that can show/hide (shown when obstacle is detected on left side of the vehicle)
- 1670 - far blind spot indicator (side depends on `left_hand_traffic` interior data attribute), can be any element that can show/hide (shown when obstacle is detected on right side of the vehicle)
- 1680 - trip recuperation (energy returned)
- 1690 - ui_text_bar for power consumption, the text is cut according to current value (specific behavior based on Renaut E-Tech)
- 1700 - ui_text_bar for rpm, the text is cut according to current value (values in RPM)
- 1710 - ui_text_bar for speed, the text is cut according to current value (values in km/h)
- 1720 - power consumption gauge, expected to be ui_gauge element type (max recuperation: -1, idle: 0, max power: 1)
- 1730 - engine RPM divided by 1000 (rounded to one decimal place)
- 1740 - fuel gauge, expected to be ui_gauge element type (empty fuel: 0, max. fuel: 1)
- 1750 - average (trip) consumption gauge, expected to be ui_gauge element type (value in l/100km)
- 1760 - oil pressure value

> **Note:** In 1.49 text bars were changed to ui_text_bar element. No additional data is needed now, all is kept in regular members (vertical, min_size, max_size, min_value, max_value).
>
> Old system (pre 1.49) used secondary text fields. Data for bars were entered in format "H~~0~~130", H means the bar is horizontal (or V for vertical), leftmost position represents value 0, rightmost position represents value 130. Empty text defaults to "H~~0~~1".

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Truck_Interior_Animations_and_IDs | revision: 5808 | captured: 2026-10-21 23:56:14 -->
