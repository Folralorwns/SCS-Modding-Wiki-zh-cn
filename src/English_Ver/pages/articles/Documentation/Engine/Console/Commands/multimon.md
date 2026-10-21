# Documentation/Engine/Console/Commands/multimon

While the **multimon** command allows dynamic changes of the size of the monitor views at runtime, increasing the size can not increase the maximal effective rendering resolution beyond the resolution used by the biggest view the game started with. In that case the changed view will have proper size however its content might look blurry. To fix it, restart the game or temporarily change (and apply) vsync settings in display options **after saving** the configuration first using **multimon save**.

The multi-monitor support assumes that the graphics drivers are providing a virtual screen spanning over all the physical monitors.

The following commands are supported:

### init

Syntax: multimon init <setup_name>

Example: multimon init three

This command initializes the runtime configuration using one from predefined setups. Following setups are supported:

- **empty** - No views, UI over entire screen. This is convenient starting point for more complex custom setups.
- **one** - Creates single wide view UI over entire screen. This is similar to predefined mode **0** however it provides ability to disable interior rendering if desired.
- **three** - Setup corresponding to predefined mode **2**
- **three_with_dash** - Setup corresponding to predefined mode **3**

When initializing using **three** or **three_with_dash**, the state of corresponding tweaking cvars at the moment of the initialization is applied to the runtime configuration. This can be used to do basic setup using the cvars in predefined mode and use the custom mode to only tweak the result.

### reload

Syntax: multimon reload

Example: multimon reload

Replaces the runtime configuration using a content of **multimon_config.sii**

### save

Syntax: multimon save

Example: multimon save

Saves the current runtime configuration to **multimon_config.sii**. This **MUST** be used for the changes to persist restart of the game or change of display settings.

### add

Syntax: multimon add &lt;name&gt; &lt;x&gt; &lt;y&gt; &lt;width&gt; &lt;height&gt;

Example: multimon add left 0.25 0 0.5 1

Defines monitor in specified area of output resolution and associates it with specified name. Note that name ui is reserved for special use.

### remove

Syntax: multimon remove &lt;name&gt;

Example: multimon remove left

Removes monitor associated with specified name.

### make primary

Syntax: multimon make_primary &lt;name&gt;

Example: multimon make_primary center

Marks specified monitor as primary. The primary monitor is used as source of base values for some relative attributes and the HDR eye adaptation is calculated from this monitor. This corresponds to the first monitor defined in the config file.

### list

Syntax: multimon list

Example: multimon list

List names of all defined monitors

### set

Syntax: multimon set &lt;name&gt; &lt;attribute&gt; &lt;value&gt;

Example: multimon set left horizontal_fov_override 60

Sets specified attribute for specified monitor. Special monitor name ui allows changes of position of the ui itself.

### get

Syntax: multimon get &lt;name&gt; [<attribute_prefix>]

Example: multimon get left normalized_

Prints values of all attributes of specified monitor whose name begins with specified prefix. As with set ui provides access to the ui itself.

## Supported attributes for **get** and **set**

| Name | Example | Description |
| --- | --- | --- |
| `normalized_ui_x` | `normalized_ui_x: 0.333333` | Decimal between 0 an 1. Horizontal position in the whole virtual screen to start drawing the UI. For instance, second monitor in a 3-monitor setup would be **0.333333**. Third monitor would be **0.666666**. In a two-monitor setup where UI should be drawn in the rightmost monitor, **0.5**. |
| `normalized_ui_width` | `normalized_ui_width: 0.333333` | Decimal between 0 and 1. Width the UI should take in the whole virtual screen. For one monitor in a 3-monitor setup, **0.333333** (1/3 of the whole area), 2-monitor, **0.5**. To take the space of all monitors it should be **1.0** and **normalized_ui_x** above, **0.0**. |
| `name` | `name: middle` | String. A handle for the monitor to be used with `multimon get` and `multimon set`. The **ui** name is reserved. |
| `normalized_x` | `normalized_x: 0.333333` | Decimal between 0 and 1. The x-axis (horizontal) position in the whole virtual screen corresponding to the left edge of this monitor. In a 3-monitor setup 1st monitor will get **0.0**, 2nd **0.333333**, 3rd **0.666666**. 2-monitor: **0.0** and **0.5** respectively. |
| `normalized_y` | `normalized_y: 0.5` | Decimal between 0 and 1. The y-axis (vertical) position in the whole virtual screen corresponding to the bottom edge of this monitor. For 2-row monitor setup (with identical resolution and size monitors), 1st monitor should have **0.0** and 2nd monitor, **0.5**. In single-row setups, it should be **0.0**. |
| `normalized_width` | `normalized_width: 0.333333` | Decimal between 0 and 1. The x-axis (horizontal) length of the monitor in the whole virtual screen. For 3-monitor setup (with identical resolution and size monitors) all monitors should have **0.333333** whilst a 2-monitor setup, **0.5**. |
| `normalized_height` | `normalized_height: 0.5` | Decimal between 0 and 1. The y-axis (vertical) length of the monitor in the whole virtual screen. For 2-row monitor setup (with identical resolution and size monitors) all monitor should have **0.5**. In single-row setups, it should be **1.0**. |
| `heading_offset` | `heading_offset: -2.0` | Decimal value between -180.0 and 180.0. The heading angle (in degrees) added to the camera when rendering content for this monitor. |
| `pitch_offset` | `pitch_offset: -15.0` | Decimal value between -90.0 and 90.0. The pitch angle (in degrees) added to the camera when rendering content for this monitor (to compensate its tilt, angle or rotation). |
| `roll_offset` | `roll_offset: -15.0` | Decimal value between -180.0 and 180.0. The overall roll angle (in degrees) added to the camera when rendering content for this monitor (to compensate its angle or rotation). |
| `horizontal_fov_relative_offset` | `horizontal_fov_relative_offset: 1.0` | Decimal value. Additional heading angle added to the camera when rendering content for this monitor. Unlike **heading_offset** this value is expressed in multiplies of the horizontal FOV of the camera used to render the primary monitor. Should be set to 0.0 for the primary monitor. |
| `vertical_fov_relative_offset` | `vertical_fov_relative_offset: 0.0` | Decimal value. Additional pitch angle added to the camera when rendering content for this monitor. Unlike **pitch_offset** this value is expressed in multiplies of the vertical FOV of the camera used to render the primary monitor. Should be set to 0.0 for the primary monitor. |
| `camera_space_offset` | `camera_space_offset: (0.000000, 0.000000, 0.000000)``multimon set left camera_space_offset 0.0 0.0 0.0` | Triple with Decimal values for x (horizontal, left-right), y (vertical, up-down) z (depth, back-forth) coordinates. Offset added to the position of the camera when rendering content for this monitor. Notice in config file the syntax is **(x, y, z)** (wrapped by parenthesis characters, comma separated) whilst console, **x y z** (space separated sequence). |
| `horizontal_fov_override` | `horizontal_fov_override: 85.0` | Decimal value between 0.0 and 178.0. Overrides the horizontal FOV for this monitor. A value of **0.0** means **not overridden**. If both horizontal and vertical FOVs are not overridden for the monitor, then the FOV is taken from the default camera and can be adjusted using the "seat adjuster" UI. Otherwise the slider in the seat adjuster is ignored. If only one from the FOVs is overridden for the monitor, the non-overridden FOV is calculated from the overridden one to preserve the aspect ratio. |
| `vertical_fov_override` | `vertical_fov_override: 72.3` | Decimal value between 0.0 and 178.0. Overrides the vertical FOV for this monitor. For more info see **horizontal_fov_override** |
| `frustum_subrect_x` | `frustum_subrect_x: 0.3` | Decimal value between 0 and 1. Sets the left edge of the visible part of the view frustum used to render this monitor. The resulting frustum content is stretched to fit the screen area defined by the **normalized_*** settings. Can be used to create asymmetrical FOV. |
| `frustum_subrect_y` | `frustum_subrect_y: 0.3` | Decimal value between 0 and 1. Sets the bottom edge of the visible part of the view frustum used to render this monitor. See **frustum_subrect_x** |
| `frustum_subrect_width` | `frustum_subrect_width: 0.3` | Decimal value between 0 and 1. Sets the width of the visible part of the view frustum used to render this monitor. See **frustum_subrect_x** |
| `frustum_subrect_height` | `frustum_subrect_height: 0.3` | Decimal value between 0 and 1. Sets the height of the visible part of the view frustum used to render this monitor. See **frustum_subrect_x** |
| `render_interior` | `render_interior: true``multimon set middle render_interior 1` | Boolean true/false (1/0). Whether to render or not interior (dashboard). Notice in the config file **true** and **false** are accepted values. In console, you should use **1** and **0**, respectively. |
| `render_exterior` | `render_exterior: true``multimon set middle render_exterior 1` | Boolean true/false (1/0). Whether to render or not the exterior (all except dashboard, actually). Notice in the config file **true** and **false** are accepted values. In console, you should use **1** and **0**, respectively. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Console/Commands/multimon | revision: 5612 | captured: 2026-10-21 23:56:14 -->
