# 文档/工具/SCS Blender Tools/变体系统

![SCS_Tools_Object_Specials_-_Variants_05.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Variant%20system/SCS_Tools_Object_Specials_-_Variants_05.280.png)

**变体**是**部件**的分组，可用于为游戏模型设置不同的变化形式。例如同一卡车模型的多种变化，其中不同的变体可以使用不同的驾驶室、底盘或扰流板。变体提供了一种有效方式，可按部件的任意组合来设置这些“卡车版本”。

如果你想在游戏模型中设置*变体*，必须先设置一些*部件*并创建一个 *SCS Root Object*（参见 [术语与基础](Terminology%20and%20basics.md) 或 [根对象](Root%20objects.md)）。然后选中 *SCS Root Object*，转到 Blender 属性窗口的 *Object* 选项卡，在 *SCS Object* 面板中即可找到 *SCS Variants* 子面板。在这里你可以找到用于处理*变体*的所有设置与工具。

## 变体列表

变体列表中可以不含任何变体。该面板右侧设有用于添加/移除变体的按钮，以及用于重新排序的箭头按钮。你也可以双击列表中的任何项目来重命名它。

如果至少创建了一个变体，列表下方会显示*变体-部件表格*（在“整合”视图样式下则直接显示在列表内；见下文）。该*变体-部件表格*始终包含所有部件的完整列表，这些部件是从当前 *SCS Game Object* 中的所有对象收集而来的。在此可以为单个变体开启或关闭任意部件。

变体列表使用 Blender 标准的列表机制，因此你可以利用该系统的全部优势——项目筛选与自定义排序。只需点击列表左下角的小图标即可启用这些功能。

### 附加列表工具

变体列表中的每个项目还集成了附加工具，可用于方便地选择/取消选择（箭头图标）或隐藏/显示（眼睛图标）特定变体。它的作用类似开关，因此反复按下时会选择与取消选择或隐藏与显示所有变体项目。按住 `⇧ Shift` 时，它始终向现有选择中添加，或始终显示变体项目；按住 `Ctrl` 时，它始终从现有选择中减去，或始终隐藏变体项目。

## 视图样式

你可以为*变体-部件表格*选择四种视图样式：**紧凑**（Compact）、**垂直**（Vertical）、**水平**（Horizontal）和**整合**（Integrated）。默认为 **水平** 视图样式。

### 紧凑视图样式

[![SCS_Tools_Object_Specials_-_Variants_07.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Variant%20system/SCS_Tools_Object_Specials_-_Variants_07.280.png)](../../../../files/SCS%20Tools%20Object%20Specials%20-%20Variants%2007.280.png.md)

仅显示列表中的当前活动变体。如果你拥有任意数量的部件与变体，并且希望一次查看和编辑单个变体，此样式非常合适。

你可以使用部件按字母排序按钮，将部件的显示顺序从无序（项目创建的顺序）改为按字母顺序。

### 垂直视图样式

[![SCS_Tools_Object_Specials_-_Variants_08.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Variant%20system/SCS_Tools_Object_Specials_-_Variants_08.280.png)](../../../../files/SCS%20Tools%20Object%20Specials%20-%20Variants%2008.280.png.md)

所有变体以列的形式垂直显示。如果你拥有大量变体，并希望逐个浏览它们，此样式非常合适。

你可以使用部件或变体的按字母排序按钮，将部件和/或变体的显示顺序从无序（项目创建的顺序）改为按字母顺序。

### 水平视图样式

[![SCS_Tools_Object_Specials_-_Variants_06.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Variant%20system/SCS_Tools_Object_Specials_-_Variants_06.280.png)](../../../../files/SCS%20Tools%20Object%20Specials%20-%20Variants%2006.280.png.md)

所有变体以行的形式水平显示，其所有部件分列于各列中。如果你的变体数量较少，并希望以井然有序的表格形式查看和编辑它们，此样式非常合适。

你可以使用部件或变体的按字母排序按钮，将部件和/或变体的显示顺序从无序（项目创建的顺序）改为按字母顺序。

### 整合视图样式

[![SCS_Tools_Object_Specials_-_Variants_09.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Variant%20system/SCS_Tools_Object_Specials_-_Variants_09.280.png)](../../../../files/SCS%20Tools%20Object%20Specials%20-%20Variants%2009.280.png.md)

在这种视图样式下，没有用于展示所有部件的“变体-部件表格”专用区域，而是直接在变体列表中显示它们。如果你的部件数量较少，并希望在不产生额外界面杂乱的情况下，以井然有序的表格形式查看和编辑它们，此样式会很有帮助。

在这种情况下，附加列表工具（见上文）显示在列表框正下方，并且始终作用于列表中的选中项目。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Variant_system | revision: 4302 | captured: 2026-10-21 23:56:14 -->
