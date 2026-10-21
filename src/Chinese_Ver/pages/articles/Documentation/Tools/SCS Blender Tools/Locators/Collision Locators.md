# Documentation/Tools/SCS Blender Tools/Locators/Collision Locators

Collision locators are used for simulation of realistic physical interactions between objects in game. There are four types of primitives: **Box**, **Sphere**, **Capsule** and **Cylinder**. Beside primitives there is also special type of collision locator named **Convex** which uses convex geometry instead.

Each locator object has its own display options which will set rendering mode of locator in 3D view. You can switch rendering of wire frame (**Wireframes**) and shell (**Faces**) of locator.

All primitive collision locators have **Locator Centered** property, which will position primitive to center of locator.

All types also features physical property **Mass Weight** which specifies mass of the object.

### Box

[![SCS_Tools_Locators_Collision_1Box_01.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Collision%20Locators/SCS_Tools_Locators_Collision_1Box_01.280.png)](../../../../../files/SCS%20Tools%20Locators%20Collision%201Box%2001.280.png.md)

- **X/Y/Z Dimension** - size of the body on each axis.

### Sphere

[![SCS_Tools_Locators_Collision_2Sphere_01.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Collision%20Locators/SCS_Tools_Locators_Collision_2Sphere_01.280.png)](../../../../../files/SCS%20Tools%20Locators%20Collision%202Sphere%2001.280.png.md)

- **Sphere Diameter** - size of the sphere.

### Capsule

[![SCS_Tools_Locators_Collision_3Capsule_01.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Collision%20Locators/SCS_Tools_Locators_Collision_3Capsule_01.280.png)](../../../../../files/SCS%20Tools%20Locators%20Collision%203Capsule%2001.280.png.md)

- **Capsule Diameter** - size of the capsule ending.
- **Capsule Length** - length of the capsule body.

### Cylinder

[![SCS_Tools_Locators_Collision_4Cylinder_01.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Collision%20Locators/SCS_Tools_Locators_Collision_4Cylinder_01.280.png)](../../../../../files/SCS%20Tools%20Locators%20Collision%204Cylinder%2001.280.png.md)

- **Cylinder Diameter** - diameter of cylinder.
- **Cylinder Length** - length of cylinder body.

### Convex

[![SCS_Tools_Locators_Collision_5Convex_01.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Collision%20Locators/SCS_Tools_Locators_Collision_5Convex_01.280.png)](../../../../../files/SCS%20Tools%20Locators%20Collision%205Convex%2001.280.png.md)

- **Collision Margin** - scales the convex envelope by the same distance on all axis.

Convex locator features additional info line which tells you how many vertices is in this convex locator.

For easy convex locator creation, please see the section [SCS Tools in Tool Shelf#Convex](../SCS%20Tools%20in%20Tool%20Shelf.md#Convex).

> > **Note:** Keep in mind that convex locator should have really small amount of vertices (ideally up to 64 vertices) because of expensive calculations in game.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Locators/Collision_Locators | revision: 5740 | captured: 2026-10-21 23:56:14 -->
