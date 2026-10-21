# 文档/引擎/单元/配件内饰数据

**accessory_interior_data** 单元类用于为[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)定义内饰及其动画。此类型的单元通常定义在 **/def/vehicle/truck/<brand.model>/interior/*.sii** 中，并通过以下文件大量使用[包含](../Units.md#Includes)：

- **/def/vehicle/truck/<brand.model>/interior/animations.sui**（与动画相关的属性；ETS2 中右舵车辆使用 **animations_uk.sii**）
- **/def/vehicle/truck/<brand.model>/interior/dashboard_color.sii**（dashboard_color 数组属性）
- **/def/vehicle/truck/<brand.model>/interior/seat.sui**（座椅调节限制；ETS2 中右舵车辆使用 **seat_uk.sui**）

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| model | string |  | 刚性内饰模型的模型描述符（.pmd）路径。 |
| animated_model | string |  | 动画内饰模型的模型描述符（.pmd）路径。 |
| collision | string |  | 碰撞描述符（.pmc）路径。此文件用于玩具的物理模拟。 |
| variant | token |  | 用于内饰模型和碰撞的 variant 名称。 |
| look | token |  | 用于内饰模型的 look 名称。 |
| ext_model | string |  | 外部模型（从外部摄像机可以看到的内饰）的模型描述符（.pmd）路径。 |
| ext_variant | token |  | 用于外部模型的 variant 名称。 |
| ext_look | token |  | 用于外部模型的 look 名称。 |
| *动画属性* | string / float |  | 目前有近 70 个[内饰动画](../Truck%20Interior%20Animations%20and%20IDs.md#Interior_Animations)属性，此外部分具有可调范围的属性还配有 _min 和 _max 属性。内饰动画通常定义在 **animations.sui** 中，并通过[包含](../Units.md#Includes)引入内饰定义。 |
| wiper_delay | array&lt;float&gt; |  | 每个成员定义间歇雨刮器在各次刮刷循环之间的延迟秒数。它们通常应按递减顺序排列，因为最后一种雨刮模式是连续模式。如果为空，则只有连续模式可用。*1.35 中移除。* |
| wiper_duration_and_delay | array&lt;float2&gt; | (2.0, 0.0) | 每个成员定义刮刷循环的持续时间（秒），以及各次刮刷循环之间的延迟（秒）。它们通常应按延迟递减、速度递减的顺序排列。*1.35 中新增。* |
| wiper_main_cycle | float2 | (0.0, 1.0) | 定义雨刮器在动画中的工作范围。0.0 到第一个值 - 雨刮器启动序列的动画，在开始主循环前播放一次；两个值之间 - 重复播放的主雨刮循环动画；第二个值到 1.0 - 雨刮器结束序列的动画，在关闭雨刮器后播放一次。*1.61 中新增。* |
| blinker_delay | float | 0.5 | 转向灯循环一半的时长（秒）。转向灯在这段时间内点亮，然后在同样长的时间内熄灭，依此类推。通常通过 **animations.sui** 包含。 |
| show_chassis_rear | bool | false | 在可以看到部分底盘或底盘配件的内饰中应将其设为 true（例如 ATS 的日间驾驶室）。它会在内饰中渲染底盘及其所有配件的预烘焙模型，因此对于安装在底盘上、但在内饰中又有自身可视化表现的物品，你可能会遇到问题 - 你可能会看到它们两次和/或出现 z-fighting。要使其在车内和车外都能正确显示，配件定位器要么只应放在底盘模型中，要么应同时放在内饰和驾驶室模型中。*1.44 中新增。* |
| dashboard_path | string |  | 仪表板显示的 UI 定义路径。 |
| gps_path | string |  | GPS 显示的 UI 定义路径。 |
| use_mile_units | bool | false | 为 true 时，仪表板上的距离和速度将使用英里单位而非公里。 |
| left_hand_traffic | bool | false | 为 true 时，车辆采用右舵（英国）规则。 |
| backlight_with_lights | bool | true | 为 false 时，仪表板背光随点火开关始终开启。否则，背光与前照灯一同正常激活。 |
| air_brake_safeguard | bool | false | 为 true 时，当供给气压降到某个阈值以下时，驻车制动会自动施加（典型的美式行为）。 |
| panel_intensity_min | float | 0.01 | 最小背光强度。 |
| panel_intensity_max | float | 0.3 | 最大背光强度。 |
| glass_panes | array<owner_ptr> |  | 每个成员指向一个 [glass_pane_data](glass%20pane%20data.md) 单元的单元名。 |
| dashboard_color | array&lt;float3&gt; |  | 包含 16 种颜色的数组，根据仪表板及内饰中其他 dif.lum 表面所 UV 映射到的瓦片，定义这些表面的照明颜色。通常通过 **dashboard_color.sui** 包含。 |
| seat_left_limit | float | -0.15 | 内饰摄像机可向左移动的最大距离。通常通过 **seat.sui** 包含。 |
| seat_right_limit | float | 0.15 | 内饰摄像机可向右移动的最大距离。通常通过 **seat.sui** 包含。 |
| seat_up_limit | float | 0.15 | 内饰摄像机可向上移动的最大距离。通常通过 **seat.sui** 包含。 |
| seat_down_limit | float | -0.15 | 内饰摄像机可向下移动的最大距离。通常通过 **seat.sui** 包含。 |
| seat_front_limit | float | -0.1 | 内饰摄像机可向前移动的最大距离。通常通过 **seat.sui** 包含。 |
| seat_back_limit | float | 0.2 | 内饰摄像机可向后移动的最大距离。通常通过 **seat.sui** 包含。 |
| sounds | array&lt;string&gt; |  | 每个条目按照 "*sound_name\|sound_path*" [格式](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories)，为一个功能分配一个 FMOD 事件。*1.39 中新增* 预期的事件名称为：air_warning、blinker_off、blinker_on、noise、stick_blinker、stick_blinker_off、stick_engine_brake、stick_hazard_warning、stick_high_beam、stick_light_horn、stick_lights、stick_park_brake、stick_park_brake_off、stick_retarder、stick_wipers、weigh_green、weigh_red、window_click、window_move、wipers_down 和 wipers_up。 |

## 玻璃窗格与雨刮器

相关单元 **glass_pane_data** 和 **wiper_data** 定义在与 accessory_interior_data 相同的 `SiiNunit` 作用域内，通过 **/def/vehicle/truck/<brand.model>/interior/glass.sui**（某些旧版情况下为 **glass.dat**）包含：

- [glass_pane_data](glass%20pane%20data.md)（用于定义雨滴积聚和雨刮器模拟的表面）
- [wiper_data](wiper%20data.md)（用于定义将雨滴从玻璃窗格上刮除的雨刮器）

例如：

```
SiiNunit
{	// start of SiiNunit global scope

accessory_interior_data : something.brand.truck.interior
{	// start of accessory_interior_data unit

	// various attributes belonging to accessory_interior_data

	// each member refers to a unit included via glass.sui
	glass_panes[]: .brand.truck.pane.front
	glass_panes[]: .brand.truck.pane.close
	glass_panes[]: .brand.truck.pane.far
	// etc...

}	// end of accessory_interior_data scope

@include "glass.sui"	// file containing glass_pane_data and wiper_data units

}	// end of SiiNunit global scope
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_interior_data | revision: 5795 | captured: 2026-10-21 23:56:14 -->
