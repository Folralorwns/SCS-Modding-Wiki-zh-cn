# 文档/工具/SCS Blender Tools/定位器

定位器用于在 [SCS Game Object](Terminology%20and%20basics.md#SCS_Game_Object) 中放置特殊元素。

## 创建定位器

要创建定位器，可以使用 Blender 标准的添加菜单并选择所需的定位器：（`⇧ Shift`+`A`**→ SCS Object → <choose locator type>**）：

[![SCS_Tools_Locators_01.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/SCS_Tools_Locators_01.280.png)](../../../../files/SCS%20Tools%20Locators%2001.280.png.md)

创建 **Prefab** 或 **Collision** 定位器时，会弹出额外对话框，要求你选择所需的子类型。

[![SCS_Locator_Creation-Prefab_Subtype.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/SCS_Locator_Creation-Prefab_Subtype.280.png)](../../../../files/SCS%20Locator%20Creation-Prefab%20Subtype.280.png.md) [![SCS_Locator_Creation-Collision_Subtype.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/SCS_Locator_Creation-Collision_Subtype.280.png)](../../../../files/SCS%20Locator%20Creation-Collision%20Subtype.280.png.md)

## 定位器上的预览模型

当你使用代表其他模型的定位器时，通常方便直接在这些定位器的位置看到那些模型，从而了解单元整体的外观。这可以通过预览模型功能实现。该功能适用于模型定位器和预制件定位器。

[![SCS_Tools_Locators_Preview_Model_01.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/SCS_Tools_Locators_Preview_Model_01.280.png)](../../../../files/SCS%20Tools%20Locators%20Preview%20Model%2001.280.png.md)

### 显示预览模型

预览模型子面板标题左侧的复选框用于启用预览模型。

### 路径

在此可以导航到 PIM 文件。其几何体随后会加载到定位器位置，以预览目标模型的形状。

### 绘制类型

此下拉菜单用于更改预览模型的绘制模式。可选值为 “Wire”、“Solid” 和 “Bounds”。请注意，“Textured” 绘制模式在此处意义不大，因为此时不会加载预览模型的材质。

> > **注意：** 你也可以使用 [Display Settings](Global%20Settings.md#Display_Settings) 子面板中的全局选项 “Show Preview Models” 来禁用/启用场景中所有预览模型的显示。

## 另见

- [模型定位器](Locators/Model%20Locators.md)
- [碰撞定位器](Locators/Collision%20Locators.md)
- [预制件定位器](Locators/Prefab%20Locators.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Locators | revision: 4310 | captured: 2026-10-21 23:56:14 -->
