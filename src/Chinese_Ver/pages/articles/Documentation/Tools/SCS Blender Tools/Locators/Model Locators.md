# Documentation/Tools/SCS Blender Tools/Locators/Model Locators

Model Locators can be used to place an existing game models to other game model without the need to include their data physically in host file. Simply said, these models are only referenced in the host file. This way you can for example define a places in a truck model, where mirrors or other upgrades will appear in the game by player's will.

[![SCS_Tools_Locators_-_Model_02.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Model%20Locators/SCS_Tools_Locators_-_Model_02.280.png)](../../../../../files/SCS%20Tools%20Locators%20-%20Model%2002.280.png.md)

### Name

This property here is the same as Blender Object's name and will be used by game engine (e. g. in the model of tire/wheel for ETS2, "bb" is the name of the locator which represents size of the wheel).

### Hookup

This property can be set according to records in “Hookup Library” (see the chapter “Path Settings” in [Global Settings](../Global%20Settings.md)). However hookup property is used to bind other game objects to the current. Examples of hookups are: flares for lights, pedestrian spawning on prefabs, company logos on prefabs etc.

Additionally two buttons can be found on left side:

- **🗘** button gives possibility to reload hookup library on the fly, without need to navigate to global settings panel,
- **⌕** button gives possibility to select Model Locators with same hookup value as current.

> > **Note:** Model Locators can also use "Preview Model" feature (see the chapter [Preview Models](../Locators.md#Preview_Models_on_Locators)).

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Locators/Model_Locators | revision: 4312 | captured: 2026-10-21 23:56:14 -->
