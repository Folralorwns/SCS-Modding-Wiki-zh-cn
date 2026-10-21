# 文档/工具/SCS Blender Tools/动画系统

SCS 游戏中的动画由骨架与关键帧动画驱动（后者通过操纵骨架中的骨骼来实现）。这类动画分为两种类型：

1. **程序驱动动画**，除非动画定义文件中另有说明，其动画范围大多为 0 到 1。也就是说，第一帧将用作 0 状态，最后一帧将用作状态 1，该范围内的任何状态都会在整个关键帧范围上插值。此类动画的示例是 Euro Truck Simulator 2 中的卡车内饰动画，它们在每个卡车定义文件夹内定义（示例路径：*"def/vehicle/truck/man.tgx/interior/animations.sui"*）。
2. **静态循环动画**，由所谓的“mover”对象使用。Mover 可以借助地图编辑器放置到游戏世界各处。mover 对象的示例包括：风车、行人、动物等。要创建你自己的 mover，你应新建 *"def/world/mover.\<id_of_your_mod>.sii"* 文件，并参照原始 *"def/world/mover.sii"* 文件中的模板在该文件中定义 mover。 > > **注意：** 名为“walkers”的特殊类型 mover 也可在其动画中使用向前移动，这可以制作成骨架对象沿 Y 轴移动的动画。

无论 SCS Animation 的类型如何，Blender Tools 中的创建流程对上述两种类型都是相同的。要创建 SCS Animation，你需要使用 Blender 的标准流程：[创建骨架](https://docs.blender.org/manual/animation/armatures/introduction.html)、[顶点蒙皮](https://docs.blender.org/manual/animation/armatures/skinning/parenting.html#with-empty-groups)、[摆放骨骼姿势](https://docs.blender.org/manual/en/latest/animation/armatures/posing/introduction.html) 和 [设置关键帧](https://docs.blender.org/manual/en/latest/animation/keyframes/introduction.html)。

> > **注意：** 在 SCS Animation 导出期间，只会导出骨骼的位移、旋转与缩放操作，其他内容都会被忽略，即使它们在 Blender 内已制作动画并能播放。

使用 Blender 动作成功为骨骼制作动画后，你需要在 #SCS Animations 面板中设置 SCS Animation。设置完成后，你就可以像以前一样导出 SCS Game Object，动画会随之一同导出。

> > **注意：** 请记住，要导出动画模型，你必须在 SCS Root Object 属性中启用 ***Animated Model***，该开关位于定位器面板 [Root objects](Root%20objects.md) 中。

## SCS Animations 面板

要将创建的 Blender 动作导出到游戏中，你必须借助 SCS Animations 子面板来定义 SCS Animation，该子面板位于 Blender 属性窗口的 *Object* 选项卡下的 *SCS Object* 面板中。仅当当前选中的对象是骨架时，该面板才会显示。

[![SCS_Tools_Object_Specials_-_Animations.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Animation%20system/SCS_Tools_Object_Specials_-_Animations.280.png)](../../../../files/SCS%20Tools%20Object%20Specials%20-%20Animations.280.png.md)

> > **注意：** 如果在动画列表处看到 "No 'SCS Root Object'!" 提示，请确保将骨架对象父级设置为 SCS Root Object。

#### 自定义导出路径

自定义导出路径用于在导出 SCS Game Object 时，把动画文件存放在与其余文件不同的位置。

当你为 walkers 创建一系列动画时，该路径可能会很有用，因为所有 walkers 都可以使用相同的骨架和动画，因此你可以将它们导出到不同目录中。

如果自定义路径保持禁用，所有 SCS Animation 将与其余文件一同导出。

#### SCS Animations 列表

SCS Animations 列表包含当前 SCS Game Object 上使用的所有动画。要创建或删除 SCS Animation，请使用动画列表侧边的 **+** 和 **−** 按钮。此外，还可以通过导入按钮（ **⤓** ）导入动画，点击后会打开文件浏览器，供你选择要导入的 SCS Animation。

每个 SCS Animation 条目包含：

- 导出包含属性，如果未勾选该项且你正在导出整个 SCS Game Object，则会将该行所用的动画排除在导出之外，
- SCS Animation 的名称，它同时将用作导出的动画文件（PIA）的名称，
- 导出操作符按钮，用于通过文件浏览器直接导出该行所用的动画。

#### 当前动画设置

该面板区域用于将 Blender 动作（动画）与列表中当前选中的 SCS Animation 关联，并为其设置各种属性。

SCS Animation 的属性：

- **Start** - 动作中用作 SCS Animation 起始帧的帧，
- **End** - 动作中用作 SCS Animation 结束帧的帧，
- **Length** - SCS Animation 的时长，单位为秒，
- **Increase Animation Step ( + )** - 将动作拉伸为原来的 2 倍，并将 ***Export Step*** 增加 1 以补偿缩放。这让你能更好地控制子关键帧以及变换随时间的分布，
- **Decrease Animation Step ( − )** - 将动作压缩为原来的 1/2，并将 ***Export Step*** 减少 1 以补偿缩放。这会移除每隔一个的关键帧，从而降低对动画的控制，
- **Export Step** - 导出期间每次迭代在 Blender 动作中步进的帧数。

#### 动画播放器

要预览当前选中的 SCS Animation，你可以使用动画播放器，它不过是对多个 Blender 编辑器中已有设置的封装界面。

第一行包含动画播放的 **Start**、**End** 和 **Current** 帧。第二行则让你可以使用播放控制，并设置动画播放的 FPS。

> > **注意：** 手动更改 FPS 会使当前选中 SCS Animation 的预览失效，因为 FPS 是根据 SCS Animation 设置的 ***Start***、***End*** 和 ***Length*** 计算得出的。

## SCS Skeleton 面板

此外还有一个面板，用于在 SCS Project Base Path 内设置自定义骨架文件路径，以及设置骨架文件（PIS）的名称，该文件将在导出动画 SCS Game Object 时创建。

[![SCS_Tools_Object_Specials_-_Skeleton.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Animation%20system/SCS_Tools_Object_Specials_-_Skeleton.280.png)](../../../../files/SCS%20Tools%20Object%20Specials%20-%20Skeleton.280.png.md)

在创建 walkers 的一系列动画时，这个自定义路径与名称同样很方便，因为所有 walkers 都可以使用相同的骨架，因此你可以把骨架导出到不同目录。

如果两个路径都为空，骨架文件（PIS）将与其他导出文件一起保存，并使用 SCS Root Object 的名称作为文件名。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Animation_system | revision: 4305 | captured: 2026-10-21 23:56:14 -->
