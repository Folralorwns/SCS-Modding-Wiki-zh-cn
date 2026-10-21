# Documentation/Engine/Sound/TruckTransmission

## Sounds - The truck transmission and the retarder

The next group of the sounds of the truck are sounds of the transmission and the retarder.

### Retarder

Event "retarder" plays sound of the retarder. It has to be 3D event. The event should be routed to the "truck_effects" audio bus.

The event must be looped and following event parameters must exist:

- retarder - the value is in the range <0 - 1> and represents the retarder activity
- trans_rpm - the value is in the range <0 - 3000> and represents the rpm of the transmission

### Air gear (noise)

Air discharge sound effect of the gearbox. This is noise played when gearbox is shifting. Eg european electro-pneumatic ATM transmissions make their typical sound in that moment. It has to be 3D event. The event should be routed to the "truck_effects" audio bus. It is possible to use randomization of the assets supported by FMOD Studio.

This is a simple ("one shot") event.

### Gear grind

Sound of grinding of the transmission gears. Used mainly as sign of wrong rpm during fully manual shifting. It has to be 3D event. The event should be routed to the "truck_effects" audio bus.

The event must be looped. There are no parameters.

### Gear wrong

Sound effect of incorrect gearbox engagement. Used as sign of damaged gearbox even when using automatic shifting. It has to be 3D event. The event should be routed to the "truck_effects" audio bus.

This is a simple ("one shot") event.

## Sound Configuration

The group of sounds configuration is stored in the "accessory_transmission_data" data.

There is no mandatory events but there is no default events either. Only the defined sounds will be played. There is array "sounds" which contents specification for the events:

- retarder
- air_gear
- gear_grind
- gear_wrong

### Example

There are configuration files for transmissions for the "Peterbilt 579" inside folder "/def/vehicle/truck/peterbilt.579/transmission".

Each accessory include *@include "sound.sui"* file which contents indirect definition of the events:

```
	sounds[]: "retarder|/sound/truck/default/retarder.soundref"
	sounds[]: "air_gear|/sound/truck/default/effects_air_gear.soundref"
	sounds[]: "gear_grind|/sound/truck/default/effects_gear_grind.soundref"
	sounds[]: "gear_wrong|/sound/truck/default/effects_gear_wrong.soundref"
```

### Sound Position

The 3D position of this sounds is (by default) the same position as the engine.<br> This position could be modified by the .soundref file. (see [Sound reference file](../Sound.md#Sound_reference_file))

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/TruckTransmission | revision: 4799 | captured: 2026-10-21 23:56:14 -->
