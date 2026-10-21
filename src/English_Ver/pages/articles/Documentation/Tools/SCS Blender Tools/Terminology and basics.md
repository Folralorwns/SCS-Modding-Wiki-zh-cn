# Documentation/Tools/SCS Blender Tools/Terminology and basics

## Terminology

### SCS Root Object

It is Blender “**EMPTY**” Object with appropriate setting in SCS Tools. It works as a root object and anything parented to it will become its content. It also carries set of settings for the whole such entity, that can be exported in a result as a “SCS Game Object” (see the chapter “SCS Game Object” below). For more details on “SCS Root Object” see the chapter “SCS Root Objects”.

### SCS Game Object

This is a general term for a unit, which consists of properly set “SCS Root Object” and its valid content. If one or more components from this entity are for any reason considered invalid during export, the user is informed about it in console and these items are automatically skipped. If all components are invalid, the entire “SCS Game Object” gets skipped.

### Model

By the term “Model” we simply mean any Blender object of **MESH** type.

### Locator

“Locators” we call any Blender object of **EMPTY** type, which is set as Locator in SCS Blender Tools.

[![SCS_Tools_Locators_-_initial_03.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Terminology%20and%20basics/SCS_Tools_Locators_-_initial_03.280.png)](../../../../files/SCS%20Tools%20Locators%20-%20initial%2003.280.png.md)

There are three types of Locators:

1. **Model Locator** - can be used to place (reference) existing game model. Details on Model Locators can be found in [Model Locators](Locators/Model%20Locators.md).
2. **Prefab Locator** - can be used to create various types of special items for use in prefab models. Details on Prefab Locators can be found in [Prefab Locators](Locators/Prefab%20Locators.md).
3. **Collision Locator** - can be used to create several types of collision envelopes for physical interaction of bodies in the game. Details on Collision Locators can be found in [Collision Locators](Locators/Collision%20Locators.md).

## Basic Principles

There are certain techniques to keep in mind in order to create and work with models for SCS game engine:

### Parts

There is a Part name assigned to every object in the scene. This way it is possible to define a sets of objects, which can make a larger units. Details on Parts can be found in [Part system](Part%20system.md).

### Variants

Parts has to be assigned to a groups which are fittingly called Variants. They can be easily used to create different variations of any SCS Game Object by creating a new Variant and by assigning some existing Parts to it. Every Variant of such model thus will be exported and will be available in the game. Details on Variants can be found in [Variant system](Variant%20system.md).

### Multi Model Work-flow

The main difference compared to the usual approach to model creation is the fact that so-called “SCS Game Objects” can be created in unlimited amount in a single scene. Any “SCS Game Object” may consist of many individual model objects and carries its own Part List and Variant List as well as some other settings. The only condition is that anything forming such “SCS Game Object” must be parented to the “SCS Root Object” either directly or indirectly. These SCS Game Objects can be exported into the game, individually or in the batch.

### Materials

To properly set the materials that works in the game it is essential to use only the settings contained in the special palette “SCS Materials”. If you change the properties of the materials using standard Blender's material palettes, the appearance of materials in the 3D View will change, but settings of SCS Materials remain the same. Details on Materials can be found in [Materials](Materials.md).

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Terminology_and_basics | revision: 4271 | captured: 2026-10-21 23:56:14 -->
