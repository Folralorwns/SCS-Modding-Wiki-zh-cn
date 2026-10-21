# Documentation/Tools/SCS Blender Tools/Scene Lighting

SCS Lighting panel enables easy to setup scene lighting by using game sun profile data and may be used for replicating different times of day from the SCS game. Panel can be found under *World* tab inside Blender properties window.

If SCS Lighting is disabled (checkbox on the left side of panel header is unticked), then Blender uses fully featured reference lighting for SCS Materials, representing neutral lighting in the middle of the day. But if you want to use your own settings or same sun profiles data as game does, then tick the checkbox in header and either setup reference profile yourself by changing values in **Active Sun Profile Settings** sub-panel or search for a sun profiles SII definition file (usually found inside game structure under: "/def/climate/<climate_type>/<weather_type>.sii"). Selecting desired sun profile entry in the list, applies it's settings to Blender scene lighting.

[![SCS_Blender_Tools_Lighting.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Scene%20Lighting/SCS_Blender_Tools_Lighting.280.png)](../../../../files/SCS%20Blender%20Tools%20Lighting.280.png.md)

## Sun Profiles Lib

*[“*.sii” file, absolute or relative path to 'SCS Project Base Path']*

Represents path to SII definition file with sun profiles. Once given list below will be populated with all sun profiles found in the file.

## SCS Lighting East

Property defining east sky direction. Changing this property will rotate whole lighting scene around global Z axis - assigns direction of the sun light.

There is also locking option placed beside lighting east: [![Blend_icon_lock_east.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Scene%20Lighting/Blend_icon_lock_east.png)](../../../../files/Blend%20icon%20lock%20east.png.md). This option will force lamps to follow rotation of the camera in 3D view on global Z-axis. Once option is unchecked lamps will remain in place. So you can easily use this option to move east lighting around in 3D view by your liking.

## Active Sun Profile Settings

This section is showing lighting values of currently selected sun profile in the list. By changing any value in this section, scene lighting will be updated accordingly to currently set values.

Settings of any selected sun profile can freely be changed, but they won't be saved back to SII definition file, so if you reload sun profiles library all changes done will be lost.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Scene_Lighting | revision: 4289 | captured: 2026-10-21 23:56:14 -->
