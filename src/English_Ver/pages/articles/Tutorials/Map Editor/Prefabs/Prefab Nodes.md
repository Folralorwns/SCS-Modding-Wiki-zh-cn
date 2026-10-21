# Tutorials/Map Editor/Prefabs/Prefab Nodes

> [← Previous part](https://modding.scssoft.com/index.php?title=Tutorials/Map_Editor/Prefabs/Prefab_Properties&action=edit&redlink=1)[Next part →](Connecting%20your%20first%20Prefab.md)
>
> [All steps](../Prefabs.md)

You should be familiar with the settings and dialog options on Prefabs by now. Before we can connect and setup our first prefab we must dive into the types of connections that prefabs can make and some weird quirks with connecting them.

Much like road nodes, prefabs have 2 main node types. A red node (*seen as a square in the map editor*), known as the *origin,* and a green node. A prefab will only have one origin (red) node, however, they can have multiple green nodes. Each node on a prefab is a potential point to connect another object, such as a road or prefab. The amount of nodes will vary depending on the prefab. Nodes are defined on the model itself and setup in a modeling program.

> **Note:** You can **never** connect a red node to a prefab red node - it *won't* work!

![Prefab_green_node.png](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/Prefab_green_node.png)

*Green Prefab Node*

![Prefab_red_node.png](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/Prefab_red_node.png)

*Red Prefab Node*

Let's take a look at a few example of different origins on a prefab using this prefab `/prefab2/cross_temp/ger/ger_r1_x_r1_t_narrow_tmpl.ppd`

|  |  |  |
| --- | --- | --- |
| **1** | [![Prefab_full.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_full.jpg)](../../../../files/Prefab%20full.jpg.md) | Prefab with an Origin of 0 <br> (Top Side) |
| **2** | [![Prefab_origin1.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_origin1.jpg)](../../../../files/Prefab%20origin1.jpg.md) | Prefab with an Origin of 1 <br> (Right Side) |
| **3** | [![Prefab_origin2.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_origin2.jpg)](../../../../files/Prefab%20origin2.jpg.md) | Prefab with an Origin of 2 <br> (Left Side) |

Notice how the red node moved to different sides of the prefab? This is the effect of changing the origin. You may have to change the origin in order to correctly connect items to the prefab. <br> <br> Here are a few examples of good and bad connections:

|  |  |  |
| --- | --- | --- |
| **1** | [![Prefab_bad_connection.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_bad_connection.jpg)](../../../../files/Prefab%20bad%20connection.jpg.md) | Prefab cannot connect to road due to 2 red nodes <br> **Note:** If you try to connect these 2 and Snap to Nodes is on, it will look like it connected, but it did not and the navigation will not work |
| **2** | [![Prefab_good_connection.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_good_connection.jpg)](../../../../files/Prefab%20good%20connection.jpg.md) | Prefab will connect to road due to 1 green and 1 red node |
| **3** | [![Prefab_good_connection2.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Prefab_good_connection2.jpg)](../../../../files/Prefab%20good%20connection2.jpg.md) | Prefab will connect to road due to 2 green nodes |

You will notice a few older prefabs, such as `/prefab/light_factory/light_factory.ppd` have multiple nodes, however, trying to connect a road to these produces a strange result:

![Funny_prefab_connection.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Prefab%20Nodes/768px-Funny_prefab_connection.jpg)

For these prefabs you simply drag a road/prefab piece to touch the prefabs geometry where you'd expect the entrance to be and the navigation will still work. This is caused by how this particular prefab was setup in Blender

> [← Previous part](https://modding.scssoft.com/index.php?title=Tutorials/Map_Editor/Prefabs/Prefab_Properties&action=edit&redlink=1)[Next part →](Connecting%20your%20first%20Prefab.md)
>
> [All steps](../Prefabs.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Prefabs/Prefab_Nodes | revision: 5491 | captured: 2026-10-21 23:56:14 -->
