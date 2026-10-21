# Tutorials/Map Editor/Introduction to the Map Editor/Saving, Loading, Sectors, and Files

> [← Previous part](Basic%20Editor%20Functions.md)
>
> [All steps](../Introduction%20to%20the%20Map%20Editor.md)

<table class="wikitable tutorial_infobox" style="float: right" width="300px">
<tbody><tr>
<td colspan="2">Saving, Loading, Sectors, and Files
</td></tr>
<tr>
<td colspan="2"><span typeof="mw:File"><a class="mw-file-description" href="../../../../files/First%20map%20ingame%2002%208.jpg.md"><img class="mw-file-element" data-file-height="2160" data-file-width="3840" decoding="async" height="169" src="../../../../../images/thumb/b/bd/First_map_ingame_02_8.jpg/300px-First_map_ingame_02_8.jpg" srcset="../../../../../images/thumb/b/bd/First_map_ingame_02_8.jpg/450px-First_map_ingame_02_8.jpg 1.5x, ../../../../../images/thumb/b/bd/First_map_ingame_02_8.jpg/600px-First_map_ingame_02_8.jpg 2x" width="300"/></a></span>
</td></tr>
<tr class="info">
<td class="row_name" width="50px"><b>Topic:</b>
</td>
<td>Map Editor
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

So far we have learned how to launch the editor, and some of the basic tools and functions that are available to us. We will continue to expand on this by learning how to save, load, and run our map. We'll also talk about where our files are being saved and what's in them.

## Placing our First Road and Saving our Map

|  |  |  |
| --- | --- | --- |
| **1** | [![First_road_piece_02_1.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/1024px-First_road_piece_02_1.png)](../../../../files/First%20road%20piece%2002%201.png.md) | With our editor open, we will click on the 'Item type' drop down and select 'Road' (shortcut: 1) |
| **2** | [![Road_properties_02_2.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/1024px-Road_properties_02_2.png)](../../../../files/Road%20properties%2002%202.png.md) | Next, click New item (shortcut: E). This will open the Road item default properties. Leave everything for now as default - we will go in depth with road pieces and connections in a later tutorial <br> **TIP:** Ensure you are in Top Camera view when placing roads (shortcut: C) |
| **3** | [![First_road_line_02_3.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/1024px-First_road_line_02_3.png)](../../../../files/First%20road%20line%2002%203.png.md) | Click near the rear of the pink car and then drag your mouse up. A red line should appear showing the road path before you click the second time drawing the road. Hit Esc to clear out placing any new items |
| **4** | [![Start_position_02_4.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/1024px-Start_position_02_4.jpg)](../../../../files/Start%20position%2002%204.jpg.md) | Activate 'Free Camera' (shortcut: C) and fly down to your road piece. Ensure our starting spot (pink car) is touching the ground - if not, ensure Snap to Ground (shortcut: G) is on and then click 'Place Start' and click somewhere on the road |
| **5** | [![Save_first_map_02_5.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/Save_first_map_02_5.png)](../../../../files/Save%20first%20map%2002%205.png.md) | Now go to File > Save As (shortcut CTRL + S); name your map whatever you want - mine is named 'deerland'. You do not need to change any settings here. Leave location and anything else unchanged |

## Loading our map

|  |  |  |
| --- | --- | --- |
| **1** |  | Launch the Map Editor |
| **2** | [![Open_first_map_02_6.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/Open_first_map_02_6.png)](../../../../files/Open%20first%20map%2002%206.png.md) | Go to File > Open; double click on your named map - it should open to where we left off<br> That's it! Loading the map is super easy and the editor should load in the last area you were before you exited <br> **TIP:** Alternatively, you can add '-edit *map_name* (-edit deerland) in your shortcut to load directly to our map |

## Running our First Map

|  |  |  |
| --- | --- | --- |
| **1** | [![First_map_ingame_02_8.jpg](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/1024px-First_map_ingame_02_8.jpg)](../../../../files/First%20map%20ingame%2002%208.jpg.md) | With your map open in the editor, click on the Run Map button. The game will load a preview profile and spawn you in at the start point <br> **Note:** If your game crashes you probably have mods enabled somewhere, either in */home* or from the steam workshop. You can still run your map by launching the game like normal and then typing 'preview *map_name*' into console IE. 'preview deertest' |

## Sectors, an Explanation

So I want you to imagine mainland Europe. Now imagine that we took a giant cookie cutter in the shape of a square and punched a chunk out in the middle of Europe. This single square is called a sector. The entire map of Europe, or any map for that matter, is made up of many of these sectors. The first sector of the map is the origin, and it's named: SEC + 0000 + 0000. A single sector has a length of 4000 meters with a height of 4000 meters or 16<sup>2</sup> km. Sectors are numbered from 0000-9999 and may either have a (-/+). The can travel near infinitely in the X and Y axis. Each subsequent sector change their value based on their location. The image below shows how sectors are numbered starting from the origin.

![Sector_layout_graph.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/Sector_layout_graph.png)

So what does that mean for us? For map editing not too much. When we get to the edge of a sector, the editor automatically creates another sector with no input necessary from you. However, if you have a problem with a single sector you don't loose your entire map, and it makes it easier to keep track of different changes. Additionally, several map makers could work on a single map project dividing the work among sector borders.

This brings us to our next topic...

## Files

When we launched the editor for the first time, a folder was automatically created in our *`/home/mod`* directory called 'user_map' This is where the game automatically saved our map and map files. Lets take a look at what was saved.

![Mod_directory_user_map_02_7.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Saving,%20Loading,%20Sectors,%20and%20Files/Mod_directory_user_map_02_7.png)

> **Note:** Typical location of the *`/home`* directory: *`C:\Users\*user*\Documents\Euro Truck Simulator 2\mod`*

Looking inside of *`/home/mod/user_map/`* we have a folder and 3 files (*remember our example map was named "deerland"*):

- deerland (*folder*)
- deerland.epa
- deerland.mbd
- deerland.set

Now looking inside of *`/home/mod/user_map/deerland/`* we have 5 files:

- sec-0001-0001.aux
- sec-0001-0001.base
- sec-0001-0001.data
- sec-0001-0001.desc
- sec-0001-0001.layer

> **Note:** Your first sector number might be different depending on where you clicked and drew your first and only road piece

These files are stored in binary format that the game reads data from. The most important part is that a single sector is made up of 5 files (*6 files counting a .SND file which is not present here since we have no sounds in our sector, yet*) In order for your map sector to function you need at least all 5 named sector files or your game will crash. Each of the 5 sector files are responsible for a different aspect of our map: roads, signs, sounds, model placement, sign layouts, overlays, cities, companies, etc. The 3 other map named files are header files that are used to open our map in the editor.

> [← Previous part](Basic%20Editor%20Functions.md)
>
> [All steps](../Introduction%20to%20the%20Map%20Editor.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Introduction_to_the_Map_Editor/Saving%2C_Loading%2C_Sectors%2C_and_Files | revision: 5593 | captured: 2026-10-21 23:56:14 -->
