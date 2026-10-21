# Documentation/Tools/SCS Blender Tools/Global Settings

Global Settings hold common settings to whole SCS Blender Tools addon and are defined either per-machine or per-blender file, depending on user choice.

***SCS Global Settings*** panel can be found inside ***Workspace*** settings of the Properties window.

[![SCS_Tools_Globals_01.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Global%20Settings/SCS_Tools_Globals_01.280.png)](../../../../files/SCS%20Tools%20Globals%2001.280.png.md)

There are three sub-panels categorizing properties into proper layout.

## Path Settings

Before you start to use the tools, it is necessary to specify where to access data sources, which are used for filling up of some library menus and addressing textures.

First of all, you’ll need to set the main folder that contains your project. Do it to the “SCS Project Base Path” entry. Other routes usually proceed from that location, and therefore can be stored in the form of a relative path. However that doesn’t need to be the rule every time and therefore the mechanism for path selection in the SCS Tools will always decide the appropriate form for the path.

If paths are set properly is clearly seen from color of its background – if any entry is faulty, the background is in red color and needs to be set to the valid location or valid library file.

[![SCS_Tools_Globals_Path_01.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Global%20Settings/SCS_Tools_Globals_Path_01.280.png)](../../../../files/SCS%20Tools%20Globals%20Path%2001.280.png.md)

### SCS Project Base Path

*[folder, always absolute path]*

***This is most important path, which leads to “base” root directory of your mod for any SCS game. Base directory always has to have specific structure, because of relative texture and definition file addressing.*** So all of the paths of following libraries should continue from this location and should be in relative form. However if you prefer another location for those libraries, you can use it and the path form will be automatically chosen.

> > **Note:** For importing sample models make sure you set SCS Project Base Path to one of the sample base folders inside "data" directory of downloaded SCS Blender Tools package.

### Trigger Action Library

*[“*.sii” file, absolute or relative path to 'SCS Project Base Path']*

Library of predefined trigger actions. You can assign them to Trigger Prefab Locators which are used in game for triggering various actions (for example sleeping areas).

### Sign Library

*[“*.sii” file, absolute or relative path to 'SCS Project Base Path']*

Library of predefined traffic Signs. You can assign them to Sign Prefab Locators which are used in game to create traffic signs or any model defined as sign. Most of them are respected by AI cars and lay the traffic rules for player.

### Semaphore Library

*[“*.sii” file, absolute or relative path to 'SCS Project Base Path']*

Library of predefined Traffic Semaphore profiles. You can assign them to Traffic Semaphore Prefab Locators which are used in game to create traffic semaphores. These are respected by AI cars and should be respected by player as well.

### Traffic Rules Library

*[“*.sii” file, absolute or relative path to 'SCS Project Base Path']*

Library of predefined Traffic Rules. You can assign them to Navigation Point Prefab Locators which are used in game to create traffic routes. These are used mainly by AI cars.

### Hookup Library

*[folder, absolute or relative path to 'SCS Project Base Path']*

Directory containing predefined Hookup files. You can assign them to Model Locators which are used in game to instance other game models within actual model.

### Mat Substance Library

*[“*.db” file, absolute or relative path to 'SCS Project Base Path']*

Library of Material Substances, which defines physical behavior of the material. You can assign them to Materials.

### Shader Presets Library

*[“*.txt” file, absolute file path]*

Shader Presets library loads all effects that can be used in SCS Materials. By default this path will be empty, as SCS Blender Tools is taking internal shader presets library, but if you ever want to use custom library, make sure to tick checkbox on left side of filepath and then search for your custom shader presets library.

## Display Settings

The “Display Settings” sub-panel brings together visual settings for all the special elements that are part of SCS Blender Tools. You can find here a visual settings for Locators, their Curves, Preview Models and other specific elements, which detail explanation follows in the text below.

[![SCS_Tools_Globals_Display.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Global%20Settings/SCS_Tools_Globals_Display.280.png)](../../../../files/SCS%20Tools%20Globals%20Display.280.png.md)

### Drawing Mode

Drawing mode for custom elements (i.e. Locators and Connections). It switches between Normal and X-Ray mode. Normal mode use normal depth testing drawing so all the custom elements are drawn within the scene the same way as the other objects, while the X-Ray mode use X-Ray drawing making all the custom elements visible on top of the other objects.

### Icon Theme

Here you can select desired icon theme to use for custom SCS Blender Tools icons, depending on which suits to your blender theme the best. By default White theme is used.

### Display Info Texts

Switches displaying of different additional information texts for Locators directly in 3D View. This is very useful when you work on Prefab models. For example, you can display only the Locator Names, or Boundary Lanes or Nodes.

### Info Text Color

Custom color for Info Texts.

### Base Paint Color

For greater diversity in SCS games there is paintable functionality, which is usually used on AI traffic cars and makes each car use different colors based on its configuration in SII file. However as Blender Tools does not read this kind of SII files, every shader with "paint" flavor will use this base paint color property for previewing.

In case you don't want to change look of shaders with this functionality make sure this property in display setting has set complete white color RGB(1.0, 1.0, 1.0).

### Show Preview Models

Turns on and off displaying of Preview models for Locators.

### Locators Display (Subpanel)

Turns on and off displaying of custom representation of Locators. This can be useful especially when tuning Navigation curves.

### Locator Size

Drawing size of Locators' custom representation.

### Locator Empty Object Size

Drawing size ratio of selectable Empty objects in Locators. Alter it if you experience difficulties with selecting of Locators.

### Prefab Loc Color

Custom color for Prefab Locators.

### Model Loc Color

Custom color for Model Locators.

### Collider Loc Wire Color

Custom color for Collider Locators wire frames.

### Collider Loc Face Color

Custom color for Collider Locators faces.

### Connections Display (Subpanel)

Turns on and off displaying of Locators connections - Curves and Lines.

### Optimized Connections Draw

Draw connections only when data are updated. Switching this off might give you FPS (frames per second), especially on heavy Prefab scenes.

### Curve Segments

Number of segments for Navigation Curves. It can improve update speed of 3D View.

### Nav Curves Color

Custom color for Navigation Curves.

### Map Line Color

Custom color for Map Lines.

### Trigger Line Color

Custom color for Trigger Lines.

## Other Settings

[![SCS_Tools_Globals_Other.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Global%20Settings/SCS_Tools_Globals_Other.280.png)](../../../../files/SCS%20Tools%20Globals%20Other.280.png.md)

### Copy BT Log To Clipboard

Simple tool to copy log of Blender Tools to clipboard. Clipboard will have whole Blender Tools log since Blender was started up.

This tool can be used to easily grab log when you want to report some issues with your usage of Blender Tools.

### Log Level

Sets level of logging inside Blender console. Recommended level for normal usage is 2, however when trying to investigate bugs or errors it is useful to use logging up to level 4.

### Use Global Settings

Sets place of global settings storage:

1. ***From Common Config File*** - will save global settings into one same config.txt file, thus this option will give you same settings for all Blender files you will be working on (global settings per machine). > > **Note:** Altered items are written to the settings file (config.txt) immediately, so the next time you start Blender all the settings will be preserved, even if application experience crash. If you want to reset settings to default navigate to installed Blender Tools in file browser, delete file "io_scs_tools/config.txt" and restart Blender.
2. ***From Blend File*** - will save global settings directly into blend file, giving you opportunity for each saved Blender file to have it's own settings (global settings per blend file).

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Global_Settings | revision: 5675 | captured: 2026-10-21 23:56:14 -->
