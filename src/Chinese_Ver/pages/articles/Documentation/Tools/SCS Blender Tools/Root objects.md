# 文档/工具/SCS Blender Tools/根对象

SCS Root Object 是一种特殊条目，充当各个 SCS Game Object 的主对象（参见[术语与基础](Terminology%20and%20basics.md)一章）。实际上，这意味着任何父级关联到 SCS Root Object 的对象都会自动成为其内容的一部分，这样的单元随后便称为 SCS Game Object。它还承载整个单元的各种设置（如[部件](Part%20system.md)、[变体](Variant%20system.md)和[外观](Look%20system.md)），并可在 SCS Object 的各子面板中编辑。

你可以通过标准 Blender *Add* 菜单中的 *SCS Object* 子菜单选择它来创建根对象（`⇧ Shift`+`A`**→ SCS Object → Root Object**）。随后，你可以在 Blender 属性窗口 *Object* 选项卡下的 *SCS Object* 面板中访问其选项。

[![SCS_Tools_Root_Object_02.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Root%20objects/SCS_Tools_Root_Object_02.280.png)](../../../../files/SCS%20Tools%20Root%20Object%2002.280.png.md)

### 导出包含

此选项用于启用或禁用该 SCS Game Object 的批量导出。

### 动画模型 | 刚性模型

如果要导出的动画游戏对象将此开关置于 “Rigid Model” 选项，那么导出结果将不带动画，就如同刚性模型一样。反之显然，如果无动画的游戏对象将此开关置于 “Animated Model” 选项，它仍将是刚性的。

### 允许自定义导出文件路径

自定义导出文件路径左侧的复选框用于允许或禁用该 SCS Game Object 使用 “Custom Export File Path”。

### 自定义导出文件路径

允许为该 SCS Game Object 的导出设置自定义文件路径（覆盖 “Default Export Path”）。

指定的路径必须是 “SCS Project Base Path” 内的相对文件路径，该游戏对象将被导出到该位置。

自定义文件路径的使用方式：

1. 如果自定义导出路径为空，Blender Tools 会尝试将游戏对象导出到已保存的 Blender 文件旁边。
2. 如果设置了自定义导出路径，Blender Tools 会将 “SCS Project Base Path” 与给定的自定义导出路径组合起来，将文件导出到该处。
3. 如果 Blender Tools 无法为上述情况找到解决方案，文件会直接导出到 “SCS Project Base Path” 中。

> > **注意：** 如果输入框被标记为红色，则路径无效，并会显示一个用于查看更多信息的额外按钮。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Root_objects | revision: 4291 | captured: 2026-10-21 23:56:14 -->
