# Documentation/Engine/Units/sound data

The **sound_data** unit class is used to define sounds.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| name | string |  | Path to the sound clip (e.g. `name: "/sound/environment/timmys_ducks.ogg"`) |
| looped | bool | false | When true, the sound clip will be looped while active. When false, it will play once when triggered. |
| is_2d | bool | false | When true, the sound ignores any spatial features (position, orientation, distance, movement). |
| volume | float | 1.0 | Playback volume relative to recorded level (0.0 is full attenuation, 1.0 is straight through, 2.0 is twice as loud) |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/sound_data | revision: 4187 | captured: 2026-10-21 23:56:14 -->
