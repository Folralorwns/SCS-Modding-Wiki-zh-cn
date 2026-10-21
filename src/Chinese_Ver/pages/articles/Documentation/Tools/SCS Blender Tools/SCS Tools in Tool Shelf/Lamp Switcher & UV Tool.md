# Documentation/Tools/SCS Blender Tools/SCS Tools in Tool Shelf/Lamp Switcher & UV Tool

Any material using lamp shader is having specific configuration of textures and UV mappings (see [Lamp system](../Materials/Lamp%20system.md)).

That's why Blender Tools are having this two additional tools to easily map UV mappings to proper texture tiles and also preview desired result.

## Lamp switcher

Lamp switcher is preview tool for switching ON and OFF different type of lights in all currently created materials.

When switching ON any type of the light you will see brighten surfaces on the meshes using lamp material. If you don't see any change in 3D view there is either problem in UV mapping of the meshes or the mask texture is not properly created. Lamp switcher can be found in 3D view under SCS Tools panel and consist of three groups:

- **Vehicle** - used for switching vehicle lights
- **Auxiliary** - used for switching vehicle auxiliary lights
- **Traffic Lights** - used for switching traffic lights

> > **Note:** To see changes in 3D view you should use GLSL shading mode and use at least one lamp material on at least one object.

[![SCS_Tools_Shelf_-_Lamp_Switcher.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/Lamp%20Switcher%20&%20UV%20Tool/SCS_Tools_Shelf_-_Lamp_Switcher.png)](../../../../../files/SCS%20Tools%20Shelf%20-%20Lamp%20Switcher.png.md)

## Lamp UV Tool

Lamp UV Tool is helper tool for positioning UV mappings of selected faces. Tool will reposition mappings on the UV layer used by mask texture in lamp material.

You can use this tool only in "Edit Mode" of mesh objects. By pressing any of the buttons tool will automatically reposition selected faces UV mappings to proper texture tile depending on selected vehicle side or auxiliary lamp color or traffic light color:

- **Vehicle** - UV mappings are positioned depending on vehicle side.
- **Auxiliary** - UV mappings are positioned depending on the lit color of auxiliary.
- **Traffic Lights** - UV mappings are positioned depending on the color of traffic light.

[![SCS_Tools_Shelf_-_Lamp_UV_Tool.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/Lamp%20Switcher%20&%20UV%20Tool/SCS_Tools_Shelf_-_Lamp_UV_Tool.png)](../../../../../files/SCS%20Tools%20Shelf%20-%20Lamp%20UV%20Tool.png.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/SCS_Tools_in_Tool_Shelf/Lamp_Switcher_%26_UV_Tool | revision: 2890 | captured: 2026-10-21 23:56:14 -->
