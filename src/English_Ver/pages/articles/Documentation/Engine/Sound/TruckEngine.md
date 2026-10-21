# Documentation/Engine/Sound/TruckEngine

### Sounds - Truck Engine

The sound of the truck engine is very specific kind of the sounds.<br> Engine sound is very sensitive to be balanced between sound sources.<br> <br> So there are a few rules for the engine sound:

- The each sound of the truck engine should be in the separate sound bank.
- There are only the four events and all should be implemented in the same bank.
- It is not recommended to combine events of different banks for the engine sound.

## Engine Sound Events

- All events should be at the folder "engine" in the events browser.
- These events should exist in the bank:<br>**engine/engine**<br>**engine/exhaust**<br>**engine/turbo** *(from 1.39)*<br>**engine/start_bad**

### Event "engine"

Event "engine" plays sound of the engine.<br> It has to be a 3D event. The event should be routed to the "truck_engine" audio bus.<br> The event must be looped and its living cycle is controlled by "play" parameter (see bellow).<br> <br> These event parameters must exist:

- engine/play<br>The parameter "play" control living cycle of the event:<br>value play = 1 means - sound is playing<br>value play = 0 means - sound should be stopped
- engine/brake<br>the value is in the range <0 - 1> and represents the action of the motor brake
- engine/load<br>the value is in the range <0 - 1><br>value represents the motor load<br>value < 0.05 means idle engine sound
- engine/rpm<br>the value is in the range <0 - 3000><br>the value represents the number of engine revs per second

### Event "exhaust"

Event "exhaust" plays sound of the exhaust.<br> It has to be a 3D event. The event should be routed to the "truck_exhaust" audio bus.<br> The event must be looped and its living cycle is controlled by "play" parameter.<br> <br> These event parameters must exist:

- exhaust/load
- exhaust/play
- exhaust/rpm

The purpose of the parameters is the same as for the "engine" event (see Event "engine").

### Event "turbo"

Event "turbo" plays sound of the turbo.<br> It has to be 3D event. The event should be routed to the "truck_turbo" audio bus.<br> The event must be looped and its living cycle is controlled by "play" parameter.<br> <br> These event parameters must exist:

- engine/turbo<br>the value is in the range <0 - 1> and represents the action of the turbo system

### Event "start_bad"

Event "start_bad" plays sound of unsuccessful starting of the engine.<br> It has to be 3D event. The event should be routed to the "truck_engine" audio bus.<br> The event is one-shot sound (without loop).<br> There are no other parameters for the event.<br> It is possible to use randomization of the assets supported by FMOD Studio.

## Engine Sound Configuration

The sound configuration of the engine sounds is stored in the "accessory_engine_data" data.<br> There is array "sounds" which contents specification for the mandatory events of the engine.<br> That means that each type of the engine can have assigned its own sound bank.<br> <br> Example:<br> There are configuration files of engines for the "Peterbilt 579" at the folder "\def\vehicle\truck\peterbilt.579\engine".<br> Each engine include *@include "sound.sui"* file which contents indirect definition of the events:

```
	sounds: 4
	sounds[]: "engine|/def/vehicle/truck/peterbilt.579/engine/sound_engine.soundref"
	sounds[]: "exhaust|/def/vehicle/truck/peterbilt.579/engine/sound_exhaust.soundref"
	sounds[]: "start_bad|/def/vehicle/truck/peterbilt.579/engine/sound_start_bad.soundref"
	sounds[]: "turbo|/def/vehicle/truck/peterbilt.579/engine/sound_turbo.soundref"
```

There are .soundref file (for each event) to specify bank end FMOD event of the sound.

Content of the sound_engine.soundref is:

```
source="/sound/truck/peterbilt_579.bank#engine/engine"
```

The record<br>sound: *"/sound/truck/peterbilt_579.bank"*<br>at the any engine configuration file assigns the sound bank to the engine.

## Engine Sound Position

The 3D position of the engine sound is (by default) 1 m above the first axle of the truck.<br> This position could be modified by the .soundref file. (see [Sound reference file](../Sound.md#Sound_reference_file))

## Engine Sound Example

Visit the [Downloads](Downloads.md) section to get template project or sound examples.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/TruckEngine | revision: 5773 | captured: 2026-10-21 23:56:14 -->
