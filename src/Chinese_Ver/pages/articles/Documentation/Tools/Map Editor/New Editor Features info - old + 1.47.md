# Documentation/Tools/Map Editor/New Editor Features info - old + 1.47

## Old features explanation

### Trajectories

- Trajectory item represents navigation lanes edited directly in the editor and stored in the map
- Each trajectory has 1 to N nodes.
- **Green** part indicates the beginning of the trajectory (first node -> id **0**) and the **red** part indicates the end of trajectory (last node -> id **N-1**).
- In the current version we are not able to spawn vehicles to the trajectory items (with the exception of manual spawning in the debug traffic camera).
  - It means these items must be connected to the traffic network.
- Important editor shortcut for Trajectory items are **F6 (drop to ground)** and **Alt + F6 (drop to ground with rotation alignment)**

When connecting Trajectories to the existing traffic lines

- Trajectory items are not connected to prefab/road nodes but to prefab/road navigation lanes. This means that you cannot use function like node snap.
- First node can be connected with 'output' lane and last node can be connected with 'input' lane.
- For a valid connection, you don't have to have exactly the same position, there is a tolerance 0.5m. Rotation of the node must be in the connection direction with tolerance 90 degrees.
- **You cannot** place trajectories near another AI lanes (prefab, road) because these are separate systems and cars will crash with each other because trajectory cars don't know about prefab/road cars and vice-versa.
- There can be always only **one connected trajectory per navigation lane**.

When connecting Trajectories to other Trajectories.

- The only valid connection is **first node <-> last node.**
- But you can have more trajectories connected with another trajectory.
- All nodes within one connection should have **same position** and **same rotation**.
- Intersections cannot have more than 4 branches (4 start + 1 end **OR** 4 end + 1 start).
- One node cannot be merge and fork intersection at one time.
- **Do not cross** trajectories -> vehicles will crash with each other.

### Traffic Tool

Traffic preview provides editor traffic debug layer. It works in the following way:

- **When the tool is activated all sectors are locked**. Traffic related pins are shown in gray color. It means that **you cannot edit map** but you can still see the map structure.

- **When it is deactivated all sector locks are restored to the state before activation**.

- This tool requires `Snap to Ground` to be turned on to work properly.

#### Speed Limit section

- Provides information about speed limits at traffic curves.
- The tool uses **speed units** based on attribute **`traffic_use_mph`** in *base/def/editor_data.sii*.
- Absolute Speed Limits
  - useful for general overview of speed limits
  - each speed limit value has its own color
  - **unset** speed limits are visualized using **white color**
- Relative speed limits
  - useful for visualization of single speed limit value
  - selected speed limit uses **white color**
  - **unset** speed limits are visualized using **pink color**

- Speed drops
  - Places where speed limit changes to a lower one without a nearby traffic sign informing about it. It is visualized using blue sphere.

Usage:

- Use combo box to change visualized vehicle type
  - By default, `(default)` is selected, which represents **limit for "general traffic"**, i.e. the limit which **corresponds to standard speed limit signs**, which are not type-exclusive (e.g. "trucks only").

- To turn on **Absolute speed limit visualization**, click on ***NO LIMIT*** button.
- To turn on **Relative speed limit visualization**, either click on one of the **button with speed limit value** or **click on one of the traffic curves** in map.

#### Access/Spawning

- Provides information about traffic access of the traffic lanes for the given vehicle type.
- Also allows spawning AI vehicles and placing spawn points at desired locations.

- **green** - access is **allowed**
  - **dark green** - access **is allowed only for vehicles without trailers**
- **yellow** - access is **allowed exclusively** for one or more vehicle types
  - **dark yellow** - access **is allowed only for vehicles without trailers**
- **red** - access is **not allowed**
- Dead Ends
  - Dead end visualization helps **identifying places**, where vehicles of certain type(s) are **not allowed to continue their movement** and **there is risk of visible despawn.**
  - Dead ends are visualized using blue sphere with text containing the first found 'blocked' vehicle type.

Usage:

- **Vehicles**
  - Use combo box to change visualized vehicle type
  - To **spawn** a vehicle of selected type, just point the mouse cursor at one of traffic lines and click left mouse button (LMB).
    - If possible, a vehicle appears at given position. Otherwise, an error message in console appears showing why the spawning has not been successful.
    - By default, spawning of selected vehicle type(s) is possible only where it would be normally spawned in game. Use ***Forced spawning*** checkbox to override.
    - If spawning of non-moving vehicles is needed, use ***Spawn paused vehicles*** checkbox or manually pause the movement using ***Pause all vehicles*** button
      - The movement is *paused*, not *stopped.* Pausing does not affect the actual vehicle speed or acceleration.
  - In **Remove vehicle** mode, vehicles can be removed by clicking with the left mouse button.
  - Switch to **Select/Manipulate** mode to manipulate spawned vehicles.
    - left mouse button (LMB) selects and deselects. Some information about the selected vehicle will be displayed in the editor's bottom status bar.
    - Ctrl + LMB stops all vehicles close to the mouse cursor, even if they are not selected.
- **Spawn points**
  - The Access/Spawning tab also offers the option to place spawn points and let vehicles spawn automatically. Additionally, you can also let spawn points generate as they would in-game.
  - For vehicles to spawn from any spawn points at all, the ***Automatic vehicle spawning*** checkbox must be checked.
  - By default, spawn points generate automatically in the editor, as in game. They will generate at a certain distance from the editor camera as white spheres. However, you can also create manual spawn points (represented by magenta spheres), which can be placed using the submodes:
    - In **Create spawn point** mode, spawn points can be placed on any valid traffic item by left mouse click.
    - In **Remove** **spawn point** mode, previously placed or automatically generated spawn points can be removed by left mouse click.
  - Manually placed spawn points have a magenta color while automatically generated spawn points are white.
  - Using the **Freeze spawn point autogeneration** button, the current state of spawn points can be then frozen at any time, which pauses the spawn point autogeneration algorithm and leaves all automatic (white) spawn points where they are. This allows you to assess roughly where spawn points will generate in-game. The button's label will change between Freeze and Unfreeze accordingly.
  - If you then want automatic generation of spawn points to resume, click the **Unfreeze spawn point autogeneration** button. New spawn points should start generating at a certain distance from the camera. Any manually placed spawn points are unaffected.
  - For quicker replacing of spawn points, some simple removal options are available.

### Visibility Area

The idea of **Visibility Areas (VA)** is a local, viewpoint based scene adjustment.

Visibility area offers what these other tools do not: precise, pinpoint optimization by allowing the map designer to tell the engine exactly which objects to draw or not, when the player is inside the VA

- Can be rotated (yaw only)
- Size can be changed

#### Modes

- **Show hidden objects**
  - shows all selected items even when they are normally hidden by the cutplane. Objects that are not hidden by the cutplane are displayed normally when the player is not inside the visibility area.

- **Hide objects**
  - All objects assigned to the visibility area are: HIDDEN when the player is inside the area and VISIBLE when the player is outside the area.

- **Show objects**
  - All objects assigned to the visibility area are: VISIBLE when the player is inside the area and HIDDEN when the player is outside the area.

#### Adding Items

- To add new objects to a VA, select the VA first, then hold down Ctrl and select on more items. Then click on VA properties and add the selected items to the area. A connecting line is created between each item in the VA list and the VA node.

#### Selecting items from the VA

- When inside VA properties you click the item from the list and then click **[Select item]**, or click **[Select all items]**, the node of that object is selected in map and you leave the VA properties window.

#### Removing Items

- Either click on object/s in the VA list and click **[Remove item]**, or click **[Remove all items]** if you wish to empty the area.
- Select one or more objects in the map together with the VA itself, then click VA properties and click **[Remove items currently selected in map]** button.

### Far Model item

Far Model Item is a way to display models that need to be seen from further away than from maximum allowed view distance of 1500m or need to be visible from certain points from further away than their set view distance.

There are two types of of items that can be displayed, each behaving a different way:

- **Far Model** = Original usage of the Far Model item and default for the all new Far Model items placed into the map.
- **Map Items** - New usage turned on by checking the box "*use map items*".

#### General Far Model usage notes

- Do not overdo it with the number of models assigned to the Far Model Item, watch the performance.
- Use at most 4-5 Far Model items per sector and not too close to each other.

#### Far Model - default, when "*use map item*s" is unchecked

- Uses only the Far Model assets.
- Those models are visible only from within Far Model area boundaries.

Usage notes:

- You can scale those models in Far Model properties.
- You can set Water Reflection to those models in properties.
- When the Far Model item node are deleted so are the Far model assets added to it!

#### Map Items - when "use map items" checked

- Can use other items placed in the map:
- Terrains, models, curves, buildings and bezier patches CAN be added to the Far Item.
- *Roads, prefabs, signs and movers CAN NOT be added to the Far Item.*
- Those models are visible from the Far Model area boundaries AND they are also visible outside far item boundaries when the camera is within their own set view distance.

Usage notes:

- You can scale the assigned models normally in their Properties.
- The water reflection of the assigned item is decided by their own Properties when outside the far item area boundary and by the Far Model item properties when inside the boundary.
- When Far Model item node is deleted the assigned map items are NOT deleted!

## New features - 1.47

### Right Mouse Button (RMB) to open item/node Properties

One can now:

- open Item properties of items in map using the Right Mouse Button click, regardless of the edit mode you are in *( `M`ove, `R`otate, `P`roperties etc.)*
- open the node properties of any node in map using the `CTRL+RMB click`, regardless of the edit mode you are in
- you don't need to select (`LMB`) the item's node beforehand, just to hover above the node and use the `RMB`

- Using `RMB click` *(or the `P`roperties mode `LMB`)* on a GREEN node of a road/terrain/building/curve item will now open it's Item Properties and selects it's red node!

### Quick Edit Mode

**This mode is a tool for a direct interaction with and manipulation of all types of terrains, roads and road edges, by using new nodes = handlers.**

You can turn this mode on and off by pressing the `Q` button *(or by going to Tools -> Quick Edit Mode)*.

![QEM.jpg](../../../../../../images/articles/Documentation/Tools/Map%20Editor/New%20Editor%20Features%20info%20-%20old%20+%201.47/300px-QEM.jpg)

*Quick Edit Mode*

**Handlers for all terrains - ◆**

- can be dragged to the sides *(using the `M`ove function)* to change the length of the terrain
- dragged up and down to change the coefficient of the terrain profile
- rotated *(using the `R`otate function)* to change the angle of the main terrain material

**All handlers for terrains, roads, edges and prefab centers - ◆ ◪ ∎**

- have their own small miniproperties you can use to make quick changes

### Hookup Item

#### What is Hookup Item?

- new type of item used to place dynamic object into the map
- what are dynamic objects? = all objects that can change their position or their look depending on the situation *(time, part of the day etc.)* or that look different depending in the place you put them in *(state, city etc.)*
  - right now that includes various types of parked vehicles *(even though at the moment only selected pools are available)*
  - but in the future this will expand to various other non-vehicle objects like parasols by restaurants *(that can be open during the day but closed at night)*, trash cans *(that can be empty one time the player drives by them but full next time)*, cargo boxes and containers placed at fake company areas etc.
- as opposed to the static models like "parked_car_physics" we have been using for this until now - objects placed through hookup item have also a certain chance to not spawn at all, leaving the parking spot empty

#### How the Hookup Item looks and what can we do with it?

- you can place into the map either an empty hookup item from the item list or specific hookup *(parked car, truck etc.)* from the Content Browser
  - the hookup item node looks similar to the static Model node, but it has a dot in the middle<br>

![Hookup_intro_01_empty.jpg](../../../../../../images/articles/Documentation/Tools/Map%20Editor/New%20Editor%20Features%20info%20-%20old%20+%201.47/300px-Hookup_intro_01_empty.jpg)

*empty hookup*

- when you open Hookup properties you are presented with several options

![Hookup_intro_02_props.jpg](../../../../../../images/articles/Documentation/Tools/Map%20Editor/New%20Editor%20Features%20info%20-%20old%20+%201.47/300px-Hookup_intro_02_props.jpg)

*Hookup Properties*

**NOTE:** the green outline around the model represents the bounding box = the size of the largest object that can spawn on this hookup

- you can select the type of hookup you want to use either from the list, or from the Content Browser as usual
- you can set up the view distance as usual
- Align to node is a new feature containing three options
  - None (the node is placed in the middle of the vehicle as usual)
  - Front - the node is placed in front of the bounding box
  - Back - the node is placed on the back of the bounding box

![Hookup_intro_03_front.jpg](../../../../../../images/articles/Documentation/Tools/Map%20Editor/New%20Editor%20Features%20info%20-%20old%20+%201.47/300px-Hookup_intro_03_front.jpg)

*Front*

![Hookup_intro_04_back.jpg](../../../../../../images/articles/Documentation/Tools/Map%20Editor/New%20Editor%20Features%20info%20-%20old%20+%201.47/300px-Hookup_intro_04_back.jpg)

*Back*

#### Spawn probability

It is meant to be used for optimization and for us to decide how often should the hookup spawn the object - in this case a car

-
  - it contains 4 setups
  - Default, 25%, 50% and 75%
  - BUT this doesn't mean that on the default probability the model will spawn 100% of the time, or that 50% means it will the spawn rate will be 50:50!
  - each type of hookup can have their spawn factor affected by multiple things - what item it is, whether they are placed in city are or not, whether it is a day or night etc.
  - just as an example let's imagine "parked car (common)" has default spawn probability set to
    - 80% spawn chance during the day
    - 20% spawn chance during night
  - changing the Spawn probability to 50% in this case would mean lowering the spawn chance to approx 40% spawn chance during the day and 10% spawn chance at night

#### Model detail

It is another new option for optimization, it is similar to picking dynamic or static lod for the static model BUT with the difference Hookup items have only dynamic lods. There are 4 options:

-
  - Default - spawns the model as usual starting from the most detailed version (lod0) when you are closest to it and dynamically changing it as you move further away (lod0->lod1->lod2->lod3)
  - Average - spawns the model from the second most detailed (lod1) and never displays lod0 no matter how close you are to the model, as you move further away it will dynamically change the model as usual (lod1->lod2->lod3)
    - you can use this option, and the options below, when you want to lower the quality of models the player cannot properly see anyway - like when they are obstructed by bushes or other vehicles etc.
  - Low - spawns the model from lod2 and never displays lod0 or lod1, dynamically changes to lod3
  - Very Low - spawns the model only at its least detailed lod

#### Water reflections

Works as usual, selecting this will allow for the spawned model to be reflected in the water surfaces

#### Ignore cut plane

Works as usual.

#### No shadows

Turns off the spawned model's shadows - use this for optimization

#### No mirror reflection

Prevents the model to be displayed in player truck's mirrors - use this for optimization

#### No physics

Turns off the spawned model's dynamic physics - use this for all objects the player should not be able to approach - like cars on the parking lots the player can't enter

#### Fixed seed

It is a new option that prevents the hookup item from constantly changing the spawned model for a different one

- the simplest description is that when the fixed seed flag is active the hookup item will always spawn the same object - f.e. red Skoda Octavia
- but this model will change whenever the pool of spawnable vehicles in the hookup item is expanded with new vehicle/model
- the intended use of this flag is when placing f.e. parked cars by the village houses or house driveways = places where you can expect always the same car
- while for us in the editor the selected car may change quite often but for the players this should happen only occasionally after new patches or releases

#### Hookup Item usage notes

- Hookup Item pools are controlled by their country - if you place f.e. Parked Police Car into location without country definition nothing will spawn!

- right now the Hookup item is still waiting for some additional optimization!
- overusing them at this point will severely affect the performance of your map

### Force Dynamic Model Spawn

Editor View panel now contains a new option named Force Dynamic Model Spawn. When checked (by default) the placed Hookup items always show some model from the hookup's pool. When unchecked the placed Hookup items spawn models depend on the relevant context (day/night) and the Spawn probability set in their Properties.

### Context Areas

- new types of traffic area rules and categorization
- when applicable affect not only AI traffic but also hookup items
- three types
  - [context]: definition of specific local context, place this over the designated location to apply the appropriate traffic behavior to it
    - added functionality in regards to Hookup Item is most important in case of "Company area (depot), explained later in this text
  - [context][urban]: definition of the urban areas, placed over cities, villages etc.
  - [context][zone]: definition of context to parts of the cities, placed over whole parts of the map that can represent f.e. residential zone, or over the supermarket grounds and their parking lots
- the intention of those areas and zones is to give context to the map so traffic knows how to behave and Hookup Items know what to spawn and when

![Context_areas_props.jpg](../../../../../../images/articles/Documentation/Tools/Map%20Editor/New%20Editor%20Features%20info%20-%20old%20+%201.47/300px-Context_areas_props.jpg)

*context areas*

- [context][zone] Residential area
  - placed over parts of the map containing buildings where people live
  - allows only regular car traffic in, no trucks or big buses (in future also small van)
  - roads inside this area spawn only such vehicles
  - hookup items for "parked car" spawn models more frequently at night than during the day
- [context][zone] Commercial area
  - placed over places people gather around during the day - stores, offices, city centers etc.
  - allows only regular car traffic in, no trucks of big buses (in future also small van)
  - roads inside this area spawn only such vehicles
  - hookup items for "parked car" spawn models more frequently during the day than at night

![Res_com_ex.jpg](../../../../../../images/articles/Documentation/Tools/Map%20Editor/New%20Editor%20Features%20info%20-%20old%20+%201.47/300px-Res_com_ex.jpg)

*Residential and Commercial Area example*

- [context] Company area
  - placed over
    - the area around a prefab depot you want to "expand"
    - over the spaces of generic decorative companies you want to make dynamic
  - when a "parked trailer (custom)"/"parked truck with trailer (custom)" is placed into this area it spawns a specific type of trailer depending on the traffic area tags written in the properties of the Traffic area item
    - SOON this should include brand names of ingame companies, and eventually also ability of the context area to take this information from the prefab placed into it
    - RIGHT NOW this includes the generic tags to spawn
      - no tag - spawns generic box trailer
      - fuel - spawns generic fuel tank trailer
      - food - spawns generic food tank trailer
      - chemical - spawns generic chemical tank trailer
      - container - spawns generic container trailer
      - construction - spawns generic construction material trailer

![Comp_ex.jpg](../../../../../../images/articles/Documentation/Tools/Map%20Editor/New%20Editor%20Features%20info%20-%20old%20+%201.47/300px-Comp_ex.jpg)

*Company Area example*

Another related change is regarding Custom vehicles areas.

Before Context areas, there were two traffic area rules which you could use to allow spawning driving custom vehicles:

- *Urban-specific vehicles area* (for spawning garbage trucks, street sweepers, ...)
- *Rural-specific vehicles area* (for spawning tractors, harvesters, ...)

**Now, we have the following rule instead: `[access] Custom vehicles area`**

The actual vehicle models which will spawn in the area will be automatically determined by the context, for example:

- in rural areas and villages - spawns rural-specific vehicles, like tractors
- in cities - spawns city-specific vehicles, like street sweeper or garbage truck
- in company areas - spawns vehicles specific for given company, like yard trucks in ports

### F8 map

- Option to see the ingame background map

- Option to highlight the roads depending on their AI traffic settings
  - green for AI traffic on
  - red for AI traffic off

- the Screenshot button now works properly
  - you can make a screenshot of the entire map
  - or you can do a "screenshot area selection"
    - you can create a rectangular selection area on the UI map when this option is checked
    - when you hover your mouse by the corner of the area, the cursor changes into a cross shape and you can drag those corners to expand the selection
  - it decides the screenshot detail based on the current zoom level of the UI map!
  - it no longer overwrites previous map screenshot in the folder
  - *(currently it makes pink screenshot together with the normal one - we will see in the future to make this a separate option)*
  - WARNING - depending on the size of the map and level of zoom, the screenshot process can take a very long time to finish or even crash the editor if your PC is not powerful enough

### Other fixes and changes

- With this update the `defaults.ini` file was updated and all terrains editor-default NOISE is now set to 0
- Scaling Far Model Item in properties no longer keeps unselecting the scaled model in the list
- Small tweak was made to Traffic Area Item to make it little more visible in the map - the boundary lines between the nodes had their color changed to light blue
- Far Model properties was updated to unify the layout with the Visibility Area
  - buttons to "select item" (highlighted in the list) and "select all items" have been added
- mouse hovering over a Visibility Area and Far Model Item node now highlights the items assigned to it in the map
- New debug mode added - `UI map view`
  - highlights the roads/prefabs that are displayed on the UI map

- Manual save and manual load now resets the autosave clock
- RMB on a vertex node or the control nodes of the area item opens the Properties of the parent item
- the Current Selection now displays the UIDs in right format
  - you can use this when you need to copy UID of an Item or Compound
- in Prefab Properties - `CTRL+TAB` now works to skip between same property fields of each node
- New shortcut `CTRL+A` now works as an additional option for selection expansion
  - using `CTRL+A` on Curve item node selects all nodes of the curve item
    - same for terrain, trajectory etc.
  - using `CTRL+A` on Road of Prefabs *(or QEM terrain handler)* expands the selection the same way as when using `.`

## See Also

- Editor Commands - [Documentation/Engine/Console/Commands/Editor](../../Engine/Console/Commands/Editor.md)
- Editor Shortcuts - [Documentation/Engine/Editor Shortcuts](https://modding.scssoft.com/index.php?title=Documentation/Engine/Editor_Shortcuts&action=edit&redlink=1)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/New_Editor_Features_info_-_old_%2B_1.47 | revision: 5299 | captured: 2026-10-21 23:56:14 -->
