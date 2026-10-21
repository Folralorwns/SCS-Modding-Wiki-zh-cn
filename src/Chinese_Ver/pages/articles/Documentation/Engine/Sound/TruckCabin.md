# Documentation/Engine/Sound/TruckCabin

## Sounds - The truck cabin

Another group of truck sounds are sounds tied to the truck cabin.

### Horn

Sound of the horn. It has to be 3D event. The event should be routed to the "truck_effects" audio bus. The event must be looped. The 3D position of this sounds is (by default) the truck model origin.

### Air Horn

Sound of the air horn. It has to be 3D event. The event should be routed to the "truck_effects" audio bus. The event must be looped. The 3D position of this sounds is (by default) 1m above the truck model origin.

### Aero Noise

The noise of the air flowing around a cabin. It has to be 3D event. The event should be routed to the "truck_noise" audio bus. The event must be looped.

The following event parameters must exist:

- aero_speed - the value is in the range <0 - 200> and represents the speed of the flowing air (in km/h)
- aero_wnd - the value is in the range <0 - 2> and represents the state of the window:
  - 0 ... disabled effect
  - (0 - 1> ... indicator (state) of the window opening
  - 2 ... camera is outside the cabin

There are two instances of this event in the game. Each is located near the (left / right) window. Each of them parameters are independent.

### Rain Noise

Sound effect of the raindrops to falling on the truck cabin. It has to be 3D event. The event should be routed to the "truck_noise" audio bus. The event must be looped.

The following event parameters must exist:

- rain_int - the value is in the range <0 - 1> and represents the relative rain intensity

The 3D position of this sounds is (by default) located in the cabin.

## Sound Configuration

The group of sounds configuration is stored in the "accessory_cabin_data" data.

There is no mandatory events but there is no default events either. Only the defined sounds will be played. There is array "sounds" which contents specification for the events:

- horn
- air_horn
- aero_noise
- rain_noise

### Example

There are configuration files for chassis for the "Peterbilt 579" inside folder "/def/vehicle/truck/peterbilt.579/cabin".

Each accessory include *@include "sound.sui"* file which contents indirect definition of the events:

```
	sounds[]: "horn|/sound/truck/horn/horn_01.soundref"
	sounds[]: "air_horn|/sound/truck/air_horn/air_horn_04.soundref"
	sounds[]: "aero_noise|/sound/truck/default/noise_aero.soundref"
	sounds[]: "rain_noise|/sound/truck/default/noise_rain.soundref"
```

### Sound Position

The sound positions could be modified by the .soundref file. (see [Sound reference file](../Sound.md#Sound_reference_file))

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/TruckCabin | revision: 4805 | captured: 2026-10-21 23:56:14 -->
