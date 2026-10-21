# Documentation/Engine/Units/sound engine data

The **sound_engine_data** unit class is used to define engine sounds. This unit is typically used in an array, with *min_rpm* and *max_rpm* ranges overlapping between members to allow crossfading.

## Uses

- [accessory_sound_data](accessory%20sound%20data.md) (engine, engine_load, engine_nofuel, engine_exhaust, engine_brake)

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| name | string |  | Path to the sound clip (e.g. `name: "/sound/truck/default/int/unloaded_1.ogg"`) |
| looped | bool | false | When true, the sound clip will be looped while active. When false, it will play once when triggered. Should always true for engine sounds. |
| is_2d | bool | false |  |
| volume | float | 0.0 | Playback volume relative to recorded level (0.0 is full attenuation, 1.0 is straight through, 2.0 is twice as loud) |
| pitch_reference | float | 0.0 | The reference engine rpm of the recording. |
| min_rpm | float | 0.0 | The lowest rpm the clip will be played at. |
| max_rpm | float | 0.0 | The highest rpm the clip will be played at. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/sound_engine_data | revision: 3275 | captured: 2026-10-21 23:56:14 -->
