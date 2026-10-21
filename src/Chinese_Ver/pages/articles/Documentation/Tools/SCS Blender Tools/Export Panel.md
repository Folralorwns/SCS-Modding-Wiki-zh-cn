# 文档/工具/SCS Blender Tools/导出面板

导出面板位于属性窗口的 *Output* 选项卡内，提供了一种将内容快速导出到游戏的途径。

[![SCS_Tools_Export_00.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Export%20Panel/SCS_Tools_Export_00.280.png)](../../../../files/SCS%20Tools%20Export%2000.280.png.md)

## 导出模式（范围）

### 选中项

仅导出选中的对象，但从初始选择中判断哪些对象应纳入导出时，存在一些逻辑规则。选中根对象时，其全部内容都会被导出。仅选中部分网格对象时，则只将这些对象导出到其所属的游戏对象中。在这些情况下，其根对象是否被选中并不重要。

勾选 **Selection** 按钮左侧的复选框后，导出前所有将要导出的对象都会被隔离到局部视图中。这是确认导出内容的极好方式。它始终只显示将要导出的几何体和定位器。选择预览是一种额外模式，在其中可以像 Blender 通常那样使用 ***Numpad*** 按键操作视图——***4*** 和 ***6*** 键将视图左右转动，***8*** 和 ***2*** 键上下转动，***+*** 和 ***-*** 则会放大和缩小。按下 ***Enter*** 开始导出，使用 ***Esc*** 键则可取消导出并回到之前的选择状态。

### 当前场景

导出当前场景中所有设置正确的游戏对象。

> > **注意：** 你可以在每个根对象中使用 “Export Inclusion” 开关指定其内容是否需要导出。

### 所有场景

导出当前 Blender 文件中所有场景内所有设置正确的游戏对象。

> > **注意：** 你可以在每个根对象中使用 “Export Inclusion” 开关指定其内容是否需要导出。

## 其他导出选项

### 默认导出路径

在此可以指定 “SCS Project Base Path” 内的相对文件路径，你的游戏对象将被导出到该位置。

默认导出路径的使用方式：

1. 如果默认导出路径为空，Blender Tools 会尝试将游戏对象导出到已保存的 Blender 文件旁边。
2. 如果设置了默认导出路径，Blender Tools 会将 “SCS Project Base Path” 与给定的默认导出路径组合起来，将文件导出到该处。
3. 如果 Blender Tools 无法为上述情况找到解决方案，文件会直接导出到 “SCS Project Base Path” 中。

> > **注意：** 如果输入框被标记为红色，则路径无效，并会显示一个用于查看更多信息的额外按钮。

> > **注意：** 可以通过指定 “Custom Export Filepath” 在根对象上覆盖导出路径。

### 导出缩放

所有导出模型与元素的最终缩放比例。该设置会被保存，因此会在每个 Blend 文件中被记住。

### 应用修改器

导出前应用所有修改器。

### 仅应用 'Edge Split'

导出前仅应用 'Edge Split' 修改器以获得锐利边缘。其他所有修改器都会被忽略。

### 输出格式

仅面向开发者的功能，目前应始终设置为 “Game Data Format”。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Export_Panel | revision: 4283 | captured: 2026-10-21 23:56:14 -->
