# 文档/工具/SCS Blender Tools/材质

SCS Blender Tools 使用自己的材质设置，因此 Blender 中的每个材质都会在 Blender 属性窗口的 *Material* 选项卡中包含一个名为 **SCS Material** 的面板。设置任何可用的材质属性时，务必只使用此处的设置。如果你在 Blender 的标准面板中更改材质设置，材质的外观会在 3D 视图中发生变化，但 SCS 材质设置不会改变，导出的材质在 SCS 游戏引擎中查看时可能看起来截然不同。

## 渲染与 3D 视图设置

为获得最接近 SCS 游戏引擎中的效果，你应使用 EEVEE 渲染引擎：

[![SCS_Material_Specials_-_EEVEE.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_EEVEE.280.png)](../../../../files/SCS%20Material%20Specials%20-%20EEVEE.280.png.md)

并将 *Viewport Shading* 切换为 *Rendered*，以便正确查看渲染后的模型。

[![SCS_Material_Specials_-_Rendered_Viewport.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_Rendered_Viewport.280.png)](../../../../files/SCS%20Material%20Specials%20-%20Rendered%20Viewport.280.png.md)

> > **注意：** 默认将使用完整的参考光照，但如果你想创建游戏中特定时段那样的光照，请参阅：[场景光照](Scene%20Lighting.md)

## 合并材质

SCS Material 面板还提供了一个颇为隐蔽但功能强大的操作符：**Merge Materials**，它位于面板标题栏右侧：

[![SCS_Material_Specials_-_Merge_Materials.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_Merge_Materials.280.png)](../../../../files/SCS%20Material%20Specials%20-%20Merge%20Materials.280.png.md)

按下该操作符按钮后，可在新出现的对话框中根据所选条件合并材质。

## 着色器用法

SCS 材质基于着色器预设创建。用户在创建和使用 SCS 材质时，可以使用列表中的任意着色器预设，并切换或编辑材质的 flavor、属性和纹理。不过，着色器的第二种用法是导入着色器，它仅在导入时创建，且只当模型使用的材质效果无法在着色器预设中找到时才会创建。

### 着色器预设

[![SCS_Material_Specials_-_Shader_Preset.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_Shader_Preset.280.png)](../../../../files/SCS%20Material%20Specials%20-%20Shader%20Preset.280.png.md)

SCS Material 面板提供 *Shader Presets* 列表，你可以从中选择带有各自预定义值的材质，并按喜好更改其中一些值。此外，每个着色器预设现在还带有 flavor，它们是许多着色器的通用扩展。

Flavor 会改变着色器的完整效果名称及其行为，并在某些情况下添加或移除一些材质属性或纹理。有些 flavor 可能不会在视觉上改变网格，因为它们用于不同目的。例如，“shadow” flavor 会告诉着色器将此材质同时用作阴影投射体，因此网格上不应有任何视觉变化。

### 导入着色器

[![SCS_Material_Specials_-_Imported_Shader.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_Imported_Shader.280.png)](../../../../files/SCS%20Material%20Specials%20-%20Imported%20Shader.280.png.md)

当你导入任何现有的游戏模型，且其中某些材质无法在现有着色器预设中找到时，就会创建“Imported Shader”。其属性无法编辑，但它仍会按原始文件中的状态正确导出。不过，为了视觉预览，可以更改纹理及其映射。

此外，此类型的着色器在“Textures”中还有一个“Mappings”字段，其中的“tex_coord_X”条目指定将为该别名导出哪个 UV 层。

## 属性与用法

材质中的属性取决于着色器类型，因此每种着色器可能有不同的属性和纹理。

### Substance

Substance 属性是物理材质列表中的一项，该列表从 Material Substance Library 文件加载（参见[全局设置#路径设置](Global%20Settings.md#Path_Settings)）。例如，它们可用于设置路面的物理类型。

### 材质属性

在此部分中，你可以找到各种可更改的着色器视觉属性。最重要的属性会以交互方式反映在 3D 视图中的模型上。

### 材质纹理

此部分提供了为不同着色器纹理通道指定纹理图像的界面。最常用的纹理会自动加载并显示在 3D 视图中。

#### 纹理

该属性定义纹理或纹理对象文件（TOBJ - 指向纹理图像的指针）的路径。使用此属性侧边的地图图标会打开文件浏览器，你可以在其中选择图像或任意 TOBJ 作为纹理。选择后，图像会自动应用到材质上。在当前选定的着色器预设旁边还可以找到搜索按钮，它让你可以快速搜索可用的预设。

> > **注意：** 使用不来自 SCS 项目目录（参见[全局设置#路径设置](Global%20Settings.md#Path_Settings)）及其子目录的纹理，可能会导致导出时出现错误和警告！

#### 设置

每个纹理还带有额外的 TOBJ 文件及其设置控件行。如果 TOBJ 尚不存在，默认会在导出时创建。不过，如果 TOBJ 文件尚不存在，会出现创建按钮，按下它会使用默认设置为该纹理创建 TOBJ 文件。如果该纹理已有 TOBJ 文件，则会显示重新加载按钮，你可以用它加载该 TOBJ 当前保存的设置。有时重新加载按钮会显示为红色，表示当前设置已过期，你应按下重新加载按钮重新加载它们。一旦 TOBJ 文件存在，你也可以更改设置中的任何值。更改设置列表中的任何设置都会立即用更新后的值重写 TOBJ 文件。

- ***U Repeat*** - 在 U 方向重复纹理。
- ***V Repeat*** - 在 V 方向重复纹理。
- ***TS Normal*** - 纹理的切线空间法线。
- ***Color Space Linear*** - 纹理处于线性色彩空间（此选项应在遮挡类着色器上配合灰度遮挡纹理使用）。

#### 映射

该属性指定此纹理将使用哪个 UV 层。对于某些纹理，你可能需要指定多个 UV 层，具体取决于所使用的着色器预设。

### 材质项额外菜单

此外，大多数材质属性都有一个 *More Options* 菜单按钮（ **𐩒** ）。其中一些可以写入全部外观（关于写入全部外观的更多内容：[外观系统#写入全部外观](Look%20system.md#Write_Through)），还有一些甚至可以按线性色彩空间复制，或从线性色彩空间粘贴。

[![SCS_Material_Specials_-_Extras_Menu.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Materials/SCS_Material_Specials_-_Extras_Menu.280.png)](../../../../files/SCS%20Material%20Specials%20-%20Extras%20Menu.280.png.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Materials | revision: 4357 | captured: 2026-10-21 23:56:14 -->
