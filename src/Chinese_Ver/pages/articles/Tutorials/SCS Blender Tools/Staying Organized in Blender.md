# 教程/SCS Blender Tools/在 Blender 中保持条理

> **注意：** 施工中 — [Smarty](../../../users/Smarty.md)（[讨论](../../../user_talk/Smarty.md)）04:51, 22 June 2017 (CEST)

使用 [SCS Blender Tools](../../Documentation/Tools/SCS%20Blender%20Tools.md) 的多模型工作流程极为强大。整个复杂的项目都可以轻松地通过单个 blend 文件来管理：一辆卡车及其所有配件、内饰变体和动画；一辆挂车及其所有货物；一套车轮和轮胎配件系统……借助此工作流程可以实现很多事情。然而，如果没有良好的组织和整理，复杂项目很快会变得笨重且难以浏览。

本教程提供一些基本技巧，帮助你在多模型工作流程的框架内保持 blend 文件井然有序。

## 使用空物体

虽然“**空物体**”可以说是 Blender 中最简单的几何对象，但它也可能是最有用的对象之一。Blender Tools 将**空物体**类型用于[根对象](../../Documentation/Tools/SCS%20Blender%20Tools/Root%20objects.md)和[定位器](../../Documentation/Tools/SCS%20Blender%20Tools/Locators.md)。当**空物体**未配置为这两种特殊类型中的任何一种时，Blender Tools 在导出时不会对其作特殊处理。需要说明的是，作为**空物体**子级的 SCS 对象仍会被视为 SCS 对象；而如果某个**空物体**本身是 SCS 对象的子级，那么作为其子级的任何对象仍会被视为属于该 SCS 对象。因此，**空物体**类型可用于组织场景中的 SCS 对象，以及 SCS 对象内的任何其他对象，就像用文件夹来组织文档一样。

- [![使用空物体为配件组织 SCS 根对象](../../../../../images/articles/Tutorials/SCS%20Blender%20Tools/Staying%20Organized%20in%20Blender/Staying_organized_001.jpg)](../../../files/Staying%20organized%20001.jpg.md) 使用空物体为配件组织 SCS 根对象
- [![使用空物体组织属于部件的对象](../../../../../images/articles/Tutorials/SCS%20Blender%20Tools/Staying%20Organized%20in%20Blender/Staying_organized_002.jpg)](../../../files/Staying%20organized%20002.jpg.md) 使用空物体组织属于部件的对象

### 设置父级

使用 `Ctrl`+`P` 快捷键可以将所选对象设为活动对象的子级。上下文菜单会提供是否保持当前变换的选项。*保持当前变换*选项会维持所选对象在场景中的绝对位置、缩放和朝向，在这种情况下通常首选此选项。

> **注意：**
>
> ![Active_selection_example.jpg](../../../../../images/articles/Tutorials/SCS%20Blender%20Tools/Staying%20Organized%20in%20Blender/100px-Active_selection_example.jpg)
>
> 选中多个对象时，**活动**对象会以较浅的颜色高亮显示，通常是你最后选中的对象。在右侧示例中，后视镜支架、镜体和天线都被选中，但后视镜支架是**活动**对象，其*浅*橙色轮廓表明了这一点。在这种情况下执行设置父级操作，会使镜体和天线成为后视镜支架的子级。

### 清除父级

也可以使用 `Alt`+`P` 清除所选对象的父级，将其移动到场景根级。此操作同样可以选择是否保持当前变换。

## 使用关联复制

对于间距不均匀的重复对象，有时使用[关联复制](https://docs.blender.org/manual/en/dev/editors/3dview/object/editing/duplication.html#linked-duplicates)会很有效。使用 `Alt`+`D` 复制对象时，会创建一个新对象，其所有数据都链接到原对象。新对象可以通过*对象*变换进行移动、旋转和缩放，而不会影响原对象，并且可以为其设置独有的约束和修改器。你在编辑模式下对网格或顶点数据所做的任何更改都会应用到所有副本。

一个有用的例子是挂车示廓灯。可以在示廓灯的网格、贴图映射（包括 lightmask）、顶点颜色等最终确定之前，先放置并旋转所有实例。所有这些数据都可以按需编辑，所有实例都会更新，而无需重新复制原对象。这样在因精细细节建模而陷入困境之前，制作整个挂车的原型就会简单得多。

![Staying_organized_003.jpg](../../../../../images/articles/Tutorials/SCS%20Blender%20Tools/Staying%20Organized%20in%20Blender/Staying_organized_003.jpg)

### 解除链接

在某些情况下，你可能希望断开重复对象之间的链接。这可以通过[**对象→设为单一用户**](https://docs.blender.org/manual/en/dev/data_system/data_blocks.html#data-system-datablock-make-single-user)实现，快捷键为 `U`。

<!-- source: https://modding.scssoft.com/wiki/Tutorials/SCS_Blender_Tools/Staying_Organized_in_Blender | revision: 3306 | captured: 2026-10-21 23:56:14 -->
