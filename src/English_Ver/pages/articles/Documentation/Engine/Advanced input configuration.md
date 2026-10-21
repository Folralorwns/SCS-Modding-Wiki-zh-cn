# Documentation/Engine/Advanced input configuration

## Basics

The H-shifter support is intended to be used with Logitech G27 and compatible wheels. It will not work with normal buttons! The shifters that are part of common commercial racing wheels are designed to mimic the layout of the manual shifters in cars that usually have up to six gears for forward movement. The trucks on the other hand tend to have much more gears. Having separate position for each gear would be not practical so an additional control is used to select an active gear set. Then a single gear from the set is selected by standard H-shifter pattern. For more information about available patterns see [Wikipedia](http://en.wikipedia.org/wiki/Manual_transmission#Truck_transmissions).

The gearbox simulated in the game has twelve forward gears and one reverse gear. In the default configuration the in-game H-shifter gearbox behaves as a "Range transmission" (see link above) where the "Shifter Toggle 1" button switches between gear set 1-6 and gear set 7-12. (see Controller options in the game, on the G27 it is mapped to the leftmost red button on the H-shifter by default).

### Gear Shifting Example

You have a gear 6 selected and you want to shift up to the gear 7 - you need to press the "Shifter Toggle 1" button to switch to gear set 7-12 and then move the H-shifter stick to the position 1. In similar way, to shift down from gear 7 to gear 6, press the "Shifter Toggle 1" to switch to gear set 1-6 and move the H-shifter stick to the position 6.

## Prepared layouts

The game provides three layouts which can be selected from the the Controllers in-game option screen using the "Shifter layout" option.

### Range transmission

This is the default configuration used by the game. The "Shifter Toggle: 1" selects between gears set 1-6 and gear set 7-12.

[![Hshifter_range.gif](../../../../../images/articles/Documentation/Engine/Advanced%20input%20configuration/Hshifter_range.gif)](../../../files/Hshifter%20range.gif.md)

### Splitter Transmission

The "Shifter Toggle: 1" selects between odd-numbered gears (1,3,5,7,9,11) and even-numbered (2,4,6,8,10,12) gears.

[![Hshifter_splitter.gif](../../../../../images/articles/Documentation/Engine/Advanced%20input%20configuration/Hshifter_splitter.gif)](../../../files/Hshifter%20splitter.gif.md)

### Range-splitter Transmission

This configuration tries to emulate a layout of a real Scania H-shifter. Note that the game does not simulate the second reverse gear nor the two crawling gears so corresponding positions are not used. This case is a combination of both preceding transmission types where the "Shifter Toggle: 1" switches between gear ranges and "Shifter Toggle: 2" switches between splitted gears.

[![Hshifter_rangesplitter.gif](../../../../../images/articles/Documentation/Engine/Advanced%20input%20configuration/Hshifter_rangesplitter.gif)](../../../files/Hshifter%20rangesplitter.gif.md)

## Advanced configuration

The default H-shifter layout was selected to fit the most players, however with some tweaking of the gearbox configuration file it is possible to create a different layouts. The gearbox configuration files for individual predefined layouts can be found in your profile directory (remember to replace the PROFILE_ID with your real profile identifier):

```
My Documents\Euro Truck Simulator 2\profile\PROFILE_ID\gearbox*.sii
```

The files contain a list of entries that map the condition triplet (h shifter position, selector 1 state, selector 2 state) to the concrete gear to use.

```
direct_gearbox_gear : _nameless.0F5B.B220 {
    gear_impulse_index: 0
    selector_1: -1
    selector_2: -1
    gear: 0
}
```

| Name | Description |
| --- | --- |
| gear_impulse_index | Defines which position should the H-shifter be in: 0 - neutral 1 - "Shifter Position: Reverse" 2 - "Shifter Position: 1" 3 - "Shifter Position: 2" ... N - "Shifter Position: N" Take care when editing the input configuration (see below). The game does not check if your H-shifter hardware supports the position you've entered. |
| selector_1 | Defines the state of the first selector: -1 - ignore the selector state 0 - the selector should be off 1 - the selector should be on |
| selector_2 | Defines the state of the second selector. See selector_1 for list of possible values. |
| gear | The gear to shift in when the three conditions above are met. |

## Custom hardware

It is possible to use a custom H-shifter hardware provided that it reports the position as continuous press of some button. With more complex custom configuration of the input a position reported as axis value (e.g. aircraft throttle) can be also supported.

If the hardware has the ability to differentiate both positions of the range or splitter toggles, an additional inputs *gearsel1on* / *gearsel2on* and *gearsel1off* / *gearsel2off*, which are not accessible through the UI, can be configured instead of the toggling one.

### Advanced Input Configuration

The game UI supports use of up to five controllers. The game itself is able to simultaneously use of more than five controllers, however such setup can not be configured through the game user interface and manual tweaking of the game's configuration files is required.

This section describes how an advanced user can manually tweak the configuration file to be able to use more than three controllers or create even more complex. By manual tweaking of the configuration it is possible to add some features not directly supported by the game UI such as

- Use a flight yoke throttle instead of h-shifter.
- Use a shift button selecting between two sets of functionalities assigned to other buttons for use with controllers which have limited number of buttons.
- Use single button to toggle between various pages in the adviser.
- Provide independent sensitivity for vertical and horizontal look control.
- Use a TrackIR compatible head tracker to control movement of the truck for people with some disabilities.

## Configuration file

The controller configuration is stored in profile directory (remember to replace the PROFILE_ID with your real profile identifier):

```
My Documents\Euro Truck Simulator 2\profile\PROFILE_ID\controls.sii
```

The file gets created when the controller or keyboard option screen is opened for the first time and contains a set of configuration lines which describe various components of the configuration.

## Example

1. This is an example how to use accelerator and brake pedal from a secondary controller and a horn button from a third controller without using the in-game UI. The same mechanism can be used if more than three controllers should be used.
2. Using the steps described in the Input identification section determine the identification of the accelerator input on the secondary controller. Example identification: di8.'{C0002222-0000-0000-0000-000000000000}|{00000000-0000-0000-0000-000000000000}'.y
3. Determine the identification of the brake pedal input on the secondary controller. Example identification: di8.'{C0002222-0000-0000-0000-000000000000}|{00000000-0000-0000-0000-000000000000}'.rz
4. Determine the identification of the button input on the third device. Example identification: di8.'{C0003333-0000-0000-0000-000000000000}|{00000000-0000-0000-0000-000000000000}'.b4
5. Restore the default configuration on both keyboard and controller options pages in the game (not strictly necessary, just for purpose of this example) and configure the primary device in a normal way using UI.
6. To connect the accelerator pedal from the secondary controller to the in-game throttle input: Find the text "input j_throttle `joy.y`" in the configuration file and change the input identification so in our example it so it reads "input j_throttle `di8.'{C0002222-0000-0000-0000-000000000000}|{00000000-0000-0000-0000-000000000000}'.y`"
7. To connect the brake pedal from the secondary controller to the in-game brake input: Find the text "input j_brake `joy.y`" in the configuration file and change the input identification to the secondary controller brake pedal identification so in our example it reads "input j_brake `di8.'{C0002222-0000-0000-0000-000000000000}|{00000000-0000-0000-0000-000000000000}'.rz`".
8. In this case the pedals are reported as two separate axes so you need to turn off the combined axis by changing the value in "constant c_jcombined 1.000000" to "constant c_jcombined 0.000000"
9. Depending on the device you might want to configure the deadzone for those inputs by changing values in "constant c_throt_dz 0.000000" and "constant c_brake_dz 0.000000"
10. To connect the button from the third controller to the in-game horn input: Find the text "mix horn `keyboard.h?0`" in the configuration file and change the input identification so in our example it reads "mix horn `di8.'{C0003333-0000-0000-0000-000000000000}|{00000000-0000-0000-0000-000000000000}'.b4`".

## Input identification

The game identifies individual inputs on the controllers using a name composed from several parts in following format:

```
SYSTEM_ID.'DEVICE_ID'.INPUT_ID
```

On Windows OS the SYSTEM_ID will be almost always set to di8 indicating that DirectInput8 is used. The DEVICE_ID is a string identifying the specific controller device. There are two ways to determine identification of the desired device. You can select the device as active in the UI and check what the game has stored in the "joy" device alias (find line containing text device joy) in configuration file. Alternatively you can look inside the game.log file for lines with following format:

```
[di8] Initializing device 'DEVICE_NAME' as 'DEVICE_ID'
```

The corresponding identification to use in the configuration file is then **di8.'DEVICE_ID'** The INPUT_ID identifies a concrete input (e.g. axis, button) on the device. The best way to determine it is to use the game UI to create binding using that input and to check what the game has stored in the configuration file. For controllers it is usually **b1 - b128** for buttons, **x, y, z, rx, ry, rz** for axes, **sl1** or **sl2** for sliders and **pov_(1|2|3|4)_(up|down|left|right)** for POVs

Sometimes the input identification is followed by an additional specification of the component of the input (e.g. "di8.rel_position.x" which represents X component of the mouse position delta). At other times a defined alias might be used to shorten part of the input name.

## Component types

### Device alias

**Example format:** device joy `di8.'{A76B60D0-A8FD-11E1-8002-444553540000}|{C29B046D-0000-0000-0000-504944564944}'`

**User-creatable:** Yes

The device alias defines a new name ("joy") which can be used in other parts of the configuration file as a shortcut to reference a specific input device without having to always use its full identification. Defining and using the device alias also allows simple switch to a different compatible device by changing the alias target without having to update the rest of the configuration. By default the game creates aliases for keyboard, mouse and joy1-6 to identify keyboard, mouse and joystick device supported by the UI. Five joysticks can be directly selected in the UI, the sixth one is supported by binding UI if manually set in the config file.

### Input alias

**Example format:** input j_steer `joy.x`

**User-creatable:** Yes

The input alias defines a new name ("j_steer") which can be used in other parts of the configuration file as a shortcut to reference a specific input (axis, button) from input device without having to specify the longer name. Same as with the device aliases case, input aliases also allow easy configuration changes. The game axis configuration UI works by changing input aliases to point to the selected axes.

### Constant

**Example format:** constant c_steer_dz 0.000000

**User-creatable:** Yes

The constant defines a named ("c_steer_dz") numeric value which might be used by calculations in other parts of the configuration file or directly by the game itself (e.g. FF strength).

### Mix

**Example format:** mix dsteerleft `keyboard.larrow?0 | keyboard.a?0`

**User-creatable:** No

The mix defines an expression which is used to calculate value of a single game input. The game can use this value as an analog input (e.g. fraction of the rotation of the steering wheel) or as a logical value (e.g. wipers toggle). The interpretation and additional configuration of the individual mixes (in what situations they are evaluated) is hardcoded in the game and it is currently not possible to create additional mixes in the configuration file. In the simplest form the expression returns value of a single input. The more complex forms can use several mathematical and logical functions (see below) to derive the results from more than one input. Note that the UI input configuration screens directly supports only a very limited subset of the expressions and will display "Complex" message if they can not handle the expression. Generally there are two types of mix evaluation.

- Event based - this mix evaluates whenever there is change in any input (or other mix) it depends on. Mixes which read to individual presses (e.g. gear change, any_cmd) are usually of this type. As of 1.3.1. those mixes get duplicate evaluations whenever they react to button which generates characters (e.g. character key in keyboard). While usually not issue, this might be important when using the mix in loopback mode (e.g. it references old value of itself).
- Frame based - this mix evaluates at end of the frame. Mixes which react to hold (e.g. horn) or provide analog values (e.g. steering) are usually of this type.

## User-created components

For some component types it is possible to create additional components simply by using additional component definition line in the configuration file. Names of such components must meet following requirements:

- Must be unique within the configuration file.
- Must have at most 12 characters.
- Only alphanumeric characters and underscore character are allowed.

## Expressions

The expressions are used to combine device inputs and apply deadzones or a non-linear functions to them. Several types of values can be used in the expression:

- A reference to a constant value (e.g. 2.0)
- A reference to a named constant (e.g. c_steer_dz).
- A reference to a controller inputs using its full (e.g. di8.keyboard.space) or aliased form (e.g. keyboard.space). In cases of some special inputs an additional component selector (.x, .y, .z, .yaw, .pitch, .roll) might be needed. In the default configuration file you will see that alternative keyboard.space?0 syntax is used. That syntax indicates that if the input can not be found, the sub-expression should behave as if a constant 0 was returned from the device instead of reporting error and failing entire expression.
- A reference to some other mix (e.g. dforward). Note that circular references are not allowed, however it is possible to reference the mix this expression belongs to. In that case a previous value is returned. Note that there are no guarantees on frequency or time between calls however it might be used to implement simple counters or toggles when used with the event-based mixes.
- A special name unbound which resolves to constant zero. It is used to preserve information if no key is assigned to the primary binding slot.

The values can be combined using arithmetical (+, -, *, /) and logical (&, |, !) operators. Note that operator precedence rules are very simple so use of the brackets is highly recommended. When a value is interpreted in a logical context (e.g. during logical OR or AND operations or when it is used as logical value by the game), values greater than or equal to 0.5 evaluate to true and other values evaluate to false. Logical operators return 1.0 for true and 0.0 for false and have a short-circuit evaluation. Since 1.35 the expression also supports logical operators with a full evaluation (&&, ||). While the short-circuit variants are preferred for most uses, the full evaluation variants should typically be used when using memory based functions. Memory based functions preserve some state between evaluations as long the mix expression (i.e. the expression string, not the result of the evaluation) does not change. Changing the expression (e.g. because of config load) will reset the memory to default state.

Following set of functions is also available. The range in brackets indicate allowed number of parameters to the function:

| Function | Version | Description |
| --- | --- | --- |
| max(1..) |  | Returns biggest from the parameters. |
| min(1..) |  | Returns smallest from the parameters. |
| pow(2..) |  | (p0^p1)^p2)... |
| abs(1) |  | Absolute value of the parameter. |
| abs_max(1..) | 1.43+ | Returns value of parameter with the biggest absolute value from all parameters. (e.g. abs_max(2, -5, -1, 4) returns -5). If there are multiple values with the same absolute value and a different sign, the value of the parameter with the lower index is returned. |
| sign(1) |  | Returns -1 if parameter is negative number, 1 if the parameter is positive number and 0 for zero. |
| gt(2) |  | Returns 1.0 if the first parameter is greater than the second one. |
| gte(2) |  | Returns 1.0 if the first parameter is greater than or equal to the second one. |
| lt(2) |  | Returns 1.0 if the first parameter is lower than the second one. |
| lte(2) |  | Returns 1.0 if the first parameter is lower than or equal to the second one. |
| sel(3) |  | Returns the second parameter if the first parameter evaluates to true (see above), for false returns the third parameter. |
| bool(1) |  | Returns 1.0 if the first parameter evaluates to true (see above) and zero otherwise. |
| normalize(2-3) |  | Returns normalized position of the first parameter in the range formed by <second parameter, third parameter>. If the value is outside of the range, it will be clamped to it. If third parameter is not provided, 1.0 will be used. If the second and third parameter do not form valid non-empty range, zero will be returned. |
| deadzone(2-3) |  | Applies a zero-symmetrical deadzone. Similar to the normalize, however it applies symmetrically to the negative values as well. If the second parameter is negative, it is set to zero. |
| memory(2) | 1.35+ | Simple single-value memory. The memory starts at zero. If the first parameter evaluates to true, the second parameter is evaluated and its value is stored in the memory. Otherwise the second parameter is not evaluated and the memory is unchanged. The function returns the current value of the memory after the processing (i.e. the new value if the memory was updated). |
| modifier(2) | 1.35+ | Supports implementation of modifier-like keys. The first parameter represents "modifier" expression and the second parameter represents "button" expression. The function starts with returning 0.0. If it detects false to true transition on the "button" parameter while the "modifier" parameter is true, it will start returning 1.0 until the "button" parameter reverts to false after which it returns back to 0.0. Please note that the function detects changes only while it is being evaluated. If something, such as short-circuit logical operator, prevents the call, the function might miss some changes. Function evaluates the "modifier" parameter only during the leading edge (false => true) on the "button" parameter. Because of this, avoid using memory based elements within the "modifier" parameter to avoid risk of unexpected behavior. |
| short_press(1-2) | 1.41+ | Supports detection of short press. If the first input is temporarily >= 0.5 for interval shorter than a threshold, the function will return 1.0 until end of the frame it detected that in. The value of the threshold in milliseconds is configured by the second parameter and uses default value (200ms as of 1.46) if the second parameter is not provided. The detection only happens if the function is being evaluated (i.e. do not use it with short-circuit logical operators). |
| long_press(1-2) | 1.41+ | Supports detection of long press. If the first input is >= 0.5 for interval longer than a threshold, the function will return 1.0 until the input goes back to < 0.5. The value of the threshold in milliseconds is configured by the second parameter and uses default value (200ms as of 1.46) if the second parameter is not provided. The detection only happens if the function is being evaluated (i.e. do not use it with short-circuit logical operators). |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Advanced_input_configuration | revision: 5183 | captured: 2026-10-21 23:56:14 -->
