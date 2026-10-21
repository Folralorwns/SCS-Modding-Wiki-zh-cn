# Documentation/Tools/SCS Blender Tools/Locators

Locators are used for placing special items in an [SCS Game Object](Terminology%20and%20basics.md#SCS_Game_Object).

## Creating a Locator

To create a Locator you can use standard Blender Add menu and select desired locator: (`⇧ Shift`+`A`**→ SCS Object → <choose locator type>**):

[![SCS_Tools_Locators_01.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/SCS_Tools_Locators_01.280.png)](../../../../files/SCS%20Tools%20Locators%2001.280.png.md)

When creating **Prefab** or **Collision** locator you will get additional dialog asking you to select desired sub-type.

[![SCS_Locator_Creation-Prefab_Subtype.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/SCS_Locator_Creation-Prefab_Subtype.280.png)](../../../../files/SCS%20Locator%20Creation-Prefab%20Subtype.280.png.md) [![SCS_Locator_Creation-Collision_Subtype.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/SCS_Locator_Creation-Collision_Subtype.280.png)](../../../../files/SCS%20Locator%20Creation-Collision%20Subtype.280.png.md)

## Preview Models on Locators

When you use Locators which represent some other models, it is often handy to see those models directly at the Locator's position, so you can see how the unit will look as a whole. This can be done via the Preview Models functionality. It is available for Model and Prefab Locators.

[![SCS_Tools_Locators_Preview_Model_01.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/SCS_Tools_Locators_Preview_Model_01.280.png)](../../../../files/SCS%20Tools%20Locators%20Preview%20Model%2001.280.png.md)

### Show Preview Model

Checkbox on the left side of preview model sub-panel header serves as a switch to enabling preview model.

### Path

Here you can navigate to the PIM file. Its geometries are then loaded to the locator's position to preview the target model's shape.

### Draw Type

This drop-down menu enables changing the drawing mode for the Preview Model. The choices are “Wire”, “Solid” and “Bounds”. Please note that the “Textured” drawing mode would make little sense here, since the materials for Preview Models are not loaded at this time.

> > **Note:** You can also disable/enable displaying of all Preview Models in the scene using the global option “Show Preview Models” in the [Display Settings](Global%20Settings.md#Display_Settings) sub-panel.

## See also

- [Model Locators](Locators/Model%20Locators.md)
- [Collision Locators](Locators/Collision%20Locators.md)
- [Prefab Locators](Locators/Prefab%20Locators.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Locators | revision: 4310 | captured: 2026-10-21 23:56:14 -->
