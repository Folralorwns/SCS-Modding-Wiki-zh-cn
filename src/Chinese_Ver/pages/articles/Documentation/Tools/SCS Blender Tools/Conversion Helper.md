# Documentation/Tools/SCS Blender Tools/Conversion Helper

Conversion helper panel features tools for automated files conversion and mod packing. Panel with conversion helper can be found below [Export Panel](Export%20Panel.md) located within *Output* tab in Blender properties window.

However before you use Conversion Helper you should download latest [Conversion Tools](../Conversion%20Tools.md) for the game you want to create mod for and set path to conversion tools under *Conversion Tools Path*. Additionally make sure you have checked [Intended workflow](Intended%20workflow.md) images, for better understanding how mod system works when using SCS Blender Tools and Conversion Tools.

[![SCS_Tools_Conv_Hlpr.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Conversion%20Helper/SCS_Tools_Conv_Hlpr.280.png)](../../../../files/SCS%20Tools%20Conv%20Hlpr.280.png.md)

Small razor icon located on the right side of SCS Conversion Helper panel header represents **Clean Converted Data** operator. This operator will immediately clean content that you converted before or is left there from some other time. In general this makes sure your mod won't have any unused resources (leftover textures, old materials) in the converted result. Same action can also be achieved while using [Mod Packing](../Conversion%20Tools.md#Mod_Packing) with enabled **Clean** option.

Conversion helper also support switchable **Custom Paths**. Once they are enabled conversion helper panel gets extended as seen on image below.

[![SCS_Tools_Conv_Hlpr_Custom_Paths.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Conversion%20Helper/SCS_Tools_Conv_Hlpr_Custom_Paths.280.png)](../../../../files/SCS%20Tools%20Conv%20Hlpr%20Custom%20Paths.280.png.md)

## Custom Paths Usage

Custom Paths are holding list property for multiple custom paths that you want to convert at the same time. Use this custom paths if you want to merge resources from 2 or more different mods of yours. Example usage is shown in [Intended workflow#Usual mod combined with dependency mod (using custom paths)](Intended%20workflow.md#Usual_mod_combined_with_dependency_mod_(using_custom_paths))

On the side of the list you can find operators for managing your custom paths:

- **+** - opens file selector where you should browse for new custom path you want to use.
- **−** - deletes currently selected custom path in the list.
- ⯅ - moves up currently selected custom path in the list. Ordering in the list doesn't have influence on converted result. It is only there so you can order paths however you like.
- ⯆ - moves down currently selected custom path in the list. Ordering in the list doesn't have influence on converted result. It is only there so you can order paths however you like.

## Manual Conversion

While mod packing with **Convert** already triggers automatic conversion before packing, one can still execute manual conversion. Currently there are three different variations:

- **CONVERT CURRENT SCS PROJECT** - operator which will only convert resources in your currently set SCS Project Base Path.
- **CONVERT CUSTOM MAPS** *(seen and functional only if custom paths are enabled)* - operator which converts resources only from defined custom paths.
- **CONVERT ALL** *(seen and functional only if custom paths are enabled)* - operator which converts resources from custom paths + resources from currently set SCS Project Base Path.

Usage of manual conversion is recommended when you want to pack your mod later or by hand.

## Mod Packing

This section is featuring properties and operators for packing a mod for SCS game.

First two options are specifying destination and name:

- **Mod Folder Path** - property holding folder where mod should be placed. On the side of this property you have search icon operator for auto retrieve of the mod paths for Euro Truck Simulator 2 or American Truck Simulator.
- **Mod Name** - property holding name of the mod ZIP file.

Third row defines type of the compression you want to use for your mod package:

- **Folder** - this option creates folder inside selected mod destination and copies result of conversion tools to it, instead of creating a ZIP package. Created folder is named the same as ZIP package: by mod name property.
- **ZIP (Uncompressed)** - pack mod into uncompressed ZIP file.
- **ZIP (Moderate)** - pack mod into compressed ZIP file (helper uses deflated compression, which is supported by SCS games).

Next row features switches of automated actions that can be done before mod will be packed:

- **Clean** - enable this switch if you want to make clean conversion without any leftovers from previous packing or converting.
- **Export** - enable this switch if you want to run automated Blender Tools export. Scope of the content which will be auto exported is defined with Export Scope property in [Export Panel](Export%20Panel.md).
- **Convert** - enable this switch if you want for your resources to be converted before packing. This automated conversion will convert SCS Project Base Path as well as any defined custom paths.

### PACK MOD aka Magic Button

Final magic operator found at the bottom of the panel is **>>>> PACK MOD <<<<**. This operator firstly executes enabled automated actions and on the end packs conversion tools result into the ZIP package and copies it to the selected mod destination.

So if you don't want to bother with manual exporting/converting, then for easy usage follow this few steps:

1. Set mod folder path to: "[<Game User Path>](../../Engine/Game%20user%20path.md)/mod"
2. Fill-in mod name
3. Enable all options
4. Press PACK MOD.
5. Once packing is done, run the game and try your mod out!

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Conversion_Helper | revision: 4287 | captured: 2026-10-21 23:56:14 -->
