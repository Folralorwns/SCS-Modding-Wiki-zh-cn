# Documentation/Engine/Sound/TruckChassis

## Sounds - The truck chassis

Another group of truck sounds are sounds tied to the truck chassis.

### Air Brake

Brake discharge air sound effect. Sounds are played randomly when the service brake is released. It has to be 3D event. The event should be routed to the "truck_effects" audio bus. This is a simple ("one shot") event. It is recommended to use randomization of the assets supported by FMOD Studio.

The following event parameter must exists:

- air_pressure - the value is in the range <0 - 1> and represents the relative pressure of the air system

### Air CutOff

Cutoff air sound effect. Sound to be played when the air compressor is unloaded by the governor. It has to be 3D event. The event should be routed to the "truck_effects" audio bus. This is a simple ("one shot") event. It is recommended to use randomization of the assets supported by FMOD Studio.

### Reverse

Back-up beeper sound. It has to be 3D event. The event should be routed to the "truck_effects" audio bus. The event must be looped.

### Lift Axle

Sound effect of lifting axle. It has to be 3D event. The event should be routed to the "truck_effects" audio bus. The event must be looped or can be "one shot" sound but long enough.

### Hook Attach

Sound effect of attaching hook. It has to be 3D event. The event should be routed to the "truck_effects" audio bus. This is a simple ("one shot") event.

### Hook Detach

Sound effect of detaching hook. It has to be 3D event. The event should be routed to the "truck_effects" audio bus. This is a simple ("one shot") event.

### Trailer Cables

Sound effect of the trailer cables connection. It has to be 3D event. The event should be routed to the "truck_effects" audio bus. This is a simple ("one shot") event.

## Sound Configuration

The group of sounds configuration is stored in the "accessory_chassis_data" data.

There are no mandatory events but there are no default events either. Only the defined sounds will be played. There is array "sounds" which contents specification for the events:

- air_brake
- air_cutoff
- reverse
- lift_axle
- hook_attach
- hook_detach
- trailer_cables

### Example

There are configuration files for chassis for the "Peterbilt 579" inside folder "/def/vehicle/truck/peterbilt.579/chassis".

Each accessory include *@include "sound.sui"* file which contents indirect definition of the events:

```
	sounds[]: "air_brake|/sound/truck/default/effects_air_brake.soundref"
	sounds[]: "air_cutoff|/sound/truck/default/effects_air_cutoff.soundref"
	sounds[]: "reverse|/sound/truck/default/effects_reverse.soundref"
	sounds[]: "lift_axle|/sound/truck/default/effects_lift_axle.soundref"
	sounds[]: "hook_attach|/sound/truck/default/effects_hook_attach.soundref"
	sounds[]: "hook_detach|/sound/truck/default/effects_hook_detach.soundref"
	sounds[]: "trailer_cables|/sound/truck/default/effects_trailer_cables.soundref"
```

### Sound Position

The 3D position of this sounds is (by default) the same position as the engine.<br> This position could be modified by the .soundref file. (see [Sound reference file](../Sound.md#Sound_reference_file))

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/TruckChassis | revision: 5613 | captured: 2026-10-21 23:56:14 -->
