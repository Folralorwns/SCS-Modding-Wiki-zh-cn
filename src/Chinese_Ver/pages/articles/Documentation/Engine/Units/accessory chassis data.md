# 文档/引擎/单元/配件底盘数据

**accessory_chassis_data** 单元类用于定义[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)的底盘特性，包括轴重、扩展阴影参数和液体容量。它也用于定义挂车和 AI 车辆的底盘特性。此类型的单元通常定义在 **/def/vehicle/truck/<brand.model>/chassis/*.sii**、**/def/vehicle/trailer/<trailer_name>/*.sii** 和 **/def/vehicle/ai/<vehicle_name>/chassis.sii.** 中。

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| detail_model | string |  | 详细网格模型描述符（.pmd）的路径。此模型仅用于玩家使用的车辆。此外，它还用于车辆预览和浏览器窗口。 |
| model | string |  | 模型描述符（.pmd）的路径。如果只使用单个 LOD，则应将其设置为 **model**，并且不应定义其他属性（detail_model、lods）。 |
| lods | array&lt;string&gt; |  | 简化细节层级模型描述符（.pmd）的路径，按观察距离递增（模型复杂度递减）的顺序排列。 |
| collision | string |  | 碰撞描述符（.pmc）的路径。 |
| pendle_axle_model | array&lt;string&gt; |  | pendle（自转向、随动）轴模型的模型描述符（.pmd）的路径，每根轴成对给出左/右模型。 |
| brake_caliper_model | array&lt;string&gt; |  | 动画制动钳模型描述符（.pmd）的路径，每根轴一个。设置时必须与轴数（**residual_travel** 的大小）一致。 |
| brake_rotor_model | array&lt;string&gt; |  | 动画制动盘（碟片）模型描述符（.pmd）的路径，每根轴一个。设置时必须与轴数（**residual_travel** 的大小）一致。 |
| trailer_brace_model | string |  | *仅用于挂车。* 动画支腿模型的路径。 |
| trailer_brace_anim | string |  | *仅用于挂车。* 支腿动画的路径。 |
| trailer_brace_up_sound | string |  | *仅用于挂车。* 收起支腿时播放的声音路径。*默认值在 1.35 中改为空白（无声音）。* |
| trailer_brace_down_sound | string |  | *仅用于挂车。* 展开支腿时播放的声音路径。*默认值在 1.35 中改为空白（无声音）。* |
| variant | token |  | 从 **detail_model**、**model** 和 **lods** 中使用的 variant。 |
| variant_uk | token |  | 在靠左行驶的国家/地区使用的 variant。如果未指定，则默认为 **variant** 的值。 |
| look | token |  | 从 **detail_model**、**model** 和 **lods** 中使用的 look。 |
| shadow_texture | string |  | 用于基础阴影的纹理。 |
| shadow_intensity | float | 1.0 | 基础阴影的相对强度。 |
| extended_shadow_texture | string |  | 用于扩展（体积）阴影的纹理。 |
| extended_shadow_intensity | float | 1.0 | 扩展（体积）阴影的相对强度。 |
| extended_shadow_fadeout_start | float | 0.0 | 设置从 fakeshadow 表面开始淡出扩展阴影的距离，单位为米。 |
| extended_shadow_fadeout_length | float | 1.0 | 设置扩展阴影淡出的长度，单位为米。 |
| extended_shadow_shared_model_variant | token |  | 如果提供，将使用模型的指定 variant 绘制共享阴影。 |
| ui_shadow | string |  | UI 阴影的模型描述符（.pmd）的路径（用于卡车/挂车浏览器、缩略图生成等）。 |
| tank_size | float | 0.0 | 燃油箱容量，单位为升。 |
| adblue_tank_size | float | 80.0 | AdBlue/DEF 罐容量，单位为升。 |
| air_tank_pressure | float | 10.0 | 气压制动储气筒的标称压力，单位为 bar。*在 ETS2 1.27/ATS 1.6 中添加。* |
| nominal_voltage | float | 24.0 | 蓄电池标称电压。*在 1.36 中添加* |
| air_resistance | float | -1.0 | 为此特定底盘覆盖 [physics_data](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/physics_data&action=edit&redlink=1) 中的空气阻力系数。未设置（为负）时，使用全局值。 |
| residual_travel | array&lt;float&gt; |  | *用于卡车和挂车。* 每根轴向上和向下行程的限值，单位为米。每个数组成员对应一根轴，从前到后排列。 |
| trailer_mass | float | 7000.0 | *仅用于挂车。* 设置挂车的空载质量。 |
| powered_axle | array&lt;bool&gt; |  | *仅用于卡车。* 为 true 时，驱动力矩将施加在该轴上。每个数组成员对应一根轴，从前到后排列。 |
| kerb_weight | array&lt;float&gt; |  | *仅用于卡车。* 为每根轴分配静态重量。每个数组成员对应一根轴，从前到后排列。 |
| brake_rotor_diameter | array&lt;float&gt; |  | 制动盘直径，单位为米。有效范围为大于 0.0 且不超过 0.6。每个数组成员对应一根轴，从前到后排列。 |
| disc_brake | array&lt;bool&gt; | false | 为 true 时，该轴使用盘式制动器。每个数组成员对应一根轴，从前到后排列。 |
| caster_angle | float | 3.0 | 前轮轴的主销后倾角，单位为度。有效范围为 -20 到 20。 |
| sway_bar_stiffness | float | 1.0 | 防侧倾（横向稳定）杆的相对刚度。有效范围为 0 到 10。 |
| axle_suspension_type | array&lt;token&gt; | solidaxle | 每根轴的悬架类型，从前到后排列。可能的值为：simple wishbone（双叉臂）macpherson solidaxle 每个数组成员对应一根轴，从前到后排列。 |
| solid_axle_suspension_model | array&lt;string&gt; |  | 整体桥车轴视觉模型描述符（.pmd）的路径，对 **axle_suspension_type** 中为 **solidaxle** 且具有可见模型的每根轴各提供一个条目。 |
| suspension_damping_factor | array&lt;float&gt; |  | 每根轴的相对悬架阻尼系数。有效范围为 0 到 2。每个数组成员对应一根轴，从前到后排列。 |
| suspension_class | token | heavy | 悬架类别，用于悬架物理调校和音频选择。可接受的值为 **heavy**、**bus** 或 **standard**；任何其他值都将默认为 **heavy**。 |
| liftable_axle | array&lt;bool&gt; |  | *用于卡车和挂车。* 为 true 时，该轴可以被提升。每个数组成员对应一根轴，从前到后排列。*挂车功能在 ETS2 1.27/ATS 1.6 中添加。* |
| steerable_axle | array&lt;token&gt; | *见描述* | *用于卡车和挂车。* 每个数组成员对应一根轴，从前到后排列。默认情况下，卡车的第一根轴为 *true*，其他所有轴均为 *false*。可能的值为：false（不可转向的轴）true（该轴上的车轮可转向）axle（转向时整个轴旋转，必须正确定义 *axle_model*，仅对挂车有效）。*在 1.31 中添加。值 "axle" 在 1.50 中添加* |
| steerable_lifted_axles | bool | false | *用于卡车和挂车。* 为 true 时，已提升的可转向轴会对转向做出反应。否则它们在提升后会自行与底盘对齐。*在 1.44 中添加。* |
| max_steering_angle | uint | *见描述* | 车轮转向轴的最大转向角，单位为度。如果未设置，卡车默认为 40，挂车默认为 50。有效范围为卡车不超过 70，挂车不超过 85。 |
| steering_pivot_point_offset | float | 0.0 | 转向枢轴点的纵向偏移，用于转向几何计算。 |
| powered_trailer | bool | false | *仅用于挂车。* 与 **powered_axle** 一起设为 true 时，出于重量分配的目的，将车辆标识为动力台车/挂车而非卡车。 |
| weight_distribution | enum | semitrailer | 决定力如何在车辆与其连接的车辆之间传递。可能的值为：truck（任何独立的、自给自足的车辆；当设置了 **powered_axle** 且 **powered_trailer** 为 false 时自动检测）semitrailer（鞍座，传递部分挂车重量）trailer（挂钩，不传递重量）spreader（移除俯仰自由度，典型用于低平板配置中的 spreader/booster/stinger）perimeter（无车轮物理的专用车辆，例如起重机）*在 ATS 1.6.2 中添加。* |
| cog_height | float | *见描述* | 重心相对底盘的高度。如果未设置（为负），则根据底盘属于卡车还是挂车使用默认值。 |
| joint_yaw_limit | float | -1.0 | 此车辆与其主车辆之间连接处的自定义偏航角限制，单位为度。有效范围为 0 到 90；负值（默认）表示没有自定义限制。 |
| joint_pitch_limit | float | -1.0 | 此车辆与其主车辆之间连接处的自定义俯仰角限制，单位为度。有效范围为 0 到 90；负值（默认）表示没有自定义限制。 |
| joint_roll_limit | float | -1.0 | 此车辆与其主车辆之间连接处的自定义侧倾角限制，单位为度。有效范围为 0 到 90；负值（默认）表示没有自定义限制。 |
| master_collision_angle | float | 90.0 | 开启此车辆与其主车辆之间碰撞的角度，单位为度。有效范围为 0 到 180。 |
| axle_model | array&lt;string&gt; |  | *仅用于挂车。* 车轴模型描述符（.pmd）的路径。*在 1.50 中添加。* |
| axle_model_collision | array&lt;string&gt; |  | *仅用于挂车。* 车轴模型碰撞描述符（.pmc）的路径。*在 1.50 中添加。* |
| axle_model_extended_shadow_texture | array&lt;string&gt; |  | *仅用于挂车。* 用于每根轴下方扩展（体积）阴影的纹理。*在 1.50 中添加。* |
| axle_model_steer_angle | unsigned int |  | *仅用于挂车。* 覆盖最后一个可转向车轴模型的最大转向角。*在 1.50 中添加。* |
| axle_model_sliding_limits | float2 | (0,0) | *仅用于挂车。* 可移动 **axle_model** 模型相对于车轴定位器的最小和最大 Z（纵向）滑动限值。需要设置 **axle_model**。 |
| cog_cargo_mass_min | float | 0 | 偏移重心时的最低货物质量。*在 1.35 中添加。* |
| cog_cargo_mass_max | float | 20000 | 偏移重心时的最高货物质量。*在 1.35 中添加。* |
| cog_cargo_offset_min | float3 | (0,0,0) | 在 **cog_cargo_mass_min** 时偏移重心的距离。*在 1.35 中添加。* |
| cog_cargo_offset_max | float3 | (0,0.6,0) | 在 **cog_cargo_mass_max** 时偏移重心的距离。*在 1.35 中添加。* |
| sounds | array&lt;string&gt; |  | 每个条目使用“*sound_name\|sound_path*”[格式](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories)为某个底盘功能分配一个 FMOD 事件。*在 1.39 中添加* 预期的声音事件名称为：air_brake、air_cutoff、reverse、lift_axle、hook_attach、hook_detach 和 trailer_cables。 |
| lamp_setup | string |  | 当默认设置不够好时，特殊前照灯设置的路径。*在 1.40 中添加* **vehicle_lamp_setup 单元的内容是实验性功能，未来很可能会发生变化！** |
| animation | array<owner_ptr> |  | 每个成员指向一个 [vehicle_animation_data](vehicle%20animation%20data.md) 单元的单元名称。*在 1.61 中添加* |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_chassis_data | revision: 5810 | captured: 2026-10-21 23:56:14 -->
