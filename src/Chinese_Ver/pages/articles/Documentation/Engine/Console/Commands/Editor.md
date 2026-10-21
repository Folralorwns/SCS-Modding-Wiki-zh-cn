# Documentation/Engine/Console/Commands/Editor

The page lists specific and/or useful commands for map editor users.

|  |  |  |
| --- | --- | --- |
| **Name** | **Parameters** | **Description** |
| edit | [map_name] | Start editor. The map_name parameter is name of the map to be edited, if not set editor stars with empty map. |
| edit_build | - | Rebuild map and check items in map editor. |
| edit_build_spawns | - | Rebuild all spawn points in map editor. |
| edit_save | - | Saves the map in map editor for loading in game. |
| edit_save_text | - | Save map in textual form for debugging purpose. |
| edit_free_camera_uplift | [max_uplift] | Set editor free camera's max uplift used when the camera is in "Drop free camera to ground" mode. |
| g_delete_idx | &lt;index&gt; | Delete item by given index in map editor |
| g_delete_uid | &lt;uid&gt; | Delete item by given unique index in map editor |
| g_dump | [asset_extension] | Dumps map. |
| g_dump_signs | - | Dumps traffic signs. |
| g_find_prefab | <prefab_name> [prefab_name] [prefab_name]... | Find prefabs by its unit name suffix and dump them into bugs file. |
| g_item_count | <(model, prefab, building, anim, mover)> | Display count of the item. If no parameter is given this function prints summary about all the items. |
| g_next_border_node | - | Finds next border node. |
| g_replace_prefab | <old_token> <new_token> | Replace old prefab with new prefab. The token is unit name without "prefab." prefix. |
| g_sel_dist | (short, close, middle, far) | Selects all items of given distance type (add them to current selection). |
| g_sel_item | &lt;index&gt; | Select item by index. |
| g_sel_type | (Terrain, Buildings, Road, Prefab, Model, Company...) | Select item by type. |
| g_sel_uid | &lt;uid&gt; | Select item by unique index. |
| g_ui_recache | - | Recache ui draw buffers. |
| g_wander_output | [fps/vm/sb/dc [error_limit][warning_limit][far_plane][night][rain]] | Sets which wander output will be shown.night [default 0]: -1 -> show only day data, 0 -> don't care, 1 -> show only night datarain [default 0]: -1 -> show only good weather data, 0 -> don't care, 1 -> show only bad weather data |
| mark_country | <country_id> | Marks roads and prefabs belong to specified country. |
| preview | [map_name] [(game, editor)] [profile_to_load] | Start game in preview mode. |
| g_save_curve_as_text | /path/filename | exports selected road (or building...) nodes absolute coordinates and directionsit is useful while tweaking ui map ferry route - create road between two ferry ports, tweak it for ui map, export, put to defsexample: g_save_curve_as_text /home/soubor.sii (text file exported to home folder) |
| g_cut_plane_ignore | 1 | Switching off cutplanes |
| g_colbox | <1 or 0> | Show or hide collision boxes |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Console/Commands/Editor | revision: 5766 | captured: 2026-10-21 23:56:14 -->
