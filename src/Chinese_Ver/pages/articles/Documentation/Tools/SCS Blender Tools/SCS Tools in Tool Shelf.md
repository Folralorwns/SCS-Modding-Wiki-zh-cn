# Documentation/Tools/SCS Blender Tools/SCS Tools in Tool Shelf

![SCS_Tools_Shelf.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/SCS_Tools_Shelf.png)

SCS Tools shelf consist of set of tools which can be used for objects in 3D viewport.

## Tool Shelf

### Add Root

Creates a new SCS Root Object. If there is any selection, it will automatically set these objects for SCS Game Object content by parenting it to the SCS Root Object.

### Add Root (with name request)

Creates a new SCS Root Object. User can specify a name for the Root object in a window, that will appear. If there is any selection, it will automatically set these objects for SCS Game Object content by parenting it to the SCS Root Object.

### Check Geometry

Checks selected objects for degenerated polygons which shall be removed before exporting, as they might cause FPS drop-down with some graphics cards. Operator takes selected objects and selects vertices of degenerated polygons. Degenerated polygons are discovered trough [Heron's Formula](https://en.wikipedia.org/wiki/Heron%27s_formula).

### VColoring

Enters a complex [Vertex coloring](SCS%20Tools%20in%20Tool%20Shelf/VColoring.md) mode, where you can edit 4 vertex color layers which are baked to vertex color layer used by shader and export in real-time. The extra icon button [![Blend_icon_file_refresh.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/Blend_icon_file_refresh.png)](../../../../files/Blend%20icon%20file%20refresh.png.md) on the side gives you ability to freshly rebake 4 layers in case you edited one of them by hand without using **VColoring** operator.

## Convex

### Make Convex

Makes a new object from selected Model objects. This new object is always convex and can be used as a base for convex colliders.

### Convert to Locator

Converts selected objects into a new Collider Locator. There are additional choices for deleting of source object(s) – Delete Original Geometry, and for creating a single Locator or multiple Locators from every selected object – Individual Objects.

### Convert to Mesh

Converts selected Collision Locator(s) into editable Model (Mesh) object(s).

## Visibility Tools

Visibility tools consists of sub-panel for viewing objects by type and three additional visibility operators.

### Switching by type

[![SCS_Tools_Shelf_Op_Table.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/SCS_Tools_Shelf_Op_Table.png)](../../../../files/SCS%20Tools%20Shelf%20Op%20Table.png.md)

First table alters visibility of Model and Locators objects. Second table is used only for Prefab Locators.

### Global vs. SCS Root

This option switches scope of visibility operators in this sub-panel. When using ***Global*** operators will be applied among all of the objects in current scene, in the case of ***SCS Root*** only the objects within current SCS Game Object will be altered.

### Current SCS Root

Additional operators for switching visibility of objects within the SCS Game Object of active object:

- ***Invert Visibility*** - inverts visibility of all objects.
- ***View All*** - shows all objects.
- ***Isolate*** - show all objects within SCS Game Object of active object and hide all other objects in scene.

## Display Methods

### Glass Objects

- ***Wires / Textured*** - two operators for quick setting of the drawing type for all Glass objects in the scene.

### Shadow Casters

- ***Wires / Textured*** - two operators for quick setting of the drawing type for all Shadow caster objects in the scene.

### Collision Locators

- ***All Wires / No Wires*** - operators to quickly turn ON or OFF all the wires in all Collision Locators in the scene.
- ***All Faces / No Faces*** - operators to quickly turn ON or OFF all the faces in all Collision Locators in the scene.

## See also

Depending on the current 3D viewport mode in Blender you will also find:

1. [Lamp Switcher & UV Tool](SCS%20Tools%20in%20Tool%20Shelf/Lamp%20Switcher%20&%20UV%20Tool.md) -> while in **Edit Mode**
2. [Wrap & Stats Tools](SCS%20Tools%20in%20Tool%20Shelf/Wrap%20&%20Stats%20Tools.md) -> while in **Vertex Paint** mode

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/SCS_Tools_in_Tool_Shelf | revision: 3439 | captured: 2026-10-21 23:56:14 -->
