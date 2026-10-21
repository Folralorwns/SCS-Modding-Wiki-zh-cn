# 教程/高级/扩展阴影

[Template:Construction](https://modding.scssoft.com/index.php?title=Template:Construction&action=edit&redlink=1)

本教程将简要概述用于玩家卡车和挂车的扩展阴影效果，并指导你为模型正确设置该效果。

## 概述

扩展阴影效果用于在玩家的卡车和挂车下方绘制阴影体积。灰度纹理用于定义阴影体积沿其长度和宽度的强度。在模型中，使用两个定位器来定义阴影体积，并使用一个表面来定义该效果在垂直方向上的界限。该效果可在相应的[底盘定义](../../Documentation/Engine/Units/accessory%20chassis%20data.md)中微调。

![Ext_shadow_001.jpg](../../../../../images/articles/Tutorials/Advanced/Extended%20Shadows/300px-Ext_shadow_001.jpg)

![Ext_shadow_002.jpg](../../../../../images/articles/Tutorials/Advanced/Extended%20Shadows/300px-Ext_shadow_002.jpg)

### 定位器

原点定位器（shadow_x_ori、shd_x_ori1、shd_x_ori2 等）定义阴影体积的上边界、中心、方向和朝向。通常应始终将此定位器调整为朝下（即旋转定位器，使其 **+y** 指向全局 **-Z**），并旋转使其 **+z** 指向全局 **-Y**。角点定位器（shadow_x_crn、shd_x_crn1、shd_x_crn2 等）定义阴影体积的宽度、长度和下边界。

### *Fakeshadow* 表面

使用 *fakeshadow* 效果的表面用于限制阴影体积内应用阴影的范围。默认情况下，扩展阴影纹理会垂直投影到整个阴影体积内，为其中的所有几何体着色。当存在 *fakeshadow* 表面时，只有相对于阴影体积原点位于该表面“外侧”的体积才会被着色。因此，通常任何 fakeshadow 表面的法线都会朝向地面。同样重要的是，*fakeshadow* 表面必须覆盖阴影体积的整个长度和宽度，否则未覆盖区域可能会出现不理想的着色。

## 模型设置

### 放置定位器

通常，卡车或挂车的扩展阴影和 UI 阴影模型会使用同一纹理。在这种情况下，必须参照 UI 阴影模型放置扩展阴影定位器，使纹理投影到阴影体积的方式与其映射到 UI 阴影的方式相同。

1. 使用 `⇧ Shift`+`A` 放置原点定位器（shadow_x_ori），使其在俯视时位于 UI 阴影模型包围盒的中心。其 Z 位置为阴影体积的顶部，即会被扩展阴影压暗的最高点。<br> ![Ext_shadow_3.jpg](../../../../../images/articles/Tutorials/Advanced/Extended%20Shadows/Ext_shadow_3.jpg)
2. 将原点定位器旋转为标准朝向：`R`、`X`、-90；`R`、`Z`、180。其在 Transform 面板中的朝向应如下所示：<br> ![Ext_shadow_3b.jpg](../../../../../images/articles/Tutorials/Advanced/Extended%20Shadows/Ext_shadow_3b.jpg)
3. 将角点定位器（shadow_x_crn）放在俯视时 UI 阴影模型的前左（+Y、-X）最外缘。通常将其放置在地面以下，这样当玩家驶过凹地时阴影不会突兀地消失。合理的值约为 -65cm。（如果它太低，阴影体积会延伸到桥梁下方等位置）<br> ![Ext_shadow_4.jpg](../../../../../images/articles/Tutorials/Advanced/Extended%20Shadows/Ext_shadow_4.jpg)

### 创建 *Fakeshadow* 表面

选择扩展阴影原点定位器（shadow_x_ori 或 shd_x_ori），并将 3D 光标吸附到其上（`⇧ Shift`+`S` → *Cursor to Selected*）。向场景添加一个平面（`⇧ Shift`+`A` → Mesh → Plane）。该平面将成为你的 fakeshadow 表面！

启用吸附（`⇧ Shift`+`Tab ↹`），选择顶点模式，并使用 *Closest* 目标模式。确保角点定位器（shadow_x_crn 或 shd_x_crn）可见。

选择你创建的平面，进入编辑模式并全选。先沿 *X* 轴缩放该平面，再沿 *Y* 轴缩放，每次都要吸附到角点定位器。使用 `Ctrl`+`F` → Flip Normals 翻转平面法线，使其朝下。

为你的 fakeshadow 表面指定一个使用 *fakeshadow* 效果的 SCS 材质。将该平面的[父级](https://docs.blender.org/manual/en/dev/editors/3dview/object/properties/relations/parents.html)设置为车辆的 SCS 根定位器。

至此，你的车辆已拥有可用的 fakeshadow 表面！不过它可能还不够贴合。可以按需细分并调整该表面。请务必确保外缘仍覆盖整个阴影体积。

> **提示：** [Loop Cut](https://docs.blender.org/manual/en/dev/modeling/meshes/editing/subdividing/loop.html) 工具可用于快速细分 fakeshadow 表面。

### 创建阴影纹理

## 定义设置

## 故障排除

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Advanced/Extended_Shadows | revision: 5346 | captured: 2026-10-21 23:56:14 -->
