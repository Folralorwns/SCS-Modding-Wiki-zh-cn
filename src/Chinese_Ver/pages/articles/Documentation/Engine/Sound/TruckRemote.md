# Documentation/Engine/Sound/TruckRemote

### Sounds - Remote Truck

The sound of a remote truck is in principle very similar to the sound of a player's truck engine.<br> (Please see the [Sounds - Truck Engine](TruckEngine.md) for a better understanding.)<br> <br> However, there are a few key differences to keep in mind:

- The engine sound is integrated into one event (usually remote / engine), including exhaust and turbo sounds.
- Due to performance considerations, the sound for the remote truck needs to be significantly simplified.

### Event "(remote/)engine"

Event "engine" plays sound of the engine of remote truck.<br> It has to be a 3D event. The event should be routed to the "traffic" audio bus.<br> The event must be looped and its living cycle is controlled by "play" parameter (see bellow).<br> <br> These event parameters must exist:

- play<br>The parameter "play" controls the living cycle of the event:<br>value play = 1 means - sound is playing<br>value play = 0 means - sound should be stopped
- brake<br>the value is in the range <0 - 1> and represents the action of the motor brake
- load<br>the value is in the range <0 - 1><br>value represents the motor load<br>value < 0.05 means idle engine sound
- rpm<br>the value is in the range <0 - 3000><br>the value represents the number of engine revs per second
- turbo<br>the value is in the range <0 - 1> and represents the action of the turbo system

## Remote Engine Sound Configuration

The sound configuration of the engine sounds is stored in the "accessory_engine_data" data.<br> There is array "sounds" which contains the specification for the mandatory events of the engine.<br> That means that each type of engine can be assigned its own sound bank.<br> The item "remote" has been added for the remote engine sound (since version 1.42) <br> Example:<br> There are configuration files of engines for the "Peterbilt 579" at the folder "\def\vehicle\truck\peterbilt.579\engine".<br> Each engine includes *@include "sound.sui"* file which contains the definition of the events:

```
	sounds: 5
	sounds[]: "engine|/def/vehicle/truck/peterbilt.579/engine/sound_engine.soundref"
	...
	sounds[]: "remote|/def/vehicle/truck/peterbilt.579/engine/sound_engine_rm.soundref"
```

There are .soundref file (for each event) to specify the bank and the FMOD event of the sound.

Content of the sound_engine_rm.soundref is:

```
source="/sound/truck/peterbilt_579_rm.bank#remote/engine"
```

## Engine Sound Example

Visit the [Downloads](Downloads.md) section to get template project or sound examples.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/TruckRemote | revision: 5761 | captured: 2026-10-21 23:56:14 -->
