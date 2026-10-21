# Tutorials/Map Editor/Prefabs/Connecting your first Prefab

> [← Previous part](Prefab%20Nodes.md)
>
> [All steps](../Prefabs.md)

Previously, we learned how to connect roads together, but what do we do once we need to connect more than one road to each other? We need a prefab! Prefabs come with many different names. SCS usually names prefabs based upon the country they are used in, how many lanes they support, and what their general function is. Use the asset browser to find the right prefab for what you are trying to do. In this tutorial we will connect a few roads together to form an intersection. For this tutorial, we are going to connect 2 roads together using a basic junction.w

> **TIP:** Use the asset's browser catagories on the left side to help find prefabs

|  |  |  |
| --- | --- | --- |
| **1** | [![Asset_browswer_prefab.png](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/512px-Asset_browswer_prefab.png)](../../../../files/Asset%20browswer%20prefab.png.md) | Decide what kind of junction you would like IE. 4 way, T, roundabout, highway, Y, etc. |
| **2** | [![Selected_prefab_cb.png](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/Selected_prefab_cb.png)](../../../../files/Selected%20prefab%20cb.png.md) | For our map I have picked a T Junction <br> Here is what we are using: `/prefab2/cross_temp/ger/ger_r1_x_r1_t_narrow_tmpl.ppd` |
| **3** | [![Prefab_setup_origin.png](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/512px-Prefab_setup_origin.png)](../../../../files/Prefab%20setup%20origin.png.md) | In the Prefab default properties I'm going to change our origin (*red node*) so that I can connect our 2 roads |
| **4** | [![Prefab_fitting_origin.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/512px-Prefab_fitting_origin.jpg)](../../../../files/Prefab%20fitting%20origin.jpg.md) | Click to place your prefab and align it with your road pieces Snap your road pieces to the junction prefab <br> <br> **Note:** Notice that each road ends with a red node - You cannot connect red road nodes to a red (origin) prefab node! |
| **5** | [![Prefab_junction_final.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/512px-Prefab_junction_final.jpg)](../../../../files/Prefab%20junction%20final.jpg.md) | Modify the prefab in the settings to adjust for terrain material, terrain size, road markings, look, variant, corner pieces, and any vegetation that is desired if it is supported <br> <br> **TIP:** Once you setup a prefab how you like, if you set as default or save as preset every prefab you place will inherit your material settings where supported |

![Junction_prefab_deco.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Prefabs/Connecting%20your%20first%20Prefab/768px-Junction_prefab_deco.jpg)

> [← Previous part](Prefab%20Nodes.md)
>
> [All steps](../Prefabs.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Prefabs/Connecting_your_first_Prefab | revision: 5481 | captured: 2026-10-21 23:56:14 -->
