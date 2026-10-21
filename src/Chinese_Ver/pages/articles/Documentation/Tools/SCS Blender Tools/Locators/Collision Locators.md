# 文档/工具/SCS Blender Tools/定位器/碰撞定位器

碰撞定位器用于模拟游戏中对象之间逼真的物理交互。共有四种基本几何体类型：**Box**、**Sphere**、**Capsule** 和 **Cylinder**。除基本几何体之外，还有一种名为 **Convex** 的特殊碰撞定位器类型，它改用凸包几何体。

每个定位器对象都有各自的显示选项，用于设置定位器在 3D 视图中的渲染模式。你可以切换定位器的线框（**Wireframes**）与外壳（**Faces**）渲染。

所有基本几何体碰撞定位器都具有 **Locator Centered** 属性，该属性会将基本几何体置于定位器中心。

所有类型还具有物理属性 **Mass Weight**，用于指定对象的质量。

### 盒体

[![SCS_Tools_Locators_Collision_1Box_01.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Collision%20Locators/SCS_Tools_Locators_Collision_1Box_01.280.png)](../../../../../files/SCS%20Tools%20Locators%20Collision%201Box%2001.280.png.md)

- **X/Y/Z Dimension** - 碰撞体在各轴上的尺寸。

### 球体

[![SCS_Tools_Locators_Collision_2Sphere_01.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Collision%20Locators/SCS_Tools_Locators_Collision_2Sphere_01.280.png)](../../../../../files/SCS%20Tools%20Locators%20Collision%202Sphere%2001.280.png.md)

- **Sphere Diameter** - 球体的尺寸。

### 胶囊体

[![SCS_Tools_Locators_Collision_3Capsule_01.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Collision%20Locators/SCS_Tools_Locators_Collision_3Capsule_01.280.png)](../../../../../files/SCS%20Tools%20Locators%20Collision%203Capsule%2001.280.png.md)

- **Capsule Diameter** - 胶囊末端的尺寸。
- **Capsule Length** - 胶囊体的长度。

### 圆柱体

[![SCS_Tools_Locators_Collision_4Cylinder_01.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Collision%20Locators/SCS_Tools_Locators_Collision_4Cylinder_01.280.png)](../../../../../files/SCS%20Tools%20Locators%20Collision%204Cylinder%2001.280.png.md)

- **Cylinder Diameter** - 圆柱的直径。
- **Cylinder Length** - 圆柱体的长度。

### 凸包

[![SCS_Tools_Locators_Collision_5Convex_01.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Collision%20Locators/SCS_Tools_Locators_Collision_5Convex_01.280.png)](../../../../../files/SCS%20Tools%20Locators%20Collision%205Convex%2001.280.png.md)

- **Collision Margin** - 在所有轴上以相同距离缩放凸包外壳。

凸包定位器还提供一行额外信息，显示该凸包定位器中有多少个顶点。

要便捷地创建凸包定位器，请参见 [SCS Tools in Tool Shelf#Convex](../SCS%20Tools%20in%20Tool%20Shelf.md#Convex) 一节。

> > **注意：** 请记住，凸包定位器的顶点数量应非常少（理想情况下最多 64 个顶点），因为游戏中的计算开销较大。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Locators/Collision_Locators | revision: 5740 | captured: 2026-10-21 23:56:14 -->
