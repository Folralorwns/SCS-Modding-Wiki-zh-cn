# 教程/地图编辑器/地图编辑器入门/保存、加载、扇区与文件

> [← 上一部分](Basic%20Editor%20Functions.md)
>
> [所有步骤](../Introduction%20to%20the%20Map%20Editor.md)

<table class="wikitable tutorial_infobox" style="float: right" width="300px">
<tbody><tr>
<td colspan="2">保存、加载、扇区与文件
</td></tr>
<tr>
<td colspan="2"><span typeof="mw:File"><a class="mw-file-description" href="../../../../files/First%20map%20ingame%2002%208.jpg.md"><img class="mw-file-element" data-file-height="2160" data-file-width="3840" decoding="async" height="169" src="../../../../../images/thumb/b/bd/First_map_ingame_02_8.jpg/300px-First_map_ingame_02_8.jpg" srcset="../../../../../images/thumb/b/bd/First_map_ingame_02_8.jpg/450px-First_map_ingame_02_8.jpg 1.5x, ../../../../../images/thumb/b/bd/First_map_ingame_02_8.jpg/600px-First_map_ingame_02_8.jpg 2x" width="300"/></a></span>
</td></tr>
<tr class="info">
<td class="row_name" width="50px"><b>主题：</b>
</td>
<td>地图编辑器
</td></tr>
<tr class="info">
<td class="row_name" width="50px"><b>难度：</b>
</td>
<td>简单
</td></tr>
<tr class="info">
<td class="row_name" width="50px"><b>工具：</b>
</td>
<td><a href="../../../Documentation/Tools/Map%20Editor.md" title="Documentation/Tools/Map Editor">地图编辑器</a>
</td></tr></tbody></table>

到目前为止，我们已经学习了如何启动编辑器，以及一些可用的基础工具和功能。接下来，我们将通过学习如何保存、加载和运行地图来继续扩展这些内容。我们还会讨论文件保存的位置以及这些文件中包含的内容。

## 放置第一条道路并保存地图

|  |  |  |
| --- | --- | --- |
| **1** | [![First_road_piece_02_1.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/1024px-First_road_piece_02_1.png)](../../../../files/First%20road%20piece%2002%201.png.md) | 打开编辑器后，点击“项类型”下拉菜单并选择“道路”（快捷键：1） |
| **2** | [![Road_properties_02_2.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/1024px-Road_properties_02_2.png)](../../../../files/Road%20properties%2002%202.png.md) | 接下来，点击新建项（快捷键：E）。这会打开道路项的默认属性。目前先保留全部默认设置——我们将在后续教程中深入介绍道路部件和连接 <br> **提示：** 放置道路时请确保处于俯视相机视图（快捷键：C） |
| **3** | [![First_road_line_02_3.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/1024px-First_road_line_02_3.png)](../../../../files/First%20road%20line%2002%203.png.md) | 在粉色小车尾部附近单击，然后向上拖动鼠标。在你第二次单击并绘制道路之前，应出现一条红线，显示道路的路径。按 Esc 可清除正在放置的新项 |
| **4** | [![Start_position_02_4.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/1024px-Start_position_02_4.jpg)](../../../../files/Start%20position%2002%204.jpg.md) | 激活“自由相机”（快捷键：C），并飞到你的道路部件处。确保我们的起点（粉色小车）接触地面——若未接触，请确保“吸附到地面”（快捷键：G）已开启，然后点击“放置起点”，再在道路上的某处单击 |
| **5** | [![Save_first_map_02_5.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/Save_first_map_02_5.png)](../../../../files/Save%20first%20map%2002%205.png.md) | 现在转到 文件 > 另存为（快捷键 CTRL + S）；随意为地图命名——我的地图名为“deerland”。你无需在此更改任何设置。保持位置及其他所有内容不变 |

## 加载地图

|  |  |  |
| --- | --- | --- |
| **1** |  | 启动地图编辑器 |
| **2** | [![Open_first_map_02_6.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/Open_first_map_02_6.png)](../../../../files/Open%20first%20map%2002%206.png.md) | 转到 文件 > 打开；双击你命名的地图——它应打开到我们上次结束的位置<br> 就是这样！加载地图非常简单，编辑器应加载到你退出前所在的最后区域 <br> **提示：** 或者，你可以在快捷方式中添加 “-edit *map_name*”（-edit deerland），以便直接加载我们的地图 |

## 运行第一张地图

|  |  |  |
| --- | --- | --- |
| **1** | [![First_map_ingame_02_8.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/1024px-First_map_ingame_02_8.jpg)](../../../../files/First%20map%20ingame%2002%208.jpg.md) | 在地图于编辑器中打开的情况下，点击“运行地图”按钮。游戏将加载预览配置，并让你在起点处生成 <br> **注意：** 如果你的游戏崩溃，可能是某处启用了模组，无论是在 */home* 中，还是来自 Steam 创意工坊。你仍然可以像平常一样启动游戏，然后在控制台中输入 “preview *map_name*”（例如 “preview deertest”）来运行地图 |

## 扇区说明

那么，请你设想一下欧洲大陆。现在想象我们用一把巨大的方形饼干模具，在欧洲中部切下一块。这一个正方形就是一个扇区。整个欧洲地图，或任何地图，都是由许多这样的扇区组成的。地图的第一个扇区是原点，其名称为：SEC + 0000 + 0000。单个扇区的长度为 4000 米、高度为 4000 米，即 16<sup>2</sup> km。扇区编号从 0000 到 9999，并且可以带有（-/+）。它们可以在 X 轴和 Y 轴方向上近乎无限地延伸。每个后续扇区会根据其位置改变数值。下图展示了从原点开始扇区是如何编号的。

![Sector_layout_graph.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/Sector_layout_graph.png)

那么这对我们意味着什么？对地图编辑而言影响不大。当我们到达某个扇区的边缘时，编辑器会自动创建另一个扇区，无需你进行任何操作。不过，如果某个扇区出现问题，你也不会丢失整张地图，而且这更便于跟踪不同的改动。此外，多名地图制作者可以共同处理同一个地图项目，按扇区边界分工。

这就引出了我们下一个话题……

## 文件

当我们首次启动编辑器时，*`/home/mod`* 目录中自动创建了一个名为“user_map”的文件夹。游戏就是在这里自动保存我们的地图和地图文件。我们来看看保存了哪些内容。

![Mod_directory_user_map_02_7.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/Mod_directory_user_map_02_7.png)

> **注意：** *`/home`* 目录的常见位置：*`C:\Users\*user*\Documents\Euro Truck Simulator 2\mod`*

查看 *`/home/mod/user_map/`* 内部，我们有一个文件夹和 3 个文件（*请记住我们的示例地图名为“deerland”*）：

- deerland（*文件夹*）
- deerland.epa
- deerland.mbd
- deerland.set

现在查看 *`/home/mod/user_map/deerland/`* 内部，我们有 5 个文件：

- sec-0001-0001.aux
- sec-0001-0001.base
- sec-0001-0001.data
- sec-0001-0001.desc
- sec-0001-0001.layer

> **注意：** 你的第一个扇区编号可能不同，具体取决于你在何处单击并绘制了第一条（也是唯一一条）道路部件

这些文件以二进制格式存储，游戏从中读取数据。最重要的是，一个扇区由 5 个文件组成（*把 .SND 文件算上则是 6 个，这里没有该文件，因为我们的扇区中还没有声音*）。要让地图扇区正常工作，你至少需要这 5 个扇区文件，否则游戏会崩溃。这 5 个扇区文件分别负责地图的不同方面：道路、标志牌、声音、模型放置、标志牌布局、叠加层、城市、公司等。另外 3 个以地图命名的文件是头文件，用于在编辑器中打开我们的地图。

> [← 上一部分](Basic%20Editor%20Functions.md)
>
> [所有步骤](../Introduction%20to%20the%20Map%20Editor.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Introduction_to_the_Map_Editor/Saving%2C_Loading%2C_Sectors%2C_and_Files | revision: 5593 | captured: 2026-10-21 23:56:14 -->
