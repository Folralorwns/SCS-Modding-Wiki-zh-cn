# Documentation/Engine/Sound/Tires

### Sounds - Tires

This section is related to the sound of tires on different road substances.

## Tire Sound Events

Tire sounds are kept separate for the truck tires and trailer tires, but both have the same events and parameters.<br> Currently there are 4 supported substances each with their own sound event:

- asphalt
- rumble
- gravel
- grass<br>

### Tire Sound Parameters

Sound parameters:

- <name_of_event>/speed<br>The parameter "speed" (km/h) controls the pitch and volume of the substance sound.
- skid_speed<br>The parameter "skid_speed" (m/s) represents the speed of wheel slip in either direction.
- note<br>The parameter "note" is present only for the "rumble" substance. <br>It is a frequency multiplier that is applied to the root note G and forms the melody for the singing road.

## Engine Sound Configuration

The tire sounds paths are stored in these 4 soundrefs for the truck:

```
	sound/tires/rumble.soundref
	sound/tires/grass.soundref
	sound/tires/gravel.soundref
	sound/tires/asphalt.soundref
```

and these 4 for the trailer:

```
	sound/trailer/tires/rumble.soundref
	sound/trailer/tires/grass.soundref
	sound/trailer/tires/gravel.soundref
	sound/trailer/tires/asphalt.soundref
```

Example:

Content of the "sound/tires/rumble.soundref" is:

```
source="/sound/tires/tires.bank#rumble"
```

The location of the sound bank for the truck: *"/sound/tires/tires.bank"*<br> and sound bank for the trailer: *"/sound/trailer/tires/tires.bank"*

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/Tires | revision: 5294 | captured: 2026-10-21 23:56:14 -->
