# Tutorials/Map Editor/Roads/Creating a Simple Road

> [← Previous part](Road%20Item%20Properties%20Dialog.md)[Next part →](Road%20Node%20Manipulation.md)
>
> [All steps](../Roads.md)

In this tutorial, we will create a simple set of roads with some vegetation, and some small decoration provided by the Road item properties dialog. Before we do, however, we must explain about Node Snapping. <br> <br> Every Item type that can be connected has 2 ends. Each end has either, a green circle/square node, or a red circle/square node(prefabs have more but we will cover that later) Nodes can be connected together but not always - the colors that go together are important. Here is the general rule of thumb regarding snapping: **Green and Red nodes can connect to each other; same colored nodes cannot connect.**

![Road_node_red.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Creating%20a%20Simple%20Road/Road_node_red.png)

*Red Node*

![Road_node_green.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Creating%20a%20Simple%20Road/Road_node_green.png)

*Green Node*

|  |  |  |
| --- | --- | --- |
| **1** | [![Basic_road.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Creating%20a%20Simple%20Road/712px-Basic_road.jpg)](../../../../files/Basic%20road.jpg.md) | Select 'Road' then select New item (*E Key*) Click on Road type and pick `ger road 1 tmpl` Click at the base of the pink starter car and drag up to just under the main toolbar and click again Hit *Esc* - we should have a nicely placed road <br> <br> **TIP:** Make sure you are in top down camera view when placing roads! <br> |
| **2** | [![Road_item_properties.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Creating%20a%20Simple%20Road/712px-Road_item_properties.png)](../../../../files/Road%20item%20properties.png.md) | Go to Item properties (*P Key*) and click on one of the nodes |
| **3** | [![Basic_road_decor.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Creating%20a%20Simple%20Road/712px-Basic_road_decor.jpg)](../../../../files/Basic%20road%20decor.jpg.md) | In the dialog box, adjust options to your liking Play around with all the potential settings to get your first stretch of road looking nice When you are done click the 'Set as default' button <br> <br> **TIP:** You might find it easier at first to set your Terrain size to something small like 5 - 25 meters to make placing multiple roads easier <br> |
| **4** | [![2_basic_roads.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Creating%20a%20Simple%20Road/712px-2_basic_roads.jpg)](../../../../files/2%20basic%20roads.jpg.md) | Now, zoom your camera out a bit and repeat step # 1 this time placing the road just above the road you have just made |
| **5** | [![Basic_road_connected.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Creating%20a%20Simple%20Road/712px-Basic_road_connected.jpg)](../../../../files/Basic%20road%20connected.jpg.md) | Click the Move tool (*M Key*) and click on the red node of the 2nd road piece you just placed and drag this node over to the green node of the first road <br> <br> **TIP:** Ensure Snap to nodes is enabled in the main toolbar <br> **Note:** You will notice the 2 road pieces snapped together and are now connected. Additionally, the editor automatically curved the roads based on the different angle between nodes. Snapping subsequent road pieces together will continue bending roads yielding smooth curves, however, these simple roads aren't good for more tighter or precise turns |

> [← Previous part](Road%20Item%20Properties%20Dialog.md)[Next part →](Road%20Node%20Manipulation.md)
>
> [All steps](../Roads.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Roads/Creating_a_Simple_Road | revision: 5449 | captured: 2026-10-21 23:56:14 -->
