# Tutorials/Map Editor/Introduction to the Map Editor/Basic Editor Functions

> [← Previous part](Launching%20the%20Map%20Editor.md)[Next part →](Saving,%20Loading,%20Sectors,%20and%20Files.md)
>
> [All steps](../Introduction%20to%20the%20Map%20Editor.md)

<table class="wikitable tutorial_infobox" style="float: right" width="300px">
<tbody><tr>
<td colspan="2">Basic Editor Functions
</td></tr>
<tr>
<td colspan="2"><span typeof="mw:File"><a class="mw-file-description" href="../../../../files/Editor%20toolbar%20full.png.md"><img class="mw-file-element" data-file-height="39" data-file-width="2362" decoding="async" height="5" src="../../../../../images/thumb/7/7c/Editor_toolbar_full.png/300px-Editor_toolbar_full.png" srcset="../../../../../images/thumb/7/7c/Editor_toolbar_full.png/450px-Editor_toolbar_full.png 1.5x, ../../../../../images/thumb/7/7c/Editor_toolbar_full.png/600px-Editor_toolbar_full.png 2x" width="300"/></a></span>
</td></tr>
<tr class="info">
<td class="row_name" width="50px"><b>Topic:</b>
</td>
<td>Map Editor Intro Part 2
</td></tr>
<tr class="info">
<td class="row_name" width="50px"><b>Difficulty:</b>
</td>
<td>Easy
</td></tr>
<tr class="info">
<td class="row_name" width="50px"><b>Tools:</b>
</td>
<td><a href="../../../Documentation/Tools/Map%20Editor.md" title="Documentation/Tools/Map Editor">Map Editor</a>
</td></tr></tbody></table>

Now that we have the map editor loaded up, I will explain what each button does in the main toolbar and some common uses of them. As well as some helpful shortcut keys and useful notes. Advanced items, and explanation of the editor tools will be found in later tutorials.

|  |  |
| --- | --- |
| **MAP** | [![Editor_toolbar_map.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_map.png)](../../../../files/Editor%20toolbar%20map.png.md) |

|  |  |
| --- | --- |
| **New Map** | Starts a new map |
| **Load Map** | Loads an existing map |
| **Save Map** | Saves the current map |
| **Export Map** | Used for exporting a selection of your map as Selection Binary Data (SBD) or as an OBJ (useful in modeling programs) This can be used to copy sections of map or to aid in making a custom prefab or modeled object. See the Advanced tutorial to learn more |
| **Import Map** | Importing SBD into currently loaded map |
| **Run Map** | Closes the editor and starts the game with a preview profile to test the currently opened map |

|  |  |
| --- | --- |
| **Edit Mode** | [![Editor_toolbar_editmode.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_editmode.png)](../../../../files/Editor%20toolbar%20editmode.png.md) |

|  |  |
| --- | --- |
| **New Item** | Opens the respective dialog box depending on the selected Item type to add new item |
| **Move Item** | Movement tool on item to move along X, Y, Z axis |
| **Scale Item** | Scale tool on applicable item to move along X, Y, Z axis |
| **Delete Item** | Deletes selected item(s) |
| **Item Properties** | Opens the respective dialog box depending on selected Item type to modify whole item |
| **Node Properties** | Displays info about selected node including Type, UID, Rotation, Position, Locked, Free Rotation etc. |
| **Place Start** | Places the start point for previewing the map (pink car in ETS2 / pink truck in ATS) |
| **Height** | Moves a selected object along the Z axis |
| **Rotate X** | Rotates selected item along X, Y, Z axis |
| **Rotate Y** | Rotates selected item along X, Y, Z axis |
| **Rotate Z** | Rotates selected item along X, Y, Z axis |
| **Brush** | Used to paint textures on terrain and road item terrain and remove vegetation |
| **Ruler** | Tool used to measure distance in meters, can be clicked multiple times to draw segments |
| **Terrain Picker** | &lt;Defunct&gt; |
| **Scene Preview** | &lt;Defunct&gt; |
| **Traffic tool** | Used to check AI traffic flow, can also help find errors with road connections, see speed limits |
| **Vertex tool** | Used to manipulate vertices on terrain quads; can build terrain look and seal gaps |
| **Mute all sounds** | Mutes all sound |

|  |  |
| --- | --- |
| **Snap** | [![Editor_toolbar_snap.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_snap.png)](../../../../files/Editor%20toolbar%20snap.png.md) |

|  |  |
| --- | --- |
| **Snap to nodes** | Nodes will snap to other nodes; used for connecting road/prefab pieces or stacking models |
| **Snap to vertices** | Vertices will snap to other vertices; used with the vertex tool |
| **Snap to grid** | Items will snap to points on the editor's grid |
| **Snap to ground** | Items will fall to ground or other lowest point; another objects collision is ignored |
| **Snap to All Static Collisions** | Items will fall to ground or another objects collision model; IE. stacking two models on top of each other |

|  |  |
| --- | --- |
| **Selection** | [![Editor_toolbar_selection.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_selection.png)](../../../../files/Editor%20toolbar%20selection.png.md) |

|  |  |
| --- | --- |
| **Box Selection** | Select items by clicking and draging a box around them. Holding CTRL adds item to selection and holding ALT removes items from selection |
| **Lasso Selection** | Select items by clicking and drawing a free form shape around them. Holding CTRL adds item to selection and holding ALT removes items from selection |

|  |  |
| --- | --- |
| **Camera** | [![Editor_toolbar_camera.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_camera.png)](../../../../files/Editor%20toolbar%20camera.png.md) |

|  |  |
| --- | --- |
| **Top Camera** | Top down view of the world used for getting the big picture and creating general layout of an area; The grid can only be seen using this mode |
| **Free Camera** | Allows you to fly around the map with W, A, S, D, Q, E, Scroll Wheel up/down |
| **Freeze camera view** | Works much like the pause option in game; flying around with the free camera or newly placed objects will not render until the camera is unfrozen |

|  |  |
| --- | --- |
| **Tools** | [![Editor_toolbar_tools.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_tools.png)](../../../../files/Editor%20toolbar%20tools.png.md) |

|  |  |
| --- | --- |
| **Content browser** | This window shows all assets in the game separated into categories; lots of information can be seen here regarding a particular asset - see the advanced tutorial for more info |
| **Weather editor** | Allows you to edit the weather, sunlight, color, clouds, and DOF |
| **Settings** | Settings for the editor including scale, zoom speed, and auto save time |
| **Find** | Dialog box for finding all types of items with all types of identifiers (sector, UID, city, position, etc.) |

|  |  |
| --- | --- |
| **Item Type** | [![Editor_toolbar_item_type.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_item_type.png)](../../../../files/Editor%20toolbar%20item%20type.png.md) |

|  |  |
| --- | --- |
| **Bezier Patch** | Placeable piece of terrain that can be configured in a few ways; good for patching up odd holes in the terrain |
| **Buildings** | Lines of models used for decoration and function (invisable walls, tree walls, fences, etc.) |
| **Camera Path** | Path for a cutscene camera to travel along |
| **Camera point** | A stationary point that a camera rotates around IE first garage, first truck, etc. |
| **City** | Item that defines city name and city size; new cities must be setup in game DEF files |
| **Curve** | Similar to building item, however, these items have more options and are more flexible for complex situations depedning on item |
| **Cut plane** | Performance item, used for controlling visibility of objects on either side of a plane |
| **Cutscene** | Item to control game, map, and cutscene events |
| **Far model** | Performance item, controls visibility of items at certain distances |
| **Ferry** | Rail/ferry item to teleport player from one point to another as defined in game DEF files |
| **Gate** | Animated gate that follow certain parameters or triggers |
| **Hookup** | Places a model hookup item; see the tutorial on hookups |
| **Map area** | Drawn item with 3 or more points that define some area on the gps or "fake" road/prefab |
| **Map Overlay** | Item that puts an overlay on the map - icon, landmark, text, etc. |
| **Model** | Model item from */def/world/model.sii* |
| **Mover** | Mover item from */def/world/mover.sii*; an object that is animated or follows a path IE train, animals, people |
| **No weather area** | A defined area where weather is effected; IG. for marking no rain inside tunnel or inside building, etc. |
| **Prefab** | Models that have advanced uses and complex layouts and parts; companies, services, fuel stations, highway interchanges, joints, intersections, junctions, etc. |
| **Road** | Main item used for connecting items together and options for connected terrain |
| **Sign** | Editable signs/boards and static (unediatable) signs |
| **Terrain** | Similar to road piece, but no road |
| **Traffic area** | Drawn item with 3 or more points that define some area regarding how traffic will behave in certain situations |
| **Trajectory** | Item that effects how vehicles behave in certain situations; used mostly with oversized missions and other road events |
| **Trigger** | Drawn item with 2 or more points that define some area that triggers some object, script, event IE sleeping area |
| **Visibility area** | Performance item, used in managing what is visible to the player and where; works in tandem with cut planes |

|  |  |
| --- | --- |
| **Grid** Defined the grid size in meters <br> **TIP:** the grid can only be seen in the top camera view | [![Editor_toolbar_grid.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_grid.png)](../../../../files/Editor%20toolbar%20grid.png.md) |

|  |  |
| --- | --- |
| **Rotation** Rotation step of an object in degrees; hold Shift to take effect | [![Editor_toolbar_rotation.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_rotation.png)](../../../../files/Editor%20toolbar%20rotation.png.md) |

|  |  |
| --- | --- |
| **Gizmo** | [![Editor_toolbar_gizmo.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_gizmo.png)](../../../../files/Editor%20toolbar%20gizmo.png.md) |

|  |  |
| --- | --- |
| **Global** | Aligns the move/rotation gizmo to be pointed in Northern direction |
| **Local** | Aligns the move/rotation gizmo to be pointed in relation to the object |
| **View** | Aligns the move/rotation gizmo to be pointed in relation to the camera view |
| **Curve** | &lt;Defunct&gt; |
| **Circle** | Aligns the move/rotation gizmo to be follow a circle; useful for roads and other curved objects |

That is everything covered on the main toolbar and should get you started in the right direction. In future tutorials, we will examine more advanced tools and map debugging items.

## Helpful Notes

**F1 Key** - Opens help dialog where you can find all types of key shortcuts to make your life easier along with a few quick references<br> **F5 Key** - Opens the mini gps view on the top right of the editor to help visualize what you are doing<br> *Where did my items go?* - Hit the A key a few times to toggle between showing background map, items, and map + items<br> *Help! I can't click items or open the console/dialog box in the editor* - Minimize the editor and go to desktop. When you go back to editor everything should be working<br> *My editor crashes randomly or while saving/loading* - Check the editor.log.txt to see the nature of the crash

> [← Previous part](Launching%20the%20Map%20Editor.md)[Next part →](Saving,%20Loading,%20Sectors,%20and%20Files.md)
>
> [All steps](../Introduction%20to%20the%20Map%20Editor.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Introduction_to_the_Map_Editor/Basic_Editor_Functions | revision: 5504 | captured: 2026-10-21 23:56:14 -->
