# 教程/地图编辑器/道路/高级道路建造

> [← 上一部分](Road%20Node%20Manipulation.md)
>
> [所有步骤](../Roads.md)

现在我们已经基本了解如何连接道路以及为道路添加简单装饰。接下来让我们专注于使用 `Road` 项类型的一些高级内容。

## **桥梁**

|  |  |  |
| --- | --- | --- |
| **1** | [![Road_piece_tunnel_start.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_piece_tunnel_start.jpg)](../../../../files/Road%20piece%20tunnel%20start.jpg.md) | 使用我们的示例地图，放置一条道路并编辑属性，设置道路外观、变体，并将地形尺寸设为 0 米 |
| **2** | [![Road_bridge_start.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_bridge_start.jpg)](../../../../files/Road%20bridge%20start.jpg.md) | 转到护栏标签页，挑一个漂亮的桥梁模型 <br> 我们使用的是：`/model2/railing/bridge/shared_simple.pmd` <br> 注意道路边缘材质和地形材质（*大多数模型都需要这些才能获得美观的边缘*） |
| **3** | [![Road_bridge_settings.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_bridge_settings.jpg)](../../../../files/Road%20bridge%20settings.jpg.md) | 调整桥梁的对齐方式，使其外观美观并与区域契合 <br> <br> **提示：** 你可以使用标记模型（例如 `/model2/proxy_trailer_overweight.pmd`）来确保桥梁相对于相邻道路部件不会太低 |
| **4** | [![No_veg_sphere.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-No_veg_sphere.jpg)](../../../../files/No%20veg%20sphere.jpg.md) | 在我们的示例中，树木穿过了桥梁模型。 <br> 打开（有问题的道路部件地形的）道路项属性对话框，点击 `Add veg. sphere.` 修改属性以调整尺寸和位置，并将其设为 `No Vegetation` 以清理该区域 |
| **5** | [![Road_bridge_final.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_bridge_final.jpg)](../../../../files/Road%20bridge%20final.jpg.md) | 使用画笔和顶点工具等几种工具，将地形修饰成符合桥梁模型的样子，以营造你想要的外观 |

## **隧道**

隧道与桥梁完全一样，只是方向相反，但愿不会漂浮在空中！

|  |  |  |
| --- | --- | --- |
| **1** | [![Road_piece_tunnel_start.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_piece_tunnel_start.jpg)](../../../../files/Road%20piece%20tunnel%20start.jpg.md) | 使用我们的示例地图，放置一条道路并编辑属性，设置道路外观、变体，并将地形尺寸设为 0 米 |
| **2** |  | 转到护栏标签页，挑一个漂亮的隧道模型 <br> 我们使用的是：`/model2/railing/tunnel/tunnel_hw_2_lanes_one_way_it.pmd` |
| **3** |  | 使用模型、标志牌、建筑项和画笔，使你的项与该区域契合并显得美观 |
| **4** | [![Road_piece_tunnel_final.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_piece_tunnel_final.jpg)](../../../../files/Road%20piece%20tunnel%20final.jpg.md) | 添加一个无天气区域项并设为隧道 将天气区域调整为与隧道契合 |

> [← 上一部分](Road%20Node%20Manipulation.md)
>
> [所有步骤](../Roads.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Roads/Advanced_Road_Construction | revision: 5497 | captured: 2026-10-21 23:56:14 -->
