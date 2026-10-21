# Documentation/Engine/Configuration variables

> **提示：** 请注意，本页面已过时，日后应使用所有注释对其进行更新。

下列变量用于配置游戏的不同方面。

其中一些（全局设置）从 ***config.cfg*** 加载，该文件可在[游戏用户文件夹](Game%20user%20path.md)中找到；其他变量（与玩家档案关联）将保存在档案文件夹中（例如 "*<game_user_path>/profiles/<profile_id>*"）。

其中大多数可在游戏过程中通过[控制台](Console.md)更改。操作方法是输入变量名，随后输入所需的值以进行更改，然后按 Enter。此外，也可以在 cvar 名称前使用命令 **uset**，但并非必需。

要查看变量的当前值和默认值，只需输入其名称。

示例：

```
g_police 0     (disables traffic fines)
g_colbox 1     (displays collision boxes)

r_mirror_view_distance  (might return the following)
"r_mirror_view_distance" is: "400" default:"80.0"
```

变量列表（*表格中的部分列可通过点击上/下箭头进行排序*）：

| 名称 | 类型 | 默认值 | 配置 | 用途 |
| --- | --- | --- | --- | --- |
| g_additional_water_fov | float | 20.0f | global | 渲染水面效果时水平 FOV 的增加量。 |
| g_adviser | integer | 1 | profile | 顾问模式：0 = 隐藏，1 = 显示，2 = 迷你模式。 |
| g_adviser_auto_parking | integer | 1 | profile | 启用/禁用自动泊车功能。 |
| g_adviser_keep_hidden | integer | 0 | profile | 让顾问保持隐藏状态（不显示任何消息）。 |
| g_artist_id | integer | 0 | global | 特定艺术家的 id。（范围 0-15） |
| g_auto_traffic_headlights | integer | 1 | global | 启用/禁用自动交通车辆的前照灯。 |
| g_autoload_ignore_autosave | integer | 0 | profile | 自动加载是否应忽略所有自动存档，仅使用手动存档？ |
| g_axle_drop_auto | integer | 1 | profile | 是否启用自动降轴？ |
| g_bad_weather_factor | float | 0.07 | profile | 恶劣天气系数。影响降雨天气出现的概率。 |
| g_brake_intensity | float | 1.0 | profile | 制动强度修正系数。 |
| g_brake_light_all | integer | 1 | profile | 为所有制动显示刹车灯（值：1），还是仅为行车制动、缓速器和挂车制动显示（值：0）？ |
| g_cam_blinker | integer | 0 | profile | 是否启用基于转向灯激活的驾驶室视角移动。 |
| g_cam_physics | integer | 1 | profile | 是否启用基于驾驶员物理运动的驾驶室视角移动？ |
| g_cam_physics_value | float | 1.0 | profile | 基于驾驶员物理运动的驾驶室视角移动量。 |
| g_cam_steering | integer | 0 | profile | 是否启用基于转向角度的驾驶室视角移动？ |
| [g_cam_steering_reverse](Configuration%20variables/g%20cam%20steering%20reverse.md) | integer | 1.0 | profile | 基于转向角度的驾驶室视角移动在倒车时的行为。 |
| g_cam_steering_value | float | 1.0 | profile | 基于转向角度的驾驶室视角移动的乘数。 |
| [g_cargo_sort](Configuration%20variables/g%20cargo%20sort.md) | integer | 0 | global | 当前货物排序方式。 |
| g_city_name_move | integer | 0 | global | 启用在地图上移动城市名称的功能。 |
| g_clock_24 | integer | 1 | profile | 使用 24 小时制还是 12 小时制（值 1 = 24 小时制，值 0 = 12 小时制） |
| g_console | integer | 0 | global | 是否启用控制台？ |
| g_convoy_allow_load | integer | 0 | global | 是否启用护航模式会话中的读取功能。在特定护航模式事件期间读取存档可能导致问题。 |
| g_cruise_control_grid | float | 5.0 | profile | 数字定速巡航的步进值。 |
| g_cruise_control_smart | float | 0.0 | profile | 智能定速巡航窗口，如需禁用它请设为负值。 |
| [g_currency](Config%20variables/g%20currency.md) | integer | 0 | profile | 游戏中使用的货币。 |
| g_cutscenes | integer | 1 | profile | 启用/禁用过场动画。 |
| g_debug_interior_cam | integer | 0 | global | 允许在驾驶室视角模式下也绘制卡车几何体。 |
| g_debug_map_limits | integer | 0 | global | 启用/禁用地图限速调试。 |
| g_desktop_fadeout | float | 60 | global | 桌面 UI 空闲时淡出前的延迟秒数。 |
| g_desktop_tutorial | integer | 1 | profile | 是否启用桌面教程？ |
| g_developer | integer | 0 | global | 是否启用开发者模式？ |
| g_disable_hud_activation | integer | 0 | global | 是否禁用特定的 HUD 激活项？ |
| g_engine_start_auto | integer | 1 | profile | 是否启用发动机自动启动？ |
| g_fahrenheit | integer | 0 | profile | 游戏温度显示使用华氏度（值：1）还是摄氏度（值：0）？ |
| g_fatigue | integer | 1 | profile | 疲劳模拟状态 |
| g_flyspeed | float | 100.0 | global | 调试相机飞行速度 |
| g_force_economy_reset | integer | 0 | profile | 值为 1 时强制重置经济系统（生成新的任务列表）。<br>玩家应在自由驾驶状态下发出该命令，之后进入并退出档案管理器。 |
| [g_force_load_selector](Config%20variables/g%20force%20load%20selector.md) | integer | 0 | profile | 强制显示读取存档槽位选择器。 |
| g_force_online_lscrs | integer | 0 | global | 强制使用在线加载画面。如果在指定类别（渡轮、欧洲隧道、普通）中未指定加载画面，则显示内置画面。 |
| g_fps | integer | 0 | global | 在迷你控制台中显示 FPS。 |
| g_fuel_simulation | integer | 0 | profile | 是否启用真实燃油消耗？ |
| g_gallon | integer | 0 | profile | 游戏容量显示使用加仑（值：1）还是升（值：0）？ |
| g_gfx_advanced | integer | 0 | global | 上次使用的图形设置（0 = 简单，1 = 高级）。 |
| g_gfx_all_scales | integer | 0 | global | 即使在虚拟内存较小的机器上，也允许在 UI 中选择所有渲染缩放比例。 |
| g_gfx_quality | integer | -1 | global | 图形质量预设。直接关联到 quality_level_t 枚举，以 "-1" 表示 "custom" 状态。 |
| g_global_force_load_selector | integer | 0 | global | 为所有档案强制显示读取存档槽位选择器。（正确值为：0、1） |
| [g_grass_density](Configuration%20variables/g%20grass%20density.md) | integer | 2 | global | 草地密度设置。 |
| g_hardcore_simulation | integer | 0 | profile | 是否启用空气制动模拟？ |
| g_hmd_no_3d_background | integer | 0 | profile | 禁用菜单的 3D 背景。 |
| g_hmd_no_artifical_movement | integer | 0 | profile | 禁用驾驶室内饰基于角度的人为移动。 |
| g_hmd_no_special_menu | integer | 0 | profile | 在启用 HMD 时禁用菜单 UI 的特殊变体。 |
| g_hmd_reduced_cabin_movement | integer | 1 | profile | 通过在视觉层面禁用驾驶室的独立移动来减少驾驶室移动。 |
| [g_hshifter_layout](Configuration%20variables/g%20hshifter%20layout.md) | integer | 0 | profile | hshifter 布局的类型。 |
| g_hshifter_layout_shifting | integer | 1 | profile | 分析布局，并将其用于更逼真的换挡音效。 |
| g_hshifter_synchronized | integer | 1 | profile | 表现/声音如同同步变速箱。 |
| [g_hud_speed_limit](Configuration%20variables/g%20hud%20speed%20limit.md) | integer | 1 | profile | 顾问上的限速状态。 |
| g_ignore_low_fps | integer | 0 | global | 启用/禁用低帧率警告。 |
| g_income_factor | float | 1.0 | profile | 收入系数（最小 0.0，最大 1.0）。会与所有收入相乘。 |
| g_input_configured | integer | 0 | profile | 是否已配置输入？ |
| g_interior_camera_zero_pitch | integer | 0 | global | 在卡车驾驶室内是否忽略默认鼠标位置？使用 Oculus Rift 之类的 HMD 时应将其设为 1。 |
| g_job_distance_limit | float | -1.0 | profile | 限制生成与玩家当前位置处于指定范围内的任务。负值表示不限制生成。 |
| g_kdop_preview | integer | 0 | global | 启用/禁用生成的 k-DOP 预览。 |
| g_lang | string | en_gb | profile | 游戏当前使用的语言。 |
| g_lang_set | integer | 1 | profile | 语言是否为手动设置（1）？ |
| g_light_distance_factor | float | 1.0 | global | 光源淡出起始距离与该值相乘。 |
| g_light_span_factor | float | 1.0 | global | 光源淡出跨度与该值相乘。 |
| g_line_sort | integer | 0 | global | 当前任务列表的排序依据。 |
| g_lod_factor_parked | float | 1.0 | global | 停放车辆的 LOD 距离与该系数相乘。 |
| g_lod_factor_pedestrian | float | 1.0 | global | 行人的 LOD 距离与该系数相乘。 |
| g_lod_factor_traffic | float | 1.0 | global | 交通车辆的 LOD 距离与该系数相乘。 |
| g_max_convoy_size | integer | 8 | global | 定义护航模式的最大规模（多人会话中的玩家数量） |
| g_menu_aa_limit | integer | 8 | global | 低于该瓦片数时，在菜单场景中启用 SSAA。 |
| g_minicon | integer | 0 | global | 是否启用迷你控制台？ |
| g_mm_help_shown | integer | 0 | global | 用于标记玩家是否首次进入模组管理器，以便显示欢迎界面。 |
| g_motor_brake_auto | integer | 0 | profile | 是否启用发动机制动的自动使用？ |
| g_mph | integer | 0 | profile | 使用英里（1）还是公里（0）。 |
| [g_news](Configuration%20variables/g%20news.md) | integer | -1 | global | 是否启用在线新闻？ |
| [g_online_loading_screens](Configuration%20variables/g%20online%20loading%20screens.md) | integer | -1 | global | 是否启用在线加载画面？ |
| [g_parking_difficulty](Config%20variables/g%20parking%20difficulty.md) | integer | 0 | profile | 泊车难度 |
| g_pedal_clutch_range | float | 1.0 | profile | 离合器行程范围。 |
| g_pedestrian | integer | 1 | global | 启用/禁用行人生成。 |
| g_police | integer | 1 | profile | 是否启用警察模拟？设为 0 则不会受到任何处罚。 |
| [g_pounds](Config%20variables/g%20pounds.md) | string | kg | profile | 设置重量单位 |
| g_radio_mode | integer | 1 | global | 收音机播放器模式。 |
| g_rain_reflect_actor | integer | 1 | global | 是否在雨水中反射游戏中的 actor？ |
| g_rain_reflect_cache | integer | 1 | global | 是否在雨水中反射几何缓存？ |
| g_rain_reflect_hookups | integer | 1 | global | 是否在雨水中反射与路段项目关联的挂接对象（例如路灯的光晕）？ |
| g_rain_reflect_traffic | integer | 1 | global | 是否在雨水中反射交通车辆？ |
| [g_rain_reflection](Configuration%20variables/g%20rain%20reflection.md) | integer | 3 | global | 雨水反射质量。 |
| [g_reflection](Configuration%20variables/g%20reflection.md) | integer | 3 | global | 反射细节。 |
| g_reg_setting | string | 无默认值 | profile | 区域设置单元的名称。ETS2 默认为 reg_setting.europe，ATS 默认为 reg_setting.usa。 |
| g_remove_missing_accessories | integer | 0 | profile | 移除游戏中已不再可用的所有配件，并在可能时用后备配件替换。 |
| g_retarder_auto | integer | 0 | profile | 是否启用缓速器的自动使用？ |
| [g_save_format](Configuration%20variables/g%20save%20format.md) | integer | 0 | global | 用于存储游戏存档的格式。 |
| g_save_idx | integer | 1 | profile | 当前档案的存档索引。用于自动命名存档。 |
| g_screenshot_on_bug | integer | 0 | global | 启用/禁用报告 bug 时自动生成截图，即使使用的是常规组合键。 |
| g_show_game_elements | integer | 1 | global | 是否启用激活点？ |
| g_start_in_truck | integer | 0 | profile | 若档案已分配卡车，是否跳过桌面并直接在该卡车中开始？ |
| g_steam_browser | integer | 1 | global | 游戏打开外部链接时使用 Steam 内置浏览器还是用户默认浏览器？ |
| g_steam_rich_presence | integer | 1 | global | 是否启用 Steam Rich Presence？ |
| [g_steam_screenshots](Configuration%20variables/g%20steam%20screenshots.md) | integer | 2 | global | Steam 版本中处理截图的方式。 |
| g_steer_autocenter | integer | 1 | profile | 是否启用方向盘自动回正？ |
| g_texture_usage_stats | integer | 0 | global | 是否将纹理使用统计输出到控制台？ |
| g_throttle_auto_shift | integer | 0 | profile | 自动变速箱将油门作为换挡策略的输入。 |
| g_tooltip_delay | float | 0.4 | global | 以秒为单位的延迟，表示悬停在带提示的项上后多久显示工具提示。 |
| g_toy_physics | integer | 1 | profile | 是否启用玩具物理运动模拟？ |
| g_trackir | integer | 1 | global | 启用/禁用 TrackIR 支持。 |
| g_traffic | float | 1.0 | global | 交通强度。0.0 - 禁用交通，10.0 - 最大交通强度 |
| g_trailer_stability | float | 0.5 | profile | 挂车稳定性系数。 |
| [g_trans](Configuration%20variables/g%20trans.md) | integer | 0 | profile | 变速箱类型。 |
| [g_truck_light_quality](Configuration%20variables/g%20truck%20light%20quality.md) | integer | 1 | global | 前照灯计算结果的质量。 |
| g_truck_light_specular | integer | 1 | global | 启用/禁用前照灯计算期间的高光。 |
| g_tutorial | integer | 1 | profile | 是否启用教程？ |
| g_use_speed_limiter | integer | 1 | profile | 是否启用限速器？ |
| g_veg_detail | integer | 2 | global | 植被细节设置。0 - 低，1 - 中，2 - 高 |
| g_vehicle_flare_lights | integer | 1 | global | 启用/禁用与车辆光晕关联的灯光。 |
| i_virtual_cursor_speed | float | 500.0 | global | 使用类手柄输入时光标的移动速度，单位为像素/秒。<br>设为 0 或负值可禁用手柄和操纵杆控制光标移动。 |
| p_profile_draws | integer | 0 | global | 对绘制调用进行性能分析 |
| r_anisotropy_factor | float | 0.25 | global | 各向异性系数。 |
| r_cloud_shadows | integer | 1 | global | 是否启用云阴影？ |
| [r_color_correction](Configuration%20variables/r%20color%20correction.md) | integer | 1 | global | 颜色校正状态。 |
| r_color_cyan_red | float | 0.0 | global | 颜色校正的青-红系数，范围为 -1 到 1。 |
| r_color_magenta_green | float | 0.0 | global | 颜色校正的品红-绿系数，范围为 -1 到 1。 |
| r_color_saturation | float | 1.0 | global | 颜色饱和度系数，1.0 为中性。 |
| r_color_yellow_blue | float | 0.0 | global | 颜色校正的黄-蓝系数，范围为 -1 到 1。 |
| r_deferred | integer | 1 | global | 是否启用延迟渲染？设为 0 时游戏使用前向渲染管线，会禁用阴影、灯光和所有后处理效果。 |
| [r_deferred_debug](Config%20variables/r%20deferred%20debug.md) | integer | 0 | global | 若值大于 0，则运行延迟渲染器调试。 |
| r_deferred_mirrors | integer | 1 | global | 渲染后视镜时是否使用延迟渲染管线？ |
| r_device | string | dx9 | global | 渲染设备（正确值：dx9、dx11、gl）。 |
| r_dof | integer | 1 | global | 是否启用景深效果？ |
| r_dof_filter_size | float | 0.5 | global | 景深滤镜的大小。 |
| r_dof_start | float | 200.0 | global | 景深的起始范围 |
| r_dof_transition | float | 400.0 | global | 最小与最大景深模糊之间范围的长度。 |
| [r_fake_shadows](Configuration%20variables/r%20fake%20shadows.md) | integer | 2 | global | 假阴影状态。 |
| r_fullscreen | integer | 1 | global | 是否启用全屏？ |
| r_gamma | float | 1.0 | global | 伽马校正系数（仅在全屏模式下有效） |
| r_hdr | integer | 1 | global | 是否启用 HDR？ |
| r_manual_stereo_buffer_scale | float | 1.0 | global | 创建立体缓冲时使用的缩放系数。 |
| r_manual_stereo_in_menu | integer | 1 | global | 是否在菜单中也启用手动立体渲染？ |
| r_manual_stereo_ui_dist | float | 0.8 | global | 使用立体渲染时 UI 绘制平面的距离。 |
| r_manual_stereo_ui_dist_game | float | 0.5 | global | 使用立体渲染时 UI 绘制平面的距离。 |
| r_manual_stereo_ui_fov | float | 80 | global | 使用立体渲染时手动立体 UI 的视野。 |
| r_manual_stereo_ui_fov_game | float | 100 | global | 使用立体渲染时手动立体 UI 的视野。 |
| r_minimal_unfinished_frames | integer | 0 | global | 在跟踪完成帧时模拟更大的队列。 |
| r_mirror_scale_x | float | 1.0 | global | X 轴后视镜渲染缩放系数。 |
| r_mirror_scale_y | float | 1.0 | global | Y 轴后视镜渲染缩放系数。 |
| r_mirror_view_distance | float | 80.0 | global | 后视镜的可视距离。 |
| r_mlaa | integer | 1 | global | 是否启用 MLAA？ |
| r_mlaa_threshold | float | 1.0 | global | MLAA 抗锯齿使用的边缘阈值 |
| r_mode | string | 无默认值 | global | 当前分辨率，格式为：{screen_width}x{screen_height}x{color_depth}x{refresh_rate} |
| r_multimon_border_fov_left | float | 0 | global | 为相机之间的偏移量额外增加的角度，用于表示被显示器边框遮挡的区域。 |
| r_multimon_border_fov_right | float | 0 | global | 为相机之间的偏移量额外增加的角度，用于表示被显示器边框遮挡的区域。 |
| r_multimon_exterior_in_aux | integer | 0 | global | 是否在辅助视图中渲染外观？ |
| r_multimon_fov_horizontal | float | 50 | global | 多显示器配置下使用的水平视野。 |
| r_multimon_fov_vertical | float | 0 | global | 多显示器配置下使用的垂直视野。 |
| r_multimon_interior_in_main | integer | 1 | global | 是否在主视图中渲染内饰。 |
| [r_multimon_mode](Config%20variables/r%20multimon%20mode.md) | integer | 0 | global | 控制多显示器模式。 |
| r_multimon_rotation_aux | float | 0 | global | 辅助显示器的旋转角。 |
| r_multimon_rotation_center | float | 0 | global | 中间显示器的旋转角。 |
| r_multimon_rotation_left | float | 0 | global | 左侧显示器的旋转角。 |
| r_multimon_rotation_right | float | 0 | global | 右侧显示器的旋转角。 |
| r_multimon_vert_offset_left | float | 0 | global | 左侧显示器的额外垂直偏移。 |
| r_multimon_vert_offset_right | float | 0 | global | 右侧显示器的额外垂直偏移。 |
| r_no_frame_tracking | integer | 0 | global | 禁用帧跟踪功能。 |
| r_normal_maps | integer | 1 | global | 是否启用法线贴图？ |
| r_nowmi | integer | 0 | global | 在检测显卡内存信息时禁用 WMI。 |
| [r_nv_stereo_mode](Configuration%20variables/r%20nv%20stereo%20mode.md) | integer | 2 | global | 如何处理 NV 3D Vision 立体模式。 |
| r_path | string | 无默认值 | global | 渲染路径。 |
| r_scale_x | float | 1.0 | global | X 轴渲染缩放系数。 |
| r_scale_y | float | 1.0 | global | Y 轴渲染缩放系数。 |
| r_segment_buffer_size | integer | 128 | global | 路段缓冲区大小，单位为 MB |
| r_setup_done | integer | 0 | global | 是否已完成默认图形设置？ |
| r_show_light_pixel_coverage | integer | 0 | global | 是否显示灯光调试辅助工具？ |
| r_startup_progress | integer | 0 | global | 表示游戏启动进度。 |
| r_sun_shadow_quality | integer | 4 | global | 太阳阴影质量。 |
| r_sun_shadow_texture_size | integer | 4096 | global | 太阳阴影纹理的大小。数值越大 = 画面越好，fps 越低 |
| r_sunshafts | integer | 1 | global | 是否启用阳光光束？ |
| r_texture_detail | integer | 0 | global | 纹理细节。要跳过的最大 mipmap 层级数。 |
| r_use_depth_bounds | integer | 1 | global | 游戏是否使用深度边界来加速灯光渲染？（仅在支持的硬件上有效） |
| r_vsync | integer | 1 | global | 是否启用垂直同步？ |
| r_wireframe | integer | 0 | global | 启用线框渲染。 |
| s_air_noise | float | 1.0 | profile | 高速行驶时的空气声。 |
| s_interior_volume | float | 1.0 | profile | 驾驶室内声音音量乘数。 |
| s_master_volume | float | 1.0 | profile | 主音量。 |
| s_music_enabled | integer | 1 | profile | 是否启用音乐？ |
| s_music_volume | float | 0.8 | profile | 音乐音量。 |
| s_radio_volume | float | 1.0 | profile | 收音机音量。 |
| s_reverse_enabled | integer | 1 | profile | 是否启用倒车音效？ |
| s_reverse_stereo | int | 0 | profile | 是否反转立体声？ |
| s_rumble_enabled | integer | 1 | profile | 是否启用隆隆声音效？ |
| s_sfx_enabled | integer | 1 | profile | 是否启用 SFX？ |
| s_sfx_volume | float | 1.0 | profile | SFX 音量。 |
| s_wheel_noise | float | 1.0 | profile | 高速行驶时的车轮声。 |
| sys_info | string | 无默认值 | global | 存储操作系统相关信息 |
| t_averaging_window_duration | integer | 100 | global | 用于计算当前帧时长的过去帧最大合计时长，以毫秒为单位。 |
| t_averaging_window_length | integer | 10 | global | 用于计算当前帧时长的过去帧最大数量。 |
| vid_mem | string | 无默认值 | global | 存储当前所用显卡的显存信息。 |
| vid_name | string | 无默认值 | global | 存储当前所用显卡的信息。 |
| vid_ver | string | 无默认值 | global | 存储当前所用显卡驱动版本的信息。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Configuration_variables | revision: 5727 | captured: 2026-10-21 23:56:14 -->
