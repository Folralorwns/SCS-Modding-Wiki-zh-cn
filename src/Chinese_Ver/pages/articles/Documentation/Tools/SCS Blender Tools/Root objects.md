# Documentation/Tools/SCS Blender Tools/Root objects

SCS Root Objects are special items, which serves as master objects for individual SCS Game Objects (see the chapter [Terminology and basics](Terminology%20and%20basics.md)). Practically it means, that any object parented to the SCS Root Object automatically belongs to its content and such unit is then called SCS Game Object. It also carries various settings for the whole unit (like [Parts](Part%20system.md), [Variants](Variant%20system.md) and [Looks](Look%20system.md)) and can be edited in the SCS Object sub-panels.

You can create a Root Object by selecting it in *SCS Object* sub-menu within standard Blender *Add* menu (`⇧ Shift`+`A`**→ SCS Object → Root Object**). Then you can access it's options in *SCS Object* panel under *Object* tab in Blender properties window.

[![SCS_Tools_Root_Object_02.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Root%20objects/SCS_Tools_Root_Object_02.280.png)](../../../../files/SCS%20Tools%20Root%20Object%2002.280.png.md)

### Export Inclusion

With this option you can enable or disable batch export of this SCS Game Object.

### Animated Model | Rigid Model

If an animated Game object is going to be exported with this switch on “Rigid Model” option, it will be without animation as it was rigid model. And obviously, if game object without animation will be exported with this switch on “Animated Model” option, it will be still rigid.

### Allow Custom Export File Path

Checkbox on left side of custom export filepath allows or disables the use of “Custom Export File Path” for this SCS Game Object.

### Custom Export File Path

Allows to set a custom file path for export of this SCS Game Object (overwrites "Default Export Path").

Specified path must be relative filepath inside "SCS Project Base Path" where this Game Object will be exported.

How is custom file path used:

1. If custom export path is empty, Blender Tools will try to export Game Object beside saved Blender file.
2. If custom export path is set, Blender Tools will combine "SCS Project Base Path" with given custom export path to export files there.
3. If Blender Tools can't find any solution for cases above, files are exported directly into "SCS Project Base Path".

> > **Note:** if input field will be marked red, then path is invalid and extra button for more info will be shown.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Root_objects | revision: 4291 | captured: 2026-10-21 23:56:14 -->
