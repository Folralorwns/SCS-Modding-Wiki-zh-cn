# Documentation/Engine/Sound/TruckCabinFiltering

## The truck cabin filtering

There is the possibility of individual (per truck) sound filtering for the truck cabin. *(Added in 1.43 version)*<br> (*Hard-coded equalizer settings (automation) in the master bank has been removed since version 1.43.*)

## Sound processing

The following features are important when processing cabin sound:

**Listener position (inside / outside)**

- This state is controlled by the global parameter *cabin_out* (0 means inside, 1 means outside).

**Window opening status (closed / open)**

- This state is controlled by the global parameters *wnd_left*, *wnd_right* (0 means closed, 1 means opened).

**Sound processing**

- 1. The sound is processed as external generally with respect to the position of the listener. The result of processing is in the audio bus [**Grp outside**].
- 2. Subsequently, this channel is redirected (divided) into three audio buses:
  - [**Rtn window_out**] Central sound overhang in the cab.
  - [**Rtn window_left**] Pass the sound through the left window.
  - [**Rtn window_right**] Pass the sound through the right window.
- 3. Finally, all three buses are mixed into the resulting sound.

![Truck_cabin_sound.png](../../../../../../images/articles/Documentation/Engine/Sound/TruckCabinFiltering/Truck_cabin_sound.png)

## Adjust the volume

The volume setting is hard-coded to the FMOD master bank, but its understanding is necessary for further processing.

The volume is controlled according to the position of the listener and affects the resulting mixing of the processed audio buses:

| Audio bus | Listener inside | Listener outside |
| --- | --- | --- |
| [**Rtn window_out**] | -6 dB | +4 dB |
| [**Rtn window_left**] | -7 dB | *muted* |
| [**Rtn window_right**] | -7 dB | *muted* |

## Sound attenuation when the window is open/closed

Sound attenuation is controlled by an equalizer (3-EQ), which is located on each sound bus that processes the passage of sound through the window. The equalizer setting is individual for each truck (from version 1.43) and is part of the interior sound settings.

| Window | Audio bus | opened | closed |
| --- | --- | --- | --- |
| Left | [**Rtn window_left**] | .effect.add.window_eq.opened | .effect.add.window_eq.closed |
| Right | [**Rtn window_right**] | .effect.add.window_eq.opened | .effect.add.window_eq.closed |

The transition between the equalizer limit parameters is linearly approximated by the application. Please be very careful when setting a large difference boundaries for the low_crossover, high_crossover parameters on the same equalizer. Large differences can generate unwanted sound patterns.

## Sound attenuation depending on the position of the listener

Sound attenuation is controlled by an equalizer (3-EQ) , which is located on the [**Rtn window_out**] audio bus. The equalizer setting is individual for each truck (from version 1.43) and is part of the interior sound settings.

| Listener | Audio bus | inside | outside |
| --- | --- | --- | --- |
| Listener | [**Rtn window_out**] | .effect.equalizer.cabin.inside | .effect.equalizer.cabin.outside |

The transition between the equalizer limit parameters is linearly approximated by the application. Please be very careful when setting a large difference boundaries for the low_crossover, high_crossover parameters on the same equalizer. Large differences can generate unwanted sound patterns.

## Reverb in the cabin

Reverb in the cabin depends on both the position of the listener and the state of opening / closing the windows. The reverb setting is processed only on the final mix of all three audio buses. (*Within the sound bank, the Reverb effect is placed on the [Grp cabin] audio bus.*)

The reverb setting is individual for each truck (from version 1.43) and is part of the interior sound settings.

| Reverb | Audio bus | inside | outside |
| --- | --- | --- | --- |
| reverb effect | [**Grp cabin**] | .effect.reverb.window.closed | .effect.reverb.window.opened |

The transition between the reverb limit parameters is linearly approximated by the application. The external reverb should correspond approximately to the external (open) environment. Therefore, we recommend a setting that does not change the echo too much.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/TruckCabinFiltering | revision: 5163 | captured: 2026-10-21 23:56:14 -->
