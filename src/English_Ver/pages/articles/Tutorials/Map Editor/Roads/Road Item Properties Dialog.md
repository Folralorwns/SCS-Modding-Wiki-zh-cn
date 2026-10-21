# Tutorials/Map Editor/Roads/Road Item Properties Dialog

> [← Previous part](Road%20Item%20Default%20Properties%20Dialog.md)[Next part →](Creating%20a%20Simple%20Road.md)
>
> [All steps](../Roads.md)

If we click Item Properties (*P key*) and then click the road piece, we will get a new dialog box which shows all options for our road. Most of the options listed here are similar to the previous dialog box. Listed below are the new items.

![Road_item_properties.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_item_properties.png)

## Main Dialog

|  |  |
| --- | --- |
| **View Distance** (*Slider*) | Distance in meters that the object can be viewed from |

![Road_prop_checkboxes.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/768px-Road_prop_checkboxes.png)

|  | Checkboxes |
| --- | --- |
| **High-poly road** | Enables more terrain quads; good for blending terrain using brush tool |
| **Low-poly veg.** | Low quality vegetation used for performance |
| **Superfine** | &lt;Defunct&gt; |
| **Tunnel road** | &lt;Defunct&gt; Use `Weather area` |
| **No Collision** | Turns of collision for road piece |
| **Ignore cut planes** | Road item ignores cut planes and loads regardless |
| **Terrain shadows** | Terrain cast shadows on road piece |
| **Show in UI map** | Shows road on GPS and enables navigation |
| **Water reflection** | Road reflects on water surfaces |
| **Smooth detail veg.** | Smooth transition of terrain and brushes |
| **No AI vehicles** | Disables AI traffic for selected road |
| **Left-hand traffic** | Reverses AI pathing on roadway for left hand drive traffic |
| **GPS Avoid** | Game will ignore road piece for navigation |
| **No boundary** | Removes invisible walls surrounding road |
| **Stretch terrain** | &lt;Defunct&gt; |
| **Secret road** | Road shows up on gps only after being discovered |

![Road_prop_terrain_size.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/Road_prop_terrain_size.png)

|  |  |
| --- | --- |
| **Terrain size** | Size in meters the terrain will extend from road model |
| **Road heigh offset** | Offset height of the terrain in meters |
| **Shoulder blocked** | Disables spawning of items close to road edge |

![Road_prop_profile.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/Road_prop_profile.png)

|  |  |
| --- | --- |
| **Profile** | Predefined terrain shape |

## Vegetation Tab

![Road_properties_vegetation.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_properties_vegetation.png)

3 drop-down boxes for selecting 3 different vegetation models as defined in`/def/world/vegetation.sii`

|  |  |
| --- | --- |
| **Sparsity** | Denesity of vegetation; lower values = higher density |
| **From/to** | Selected vegetation model appears between which distances on terrain in meters |

## Model Tab

![Road_properties_model.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_properties_model.png)

2 drop-down boxes for selecting models; these are used as a repeating object separated by distance IE lamps, signs, posts, etc.

## Railing Tab

![Road_properties_railing.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_properties_railing.png)

3 drop-down boxes for selecting models; these are used as a continuous object IE guardrails, tunnel walls, bridge walls, etc.

## Overrides Tab

![Road_prroperties_overrides.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_prroperties_overrides.png)

Used for overriding variants and edges on the road piece to add multiple looks/edges to the same road piece

## Misc. Tab

![Road_properties_misc.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_properties_misc.png)

Additional parts supported by the road model can be turned on/off here

> [← Previous part](Road%20Item%20Default%20Properties%20Dialog.md)[Next part →](Creating%20a%20Simple%20Road.md)
>
> [All steps](../Roads.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Roads/Road_Item_Properties_Dialog | revision: 5458 | captured: 2026-10-21 23:56:14 -->
