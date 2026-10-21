# Documentation/Engine/Console/Commands/Editor

本页列出了面向地图编辑器用户的具体和/或实用命令。

|  |  |  |
| --- | --- | --- |
| **名称** | **参数** | **描述** |
| edit | [map_name] | 启动编辑器。map_name 参数为要编辑的地图名称；若未设置，编辑器将以空地图启动。 |
| edit_build | - | 在地图编辑器中重建地图并检查项目。 |
| edit_build_spawns | - | 在地图编辑器中重建所有生成点。 |
| edit_save | - | 在地图编辑器中保存地图，以便在游戏中加载。 |
| edit_save_text | - | 以文本形式保存地图，用于调试。 |
| edit_free_camera_uplift | [max_uplift] | 设置编辑器自由相机的最大抬升高度，用于“Drop free camera to ground”模式。 |
| g_delete_idx | &lt;index&gt; | 在地图编辑器中按给定索引删除项目 |
| g_delete_uid | &lt;uid&gt; | 在地图编辑器中按给定唯一索引删除项目 |
| g_dump | [asset_extension] | 转储地图。 |
| g_dump_signs | - | 转储交通标志。 |
| g_find_prefab | <prefab_name> [prefab_name] [prefab_name]... | 按单元名称后缀查找预制件，并将其转储到 bugs 文件中。 |
| g_item_count | <(model, prefab, building, anim, mover)> | 显示项目的数量。若未给出参数，此函数将输出所有项目的汇总信息。 |
| g_next_border_node | - | 查找下一个边界节点。 |
| g_replace_prefab | <old_token> <new_token> | 用新预制件替换旧预制件。token 为不带“prefab.”前缀的单元名称。 |
| g_sel_dist | (short, close, middle, far) | 选择给定距离类型的所有项目（将其加入当前选择）。 |
| g_sel_item | &lt;index&gt; | 按索引选择项目。 |
| g_sel_type | (Terrain, Buildings, Road, Prefab, Model, Company...) | 按类型选择项目。 |
| g_sel_uid | &lt;uid&gt; | 按唯一索引选择项目。 |
| g_ui_recache | - | 重新缓存 UI 绘制缓冲区。 |
| g_wander_output | [fps/vm/sb/dc [error_limit][warning_limit][far_plane][night][rain]] | 设置将显示哪些 wander 输出。night [默认 0]：-1 -> 仅显示白天数据，0 -> 不关心，1 -> 仅显示夜间数据rain [默认 0]：-1 -> 仅显示良好天气数据，0 -> 不关心，1 -> 仅显示恶劣天气数据 |
| mark_country | <country_id> | 标记属于指定国家的道路和预制件。 |
| preview | [map_name] [(game, editor)] [profile_to_load] | 以预览模式启动游戏。 |
| g_save_curve_as_text | /path/filename | 导出所选道路（或建筑等）节点的绝对坐标与方向——在调整 UI 地图轮渡路线时很有用：在两个轮渡港口之间创建道路，针对 UI 地图调整它，导出后放入 defs。示例：g_save_curve_as_text /home/soubor.sii（文本文件导出到 home 文件夹） |
| g_cut_plane_ignore | 1 | 关闭切割平面 |
| g_colbox | <1 or 0> | 显示或隐藏碰撞盒 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Console/Commands/Editor | revision: 5766 | captured: 2026-10-21 23:56:14 -->
