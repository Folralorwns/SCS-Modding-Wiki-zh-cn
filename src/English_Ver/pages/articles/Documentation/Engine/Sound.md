# Documentation/Engine/Sound

> **Note:** **The sound system and current pages are in a 'work in progress' state. We will continuously update content of the site and the audio data structures.**

## FMOD®

The FMOD® system is now (from 1.37 version) used as a core sound engine in the game.<br> The FMOD® Studio version you should use depending on your game version can be found [here](Sound/Downloads.md).

*See FMOD documentation ([www.fmod.com](http://www.fmod.com)) to get a better understanding of the sound system.*

## Sound and Sound Bank(s)

Each sound is represented by the sound **Event**. An Event is an instanceable sound unit of the FMOD Studio project. All sounds/events are provided by sound banks. The final sound banks are built by FMOD Studio.

FMOD Studio builds the "[bank name].bank" file for each bank in the sound project. It is a collection of the Events and Parameters used for the sound playing in the game.

## Master Bank

Master Bank is the primary sound bank of the sound system. There are no Events in the bank.

**The Master Bank defines:**

- The sound buses<br>Events in FMOD Studio do not exist in a vacuum. Their output is routed into the project mixer. The Events have to be routed to one of the buses registered in the Master Bank. Users can set the sound volume and mute state in the application settings for each bus which is used as a routing target for sound events.
- Mixer and Routing<br>The project mixer consists of a number of interconnected buses. Connection between the audio buses describe the sound event flow through the sound system.
- Global Parameters<br>An event contains and is primarily composed of tracks and parameters. Some parameters are defined in the master. These parameters are global and can be used for Automation and Modulation of events across all banks.

The Master Bank is a fundamental building block of the sound system so: **Never change the Master Bank!**

Only if you are absolutely sure what you are doing and you are rewriting all the sounds of the game you can change it.

## Sound definition

A common sound in game is the **Event** in the FMOD Studio project. Each object (bank, bus, event, parameter, etc.) used by the FMOD system has a Globally Unique Identifier - **GUID**.<br> (*GUID is something like this: {1315eda7-1829-4dd8-9d1a-176f65637ab2}*)

The sound system uses GUIDs internally for the processing objects. It's very important. If you delete an object in the sound project (bus, event, etc.) and create a new object even with the same name, it will be a different object because the object has a different GUID.

FMOD Studio exports GUIDs to the txt file.

1. Use FMOD Studio menu command: File / Export GUIDs...
2. A new file GUIDS.txt is written to the "build" subfolder of the project main folder.
3. The file has to be renamed to "[bank filename].guids" and has to be placed next to the corresponding "bank" file. It's a "dictionary" between names of the objects in the bank and their GUIDs.

The game uses two ways to define usage of a sound object:

1. Direct 'sound id':<br>"Sound id" is string in format "[bank filename]#[event name]". Where [bank filename] is file of the bank relative to the game "base" folder and [event name] is name of the event in the FMOD Studio project.<br>Example: *"/sound/ui/ui.bank#click"*
2. Sound reference file:<br>Sound reference file is used as link for the sound specification. It uses a simple path to the soundref file (e.g. *"/sound/ui/ui_click.soundref"*).

## Sound reference file

We prefer and we recommend to use sound reference files.

- There are more possibilities to configure sound.
- It is easier for changing / modding individual sounds.

**Sound reference file structure:**

Soundref file is a text file (with UTF-8 encoding).

- Its contents are a 'sound id' on one line with following format: source="[bank filename]#[event name]".
- There is possibility in the file to change the 3D placement of the sound relative to the default position. Format is as follows, on a separate line: "position_offset=-left/+right;-down/+up;-front/+back" (in meters).

Example of content of the file *"ui_click.soundref":* `source="/sound/ui/ui.bank#click"`

## Sound documentation

- [Audio buses, routing and mixer](Sound/Mixer.md)
- (WIP) Global parameters
- [Sounds - Truck Engine](Sound/TruckEngine.md)
- [Sounds - Truck Transmission and Retarder](Sound/TruckTransmission.md)
- [Sounds - Truck Chassis](Sound/TruckChassis.md)
- [Sounds - Truck Cabin (horns and noises)](Sound/TruckCabin.md)
- [Sounds - Truck Cabin Filtering (in/out, windows)](Sound/TruckCabinFiltering.md)
- [Sounds - Remote Truck (multiplayer)](Sound/TruckRemote.md)
- (WIP) Sounds - Truck Interior
- [Sounds - Tires](Sound/Tires.md)
- (WIP) Sounds - Collisions
- (WIP) Sounds - Traffic
- [Sounds - World](Sound/SoundWorld.md)
- (WIP) Sounds - Game UI and Music
- [Modding sounds](Sound/Modding.md)
- [Downloads (templates, samples)](Sound/Downloads.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound | revision: 5784 | captured: 2026-10-21 23:56:14 -->
