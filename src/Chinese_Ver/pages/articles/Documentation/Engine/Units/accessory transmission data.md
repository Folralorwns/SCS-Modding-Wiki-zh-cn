# Documentation/Engine/Units/accessory transmission data

The **accessory_transmission_data** unit class is used to define the transmission characteristics for the [player's vehicle](../Game%20data/Player%20trucks%20definitions.md), as well as the differential ratio. Units of this type are usually defined in **/def/vehicle/truck/<brand.model>/transmission/*.sii** and valid unit names end in `.transmission`.

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md).

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| stall_torque_ratio | float | -1.0 | Torque ratio multiplier if torque converter/multiplier is present. Any positive value is used as multiplier on lower RPM torque. |
| differential_ratio | float | 1.0 | This defines the differential/final drive ratio between the transmission output shaft and the wheels. |
| torque_converter_lock_gear | uint | 2 | The gear (1-based) from which the torque converter (if present, see **stall_torque_ratio**) is locked. Zero means the torque converter is never locked. |
| transmission_class | token | heavy | Transmission class, used for shifting behavior/sound selection. Acceptable values are **heavy** or **standard**; any other value defaults to **heavy**. |
| torque_converter_crawl | bool | false | When true, allows crawling on the torque converter (if present) without the throttle being engaged. |
| retarder | uint | 0 | The number of output levels for the retarder if applicable. If zero, retarder behavior is disabled for the transmission. |
| auxiliary_brakes | array&lt;float3&gt; |  | When set, this overrides the retarder control so that it controls both the retarder and engine brake. The components are (retarder strength, engine brake strength, forced downshift). The value of retarder must match the number of members in auxiliary_brakes. (*Added in 1.28*) For example: retarder: 5 auxiliary_brakes[]: (0.3, 0, 0) // 30% retarder only auxiliary_brakes[]: (0.6, 0, 0) // 60% retarder only auxiliary_brakes[]: (1.0, 0, 0) // 100% retarder only auxiliary_brakes[]: (1.0, 1, 0) // 100% retarder and 100% engine brake auxiliary_brakes[]: (1.0, 1, 1) // 100% retarder, 100% engine brake and downshift |
| ratios_reverse | array&lt;float&gt; |  | This defines the reverse gear ratios in order of decreasing gear reduction. The values should be negative. Example: ratios_reverse[0]: -11.002 ratios_reverse[1]: -8.875 |
| ratios_forward | array&lt;float&gt; |  | This defines the forward gear ratios in order of decreasing gear reduction. The values should be positive. Example: ratios_forward[0]: 11.32 ratios_forward[1]: 9.132 ratios_forward[2]: 7.207 ...etc... |
| transmission_names | owner_ptr |  | Points to a unit of the type [transmission_names](transmission%20names.md), usually nameless and within the same unit definition file or [included](../Units.md#Includes) from a Serialized Unit Include (.sui) type file. This is used to assign custom names to each gear in automatic and sequential modes (these are overridden by h-shifter pattern definitions). |
| auto_mode_name | string | A | Prefix for gear number in dashboard display (element id 1310) during automatic transmission mode. *(Added in 1.35)* |
| manual_mode_name | string | M | Prefix for gear number in dashboard display (element id 1310) during manual transmission mode. *(Added in 1.35)* |
| crawls | uint | 0 | The number of ratios_forward to handle as crawler gears for UI display. *(Added in ETS2 [1.27.2](../../../Games/ETS2/Modding%20guides/1.27.2.md#Transmission_Data))* |
| reverse_crawls | uint | 0 | The number of ratios_reverse to handle as crawler gears for UI display. *(Added in 1.60)* |
| shift_time | float | 1.0 | The time, in seconds, it takes to shift gears in automatic shifting. *(Added in 1.31)* |
| sounds | array&lt;string&gt; |  | Each item assigns an FMOD event to a function, using the "*sound_name\|sound_path*" [format](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories). *(Added in 1.39)* Expected sound event names are: air_gear, retarder, gear_grind, and gear_wrong. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_transmission_data | revision: 5786 | captured: 2026-10-21 23:56:14 -->
