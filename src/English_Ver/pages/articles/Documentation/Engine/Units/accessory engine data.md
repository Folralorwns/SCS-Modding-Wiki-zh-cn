# Documentation/Engine/Units/accessory engine data

The **accessory_engine_data** unit class is used to define the engine characteristics for the [player's vehicle](../Game%20data/Player%20trucks%20definitions.md), as well as some upshift and downshift characteristics for automatic transmission gameplay. Units of this type are usually defined in **/def/vehicle/truck/<brand.model>/engine/*.sii**

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md).

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| info | array&lt;string&gt; |  | This member is attribute of accessory data, however three **info** members are usually defined for **accessory_engine_data**. info[]: "197 @@hp@@ (147@@kw@@)" // The first is the rated power info[]: "550 @@lb_ft@@ (782 @@nm@@)" // The second is the peak torque info[]: "1@@dg@@200 @@rpm@@" // The third is the peak torque speed **Note:** The info attribute has no effect on the engine simulation. Rather, it is used for UI display and for attaching to World of Trucks profile truck uploads. **TIP:** The strings surrounded by *@* are for localization — `@@hp@@` displays the localized shorthand for horsepower, `@@dg@@` displays the localized thousands separator, etc. |
| type | token | diesel | This defines type and behavior of engine, powertrain, and few other aspects of the vehicle. Acceptable values are **diesel**, **electric**, or **petrol**. Any other (or unset) value defaults to **diesel**. *(Added in 1.50, petrol added in 1.61)* |
| engine_aspiration | token | turbocharger | Type of engine aspiration. Acceptable values are **natural**, **turbocharger**, or **supercharger**. Ignored (forced to **natural**) for **electric** engines. |
| torque | float | 0.0 | This defines the maximum torque output of the engine in N·m. |
| secondary_torque | float | 0.0 | If positive and greater than zero, this defines the secondary maximum torque output of the engine in N·m for multi-torque engines. *(Added in 1.30)* |
| secondary_torque_gear_ratio | float | 1.0 | This defines the transmission gear ratio below which **secondary_torque** is used on multi-torque engines. *(Added in 1.30)* |
| torque_curve | array&lt;float2&gt; | *See description* | This defines the torque output of the engine at various engine speeds, relative to the maximum torque defined in **torque**. If unset, the default curve is used: torque_curve[]: (300, 0) torque_curve[]: (440, 0.5) torque_curve[]: (1000, 1) torque_curve[]: (1300, 1) torque_curve[]: (1900, 0.77) torque_curve[]: (2400, 0.4) torque_curve[]: (2600, 0) The torque output is linearly interpolated between data points. For engine speeds outside the domain of the data points, the output is clamped to the values at the highest/lowest rpm points. The valid range for torque output is 0-1. |
| secondary_torque_curve | array&lt;float2&gt; | *See description* | This defines the secondary torque output of a multi-torque engine at various engine speeds, relative to the maximum torque defined in **secondary_torque**. If unset, **torque_curve** is used instead. The syntax is the same as **torque_curve**. *(Added in 1.30)* |
| power | float | 0 | This is simplified definition value. It is used only for **electric** engines and when the **torque_curve** is not defined. The **torque_curve** is then generated to create nominal torque from 0 rpm to the point when engine output reaches given **power**. At higher rpm the torque is gradually lowered to keep output at given **power** up to the maximum rpm. *(Added in 1.60)* |
| secondary_power | float | 0 | This is simplified definition value. It is used only for **electric** engines and when the **secondary_torque_curve** nor **torque_curve** are defined. The **secondary_torque_curve** is then generated to create nominal torque from 0 rpm to the point when enigne reaches given **secondary_power**. At higher rpm the torque is gradually lower to keep given **secondary_power** up to the maximum rpm. *(Added in 1.60)* |
| resistance_torque | float | -1 | This is the resistive torque in N·m at 2000rpm, used for passive engine braking and consumption. *(New as of ETS 1.27/ATS 1.6)* **Note:** When unset, or when set to any negative value, resistance_torque is calculated as (*volume* × 20.0). |
| rpm_idle | float | 550 | This is the engine speed the virtual engine controller will attempt to maintain with no throttle input. Valid range is 500-850 rpm. |
| rpm_limit | float | 2500 | This is the maximum engine speed the virtual engine controller will allow except if the engine is being driven by the wheels (e.g. if the vehicle is running away downhill or the player makes an ill-advised downshift). |
| rpm_limit_hysteresis | float | 0.0 | Hysteresis (in RPM) for the **rpm_limit** limiter. When greater than zero, a hard-cut style limiter is used instead of the default soft limiter. Cannot be negative. |
| rpm_limit_neutral | float | 2500 | This is the maximum engine speed the virtual engine controller will allow if the transmission is in neutral – unless **rpm_limit** is lower, in which case it is clamped. |
| rpm_limit_neutral_hysteresis | float | 0.0 | Hysteresis (in RPM) for the **rpm_limit_neutral** limiter. When greater than zero, a hard-cut style limiter is used instead of the default soft limiter. Cannot be negative. |
| rpm_range_low_gear | float2 | (700, 1500) | Defines the downshift and upshift engine speeds in low-range gears (automatic transmission). |
| rpm_range_high_gear | float2 | (1000, 1350) | Defines the downshift and upshift engine speeds in high-range gears - typically peek torque range (automatic transmission). *(Tweaked in 1.38)* |
| rpm_range_power | float2 | (1400, 1900) | Defines the rough rpm range if more power is requested - used either in hills or for adaptive shifting, especially power mode (automatic transmission). *(Added in 1.37, tweaked in 1.38)* |
| *rpm_range_power_boost* | float2 | (550, 450) | *(Obsolete in 1.37)* Defines the rough rpm range *change* to **rpm_range_low_gear** and **rpm_range_high_gear** if more power is requested - used either in hills or for adaptive shifting, especially power mode. (Automatic transmission). **TIP:** Be careful that the resulting values when **rpm_range_power_boost** is added to **rpm_range_*_gear** don't exceed **rpm_limit**. Otherwise, the transmission may fail to shift correctly in adaptive automatic mode. |
| rpm_range_engine_brake | float2 | (1500, 2500) | Defines the downshift and upshift engine speeds while the engine brake is operating. (Automatic transmission) |
| engine_brake | float | 1.0 | Engine braking torque relative to a typical exhaust brake on an engine of the same **volume**. |
| engine_brake_downshift | bool | true | When true, automatic transmissions will downshift upon beginning engine brake behavior, to keep rpm within **rpm_range_engine_brake**. When false, the regular rpm are kept. |
| engine_brake_positions | uint | 3 | Defines the number of strength levels for the engine brake. The braking torque at each position is based linearly on the number of positions. So for `engine_brake_positions: 3` the first position will have <sup>1</sup>⁄<sub>3</sub> of the full strength, the second position will have <sup>2</sup>⁄<sub>3</sub> of the full strength, and the highest position will have the full strength. |
| auxiliary_brakes | array&lt;float3&gt; |  | When set, this overrides the engine brake control so that it controls both the engine brake and retarder (if present). The components are (engine brake strength, forced downshift, retarder strength). The value of **engine_brake_positions** must match the number of members in auxiliary_brakes. (*Added in 1.40*) For example: engine_brake_positions: 5 auxiliary_brakes[]: (0.3, 0, 0) // 30% engine brake only auxiliary_brakes[]: (0.6, 0, 0) // 60% engine brake only auxiliary_brakes[]: (1.0, 0, 0) // 100% engine brake only auxiliary_brakes[]: (1.0, 1, 0) // 100% engine brake and downshift auxiliary_brakes[]: (1.0, 1, 1) // 100% engine brake, downshift and 100% retarder |
| volume | float | 0.0 | The volumetric displacement of the engine in liters. It is used in base fuel consumption calculation, engine mass & inertia calculations, and also default **resistance_torque** calculations. Minimum acceptable engine volume is 0.8. |
| consumption_coef | float | 1.0 | This is used to scale the fuel consumption of the engine relative to the game's calculated value. |
| cold_start_rpm | float | *See description* | The idle RPM of the engine when cold (~20°C). If unset (negative), defaults to **rpm_idle**. Cannot be lower than **rpm_idle**. *(Added in 1.61)* |
| flywheel_inertia | float | *See description* | Inertia of the engine flywheel, in kg·m². If unset (negative), it is estimated from **volume**. *(Added in 1.61)* |
| adblue_consumption | float | 0.05 | This is how many liters of AdBlue (Diesel Exhaust Fluid) are consumed per liter of fuel. **TIP:** For older engines which do not use AdBlue, this attribute should be set to 0. |
| no_adblue_power_limit | float | 1.0 | When the AdBlue tank is empty, the engine's power is scaled by this factor. |
| sound | string |  | Path to the truck [engine sound bank.](../Sound/TruckEngine.md) (format like "/sound/truck/engine.bank"). *(Obsolete, replaced by **sounds**. Removed in 1.39.)* |
| sounds | array&lt;string&gt; |  | Each item assigns an FMOD event to an engine function, using the "*sound_name\|sound_path*" [format](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories). *(Added in 1.39)* Expected sound event names are: engine, exhaust, exhaust_ignite, start_bad, and turbo. |
| sound_location_engine | token | front | Location of the engine sound source relative to the vehicle. Acceptable values are **front** or **rear**; any other value defaults to **front**. |
| sound_location_exhaust | token | front | Location of the exhaust sound source relative to the vehicle. Acceptable values are **front** or **rear**; any other value defaults to **front**. |

## Relevant Unit Conversions and Formulas

### Cubic Inches to Liters

1 cu·in = 0.0164 L

### Pound-Feet to Newton-Meters

1 lb<sub>f</sub>·ft = 1.3558 N·m

### Horsepower to Kilowatts

1 hp = 0.7457 kW

### Torque from Power and Speed (Metric Units)

T [N·m] = ( P [kW] × 9549 ) ÷ N [RPM]

### Torque from Power and Speed (English Units)

T [lb<sub>f</sub>·ft] = ( P [hp] × 5252 ) ÷ N [RPM]

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_engine_data | revision: 5792 | captured: 2026-10-21 23:56:14 -->
