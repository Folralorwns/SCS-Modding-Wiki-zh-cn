# Documentation/Tools/SCS Blender Tools/Export Panel

Export panel is located within *Output* tab of properties window and offers a quick way for content export to the game.

[![SCS_Tools_Export_00.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Export%20Panel/SCS_Tools_Export_00.280.png)](../../../../files/SCS%20Tools%20Export%2000.280.png.md)

## Export modes (Scope)

### Selection

Exports only selected objects, while there are certain logical rules for deciding about objects' inclusion in export from initial selection. When the Root Object is selected, all its content will be exported. When only some mesh objects are selected, then only those are exported for their Game Objects. In these cases it is not important if their Root Object is selected or not.

When checkbox on the left of **Selection** button is ticked, then before export all the objects that will be exported will be isolated in local view. This is very good way, how to be sure about exported content. It will always show only geometries and locators, that are going to be exported. Selection previewing is extra mode, where you can use ***Numpad*** keys for view manipulation similar way like Blender standardly does – ***4*** and ***6*** keys turn the view left and right, ***8*** and ***2*** keys up and down and ***+*** and ***-*** will zoom in and out. If you press ***Enter*** the export begins and with ***Esc*** key you can cancel the export and get back to the previous selection state.

### Active Scene

Exports all properly set Game Objects in current scene.

> > **Note:** You can specify in each Root Object whether its content has to be exported or not using “Export Inclusion” switch.

### All Scenes

Exports all properly set Game Objects in all scenes in current Blender file.

> > **Note:** You can specify in each Root Object whether its content has to be exported or not using “Export Inclusion” switch.

## Other export options

### Default Export Path

Here you can specify relative filepath inside "SCS Project Base Path" where your Game Objects will be exported.

How is default export path used:

1. If default export path is empty, Blender Tools will try to export Game Object beside saved Blender file.
2. If default export path is set, Blender Tools will combine "SCS Project Base Path" with given default export path to export files there.
3. If Blender Tools can't find any solution for cases above, files are exported directly into "SCS Project Base Path".

> > **Note:** If input field will be marked red, then path is invalid and extra button for more info will be shown.

> > **Note:** Export path can be overwritten on Root Object by specifying "Custom Export Filepath".

### Export Scale

The resulting scale of all exported models and elements. This setting is saved and thus remembered in every Blend file.

### Apply Modifiers

Apply all modifiers before export.

### Apply Only 'Edge Split'

Apply only 'Edge Split' modifier before export to get sharp edges. All the other modifiers will be ignored.

### Output Format

Developers feature only, for now it should be always set to "Game Data Format".

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Export_Panel | revision: 4283 | captured: 2026-10-21 23:56:14 -->
