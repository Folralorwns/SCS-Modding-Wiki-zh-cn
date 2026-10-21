# 文档/工具/SCS Blender Tools/导入

通过导入功能，可以导入先前导出为 *SCS 中间格式* 数据的模型和其他元素。

所有这些文件都使用 ***PIX*** 扩展名：***PIM*** 文件被视为包含模型几何体的主文件，其他扩展名包括 ***PIT***（特性数据）、***PIC***（碰撞体数据）、***PIP***（预制件数据）、***PIS***（骨架数据）和 ***PIA***（动画数据）。

[![SCS_Tools_Import_01.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Import/SCS_Tools_Import_01.280.png)](../../../../files/SCS%20Tools%20Import%2001.280.png.md)

导入功能位于 Blender 的导入菜单中，名称为 **SCS Game Object (.pim)**，它会打开文件浏览器对话框，让用户导入所需的 SCS Game Object。在对话框右侧，可以按需设置导入选项。

## 导入选项

[![SCS_Tools_Import_02.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Import/SCS_Tools_Import_02.280.png)](../../../../files/SCS%20Tools%20Import%2002.280.png.md)

- **SCS Project Base Path** - 可在导入前使用 *Set Current Dir as Project Base* 设置合适的 SCS Project Base Path。该操作符会将文件浏览器中当前选中的路径设为 SCS Project Base Path（更多信息见：[SCS Project Base Path](Global%20Settings.md#SCS_Project_Base_Path)）。
- **Scale** - 导入网格及其他元素的缩放比例。
- **Preserve Path for Export** - 自动为导入的 SCS Game Object 设置自定义导出路径，使你可以轻松地将其导出回导入时的同一位置。
- **Import Model (PIM)** - 你可以将 *Model* 文件加载**打开**和**关闭**。
- **Use Normals** - 如果勾选此属性，网格将使用文件中写入的法线导入。否则法线由 Blender 自行重新计算。
- **Use Welding** - 如果勾选此属性，将对所有导入的网格执行自动顶点焊接操作。这有时是必要的，因为 ***PIX*** 文件中的网格几何体是以一种可称为 “对显卡友好” 的形式导出的。这意味着顶点在许多情况下被重复——凡是有硬边的地方、UV 不连续处、相邻面顶点颜色不同的位置，都是如此。自动焊接会尽可能使几何体紧凑。
- **Welding Precision** - 以小数位数表示的阈值，数值必须相同到该位数才能进行焊接。因此对于默认值 4，数值必须匹配到小数点后四位，以毫米计即 0.1 mm。
- **Import Trait (PIT)** - 你可以将 *Trait* 文件加载***打开***和***关闭***。
- **Load Textures** - 如果勾选此属性，将加载所有图像纹理。
- **Import Collision (PIC)** - 你可以将 *Collision* 文件加载***打开***和***关闭***。
- **Import Prefab (PIP)** - 你可以将 *Prefab* 文件加载***打开***和***关闭***。
- **Import Skeleton (PIS)** - 你可以将 *Skeleton* 文件加载***打开***和***关闭***。
- **Bone Scale** - 在此可以指定导入骨骼的尺寸。之后更改其尺寸通常相当麻烦。
- **Import Animations (PIA)** - 你可以将 *Animation files* 加载***打开***和***关闭***。
- **Search Subdirectories** - 如果勾选此属性，将在所有可用的子目录中搜索动画文件。
- **Log Level** - 可在导入前设置日志记录级别。

> > **注意：** 只能加载属于实际骨架的动画文件。如果它们未放置在 PIX 文件旁边或任何子目录中，你仍可以稍后从 [Animation system#SCS Animations panel](Animation%20system.md#SCS_Animations_panel) 导入动画。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Import | revision: 4363 | captured: 2026-10-21 23:56:14 -->
