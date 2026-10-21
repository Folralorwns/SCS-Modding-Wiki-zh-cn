# Documentation/Engine/Multi monitor configuration

## Prerequisites

Only multimon configurations which are presented to the game as a single big resolution virtual screen are supported. You need to be using either Nvidia Surround or AMD Eyefinity or equivalent depending on your graphics chipset type. When using the game set up with multiple separate views per the instructions below, the driver based bezel correction (the one that your display drivers may offer) should be disabled and the corresponding cvars (game config variables, see bellow) should be used instead to have the game handle the bezel gaps on its own.

The default interior cameras look slightly downwards to make the truck dashboard more visible. While that works well for normal monitor, it looks wrong on side views of multi monitor setup. For that reason it is recommended to set g_interior_camera_zero_pitch to 1 before launching the game to disable this feature without need to modify game data.

## Predefined modes

### Types

The game supports several built-in modes. Those modes are selected using **r_multimon_mode** cvar. Note that all built in-modes expect at least three monitors and will actually enabled only when the resolution has aspect ratio of at least 2.5:1.

Following modes are supported:

- **0** - Single view and UI covering entire area. The display is represented as single ultra wide planar display with the UI (user interface) covering the entire area. This is the default. The disadvantage is that because of the wide FOV (field of view), the image on the sides is significantly distorted.

[![Multimon_schema_flat.png](../../../../../images/articles/Documentation/Engine/Multi%20monitor%20configuration/Multimon_schema_flat.png)](../../../files/Multimon%20schema%20flat.png.md)

- **1** - Single view covering entire area with the UI elements positioned in the center of the third monitor (e.g. on the center monitor in three-monitor setup). This is similar to **0** however the UI covers only the area of the center monitor.
- **2** - Three separate views for three monitors. Each monitor has its own view, with the default FOV of 50 degrees horizontally. UI is positioned on the center monitor.

[![Multimon_schema_3.png](../../../../../images/articles/Documentation/Engine/Multi%20monitor%20configuration/Multimon_schema_3.png)](../../../files/Multimon%20schema%203.png.md)

- **3** - Uses leftmost three monitors from a four-monitor setup to show the same views as with **2** and the last monitor shows auxiliary view looking downwards at the dashboard and steering wheel.

[![Multimon_schema_31.png](../../../../../images/articles/Documentation/Engine/Multi%20monitor%20configuration/Multimon_schema_31.png)](../../../files/Multimon%20schema%2031.png.md)

### Additional configuration

The visualization in modes **2** and **3** can be further controlled by following cvars:

- **r_multimon_border_fov_left** and **r_multimon_border_fov_right** - Visual angle in degrees covered by the bezel (e.g. monitor frame) between center and left/right monitor. Used for bezel correction.
- **r_multimon_fov_horizontal** and **r_multimon_fov_vertical** - Field of view used for each view. If only one from them is nonzero, the remaining one is calculated to keep the aspect ratio of the resolution. If both are zero, the default FOV calculation based on current in-game camera is used.
- **r_multimon_vert_offset_left** and **r_multimon_vert_offset_right** - Vertical offset in meters of the left/right monitor from the center one. Can be used to move the left side view up or down to improve visibility of the mirrors given the limited vertical field of view.
- **r_multimon_rotation_center**, **r_multimon_rotation_left**, **r_multimon_rotation_right** and **r_multimon_rotation_aux** - Additional counter-clockwise rotation applied to of views of individual monitors. Most likely used with value 90 or -90 to compensate for monitor which is physically in different orientation (e.g. portrait vs landscape) than configured in the graphics driver. This allows for mixing portrait and landscape orientations even when not supported by the driver.
- **r_multimon_interior_in_main** - Controls rendering of the cabin interior in the main views. Can be used to disable interior if some form of physical interior is present.
- **r_multimon_exterior_in_aux** - Controls rendering of the exterior to the auxiliary view (mode 3). Note that shadows are currently still updated even if exterior is disabled.

## Customized mode

This mode allows bigger flexibility over the setup for 1-4 monitors. It is enabled by setting **r_multimon_mode** cvar to 4. Note that unlike the predefined modes, this mode can be enabled regardless of the aspect ratio of the display. In this mode the game takes the configuration from **\Documents\<game name>\multimon_config.sii**. If the file does not exist, it is created the first time the game starts in this mode. You can either edit the file manually or use in-game [multimon](Console/Commands/multimon.md) command to do most adjustments on the fly. Note that when using the **[multimon](Console/Commands/multimon.md)** command, care must be taken to explicitly save the result before exiting the game or changing settings using the game options screen as the changes would be lost in that case.

Position of the UI and monitors in the virtual display created by driver is specified using normalized coordinates where [0,0] corresponds to left bottom corner and [1,1] corresponds to top right corner. Entire monitor or UI must fit inside the [0;1] range or the behavior is undefined.

### Attributes of the ui

- **normalized_ui_x** - Position of bottom left corner of the UI in the virtual display created by driver.
- **normalized_ui_width** - Width of the UI inside the virtual display created by driver.

### Attributes of single monitor

- **name** - Name of the monitor for use with **[multimon](Console/Commands/multimon.md)** command.
- **normalized_x** and **normalized_y** - Position of bottom left corner of the monitor in the virtual display created by driver.
- **normalized_width** and **normalized_height** - Dimensions of the view of the monitor in the virtual display created by driver.
- **horizontal_fov_relative_offset** and **vertical_fov_relative_offset** - This value is multiplied by field of view of the primary monitor and added to heading and pitch of the camera. Can be used to make the monitor position itself relatively when the fov of the primary monitor is calculated automatically.
- **heading_offset**, **pitch_offset** and **roll_offset** - Rotational offset in degrees added to orientation of the camera. Can be used to point the view in desired relative direction or to do bezel correction.
- **camera_space_offset** - Offset of the camera from the standard position. Can be used to move the camera to some specific position or bias it vertically to better match physical layout of monitors.
- **horizontal_fov_override** and **vertical_fov_override** - Overrides corresponding field of view angle. If both values are zero, the angle calculated by the standard camera is used. If at least one is non-zero, it is used directly and the second angle is calculated to keep the aspect ratio.
- **render_interior** - Enables rendering of the cabin interior. Can be used if you have a physical cabin.
- **render_exterior** - Enables rendering of the exterior scene (e.g. skybox, world and outside of the truck) to the view. Note that shadows cast to the view will still contain the exterior scene regardless of this setting.
- **frustum_subrect_x**, **frustum_subrect_y**, **frustum_subrect_width** and **frustum_subrect_height** - Allows to specify part of the full frustum cone which is rendered into the monitor. Can be used to move center of the projection outside of the center of the monitor. For example when using two front monitors to represent windshield of the truck while the driver is sitting before the left one, left part of the frustum can be removed to move the center of the projection before the driver. Note that change of this view will change the effective aspect ratio so both fov overrides need to be set to correct it.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Multi_monitor_configuration | revision: 1686 | captured: 2026-10-21 23:56:14 -->
