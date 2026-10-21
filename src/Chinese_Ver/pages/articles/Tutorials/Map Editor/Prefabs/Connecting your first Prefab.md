# 教程/地图编辑器/预制件/连接你的第一个预制件

> [← 上一部分](Prefab%20Nodes.md)
>
> [所有步骤](../Prefabs.md)

之前，我们学习了如何将道路连接在一起，但当我们需要将不止一条道路彼此连接时该怎么做？我们需要预制件！预制件有许多不同的名称。SCS 通常根据预制件所使用的国家、支持的车道数以及其一般功能来命名预制件。使用内容浏览器找到适合你要做的事情的预制件。在本教程中，我们将把几条道路连接在一起，形成一个交叉路口。在本教程中，我们将使用一个基础的 junction.w 将 2 条道路连接在一起。

> **提示：** 使用左侧的内容浏览器分类来帮助查找预制件

|  |  |  |
| --- | --- | --- |
| **1** | [![Asset_browswer_prefab.png](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/512px-Asset_browswer_prefab.png)](../../../../files/Asset%20browswer%20prefab.png.md) | 决定你想要的交叉路口类型，例如四向、T 形、环岛、高速公路、Y 形等。 |
| **2** | [![Selected_prefab_cb.png](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/Selected_prefab_cb.png)](../../../../files/Selected%20prefab%20cb.png.md) | 对于我们的地图，我选择了一个 T 形交叉路口 <br> 我们使用的是：`/prefab2/cross_temp/ger/ger_r1_x_r1_t_narrow_tmpl.ppd` |
| **3** | [![Prefab_setup_origin.png](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/512px-Prefab_setup_origin.png)](../../../../files/Prefab%20setup%20origin.png.md) | 在预制件默认属性中，我将更改原点（*红色节点*），以便连接我们的 2 条道路 |
| **4** | [![Prefab_fitting_origin.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/512px-Prefab_fitting_origin.jpg)](../../../../files/Prefab%20fitting%20origin.jpg.md) | 单击以放置预制件，并使其与你的道路部件对齐。将道路部件吸附到交叉路口预制件 <br> <br> **注意：** 每条道路的末端都有一个红色节点——你无法将红色道路节点连接到红色的（原点）预制件节点！ |
| **5** | [![Prefab_junction_final.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/512px-Prefab_junction_final.jpg)](../../../../files/Prefab%20junction%20final.jpg.md) | 在设置中修改预制件，以调整地形材质、地形尺寸、道路标线、look、variant、转角部件，以及在支持的情况下所需的任何植被 <br> <br> **提示：** 一旦你按喜好设置好预制件，如果你将其设为默认或保存为预设，那么你放置的每个预制件都会在支持的情况下继承你的材质设置 |

![Junction_prefab_deco.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/768px-Junction_prefab_deco.jpg)

> [← 上一部分](Prefab%20Nodes.md)
>
> [所有步骤](../Prefabs.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Prefabs/Connecting_your_first_Prefab | revision: 5481 | captured: 2026-10-21 23:56:14 -->
