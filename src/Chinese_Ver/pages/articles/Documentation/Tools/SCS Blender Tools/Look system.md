# 文档/工具/SCS Blender Tools/外观系统

SCS 游戏中的外观用于以不同的纹理或材质属性来定义同一个模型。借助此系统，你可以轻松地为模型扩展出多个外观，而无需反复导出相同的几何体。SCS 游戏中典型的外观用途包括：加油站、挂车、货场公司等。

因此，Blender 文件中的每个 SCS 游戏对象都有各自的外观定义。当 SCS 根对象处于激活状态时，可以在 *SCS Object* 面板下的 **SCS Looks** 子面板中创建、删除和编辑外观名称；当网格对象处于激活状态时，也可以在 Blender 属性窗口 *Material* 选项卡的 **SCS Looks** 面板中完成这些操作。

[![SCS_Tools_Object_Specials_-_SCS_Looks.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Look%20system/SCS_Tools_Object_Specials_-_SCS_Looks.280.png)](../../../../files/SCS%20Tools%20Object%20Specials%20-%20SCS%20Looks.280.png.md)

要为某个外观更改材质属性或纹理，你需要先在上面显示的列表中选中该外观，然后直接更改材质属性。此后，每当你切换活动外观时，当前 SCS 游戏对象中的所有材质都会更新为该外观中的值，你也能在 3D 视图中看到这些变化。

> > **注意：** 在多个 SCS 游戏对象中使用同一个材质时，材质会采用当前选中的 SCS 游戏对象中的值。因此，其他 SCS 游戏对象中使用该材质的网格将无法正确显示，但它们仍会被正确导出。

### 写入全部外观

大多数 SCS 材质设置都可以“写入全部外观”，这意味着该设置的当前值会被写入所有外观。这样一来，例如你可以轻松更改希望在全部外观中使用的纹理，而无需逐个选中每个外观并反复查找该纹理。

写入全部外观功能可通过属性右侧的 *More Options* 菜单按钮（ **𐩒** ）访问：

[![SCS_Material_Specials_-_WT.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Look%20system/SCS_Material_Specials_-_WT.280.png)](../../../../files/SCS%20Material%20Specials%20-%20WT.280.png.md)

#### WT 菜单

写入全部外观菜单包含三个选项：

[![SCS_Material_Specials_-_WT_Menu.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Look%20system/SCS_Material_Specials_-_WT_Menu.280.png)](../../../../files/SCS%20Material%20Specials%20-%20WT%20Menu.280.png.md)

- **WT** - 将值写入当前 SCS 根对象内的所有外观，
- **WT - Same Look on All SCS Roots** - 将值写入其他任何 SCS 根对象中的同名外观（若找到则写入，否则不执行任何操作），
- **WT - All Looks on All SCS Roots** - 将值写入当前 blend 文件中所有 SCS 根对象的所有外观。

> > **注意：** 当你在模型中未定义任何外观，或只定义了一个外观时，写入全部外观不会对材质产生任何效果。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Look_system | revision: 4336 | captured: 2026-10-21 23:56:14 -->
