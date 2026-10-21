# Documentation/Tools/SCS Blender Tools/Look system

Looks in SCS games are used to define same model with different textures or material attributes. With this system you can easily extend your model to have several looks without exporting same geometry over and over again. Examples of typical look usage in SCS games are: gas stations, trailers, depot companies etc.

So each SCS Game Object inside Blender file has it's own definitions for looks. You can create, delete and edit look names in **SCS Looks** sub-panel under *SCS Object* panel when SCS Root Object is active or in **SCS Looks** panel in *Material* tab of Blender properties window when mesh object is active.

[![SCS_Tools_Object_Specials_-_SCS_Looks.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Look%20system/SCS_Tools_Object_Specials_-_SCS_Looks.280.png)](../../../../files/SCS%20Tools%20Object%20Specials%20-%20SCS%20Looks.280.png.md)

To change material attributes or textures for some look, you have to select it in the list shown above and then just change the material attributes. Now whenever you will change active look all of the materials in current SCS Game Object will be updated with values from this look and you will also be able to see the changes in 3D view.

> > **Note:** Using same material in multiple SCS Game Objects will adopt materials to values in currently selected SCS Game Object. With that in mind any meshes with this material in other SCS Game Objects won't be displayed properly, but still they will be properly exported.

### Write Through

Most of SCS material settings can be "written through" which means that the current value of setting is written to all looks. This way you can for example easily change texture which you want to use in all looks without selecting each look and searching for the texture over and over again.

Write through can be accessed via *More Options* menu button ( **𐩒** ) accessible on the right side of attributes:

[![SCS_Material_Specials_-_WT.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Look%20system/SCS_Material_Specials_-_WT.280.png)](../../../../files/SCS%20Material%20Specials%20-%20WT.280.png.md)

#### WT menu

Write through menu has three options:

[![SCS_Material_Specials_-_WT_Menu.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Look%20system/SCS_Material_Specials_-_WT_Menu.280.png)](../../../../files/SCS%20Material%20Specials%20-%20WT%20Menu.280.png.md)

- **WT** - will write value to all looks inside current SCS Root Object,
- **WT - Same Look on All SCS Roots** - will write value to same look on any other SCS Root Objects (if found otherwise nothing happens),
- **WT - All Looks on All SCS Roots** - will write value to all looks on all SCS Root Objects in current blend file.

> > **Note:** When you don't define any looks in the model or you have defined only one, write through won't have any effect on material.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Look_system | revision: 4336 | captured: 2026-10-21 23:56:14 -->
