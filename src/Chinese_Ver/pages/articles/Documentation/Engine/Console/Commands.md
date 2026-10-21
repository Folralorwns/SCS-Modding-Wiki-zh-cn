# Documentation/Engine/Console/Commands

> **提示：** 请注意，本页面已过时，日后应使用所有命令对其进行更新。

更多配置参数可在 [cvar](../Configuration%20variables.md) 页面中找到。

## 列表

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| check | &lt;what&gt; | 检查数据是否正确。目前 &lt;what&gt; 参数只能是 “company”，此时该命令会校验公司之间的所有连接是否正确。 |
| cs_export | <cutscene_name> | 按名称导出过场动画。 |
| dispatch | - | 处理游戏启动后进入初始状态的过程。 |
| echo | &lt;message&gt; | 向控制台输出消息。 |
| edit | <map_name> | 启动编辑器。map_name 参数为要编辑的地图名称；若未设置，编辑器将以空地图启动。 |
| edit_build | - | 在地图编辑器中重建编辑器。 |
| edit_build_spawns | - | 在地图编辑器中重建所有生成点。 |
| edit_mark | 参数见描述 | 标记或取消标记区块。edit_mark [set_filtered (base\|dlc_foo\|any) (dev\|rel\|any) [hexacolor]] edit_mark [set sector_files [hexacolor]] edit_mark [set_all hexacolor] edit_mark [intersect first_file second_file [hexacolor]] edit_mark [clear_all] edit_mark [lock [sector_files]] edit_mark [unlock [sector_files]] |
| edit_save | - | 在地图编辑器中保存地图，以便在游戏中加载。 |
| edit_save_text | - | 以文本形式保存地图，用于调试。 |
| exec | <script file name> | 加载并执行其他命令脚本。例如，若将此脚本放入 My Documents/Euro Truck Simulator 2 目录：# P3D Screenshot script. echo "Taking screenshot.." screenshot echo "Screenshot has been taken" 然后运行游戏，并在控制台输入 "exec /home/script_file_name"，该脚本即会执行。 |
| exit | &lt;reason&gt; | 发生错误时退出游戏的命令。（会卸载档案） |
| g_colbox | &lt;mode&gt; | 在编辑器中显示碰撞盒。1：开，0：关 |
| g_delete_idx | &lt;index&gt; | 在地图编辑器中按给定索引删除项目 |
| g_delete_uid | &lt;uid&gt; | 在地图编辑器中按给定唯一索引删除项目 |
| g_disable_beacons | &lt;mode&gt; | 更改 AI 车辆/卡车上闪烁警示灯的行为（面向癫痫患者的无障碍功能）。0 - 默认 1 - 关闭频闪灯和警示灯的聚光灯 2 - 同 1，并让其光晕常亮以停止闪烁 |
| g_dump | [asset extension] | 转储地图。 |
| g_dump_signs | - | 转储交通标志。 |
| g_find_prefab | <prefab name> [prefab name] [prefab name] ... | 按单元名称后缀查找预制件，并将其转储到 bugs 文件中。 |
| g_info | - | 输出应用程序信息。输出内容取决于你是在游戏中还是在使用地图编辑器。 |
| g_item_count | (model, prefab, building, anim, mover) | 显示项目的数量。若未给出参数，此函数将输出所有项目的汇总信息。 |
| g_mode | g_mode &lt;width&gt; &lt;height&gt; <refresh_rate> &lt;fullscreen&gt; | 更改图形模式。例如，窗口化 1080p 60Hz：g_mode 1920 1080 60 0 |
| g_msaa | <sample_count> | 更改 [msaa](https://en.wikipedia.org/wiki/Multisample_anti-aliasing) 采样数。 |
| g_next_border_node | - | 查找下一个边界节点。 |
| g_replace_prefab | <old_token> <new_token> | 用新预制件替换旧预制件。token 为不带 “prefab.” 前缀的单元名称。 |
| g_save_curve_as_text | <file_name> | 将曲线保存到文本文件。 |
| g_sel_dist | (short, close, middle, far), | 将给定距离类型的所有项目添加到选择中。 |
| g_sel_item | &lt;index&gt; | 按索引选择项目。 |
| g_sel_type | (Terrain, Buildings, Road, Prefab, Model, Company, Services, Cut plane, Mover, No weather area, City, Hinge, Parking, Animated Model, Map Overlay, Ferry, Sound, Garage, Camera point, Walker, Trigger, Services, Sign, bus_stop, Traffic area, Bezier Patch, Compound Model) | 按类型选择项目。 |
| g_sel_uid | &lt;uid&gt; | 按唯一索引选择项目。 |
| g_set_skybox | <skybox_idx> | 按索引设置当前天空盒。 |
| g_set_climate | <climate name> [i\|f] | 设置气候。参数说明：i - 插值变化，f - 强制变化 |
| g_set_weather | <weather_index> [i\|f] | 设置天气。参数说明：weather_index 0 - 好 1 - 差 i - 插值变化，f - 强制变化 |
| g_set_time | &lt;hours&gt; [minutes] [remove_traffic] | 设置游戏时间。参数说明：remove_traffic 0 - 否 1 - 是 |
| g_ui_recache | - | 重新缓存 UI 绘制缓冲区。 |
| g_wander_output | [fps/vm/sb/dc [error limit][warning limit][far plane]]" | 设置将显示哪些 wander 输出。 |
| game | <save_slot> | 启动游戏。 |
| goto | <x;y;z> 或 &lt;cityname&gt; | 将调试摄像机传送到地图上的指定位置。按 `CTRL` + `F9` 可将卡车放置到摄像机所在位置。 |
| mark_country | <country_id> | 标记属于指定国家的道路和预制件。 |
| mm_check | - | 检查资源管理器系统的完整性。 |
| mm_defrag | - | 运行内存管理器碎片整理。 |
| mm_dump | [?bim] (help, blocks, items, mlru) [c] (children) | 转储内存管理器的内容。 |
| mm_flush | - | 运行内存管理器垃圾回收器。 |
| mm_flush_repeatedly | - | 运行内存管理器垃圾回收器。 |
| [multimon](Commands/multimon.md) | &lt;operation&gt; &lt;mixed&gt; | 允许配置多显示器支持。 |
| pause | - | 切换游戏暂停状态 |
| phys_info | - | 显示物理子系统的相关信息。 |
| preview | <map_name> <preview_editor> <profile_to_load> | 以预览模式启动游戏。参数：map_name - 要预览的地图名称 preview_editor - editor = 启动编辑器，game = 启动游戏 profile_to_load - 要加载的档案名称 |
| quit | - | 关闭游戏 |
| route | <start company name> <end company name> | 该命令在两个给定点之间运行导航，并标记所考察的路网以供可视化预览 |
| s_info | - | 报告声音子系统的信息 |
| save | - | 强制保存游戏 |
| screenshot | <custom_name> | 截取屏幕截图。<custom_name> 参数用于设置截图文件名的自定义名称。该参数为可选。 |
| sdk | &lt;operation&gt; | 执行 SDK 操作。&lt;operation&gt; 参数可以是：reinit - 重新初始化 SDK unload - 卸载所有插件 reload - 重新加载所有插件 |
| spawn | <object_type> | 生成交通对象。允许的对象类型：vehicle - 标准 AI 车辆 vehicle_forced - 强制 AI 车辆（忽略交通起点与密度） |
| test | - | 在最终版本中不可用 |
| uset | &lt;cvar&gt; &lt;value&gt; | 按名称设置 [cvar](../Configuration%20variables.md) 的值 - 若未找到该 cvar，则创建一个新的。 |
| validate | - | 开始校验 |
| warp | &lt;speed&gt; | 设置游戏速度。speed 参数的正确取值为 0.0001 到 60.0 范围内的浮点数 |
| ui | <command[[:flags] name[:class] ["parameters"]]> | 内部 UI 操作命令。command 's'(how) - 显示一个窗口。参数 [ui_script [left=0 bottom=0]] 'h'(ide) - 隐藏一个窗口 't'(oggle) - 切换窗口显示。参数参见 's' 'i'(nsert) - 插入一个窗口。参数参见 's' 'r'(emove) - 移除一个窗口 'c'(ommand) - 对 UI 组件执行命令。参数 [component_name parameters] flags 'v'(iew) - 在此窗口顶部隐藏指针 'l'(ock 0) - 显示此窗口时不锁定输入 'm'(odular)- 使窗口模块化 'f'(ocus 0)- 显示此窗口时不获取焦点 'e'(vfiltr)- 作为 eventfilter 创建 't'(opmost)- 作为最顶层创建 'b'(ottomm)- 作为最底层创建 |

## 图例

**命令参数**

- 用 <> 括起的参数为必需参数。
- 用 [] 括起的参数为可选参数。
- 用 () 括起的参数为可用作该参数的值 - 其他值的效果取决于具体命令。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Console/Commands | revision: 5594 | captured: 2026-10-21 23:56:14 -->
