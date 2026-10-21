# Documentation/Engine/Console/Commands

> **TIP:** Be aware that this page is obsolete, it should be updated with all commands in the future.

Further configuration parameters are available on the [cvar](../Configuration%20variables.md) page.

## List

| Name | Parameters | Description |
| --- | --- | --- |
| check | &lt;what&gt; | Check if data is correct. At the moment the &lt;what&gt; parameter can be only "company" and then the command will validate if all connections between companies are correct. |
| cs_export | <cutscene_name> | Export cutscene by name. |
| dispatch | - | Handle entering initial state after game launch. |
| echo | &lt;message&gt; | Prints message to console. |
| edit | <map_name> | Start editor map_name parameter is name of the map to be edited, if not set editor stars with empty map. |
| edit_build | - | Rebuild editor in map editor. |
| edit_build_spawns | - | Rebuild all spawn points in map editor. |
| edit_mark | See description for parameters | Marks or unmarks sector. edit_mark [set_filtered (base\|dlc_foo\|any) (dev\|rel\|any) [hexacolor]] edit_mark [set sector_files [hexacolor]] edit_mark [set_all hexacolor] edit_mark [intersect first_file second_file [hexacolor]] edit_mark [clear_all] edit_mark [lock [sector_files]] edit_mark [unlock [sector_files]] |
| edit_save | - | Saves the map in map editor for loading in game. |
| edit_save_text | - | Save map in textual form for debugging purpose. |
| exec | <script file name> | Load and execute different command script. For example if you put this script into My Documents/Euro Truck Simulator 2: # P3D Screenshot script. echo "Taking screenshot.." screenshot echo "Screenshot has been taken" Run the game and then write in console "exec /home/script_file_name" it will execute. |
| exit | &lt;reason&gt; | Exit game command in case of error. (unloads profile) |
| g_colbox | &lt;mode&gt; | Displays collision boxes while in editor. 1:on, 0:off |
| g_delete_idx | &lt;index&gt; | Delete item by given index in map editor |
| g_delete_uid | &lt;uid&gt; | Delete item by given unique index in map editor |
| g_disable_beacons | &lt;mode&gt; | Changes behaviour of flashing beacons on AI vehicles/trucks (accessibility feature for epileptic people). 0 - default 1 - disables spot lights of strobes and beacons 2 - as 1 and also disables their flares blinking by switching them on all the time |
| g_dump | [asset extension] | Dumps map. |
| g_dump_signs | - | Dumps traffic signs. |
| g_find_prefab | <prefab name> [prefab name] [prefab name] ... | Find prefabs by its unit name suffix and dump them into bugs file. |
| g_info | - | Prints application info. Output depends if you are in game or using map editor. |
| g_item_count | (model, prefab, building, anim, mover) | Display count of the item. If no parameter is given this function prints summary about all the items. |
| g_mode | g_mode &lt;width&gt; &lt;height&gt; <refresh_rate> &lt;fullscreen&gt; | Change graphics mode. For instance, for windowed 1080p 60Hz: g_mode 1920 1080 60 0 |
| g_msaa | <sample_count> | Change [msaa](https://en.wikipedia.org/wiki/Multisample_anti-aliasing) sample count. |
| g_next_border_node | - | Finds next border node. |
| g_replace_prefab | <old_token> <new_token> | Replace old prefab with new prefab. The token is unit name without "prefab." prefix. |
| g_save_curve_as_text | <file_name> | Save curve to text file. |
| g_sel_dist | (short, close, middle, far), | Add to selection all items of given distance type. |
| g_sel_item | &lt;index&gt; | Select item by index. |
| g_sel_type | (Terrain, Buildings, Road, Prefab, Model, Company, Services, Cut plane, Mover, No weather area, City, Hinge, Parking, Animated Model, Map Overlay, Ferry, Sound, Garage, Camera point, Walker, Trigger, Services, Sign, bus_stop, Traffic area, Bezier Patch, Compound Model) | Select item by type. |
| g_sel_uid | &lt;uid&gt; | Select item by unique index. |
| g_set_skybox | <skybox_idx> | Set current skybox by index. |
| g_set_climate | <climate name> [i\|f] | Set climate. Parameter explanation: i - interpolated change, f - forced change |
| g_set_weather | <weather_index> [i\|f] | Set weather. Parameter explanation: weather_index 0 - nice 1 - bad i - interpolated change, f - forced change |
| g_set_time | &lt;hours&gt; [minutes] [remove_traffic] | Set game time. Parameters explanation: remove_traffic 0 - no 1 - yes |
| g_ui_recache | - | Recache ui draw buffers. |
| g_wander_output | [fps/vm/sb/dc [error limit][warning limit][far plane]]" | Sets which wander output will be shown. |
| game | <save_slot> | Start game. |
| goto | <x;y;z> or &lt;cityname&gt; | Teleport debug camera to place on map. Press `CTRL` + `F9` to place your truck at the camera's location. |
| mark_country | <country_id> | Marks roads and prefabs belong to specified country. |
| mm_check | - | Check integrity of resource manager system. |
| mm_defrag | - | Run memory manager defragmentation. |
| mm_dump | [?bim] (help, blocks, items, mlru) [c] (children) | Dump memory manager content. |
| mm_flush | - | Run memory manager garbage collector. |
| mm_flush_repeatedly | - | Run memory manager garbage collector. |
| [multimon](Commands/multimon.md) | &lt;operation&gt; &lt;mixed&gt; | Allows configuration of multi monitor support. |
| pause | - | Toggle game pause state |
| phys_info | - | Display informations about physical subsystem. |
| preview | <map_name> <preview_editor> <profile_to_load> | Start game in preview mode Parameters: map_name - Name of the map to preview preview_editor - editor = start editor, game = start game profile_to_load - Name of the profile to be loaded |
| quit | - | Closes the game |
| route | <start company name> <end company name> | Command runs navigation between two given points and marks examined road network for visual preview |
| s_info | - | Reports informations about sound subsystem |
| save | - | Forces game save |
| screenshot | <custom_name> | Makes a screenshot. The <custom_name> parameter sets custom name of screenshot file name. This parameter is optional. |
| sdk | &lt;operation&gt; | Perform SDK operation &lt;operation&gt; parameter can be: reinit - reinitializes the SDK unload - unload all plugins reload - reloads all plugins |
| spawn | <object_type> | Spawn traffic object Allowed object types: vehicle - standard ai vehicle vehicle_forced - forced ai vehicle (ignoring traffic origin and density) |
| test | - | Not available in final builds |
| uset | &lt;cvar&gt; &lt;value&gt; | Set value of the [cvar](../Configuration%20variables.md) by name - in case cvar was not found creates new. |
| validate | - | Start validation |
| warp | &lt;speed&gt; | Set speed of the gameplay. The correct value of the speed parameter is a floating point number in range from 0.0001 to 60.0 |
| ui | <command[[:flags] name[:class] ["parameters"]]> | Internal ui operations command. command 's'(how) - shows a window. Parameters [ui_script [left=0 bottom=0]] 'h'(ide) - hides a window 't'(oggle) - toggles window. For parameters see 's' 'i'(nsert) - inserts a window. For parameters see 's' 'r'(emove) - removes a window 'c'(ommand) - commands ui component. Parameters [component_name parameters] flags 'v'(iew) - hides a pointer atop this window 'l'(ock 0) - doesn't lock input when showing this window 'm'(odular)- makes a window modular 'f'(ocus 0)- doesn't grab focus when showing this window 'e'(vfiltr)- create as eventfilter 't'(opmost)- create as topmost 'b'(ottomm)- create as bottommost |

## Legend

**Command parameters**

- Parameters surrounded by <> are required.
- Parameters surrounded by [] are optional.
- Parameters surrounded by () are values that can be used as this parameter - other values effect depends on the command.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Console/Commands | revision: 5594 | captured: 2026-10-21 23:56:14 -->
