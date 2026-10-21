# Documentation/Engine/Configuration variables

> **TIP:** Be aware that this page is obsolete, it should be updated with all comments in the future time.

The following variables configure different aspects of the game.

Some of them (global settings) are loaded from the ***config.cfg*** that can be found in the [game user folder](Game%20user%20path.md); others (which are associated with a player's profile) will be saved in the profile folder (e.g. "*<game_user_path>/profiles/<profile_id>*").

Most of these can be changed during the game play using the [console](Console.md). To do so, enter the variable name, followed by the desired value, to change it, and press Enter. Additionally the command **uset** can be used before the cvar name, but it is not necessary.

To determine the current and default value of a variable, enter only its name.

Example:

```
g_police 0     (disables traffic fines)
g_colbox 1     (displays collision boxes)

r_mirror_view_distance  (might return the following)
"r_mirror_view_distance" is: "400" default:"80.0"
```

Variables list (*some of the columns in the table can be sorted by clicking the up/down arrows*):

| Name | Type | Default value | Config | Purpose |
| --- | --- | --- | --- | --- |
| g_additional_water_fov | float | 20.0f | global | By how much increase the horizontal fov used to render the water effect. |
| g_adviser | integer | 1 | profile | Adviser mode: 0 = hidden, 1 = shown, 2 = mini mode. |
| g_adviser_auto_parking | integer | 1 | profile | Enable/disable auto parking feature. |
| g_adviser_keep_hidden | integer | 0 | profile | Keep adviser in hidden state (do not show any message). |
| g_artist_id | integer | 0 | global | Artist specific id. (0-15 range) |
| g_auto_traffic_headlights | integer | 1 | global | Enable/Disable headlights from automatic traffic. |
| g_autoload_ignore_autosave | integer | 0 | profile | Should auto-loading ignore all autosaves and use only manual saves? |
| g_axle_drop_auto | integer | 1 | profile | Is automatic axle drop enabled? |
| g_bad_weather_factor | float | 0.07 | profile | Bad weather factor. Affects probability of rainy weather. |
| g_brake_intensity | float | 1.0 | profile | Brake intensity modifier. |
| g_brake_light_all | integer | 1 | profile | Show brake light for all brakes (value: 1) or only service, retarder and trailer brake (value: 0)? |
| g_cam_blinker | integer | 0 | profile | Is interior camera movement based on blinker activation enabled. |
| g_cam_physics | integer | 1 | profile | Is interior camera movement based on physics movement of driver enabled? |
| g_cam_physics_value | float | 1.0 | profile | Value of interior camera movement based on physics movement of driver. |
| g_cam_steering | integer | 0 | profile | Is interior camera movement based on steering angle enabled? |
| [g_cam_steering_reverse](Configuration%20variables/g%20cam%20steering%20reverse.md) | integer | 1.0 | profile | Interior camera movement based on steering angle, behavior on reverse. |
| g_cam_steering_value | float | 1.0 | profile | Multiplier for interior camera movement based on steering angle. |
| [g_cargo_sort](Configuration%20variables/g%20cargo%20sort.md) | integer | 0 | global | Current cargo sort method. |
| g_city_name_move | integer | 0 | global | Enable ability to move city names on map. |
| g_clock_24 | integer | 1 | profile | Use 24 hour clock or 12 hour clock (value 1 = 24 hour, value 0 = 12 hour) |
| g_console | integer | 0 | global | Is console enabled? |
| g_convoy_allow_load | integer | 0 | global | Is load functionally during convoy session enabled. Loading during specific convoy events might cause issues. |
| g_cruise_control_grid | float | 5.0 | profile | Digital cruise control grid step. |
| g_cruise_control_smart | float | 0.0 | profile | Smart cruise control window, if you want to disable it set to negative value. |
| [g_currency](Config%20variables/g%20currency.md) | integer | 0 | profile | Currency used in game. |
| g_cutscenes | integer | 1 | profile | Enable/disable cutscenes. |
| g_debug_interior_cam | integer | 0 | global | Enables drawing of the truck geometry even in the interior camera mode. |
| g_debug_map_limits | integer | 0 | global | Enable/Disable the debugging of the map speed limits. |
| g_desktop_fadeout | float | 60 | global | Delay in seconds before the desktop ui will fade out when left idle. |
| g_desktop_tutorial | integer | 1 | profile | Is desktop tutorial enabled? |
| g_developer | integer | 0 | global | Is developer mode enabled? |
| g_disable_hud_activation | integer | 0 | global | Are specific hud activations disabled? |
| g_engine_start_auto | integer | 1 | profile | Is engine automatic start enabled? |
| g_fahrenheit | integer | 0 | profile | Should game display temperature in fahrenheits (value: 1) or degrees of celsius (value: 0)? |
| g_fatigue | integer | 1 | profile | State of the fatigue simulation |
| g_flyspeed | float | 100.0 | global | Debug camera fly speed |
| g_force_economy_reset | integer | 0 | profile | A value of 1 forces an economy reset (generating new job listings).<br>The player should be free-roaming when issuing the command, and afterwards entering and exiting the Profile Manager. |
| [g_force_load_selector](Config%20variables/g%20force%20load%20selector.md) | integer | 0 | profile | Forces the appearance of the load slot selector. |
| g_force_online_lscrs | integer | 0 | global | Force online loading screens. If no loading screen is specified in specified category (ferry, eurotunnel, normal) built-in one is showed. |
| g_fps | integer | 0 | global | Display FPS in mini console. |
| g_fuel_simulation | integer | 0 | profile | Is realistic fuel consumption enabled? |
| g_gallon | integer | 0 | profile | Should game display volume as gallon (value: 1) or liters (value: 0)? |
| g_gfx_advanced | integer | 0 | global | Graphics settings last used (0 = simple, 1 = advanced). |
| g_gfx_all_scales | integer | 0 | global | Enables selection of all rendering scales in ui even on machines with small virtual memory. |
| g_gfx_quality | integer | -1 | global | Quality presets of graphics. Linked directly to quality_level_t enum, with "-1" as "custom" state. |
| g_global_force_load_selector | integer | 0 | global | Forces the appearance of the load slot selector for all profiles. (Correct value are: 0, 1) |
| [g_grass_density](Configuration%20variables/g%20grass%20density.md) | integer | 2 | global | Grass density setting. |
| g_hardcore_simulation | integer | 0 | profile | Is air brake simulation enabled? |
| g_hmd_no_3d_background | integer | 0 | profile | Disables use of 3d background for the menu. |
| g_hmd_no_artifical_movement | integer | 0 | profile | Disables artifical angle based movement of the interior. |
| g_hmd_no_special_menu | integer | 0 | profile | Disables use of special variants of menu ui when HMD is enabled. |
| g_hmd_reduced_cabin_movement | integer | 1 | profile | Reduces the cabin movement by disabling its separate movement on the visual level. |
| [g_hshifter_layout](Configuration%20variables/g%20hshifter%20layout.md) | integer | 0 | profile | Type of hshifter layout. |
| g_hshifter_layout_shifting | integer | 1 | profile | Layout analyzed and used for more realistic shifting sounds. |
| g_hshifter_synchronized | integer | 1 | profile | Behaves/sounds like synchronized transmission. |
| [g_hud_speed_limit](Configuration%20variables/g%20hud%20speed%20limit.md) | integer | 1 | profile | Speed limit state on the adviser. |
| g_ignore_low_fps | integer | 0 | global | Enable/Disable the low frame rate warnings. |
| g_income_factor | float | 1.0 | profile | Income factor (minimum is 0.0 maximum is 1.0). Multiplies all incomes. |
| g_input_configured | integer | 0 | profile | Is input configured? |
| g_interior_camera_zero_pitch | integer | 0 | global | Is default mouse position ignored in truck interior? This should be set to 1 when you are using some HMD such like Oculus Rift. |
| g_job_distance_limit | float | -1.0 | profile | Limit generating of the jobs that are in specified range from current player position. Negative value means no limit for generation applied. |
| g_kdop_preview | integer | 0 | global | Enable/Disable the preview of generated k-DOPs. |
| g_lang | string | en_gb | profile | Language currently used by game. |
| g_lang_set | integer | 1 | profile | Is language set manually (1)? |
| g_light_distance_factor | float | 1.0 | global | Light source fade start distance is multiplied by this value. |
| g_light_span_factor | float | 1.0 | global | Light source fade span is multiplied by this value. |
| g_line_sort | integer | 0 | global | Current line sort criteria for jobs. |
| g_lod_factor_parked | float | 1.0 | global | LOD distances for parked vehicles are multiplied by this factor. |
| g_lod_factor_pedestrian | float | 1.0 | global | LOD distances for pedestrians are multiplied by this factor. |
| g_lod_factor_traffic | float | 1.0 | global | LOD distances for traffic vehicles are multiplied by this factor. |
| g_max_convoy_size | integer | 8 | global | Defines the maximum size of convoy (players in multiplayer session) |
| g_menu_aa_limit | integer | 8 | global | Number of tiles below which we enable SSAA in the menu scene. |
| g_minicon | integer | 0 | global | Is mini console enabled? |
| g_mm_help_shown | integer | 0 | global | Used for indication if its first time when player enters mod manager to show him welcome screen. |
| g_motor_brake_auto | integer | 0 | profile | Is automatic usage of engine brake enabled? |
| g_mph | integer | 0 | profile | Use miles (1) or kilometers (0). |
| [g_news](Configuration%20variables/g%20news.md) | integer | -1 | global | Is online news enabled? |
| [g_online_loading_screens](Configuration%20variables/g%20online%20loading%20screens.md) | integer | -1 | global | Are online loading screens enabled? |
| [g_parking_difficulty](Config%20variables/g%20parking%20difficulty.md) | integer | 0 | profile | Parking difficulty |
| g_pedal_clutch_range | float | 1.0 | profile | Cluch range. |
| g_pedestrian | integer | 1 | global | Enable/Disable pedestrian generation. |
| g_police | integer | 1 | profile | Is police simulation enabled? If set to 0 you will not get any penalties. |
| [g_pounds](Config%20variables/g%20pounds.md) | string | kg | profile | Set weight unit |
| g_radio_mode | integer | 1 | global | Radio player mode. |
| g_rain_reflect_actor | integer | 1 | global | Should we reflect game actor in the rain? |
| g_rain_reflect_cache | integer | 1 | global | Should we reflect geometry cache in the rain? |
| g_rain_reflect_hookups | integer | 1 | global | Should we reflect hookups associated with segment items (e.g. lamp flares)? |
| g_rain_reflect_traffic | integer | 1 | global | Should we reflect traffic in the rain? |
| [g_rain_reflection](Configuration%20variables/g%20rain%20reflection.md) | integer | 3 | global | Rain reflection quality. |
| [g_reflection](Configuration%20variables/g%20reflection.md) | integer | 3 | global | Reflection detail. |
| g_reg_setting | string | No default value | profile | Name of the regional settings unit. By default for ETS2 it's reg_setting.europe for ATS it's reg_setting.usa. |
| g_remove_missing_accessories | integer | 0 | profile | Remove all acccessories that are no longer available in game and replace them with fallback accessories if possible. |
| g_retarder_auto | integer | 0 | profile | Is automatic usage of retarder enabled? |
| [g_save_format](Configuration%20variables/g%20save%20format.md) | integer | 0 | global | Format used to store the game saves. |
| g_save_idx | integer | 1 | profile | Current profile save index. Used for automatic naming of saves. |
| g_screenshot_on_bug | integer | 0 | global | Enable/Disable automatic generation of screenshots when bug is reported even if the normal combination is used. |
| g_show_game_elements | integer | 1 | global | Are activation points enabled? |
| g_start_in_truck | integer | 0 | profile | If profile has assigned truck should we skip desktop and start in it? |
| g_steam_browser | integer | 1 | global | Should game use steam build-in browser or user default browser to open external links? |
| g_steam_rich_presence | integer | 1 | global | Is steam rich presence enabled? |
| [g_steam_screenshots](Configuration%20variables/g%20steam%20screenshots.md) | integer | 2 | global | Way in which we should handle the screenshots in steam version. |
| g_steer_autocenter | integer | 1 | profile | Is steering wheel autocenter enabled? |
| g_texture_usage_stats | integer | 0 | global | Print texture usage statistics into the console? |
| g_throttle_auto_shift | integer | 0 | profile | Automatic gearbox uses throttle as input for shifting policy. |
| g_tooltip_delay | float | 0.4 | global | Delay specified in seconds indicating when to show tooltip since hovering the item with tooltip. |
| g_toy_physics | integer | 1 | profile | Is simulation of toy physics movement enabled? |
| g_trackir | integer | 1 | global | Enable/Disable the TrackIR support. |
| g_traffic | float | 1.0 | global | Traffic intensity. 0.0 - traffic disabled 10.0 - maximum traffic intensity |
| g_trailer_stability | float | 0.5 | profile | Trailer stability factor. |
| [g_trans](Configuration%20variables/g%20trans.md) | integer | 0 | profile | Type of transmission. |
| [g_truck_light_quality](Configuration%20variables/g%20truck%20light%20quality.md) | integer | 1 | global | Quality of result of the head light. |
| g_truck_light_specular | integer | 1 | global | Enables/disables use of specular during head light calculation. |
| g_tutorial | integer | 1 | profile | Is tutorial enabled? |
| g_use_speed_limiter | integer | 1 | profile | Is speed limiter enabled? |
| g_veg_detail | integer | 2 | global | Vegetation detail setting. 0 - low, 1 - medium, 2 - high |
| g_vehicle_flare_lights | integer | 1 | global | Enable/Disable lights associated with vehicle flares. |
| i_virtual_cursor_speed | float | 500.0 | global | Speed of movement of the cursor when using a gamepad-like input in pixels per second.<br>Set to zero or negative value to disable use of gamepads and joysticks for cursor movement. |
| p_profile_draws | integer | 0 | global | Profile draw calls |
| r_anisotropy_factor | float | 0.25 | global | Anistropy factor. |
| r_cloud_shadows | integer | 1 | global | Are cloud shadows enabled? |
| [r_color_correction](Configuration%20variables/r%20color%20correction.md) | integer | 1 | global | Color correction state. |
| r_color_cyan_red | float | 0.0 | global | Cyan-red factor of the color correction in -1 to 1 range. |
| r_color_magenta_green | float | 0.0 | global | Magenta-green factor of the color correction in -1 to 1 range. |
| r_color_saturation | float | 1.0 | global | Color saturation factor 1.0 is neutral. |
| r_color_yellow_blue | float | 0.0 | global | Yellow-blue factor of the color correction in -1 to 1 range. |
| r_deferred | integer | 1 | global | Is deferred rendering enabled? If set to 0 game uses forward rendering pipeline which disables shadows, lights and all post process effects. |
| [r_deferred_debug](Config%20variables/r%20deferred%20debug.md) | integer | 0 | global | If value is greater than 0 runs deferred renderer debug. |
| r_deferred_mirrors | integer | 1 | global | Use deferred rendering pipeline while rendering mirrors? |
| r_device | string | dx9 | global | Render device (correct values: dx9, dx11, gl). |
| r_dof | integer | 1 | global | Is Depth Of Field effect enabled? |
| r_dof_filter_size | float | 0.5 | global | Size of the Depth Of Field filter. |
| r_dof_start | float | 200.0 | global | Starting range of the Depth Of Field |
| r_dof_transition | float | 400.0 | global | Length of range between minimal and maximal Depth Of Field blur. |
| [r_fake_shadows](Configuration%20variables/r%20fake%20shadows.md) | integer | 2 | global | Fake shadows state. |
| r_fullscreen | integer | 1 | global | Is fullscreen enabled? |
| r_gamma | float | 1.0 | global | Gamma correction factor (works only in fullscreen mode) |
| r_hdr | integer | 1 | global | Is HDR enabled? |
| r_manual_stereo_buffer_scale | float | 1.0 | global | Scale factor used when creating stereo buffers. |
| r_manual_stereo_in_menu | integer | 1 | global | Is use of manual stereo enabled even in menu? |
| r_manual_stereo_ui_dist | float | 0.8 | global | UI draw plane distance when using stereo. |
| r_manual_stereo_ui_dist_game | float | 0.5 | global | UI draw plane distance when using stereo. |
| r_manual_stereo_ui_fov | float | 80 | global | Manual stereo UI field of view when using stereo. |
| r_manual_stereo_ui_fov_game | float | 100 | global | Manual stereo UI field of view when using stereo. |
| r_minimal_unfinished_frames | integer | 0 | global | Simulate bigger queue in tracking completion frames. |
| r_mirror_scale_x | float | 1.0 | global | X-axis mirror rendering scaling factor. |
| r_mirror_scale_y | float | 1.0 | global | Y-axis mirror rendering scaling factor. |
| r_mirror_view_distance | float | 80.0 | global | View distance of the mirrors. |
| r_mlaa | integer | 1 | global | Is MLAA enabled? |
| r_mlaa_threshold | float | 1.0 | global | Edge threshold used for MLAA anti-aliasing |
| r_mode | string | No default value | global | Current resolution in format: {screen_width}x{screen_height}x{color_depth}x{refresh_rate} |
| r_multimon_border_fov_left | float | 0 | global | Additional angle added to offset between cameras to represent oblast hidden by the monitor border. |
| r_multimon_border_fov_right | float | 0 | global | Additional angle added to offset between cameras to represent oblast hidden by the monitor border. |
| r_multimon_exterior_in_aux | integer | 0 | global | Should we render exterior in the auxiliary view? |
| r_multimon_fov_horizontal | float | 50 | global | Horizontal field of view used with multi monitor configuration. |
| r_multimon_fov_vertical | float | 0 | global | Vertical field of view used with multi monitor configuration. |
| r_multimon_interior_in_main | integer | 1 | global | Should we render interior inside the main views. |
| [r_multimon_mode](Config%20variables/r%20multimon%20mode.md) | integer | 0 | global | Controls the multi-monitor mode. |
| r_multimon_rotation_aux | float | 0 | global | Roll of the auxillary monitor. |
| r_multimon_rotation_center | float | 0 | global | Roll of the center monitor. |
| r_multimon_rotation_left | float | 0 | global | Roll of the left monitor. |
| r_multimon_rotation_right | float | 0 | global | Roll of the right monitor. |
| r_multimon_vert_offset_left | float | 0 | global | Additional vertical offset of left monitor. |
| r_multimon_vert_offset_right | float | 0 | global | Additional vertical offset of right monitor. |
| r_no_frame_tracking | integer | 0 | global | Disable frame tracking feature. |
| r_normal_maps | integer | 1 | global | Is normal mapping enabled? |
| r_nowmi | integer | 0 | global | Disable usage of WMI while detecting graphics card memory informations. |
| [r_nv_stereo_mode](Configuration%20variables/r%20nv%20stereo%20mode.md) | integer | 2 | global | How to handle NV 3D vision stereo mode. |
| r_path | string | No default value | global | Render path. |
| r_scale_x | float | 1.0 | global | X-axis rendering scaling factor. |
| r_scale_y | float | 1.0 | global | Y-axis rendering scaling factor. |
| r_segment_buffer_size | integer | 128 | global | Segment buffer size in MB |
| r_setup_done | integer | 0 | global | Are default graphics settings setup? |
| r_show_light_pixel_coverage | integer | 0 | global | Show lights debugging helpers? |
| r_startup_progress | integer | 0 | global | Indicates progress of game startup. |
| r_sun_shadow_quality | integer | 4 | global | Quality of the sun shadows. |
| r_sun_shadow_texture_size | integer | 4096 | global | Size of the sun shadow texture. Bigger number = better visuals, smaller fps |
| r_sunshafts | integer | 1 | global | Are sunshafts enabled? |
| r_texture_detail | integer | 0 | global | Texture detail. Number of biggest mipmap levels to skip. |
| r_use_depth_bounds | integer | 1 | global | Should game use depth bounds to speedup rendering of the lights? (Works only on supported hardware) |
| r_vsync | integer | 1 | global | Is vertical synchronization enabled? |
| r_wireframe | integer | 0 | global | Enables wireframe rendering. |
| s_air_noise | float | 1.0 | profile | Sound of air at high speed. |
| s_interior_volume | float | 1.0 | profile | Interior sound volume multiplier. |
| s_master_volume | float | 1.0 | profile | Master volume. |
| s_music_enabled | integer | 1 | profile | Is music enabled? |
| s_music_volume | float | 0.8 | profile | Music volume. |
| s_radio_volume | float | 1.0 | profile | Radio volume. |
| s_reverse_enabled | integer | 1 | profile | Is reverse sound enabled? |
| s_reverse_stereo | int | 0 | profile | Is stereo reversed? |
| s_rumble_enabled | integer | 1 | profile | Is rumble sound enabled? |
| s_sfx_enabled | integer | 1 | profile | Is sfx enabled? |
| s_sfx_volume | float | 1.0 | profile | SFX volume. |
| s_wheel_noise | float | 1.0 | profile | Sound of wheels at high speed. |
| sys_info | string | No default value | global | Stores information about your operating system |
| t_averaging_window_duration | integer | 100 | global | Maximal combined duration of past frames used to calculate the current frame duration. Expressed in milliseconds. |
| t_averaging_window_length | integer | 10 | global | Maximal number of the past frames used to calculate the current frame duration. |
| vid_mem | string | No default value | global | Stores information about video memory of currently used graphics card. |
| vid_name | string | No default value | global | Stores information about currently used graphics card. |
| vid_ver | string | No default value | global | Stores information about currently used graphics card driver version. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Configuration_variables | revision: 5727 | captured: 2026-10-21 23:56:14 -->
