# Documentation/Engine/Units/sound noise data

The **sound_noise_data** unit class is used to define speed-dependent sounds. This unit is typically used in an array, with *min_speed* and *max_speed* ranges overlapping between members to allow crossfading.

## Uses

- [accessory_sound_data](accessory%20sound%20data.md) (wheel_*, aero_noise, gear_noise)

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| name | string |  | Path to the sound clip (e.g. `name: "/sound/truck/noises/wind_inside_int_1.ogg"`) |
| looped | bool | false | When true, the sound clip will be looped while active. When false, it will play once when triggered. Should always be true for noise sounds. |
| is_2d | bool | false |  |
| volume | float | 1.0 | Playback volume relative to recorded level (0.0 is full attenuation, 1.0 is straight through, 2.0 is twice as loud) |
| pitch_reference | float | 0.0 | The reference vehicle speed of the recording. |
| min_rpm | float | 0.0 | The lowest vehicle speed the clip will be played at. |
| max_rpm | float | 0.0 | The highest vehicle speed the clip will be played at. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/sound_noise_data | revision: 3267 | captured: 2026-10-21 23:56:14 -->
