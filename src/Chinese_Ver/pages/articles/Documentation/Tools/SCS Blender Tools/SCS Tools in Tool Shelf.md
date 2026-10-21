# 文档/工具/SCS Blender Tools/工具架中的 SCS Tools

![SCS_Tools_Shelf.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/SCS_Tools_Shelf.png)

SCS Tools 工具架由一组工具组成，这些工具可用于 3D 视口中的对象。

## 工具架

### 添加根对象

创建一个新的 SCS Root Object。如果当前有选中项，它会将这些对象父级设置为该 SCS Root Object，从而自动把它们纳入 SCS Game Object 的内容。

### 添加根对象（附带名称请求）

创建一个新的 SCS Root Object。用户可以在随后弹出的窗口中为根对象指定名称。如果当前有选中项，它会将这些对象父级设置为该 SCS Root Object，从而自动把它们纳入 SCS Game Object 的内容。

### 检查几何体

检查选中对象中是否存在退化多边形，这类多边形应在导出前移除，因为它们可能在某些显卡上导致 FPS 下降。该操作符会获取选中对象，并选中退化多边形的顶点。退化多边形通过 [海伦公式](https://en.wikipedia.org/wiki/Heron%27s_formula) 检测。

### VColoring

进入复杂的 [顶点着色](SCS%20Tools%20in%20Tool%20Shelf/VColoring.md) 模式，在其中可以编辑 4 个顶点颜色层，这些层会实时烘焙到着色器所使用的顶点颜色层并导出。侧边的额外图标按钮 [![Blend_icon_file_refresh.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/Blend_icon_file_refresh.png)](../../../../files/Blend%20icon%20file%20refresh.png.md) 让你可以重新烘焙这 4 个层，以应对你未使用 **VColoring** 操作符而手动编辑了其中某个层的情况。

## 凸包

### 生成凸包

基于选中的模型对象生成一个新对象。该新对象始终为凸形，可用作凸包碰撞体的基础。

### 转换为定位器

将选中对象转换为新的碰撞定位器。此外还可设置以下选项：用于删除源对象的 Delete Original Geometry，以及用于从每个选中对象创建单个定位器还是多个定位器的 Individual Objects。

### 转换为网格

将选中的碰撞定位器转换为可编辑的模型（网格）对象。

## 可见性工具

可见性工具包含一个按类型查看对象的子面板，以及三个额外的可见性操作符。

### 按类型切换

[![SCS_Tools_Shelf_Op_Table.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/SCS_Tools_Shelf_Op_Table.png)](../../../../files/SCS%20Tools%20Shelf%20Op%20Table.png.md)

第一个表格用于更改模型对象和定位器对象的可见性。第二个表格仅用于预制件定位器。

### 全局与 SCS Root

此选项用于切换该子面板中可见性操作符的作用范围。使用 ***Global*** 时，操作符会作用于当前场景中的所有对象；使用 ***SCS Root*** 时，则只会更改当前 SCS Game Object 内的对象。

### 当前 SCS Root

用于切换活动对象所在 SCS Game Object 内对象可见性的额外操作符：

- ***Invert Visibility*** - 反转所有对象的可见性。
- ***View All*** - 显示所有对象。
- ***Isolate*** - 显示活动对象所在 SCS Game Object 内的所有对象，并隐藏场景中的其他所有对象。

## 显示方式

### 玻璃对象

- ***Wires / Textured*** - 两个操作符，用于快速设置场景中所有玻璃对象的绘制类型。

### 投射阴影对象

- ***Wires / Textured*** - 两个操作符，用于快速设置场景中所有阴影投射对象的绘制类型。

### 碰撞定位器

- ***All Wires / No Wires*** - 用于快速开启或关闭场景中所有碰撞定位器线框的操作符。
- ***All Faces / No Faces*** - 用于快速开启或关闭场景中所有碰撞定位器面的操作符。

## 另见

根据 Blender 中当前 3D 视口的模式，你还会看到：

1. [灯光切换器与 UV 工具](SCS%20Tools%20in%20Tool%20Shelf/Lamp%20Switcher%20&%20UV%20Tool.md) -> 处于 **Edit Mode** 时
2. [包裹与统计工具](SCS%20Tools%20in%20Tool%20Shelf/Wrap%20&%20Stats%20Tools.md) -> 处于 **Vertex Paint** 模式时

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/SCS_Tools_in_Tool_Shelf | revision: 3439 | captured: 2026-10-21 23:56:14 -->
