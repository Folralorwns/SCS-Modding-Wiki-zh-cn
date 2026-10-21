# 教程/地图编辑器/预制件/预制件节点

> [← 上一部分](https://modding.scssoft.com/index.php?title=Tutorials/Map_Editor/Prefabs/Prefab_Properties&action=edit&redlink=1)[下一部分 →](Connecting%20your%20first%20Prefab.md)
>
> [所有步骤](../Prefabs.md)

到现在，你应该已经熟悉预制件的设置和对话框选项了。在连接并设置我们的第一个预制件之前，我们必须先深入了解预制件可以建立的连接类型，以及连接它们时的一些奇怪之处。

与道路节点非常相似，预制件有 2 种主要节点类型。一种是红色节点（*在地图编辑器中显示为方形*），称为*原点*；另一种是绿色节点。一个预制件只会有一个原点（红色）节点，但可以有多个绿色节点。预制件上的每个节点都是连接其他对象（例如道路或预制件）的潜在位置。节点数量因预制件而异。节点定义在模型自身上，并在建模程序中设置。

> **注意：** 你**绝不能**将红色节点连接到预制件的红色节点——那样*不会*生效！

![Prefab_green_node.png](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/Prefab_green_node.png)

*绿色预制件节点*

![Prefab_red_node.png](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/Prefab_red_node.png)

*红色预制件节点*

让我们用这个预制件 `/prefab2/cross_temp/ger/ger_r1_x_r1_t_narrow_tmpl.ppd` 来看几个预制件上不同原点的示例

|  |  |  |
| --- | --- | --- |
| **1** | [![Prefab_full.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_full.jpg)](../../../../files/Prefab%20full.jpg.md) | 原点为 0 的预制件 <br>（上侧） |
| **2** | [![Prefab_origin1.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_origin1.jpg)](../../../../files/Prefab%20origin1.jpg.md) | 原点为 1 的预制件 <br>（右侧） |
| **3** | [![Prefab_origin2.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_origin2.jpg)](../../../../files/Prefab%20origin2.jpg.md) | 原点为 2 的预制件 <br>（左侧） |

注意到红色节点是如何移动到预制件不同侧面的吗？这就是更改原点的效果。为了将项正确地连接到预制件，你可能需要更改原点。 <br> <br> 以下是几个连接正确与错误的示例：

|  |  |  |
| --- | --- | --- |
| **1** | [![Prefab_bad_connection.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_bad_connection.jpg)](../../../../files/Prefab%20bad%20connection.jpg.md) | 由于有 2 个红色节点，预制件无法连接到道路 <br> **注意：** 如果你尝试连接这两者且已开启吸附到节点，看起来像是连上了，但实际上并没有，导航将无法工作 |
| **2** | [![Prefab_good_connection.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_good_connection.jpg)](../../../../files/Prefab%20good%20connection.jpg.md) | 由于有 1 个绿色节点和 1 个红色节点，预制件可以连接到道路 |
| **3** | [![Prefab_good_connection2.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_good_connection2.jpg)](../../../../files/Prefab%20good%20connection2.jpg.md) | 由于有 2 个绿色节点，预制件可以连接到道路 |

你会注意到一些较旧的预制件（例如 `/prefab/light_factory/light_factory.ppd`）有多个节点，但尝试将道路连接到这些节点会产生奇怪的结果：

![Funny_prefab_connection.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Funny_prefab_connection.jpg)

对于这些预制件，你只需将道路/预制件部件拖到预制件几何体上你预期入口所在的位置并使其接触，导航仍然会正常工作。这是由该特定预制件在 Blender 中的设置方式造成的

> [← 上一部分](https://modding.scssoft.com/index.php?title=Tutorials/Map_Editor/Prefabs/Prefab_Properties&action=edit&redlink=1)[下一部分 →](Connecting%20your%20first%20Prefab.md)
>
> [所有步骤](../Prefabs.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Prefabs/Prefab_Nodes | revision: 5491 | captured: 2026-10-21 23:56:14 -->
