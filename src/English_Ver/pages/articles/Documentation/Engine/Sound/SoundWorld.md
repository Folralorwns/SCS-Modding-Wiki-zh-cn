# Documentation/Engine/Sound/SoundWorld

There are several types of sounds and sound effects in the sound system of the world:

- 3d sound (in the world)
- ambient sound
- reverb effect
- 3d sound on the object (prefab)
- animation (mover)

### Sound layer in the Editor

We now have a special layer for sounds on the map (up to version 1.40). The sound layer editor is just a special mode of the map editor, which can be activated using the command line:

```
eurotrucks.exe -nosingle -edit -sound
```

There is only one object that can be placed on the map in the sound layer: "sound item". However, this object works in 3 different modes:

- **3d sound** - Displays a circular area of sound whose size is determined by the audibility limit.
- **Ambient area** - Represents a user-defined area that is the source of a specified ambient sound.
- **Reverb area** - Represents a user-defined area that is the source of the reverb effect.

### Sound configuration for the sound layer

There are 3 configuration files (in the */base/def/world* folder):

- sound_item_data.sii

```
Contains a 3d sound definition with these parameters:
sound_item_data : sound.<id token of the sound item>
{
	name: "user friendly name (editor only) in format 'sound group name/sound name' "
	sound_path: "path to the sound event"
	max_dist: maximum sound distance (should be equal to or greater than the maximum audibility of the FMOD event)
	item_color: editor item color in RGBA format (0xAABBGGRR)
}
The sound is triggered on if the actor camera is in the range of the 'sound item' object. The audibility of the sound is given only by the setting of the 3D event in FMOD.
```

- sound_item_ambient.sii

```
Contains an ambient area definition with these parameters:
sound_item_data : ambient.<id token of the ambient sound>
{
	name: "user friendly name (editor only) in format 'sound group name/sound name' "
	sound_path: "path to the sound event"
	max_dist: maximum ambient sound distance
	item_color: editor item color in RGBA format (0xAABBGGRR)
	reverb: reverb.<id token of the reverb effect - Default reverb effect for the area.>
}
The sound is triggered when the actor camera is near the area.
The area on the map represents the 'full audibility' area of the ambient sound. The sound is automatically fade in/out beyond the edge of the area depending on the 'max distance' parameter.
The default reverb effect is applied only if there is no other reverb defined in the area.
```

- sound_item_reverb.sii

```
Contains a reverb area definition with these parameters:
sound_item_reverb : reverb.<id token of the reverb effect>
{
	name: "user friendly name (editor only)"
	max_dist: maximum effect distance
	item_color: editor item color in RGBA format (0xAABBGGRR)
	ceiling: true/false If true the effect is activate only if camera is under the 'sound item' object (eg under a bridge, tunnel).
	decay_time: Decay Time: Reverberation decay time at low-frequencies in milliseconds.  Ranges from 100.0 to 20000.0. Default is 1500.
	early_delay: Early Delay: Delay time of first reflection in milliseconds.  Ranges from 0.0 to 300.0.  Default is 20.
	late_delay: Reverb Delay: Late reverberation delay time relative to first reflection in milliseconds.  Ranges from 0.0 to 100.0.  Default is 40.
	hf_reference: HF Reference: Reference frequency for high-frequency decay in Hz.  Ranges from 20.0 to 20000.0. Default is 5000.
	hf_decay_ratio: Decay HF Ratio: High-frequency decay time relative to decay time in percent.  Ranges from 10.0 to 100.0. Default is 50.
	diffusion: Diffusion: Reverberation diffusion (echo density) in percent.  Ranges from 0.0 to 100.0.  Default is 100.
	density: Density: Reverberation density (modal density) in percent.  Ranges from 0.0 to 100.0.  Default is 100.
	low_shelf_frequency: Low Shelf Frequency: Transition frequency of low-shelf filter in Hz.  Ranges from 20.0 to 1000.0. Default is 250.
	low_shelf_gain: Low Shelf Gain: Gain of low-shelf filter in dB.  Ranges from -36.0 to 12.0.  Default is 0.
	high_cut: High Cut: Cutoff frequency of low-pass filter in Hz.  Ranges from 20.0 to 20000.0. Default is 20000.
	early_late_mix: Early/Late Mix: Blend ratio of late reverb to early reflections in percent.  Ranges from 0.0 to 100.0.  Default is 50.
	wet_level: Wet Level: Reverb signal level in dB.  Ranges from -80.0 to 20.0.  Default is -6.
	dry_level: Dry Level: Dry signal level in dB.  Ranges from -80.0 to 20.0.  Default is 0.
}
The effect is activated when the actor's camera enters to the defined area. (Now independent on max distance.)
But the parameters of the reverb effect are adjusted slidingly over time.
```

*Remark: Please do not modify these files if you want to add a new entry. Create in this directory a new file "<base_name>.&lt;idofyourmod&gt;.sii" where <base_name> is name of base file without the extension (e.g. "city" for "/def/city.sii") and &lt;idofyourmod&gt; is some string which is unlikely to conflict with another mod.*

### Sound events

(See [Sound examples](Downloads.md))

## 3d sounds

- This sound event represents a 3d sound coming from a specific sound source statically located on the map.
- An event is usually an infinite audio loop within a standard FMOD audio 3d event.
- Audio hearing is controlled by the FMOD spatializer. (This must correspond to the 'max distance' setting in the audio configuration.)
- Global parameters can be used to modify loop sounds.
- The sound should be mono (preferred) or stereo sample.

*Note: In our example, a restaurant sound controlled by the 'daytime' parameter is used. The example demonstrates the use of sound variants at different times of the day.*

## Ambient sounds

- This sound event is used as the sound for ambient areas in the world.
- An event is usually an infinite audio loop within a standard FMOD audio **2d event**. (Not including 3d spatializer.)
- Audio hearing is controlled by the game. (The full audibility volume should be set in FMOD.)
- Global parameters can be used to modify loop sounds.
- **The preferred format of the loop is 5.1.**
- The random events can be included in the loop.
- The event should be routed to the 'outside/unprocessed/ambient' bus.

*Note: In our example (forest_warm_con_2) is the simulation of the day / night sound of a forest including random events.*

## Other sounds in the world

For completeness: there are other sounds in the game world. All of these sounds are standard 3d FMOD events and can be created just like a '3d sound' event (see above).

They are:

- the sound assigned to a specific game object/prefab (defined in base\unit\hookup\sound_prefab.sii)
- the sound assigned to the animation / the 'mover' (defined as a part of mover definition in base\def\world\mover.sii)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/SoundWorld | revision: 5213 | captured: 2026-10-21 23:56:14 -->
