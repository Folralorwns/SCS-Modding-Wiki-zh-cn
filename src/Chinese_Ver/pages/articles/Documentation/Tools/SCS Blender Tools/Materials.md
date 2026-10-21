# Documentation/Tools/SCS Blender Tools/Materials

SCS Blender Tools uses its own material settings, so every material in Blender contains a panel called **SCS Material** in *Material* tab of Blender properties window. It is essential to use settings here exclusively to set up any available material properties. If you'll be changing the material's settings in Blender's standard panels, the appearance of the material will change in 3D View, but the SCS material settings will not change and exported material may look very different when viewed in SCS Game Engine.

## Render and 3D View Setup

To get closest result to the one in SCS Game Engine you should use EEVEE render engine:

[![SCS_Material_Specials_-_EEVEE.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_EEVEE.280.png)](../../../../files/SCS%20Material%20Specials%20-%20EEVEE.280.png.md)

and switch *Viewport Shading* to *Rendered* to see models rendered properly.

[![SCS_Material_Specials_-_Rendered_Viewport.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_Rendered_Viewport.280.png)](../../../../files/SCS%20Material%20Specials%20-%20Rendered%20Viewport.280.png.md)

> > **Note:** By default fully fledged reference lighting will be used, but if you want to create specific in-game time of the day like lighting, please refer to: [Scene Lighting](Scene%20Lighting.md)

## Merge Materials

SCS Material panel also features one well hidden powerfull operator: **Merge Materials** located in panel header on the right side:

[![SCS_Material_Specials_-_Merge_Materials.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_Merge_Materials.280.png)](../../../../files/SCS%20Material%20Specials%20-%20Merge%20Materials.280.png.md)

This operator is able to merge materials depending on selected criteria from the newly appearing dialog when operator button is pressed.

## Shader Usage

SCS Materials are created on the base of shader presets. When user is creating and using SCS Materials he can use any shader preset found in the list and switch/edit material flavors, attributes and textures. However second type of shader usage is imported shader, which is exclusively created only on import when model is using material effect that can not be found inside shader presets.

### Shader Preset

[![SCS_Material_Specials_-_Shader_Preset.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_Shader_Preset.280.png)](../../../../files/SCS%20Material%20Specials%20-%20Shader%20Preset.280.png.md)

SCS Materials panel features the list of *Shader Presets*, where you can choose from materials with its own predefined values and change some of them to your liking. Moreover each shader preset now also features flavors, which are common extensions to many shaders.

Flavors are changing behaviour of shader it's full effect name and in some cases adding or removing some material attributes or textures. Some flavors may not change mesh visually as they are used for different purposes. For example "shadow" flavor will tell shader to use this material also as shadow caster and thus there is nothing that should visually change on the mesh.

### Imported Shader

[![SCS_Material_Specials_-_Imported_Shader.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_Imported_Shader.280.png)](../../../../files/SCS%20Material%20Specials%20-%20Imported%20Shader.280.png.md)

When you import any existing game model and some of the materials cannot be found in existing shader presets, "Imported Shader" is created. Attributes cannot be edited, but it will still export correctly as it was in original file. Though textures and their mappings can be changed for visual preview.

Additionally there is "Mappings" field inside "Textures" for this type of shader, where "tex_coord_X" entries specify which UV layer will be exported for this alias.

## Properties and usage

Properties in material are shader type dependent. So each type of shader may have different attributes and textures.

### Substance

Substance property is item from list of physical materials, which is loaded from Material Substance Library file (see [Global Settings#Path Settings](Global%20Settings.md#Path_Settings)). These can for example set up the physical type of the road surface.

### Material Attributes

In this section you can find various visual shader attributes, that you can alter. Most important ones are interactively reflected on your model in 3D View.

### Material Textures

This section provides an interface for specifying texture images for different shader's texture channels. Most prominent textures are automatically loaded and displayed in the 3D View.

#### Texture

Property defining path to texture or texture object file (TOBJ - pointers to texture images). Using map icon on the side of this property will open file browser where you will be able to select image or any TOBJ for using it as texture. After selecting, the image will be automatically applied to material. Beside currently selected shader preset search button can be found, which enables you to quickly search trough available presets.

> > **Note:** Usage of texture which is not from SCS project directory (see [Global Settings#Path Settings](Global%20Settings.md#Path_Settings)) and it's sub-directories may cause errors and warnings on export!

#### Settings

Each texture also features extra row of controls for TOBJ file and it's settings. TOBJ's are by default created upon export if they don't exist yet. However create button will appear if TOBJ file doesn't exist yet and pressing it will create TOBJ file for this texture with default settings. In case this texture already has TOBJ file then reload button, with which you can load currently saved settings of this TOBJ, will be shown. Sometimes reload button may appear in red color which indicates that current settings are outdated and you should press reload button to reload them. As soon as TOBJ file exist you will also have access to change any value in settings itself. Changing any of the setting in settings list will rewrite TOBJ file with updated values right away.

- ***U Repeat*** - repeat texture in U direction.
- ***V Repeat*** - repeat texture in V direction.
- ***TS Normal*** - tangent space normal for the texture.
- ***Color Space Linear*** - texture is in linear color space (this option should be used on occlusion type of shaders in combination with grayscale occlusion texture).

#### Mapping

This property specifies which UV layer will be used for this texture. For some textures you may need to specify more then one UV layer, depends on which shader preset is used.

### Material Item Extras Menu

Additionally there is *More Options* menu button ( **𐩒** ) for most of the material attributes. Some can be written through (more about write trough: [Look system#Write Through](Look%20system.md#Write_Through)) and some can be even copied as or pasted from linear color space.

[![SCS_Material_Specials_-_Extras_Menu.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_Extras_Menu.280.png)](../../../../files/SCS%20Material%20Specials%20-%20Extras%20Menu.280.png.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Materials | revision: 4357 | captured: 2026-10-21 23:56:14 -->
