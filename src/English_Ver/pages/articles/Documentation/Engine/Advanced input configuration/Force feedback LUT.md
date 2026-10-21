# Documentation/Engine/Advanced input configuration/Force feedback LUT

With game update 1.42 (ETS2 & ATS) engine got support for custom force feedback **L**ook **U**p **T**able, which can alternate the linearity of the output force from the wheel. The intention of this is to enable users to overcome inability of some steering wheel hardware linear output and calibrate the output by their liking.

## Usage

To use custom used defined FFB LUT, one needs to create a unit file inside the profile folder:

- local profile: `<game_user_path>/profiles/<profile_hash>/ffb_lut.sii`
- Steam Cloud profile: `<game_user_path>/steam_profiles/<profile_hash>/ffb_lut.sii`

When profile with defined `ffb_lut.sii` is loaded, usage of the file will be marked with exclamation mark beside **Overall gain** option in the controller settings. Additionally, if file is properly loaded, it will be always used no matter which steering wheel is currently in use. So in case you are having two steering wheels and switching between them, then custom ffb LUT will be same for both of the wheels.

## File contents

Custom force feedback LUT is text file containing just one unit:

```
SiiNunit
{
input_force_feedback_lut : ffb.lut {
	# This ffb LUT presents simple scaling by factor 0.5

	output_values[]: 0.0   # input value: 0.0; output value: 0.0
	output_values[]: 0.25  # input value: 0.5; output value: 0.25
	output_values[]: 0.5   # input value: 1.0; output value: 0.5
}
}
```

The `input_force_feedback_lut` unit contains one array variable named `output_values`, which defines lookup value for appropriate input value. Input value for each entry is calculated as: `<entry_index> / (<number_of_entries> - 1)`. All the input values in-between are linearly interpolated between the closest two entries.

Note that all output values will be clamped to the interval <0,1> since scaling above 1.0 could mean unpredictable behavior.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Advanced_input_configuration/Force_feedback_LUT | revision: 5718 | captured: 2026-10-21 23:56:14 -->
