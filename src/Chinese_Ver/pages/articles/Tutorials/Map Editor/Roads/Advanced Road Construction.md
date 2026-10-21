# Tutorials/Map Editor/Roads/Advanced Road Construction

> [← Previous part](Road%20Node%20Manipulation.md)
>
> [All steps](../Roads.md)

Now that we have a basic understanding of how to connect roads and simple decorations for them. Lets focus on some advanced items using the `Road` item type.

## **Bridges**

|  |  |  |
| --- | --- | --- |
| **1** | [![Road_piece_tunnel_start.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_piece_tunnel_start.jpg)](../../../../files/Road%20piece%20tunnel%20start.jpg.md) | Using our example map, place a road and edit the properties to set the road look, variant, and set the terrain size to 0 meters |
| **2** | [![Road_bridge_start.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_bridge_start.jpg)](../../../../files/Road%20bridge%20start.jpg.md) | Go to railings tab, and pick a nice bridge model <br> Here is what we are using: `/model2/railing/bridge/shared_simple.pmd` <br> Take note of the road edge material and terrain material (*these are necessary with most models to have nice looking edges*) |
| **3** | [![Road_bridge_settings.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_bridge_settings.jpg)](../../../../files/Road%20bridge%20settings.jpg.md) | Allign your bridge to make it look nice and to fit with the area <br> <br> **TIP:** You can use a marker model such as `/model2/proxy_trailer_overweight.pmd` to make sure your bridge is not too low to adjacent road pieces |
| **4** | [![No_veg_sphere.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-No_veg_sphere.jpg)](../../../../files/No%20veg%20sphere.jpg.md) | In our example, we have trees clipping through the bridge models. <br> Go to the road item properties dialog box (of the problematic road piece's terrain) and click `Add veg. sphere.` Modify the properties to adjust for size and position and set to `No Vegetation` to clean up the area |
| **5** | [![Road_bridge_final.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_bridge_final.jpg)](../../../../files/Road%20bridge%20final.jpg.md) | Use a few tools such as, brush and vertex tool to round off terrain into bridge models to develop the look you are going for |

## **Tunnels**

Tunnels are exactly like bridges, but in reverse and hopefully not floating in the sky!

|  |  |  |
| --- | --- | --- |
| **1** | [![Road_piece_tunnel_start.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_piece_tunnel_start.jpg)](../../../../files/Road%20piece%20tunnel%20start.jpg.md) | Using our example map, place a road and edit the properties to set the road look, variant, and set the terrain size to 0 meters |
| **2** |  | Go to railings tab, and pick a nice tunnel model <br> Here is what we are using: `/model2/railing/tunnel/tunnel_hw_2_lanes_one_way_it.pmd` |
| **3** |  | Use models, signs, building items and brushes to make your item fit with the area and look nice |
| **4** | [![Road_piece_tunnel_final.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Advanced%20Road%20Construction/712px-Road_piece_tunnel_final.jpg)](../../../../files/Road%20piece%20tunnel%20final.jpg.md) | Add a No weather area item and set for tunnel Fit the weather area to the tunnel |

> [← Previous part](Road%20Node%20Manipulation.md)
>
> [All steps](../Roads.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Roads/Advanced_Road_Construction | revision: 5497 | captured: 2026-10-21 23:56:14 -->
