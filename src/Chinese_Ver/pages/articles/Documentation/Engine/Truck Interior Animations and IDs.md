# Documentation/Engine/Truck Interior Animations and IDs

## 内饰动画

卡车内饰中各种物体的运动由程序驱动的动画（***_anim**）控制。每个动画的范围由 ***_anim_min** 和 ***_anim_max** 值设定。由于大多数动画期望的范围是 0 到 1，这些也是默认值。如果某个动画期望其他值范围，将在下文说明。

### 特殊动画

| 属性名 | 功能 | 行为 | 备注 |
| --- | --- | --- | --- |
| wheel_anim | 方向盘 | 0 - 左满舵<br>0.5 - 居中<br>1 - 右满舵 | *(1.42 中已废弃)*<br><br>为获得最佳效果，每个关键帧应小于 45°<br>方向盘骨骼应命名为 **steering_w**，以兼容[可互换方向盘](../../Games/ETS2/Modding%20guides/1.25.md#Steering_wheel_accessory)。 |
| wheel_updown_anim | 转向柱倾斜调节 | 0 - 最低位置<br>1 - 最高位置 | 默认位置由 **wheel_updown_anim_default** 设定 |
| wheel_frontback_anim | 转向柱伸缩调节 | 0 - 完全缩回<br>1 - 完全伸出 | 默认位置由 **wheel_frontback_anim_default** 设定 |
| wiper_anim | 风挡雨刮 | 0→1 为一个完整的刮水循环<br>（从停靠位到最大行程再回到停靠位） | 0 和 1 处的关键帧应相同。 |
| rear_wiper_anim | 后风挡雨刮 | 0→1 为一个完整的刮水循环<br>（从停靠位到最大行程再回到停靠位） | 0 和 1 处的关键帧应相同。*1.61 中新增* |
| gadget_anim |  | 0→1 为一个完整的动画循环<br>（动画将作为连续循环播放） | 当卡车点火/通电时，此动画以循环方式播放。 |
| left_window_anim | 左车窗升降动画 | 0 - 关闭<br>1 - 开启 | 通过车窗升降控件操作。 |
| right_window_anim | 右车窗升降动画 | 0 - 关闭<br>1 - 开启 | 通过车窗升降控件操作。 |

### 操纵杆动画

<table class="wikitable">
<tbody><tr>
<th>属性名
</th>
<th>功能
</th>
<th>行为
</th>
<th>备注
</th></tr>
<tr>
<td>blinker_anim
</td>
<td>转向信号控制杆
</td>
<td>0 - 左侧转向灯激活<br/>0.5 - 静止位置<br/>1 - 右侧转向灯激活
</td>
<td>
</td></tr>
<tr>
<td>lights_anim
</td>
<td>前照灯控制
</td>
<td>0 - 灯光关闭<br/>0.5 - 驻车/示宽灯开启<br/>1 - 前照灯开启
</td>
<td>
</td></tr>
<tr>
<td>high_beam_anim
</td>
<td>远光灯控制
</td>
<td>0 - 静止位置<br/>1 - 远光灯开启
</td>
<td>
</td></tr>
<tr>
<td>light_horn_stick_anim
</td>
<td>灯光喇叭/城市喇叭按钮
</td>
<td>0 - 静止位置<br/>1 - 灯光喇叭被按下
</td>
<td>
</td></tr>
<tr>
<td>wiper_stick_anim
</td>
<td>风挡雨刮控制
</td>
<td>0 - 关闭<br/>1 - 最高速度
</td>
<td>此动画根据雨刮速度的总数进行插值。例如，如果有两个额外的雨刮速度（延迟），0.33 对应第一个延迟定义，0.67 对应第二个。
</td></tr>
<tr>
<td rowspan="2">parking_stick_anim
</td>
<td rowspan="2">驻车制动控制
</td>
<td rowspan="2">0 - 驻车制动释放<br/>1 - 驻车制动施加
</td>
<td><b>北美：</b>“in”（推入）还是“out”（拉出）为施加状态取决于卡车——确保动画与阀上的标签相符，否则会显得很滑稽。
<p>典型用法适用于“推入释放”系统，其中 0.0 状态为 'in'（推入），1.0 状态为 'out'（拉出）。
</p>
</td></tr>
<tr>
<td><b>欧洲：</b>
</td></tr>
<tr>
<td>parking_stick_electric_anim
</td>
<td>驻车制动控制
</td>
<td>0 - 驻车制动释放中<br/>0.5 - 驻车制动中间/中立/回位位置<br/>1 - 驻车制动施加
</td>
<td>驻车制动的电子版本。它被拨到某个位置后会自动返回默认位置（游戏以程序化方式处理回位）。
</td></tr>
<tr>
<td>parking_stick_handbrake_anim
</td>
<td>手刹控制
</td>
<td>0 - 手刹分离<br/>0.5 - 手刹接合<br/>1 - 手刹分离
</td>
<td>驻车制动的手刹版本。接合手刹时播放前半段，分离手刹时播放后半段。0.0 和 1.0 时刻的关键帧应相同。<i>1.61 中新增</i>
</td></tr>
<tr>
<td>flasher_4way_anim
</td>
<td>四闪（危险报警灯）控制
</td>
<td>0 - 静止位置<br/>1 - 危险报警灯激活
</td>
<td>对于按钮，“按下”状态应为 0.5，以使按钮在激活和停用时都能按下并回弹
</td></tr>
<tr>
<td>engine_start_anim
</td>
<td>点火与启动控制
</td>
<td>0 - 关闭<br/>0.33 - 通电<br/>0.67 - 发动机开启<br/>1 - 发动机启动中
</td>
<td>
</td></tr>
<tr>
<td>beacon_anim
</td>
<td>警示灯开/关开关
</td>
<td>0 - 警示灯关闭
<p>1 - 警示灯开启
</p>
</td></tr>
<tr>
<td>trailer_air_stick_anim
</td>
<td>挂车空气供给阀
</td>
<td>0 - 挂车未连接
<p>1 - 挂车已连接
</p>
</td>
<td>这直接关联挂车是否连接到卡车。
<p>典型用法适用于“推入供气”类型，因此阀门在 0.0 状态为 'out'（拉出），在 1.0 状态为 'in'（推入）
</p>
</td></tr>
<tr>
<td>trailer_air_stick_electric_anim
</td>
<td>挂车空气供给阀
</td>
<td>0 - 挂车断开连接中<br/>0.5 - 挂车空气中间/中立/回位位置<br/>1 - 挂车连接中
</td>
<td>挂车空气供给的电子版本。它被拨到某个位置后会自动返回默认位置（游戏以程序化方式处理回位）。
</td></tr>
<tr>
<td>trailer_brake_stick_anim
</td>
<td>挂车制动手动阀
<p>（有时称为 'spike'）
</p>
</td>
<td>0 - 静止位置
<p>1 - 挂车制动手动阀完全施加
</p>
</td>
<td>不要将其与挂车供给阀混淆——手动阀用于（很少使用）以受控方式仅施加挂车制动
</td></tr>
<tr>
<td>retarder_stick_anim
</td>
<td>缓速器控制
</td>
<td>0 - 关闭
<p>1 - 最大设置
</p>
</td>
<td>
</td></tr>
<tr>
<td>engine_brake_stick_anim
</td>
<td>发动机制动控制
</td>
<td>0 - 关闭
<p>1 - 最大设置
</p>
</td>
<td><i>1.38 中新增</i>
</td></tr>
<tr>
<td>auto_transmission_stick_anim
</td>
<td>自动变速箱换挡选择器
</td>
<td>0 - 倒挡<br/>0.5 - 空挡<br/>1 - 前进挡
</td>
<td>
</td></tr>
<tr>
<td>lift_axle_stick_anim
</td>
<td>提升桥开关/控制
</td>
<td>
</td>
<td>
</td></tr>
<tr>
<td>differential_lock_stick_anim
</td>
<td>差速锁开关/控制
</td>
<td>0 - 分离<br/>1 - 接合
</td>
<td><i>ETS2 1.27/ATS 1.6 中新增</i>
</td></tr>
<tr>
<td>left_window_stick_anim
</td>
<td>左车窗开关/控制
</td>
<td>0 - 关闭中<br/>0.5 - 静止位置<br/>1 - 开启中
</td>
<td>
</td></tr>
<tr>
<td>right_window_stick_anim
</td>
<td>右车窗开关/控制
</td>
<td>0 - 关闭中<br/>0.5 - 静止位置<br/>1 - 开启中
</td>
<td>
</td></tr>
<tr>
<td>left_window_stick_manual_anim
</td>
<td>左车窗手动控制
</td>
<td>0 - 车窗关闭<br/>1 - 车窗开启
</td>
<td>在车窗动画播放时从 0 播放到 1，允许在发动机未通电时降下车窗。<i>1.61 中新增</i>
</td></tr>
<tr>
<td>right_window_stick_manual_anim
</td>
<td>右车窗手动控制
</td>
<td>0 - 车窗关闭<br/>1 - 车窗开启
</td>
<td>在车窗动画播放时从 0 播放到 1，允许在发动机未通电时降下车窗。<i>1.61 中新增</i>
</td></tr></tbody></table>

### 仪表动画

这组动画用于模拟指针式仪表。相关的 ***_min** 和 ***_max** 属性设定动画起点和终点所对应的值。当模拟值超出 min/max 属性时，动画会被钳制。

> **注意：** 自 ETS2 1.27/ATS 1.6 起，所有 ***_psi_*** 属性已重命名为 ***_pressure_***。这是为了反映工作压力单位由 *psi* 改为 *bar*（大气压）。

| 属性名 | 功能 | 行为 | 备注 |
| --- | --- | --- | --- |
| oil_pressure_anim | 发动机机油压力（bar） | 0 - oil_pressure_anim_min 1 - oil_pressure_anim_max | 典型工作值为 3-6 bar（43.5-87 psi） |
| water_temp_anim | 发动机水温/冷却液温度（°C） | 0 - water_temp_anim_min 1 - water_temp_anim_max | 工作值 90°C |
| battery_anim | 蓄电池电压（V） | 0 - battery_anim_min 1 - battery_anim_max | 标称 24V。对于 12V 系统，将 min/max 属性设为仪表显示值的两倍，它就会表现得如同真正的 12V 系统。 |
| oil_temp_anim | 发动机机油温度（°C） | 0 - oil_temp_anim_min 1 - oil_temp_anim_max | 工作值 90°C |
| exhaust_temp_anim | 排气温度（°C） | 0 - exhaust_temp_anim_min 1 - exhaust_temp_anim_max | 工作范围约到 650°C |
| diff_temp_anim | 差速器温度（°C） | 0 - diff_temp_anim_min 1 - diff_temp_anim_max | 工作值 90°C |
| tachometer_anim | 转速表，单位 rpm（每分钟转数） | 0 - tachometer_anim_min 1 - tachometer_anim_max |  |
| speedometer_anim | 速度表（km/h） | 0 - speedometer_anim_min 1 - speedometer_anim_max | 1mph = 1.60934km/h |
| air_pressure_anim | 空气制动储气筒压力（bar） | 0 - air_pressure_anim_min 1 - air_pressure_anim_max |  |
| brake_pressure_anim | 空气制动施加压力（bar） | 0 - brake_pressure_anim_min 1 - brake_pressure_anim_max |  |
| general_air_press_anim | 总空气供给（bar） | 0 - general_air_press_anim_min 1 - general_air_press_anim_max |  |
| trailer_air_press_anim | 挂车空气供给（bar） | 0 - trailer_air_press_anim_min 1 - trailer_air_press_anim_max |  |
| suspension_load_anim | 悬架载荷（牛顿） | 0 - suspension_load_anim_min 1 - suspension_load_anim_max | 期望以牛顿为单位的范围（22t 挂车在牵引销上约产生 70kN） |
| fuel_anim | 燃油表（相对满油） | 0 - fuel_anim_min 1 - fuel_anim_max | 默认情况下，0 对应空油状态，1 对应满油 |
| ad_blue_anim | Ad Blue/DEF 表（相对满量） | 0 - fuel_anim_min 1 - fuel_anim_max | 默认情况下，0 对应空量状态，1 对应满量 |
| turbo_anim | 进气歧管压力 |  |  |
| consumption_anim | 瞬时燃油消耗，单位 l/100km | 0 - consumption_anim_min 1 - consumption_anim_max | 斯堪尼亚仪表为 0 到 120 |
| clock_big_anim | 指针时钟，分针（0-60） | 0 - clock_big_anim_min（默认 0） 1 - clock_big_anim_max（默认 60） |  |
| clock_small_anim | 指针时钟，时针（0-12） | 0 - clock_small_anim_min（默认 0） 1 - clock_small_anim_max（默认 24） |  |
| generic_anim | 用于其他仪表的动画。 | 卡车关闭时为 0，卡车开启时为 1 |  |
| odometer_digit_0_anim<br> odometer_digit_1_anim<br> odometer_digit_2_anim<br> odometer_digit_3_anim<br> odometer_digit_4_anim<br> odometer_digit_5_anim<br> odometer_digit_6_anim<br> odometer_digit_7_anim | 指针式里程表动画 | 每个动画有 10 个关键帧，数字 0-9 各一个关键帧 | 数字 0 显示十分位，数字 1 显示个位，数字 2 显示十位，……，数字 7 显示百万位。里程表要正常工作需要数字 1，其他数字是可选的。显示的距离单位（km 或 m）由 **use_mile_units** 控制，该属性位于 **accessory_interior_data** 中。*1.61 中新增* |
| trip_counter_digit_0_anim<br> trip_counter_digit_1_anim<br> trip_counter_digit_2_anim<br> trip_counter_digit_3_anim | 指针式小计里程动画 | 每个动画有 10 个关键帧，数字 0-9 各一个关键帧 | 数字 0 显示十分位，数字 1 显示个位，数字 2 显示十位，数字 3 显示百位。小计里程要正常工作需要数字 1，其他数字是可选的。显示的距离单位（km 或 m）由 **use_mile_units** 控制，该属性位于 **accessory_interior_data** 中。*1.61 中新增* |

### 指示灯动画

这些动画不在 0 到 1 之间插值。它们只有 2 种状态：关闭（0）和开启（1），因此这些动画应只有 2 个关键帧。所有指示灯动画都会在启动时的电气自检中触发，也会因其特定功能而触发。

<table class="wikitable">
<tbody><tr>
<th>属性名
</th>
<th>功能
</th>
<th>行为
</th>
<th>备注
</th></tr>
<tr>
<td>button_left_blinker
</td>
<td>左转向指示灯
</td>
<td rowspan="2">随左/右转向信号闪烁
</td>
<td rowspan="2">相关属性 <b>blinker_delay</b> 描述半个闪烁循环的长度（以秒为单位）
</td></tr>
<tr>
<td>button_right_blinker
</td>
<td>右转向指示灯
</td></tr>
<tr>
<td>button_water_temp
</td>
<td>水温警告灯
</td>
<td>发动机温度过高时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_oil_temp
</td>
<td>发动机机油温度警告灯
</td>
<td>发动机机油温度过高时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_position_lights
</td>
<td>位置灯指示灯
</td>
<td>位置灯/示宽灯/驻车灯开启时点亮
</td>
<td>
</td></tr>
<tr>
<td>button_lights
</td>
<td>前照灯指示灯
</td>
<td>前照灯开启时点亮
</td>
<td>
</td></tr>
<tr>
<td>button_high_beam_lights
</td>
<td>远光灯指示灯
</td>
<td>远光灯开启时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_aux_lights_front
</td>
<td>前辅助灯指示灯
</td>
<td><i>前</i>辅助灯开启时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_aux_lights_roof
</td>
<td>车顶辅助灯指示灯
</td>
<td><i>车顶</i>辅助灯开启时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_aux_lights_any
</td>
<td>辅助灯指示灯
</td>
<td>任何辅助灯开启时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_low_air_pressure
</td>
<td>气压过低警告灯
</td>
<td>气压降至约 5 bar 以下时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_low_oil_pressure
</td>
<td>机油压力过低警告灯
</td>
<td>发动机机油压力过低时点亮
</td>
<td>通电且发动机熄火时也会点亮
</td></tr>
<tr>
<td>button_battery_warning
</td>
<td>蓄电池电压过低警告灯
</td>
<td>蓄电池电压过低时点亮
</td>
<td>
</td></tr>
<tr>
<td>button_low_fuel
</td>
<td>燃油不足警告灯
</td>
<td>燃油液位过低时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_low_adblue
</td>
<td>AdBlue/DEF 不足警告灯
</td>
<td>AdBlue/DEF 液位过低时点亮
</td>
<td>
</td></tr>
<tr>
<td>button_jakebrake
</td>
<td>发动机制动指示灯
</td>
<td>发动机制动（雅各布制动）已预备或激活时点亮
</td>
<td>
</td></tr>
<tr>
<td>button_parking_brake
</td>
<td>驻车制动指示灯
</td>
<td>驻车制动施加时点亮
</td>
<td>
</td></tr>
<tr>
<td>button_4way
</td>
<td>四闪状态灯
</td>
<td>四闪开启时点亮
</td>
<td>指示灯应置于危险报警灯按钮上以便闪烁
</td></tr>
<tr>
<td>indicator_retarder
</td>
<td>缓速器状态灯
</td>
<td>缓速器激活时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_warning
</td>
<td>损坏警告指示灯
</td>
<td>损坏达到 15% 或以上时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_stop
</td>
<td>严重损坏指示灯
</td>
<td>损坏达到 50% 或以上时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_axle_lift
</td>
<td>提升桥指示灯
</td>
<td>提升桥升起时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_cruise_control
</td>
<td>巡航控制状态灯
</td>
<td>巡航控制接合时点亮
</td>
<td>
</td></tr>
<tr>
<td>indicator_generic
</td>
<td>用于其他指示灯的动画
</td>
<td>大部分时间为 0，卡车进行电气自检时（开启后）为 1。
</td>
<td>
</td></tr>
<tr>
<td>indicator_differential_lock
</td>
<td>差速锁状态灯
</td>
<td>差速锁接合时点亮
</td>
<td><i>ETS2 1.27/ATS 1.6 中新增</i>
</td></tr>
<tr>
<td>indicator_trailer_axle_lift
</td>
<td>挂车提升桥状态灯
</td>
<td>挂车车桥升起时点亮。
</td>
<td><i>ETS2 1.27/ATS 1.6 中新增</i>
</td></tr>
<tr>
<td>indicator_weigh_green
</td>
<td>（ATS）称重站通行应答器绿色（绕行）灯
</td>
<td>玩家可以绕过前方称重站时点亮
</td>
<td><i>ETS2 1.27/ATS 1.6 中新增</i>
</td></tr>
<tr>
<td>indicator_weigh_red
</td>
<td>（ATS）称重站通行应答器红色（不可绕行）灯
</td>
<td>玩家必须进入前方称重站时点亮
</td>
<td><i>ETS2 1.27/ATS 1.6 中新增</i>
</td></tr>
<tr>
<td>indicator_blind_spot_left
</td>
<td>左侧盲区指示灯
</td>
<td>有其他车辆接近玩家车辆的左侧盲区时点亮
</td>
<td><i>ETS2 1.47/ATS 1.45 中新增</i>
</td></tr>
<tr>
<td>indicator_blind_spot_right
</td>
<td>右侧盲区指示灯
</td>
<td>有其他车辆接近玩家车辆的右侧盲区时点亮
</td>
<td><i>ETS2 1.47/ATS 1.45 中新增</i>
</td></tr></tbody></table>

## 仪表板 ID

仪表板电脑的屏幕使用我们的 UI 库，因此显示的是 UI 元素。每个元素都有唯一 ID，且只能使用一次（因为缓存）。大多数字段可用作双参数模板——值和单位，两者都会根据当前游戏选项使用。由于不同语言中单位和其它文本可能被翻译，要确保为它们留出足够空间。

### 屏幕 ID（**ui::group** 类型）：

- 100 到 800 - 基础屏幕，最多 8 个屏幕
- 900 - 警告屏幕，在卡车受损且需要维修时使用，单独显示（不共用屏幕）
- 910 到 913 - 驻车摄像头屏幕，最多 4 个屏幕（在挂 R 挡行驶和/或用户激活驻车摄像头时启用）
- 950 - 共用屏幕（与所有基础屏幕一起使用）

### 元素 ID（大多为 **ui::text_common** 类型）：

- 1000 - 环境温度
- 1010 - 机油温度
- 1020 - 当前速度
- 1030 - 里程表，至少需要六位数字的空间
- 1040 - 当前挡位，自动挡使用 N、A[number]、R 或 R[number]，手动或顺序挡使用 N、[number]、R 或 R[number]
- 1050 - 当前时钟时间，格式正确，例如 "12:34"（省略上午/下午）
- 1060 - 油箱内剩余燃油
- 1070 - 用于燃油条的 ui_text_bar，文本根据当前油箱状态裁剪
- 1075 - *(1.49 中已废弃)* 定义燃油条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~1"，水平范围 0 到 1）
- 1080 - 车辆预估可行驶里程
- 1090 - 水温
- 1100 - 巡航控制速度值
- 1110 - 用于机油压力条的 ui_text_bar，文本根据当前机油压力裁剪
- 1115 - *(1.49 中已废弃)* 定义机油压力条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~8"，水平范围 0bar 到 8bar（116psi））
- 1120 - 用于气压条的 ui_text_bar，文本根据当前气压裁剪
- 1125 - *(1.49 中已废弃)* 定义气压条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~12"，水平范围 0bar 到 12bar（174psi））
- 1130 - 用于涡轮压力条的 ui_text_bar，文本根据当前机油压力裁剪
- 1135 - *(1.49 中已废弃)* 定义涡轮压力条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~1"，水平范围 0 到 1）
- 1140 - 用于 AdBlue 条的 ui_text_bar，文本根据当前 AdBlue 箱状态裁剪
- 1145 - *(1.49 中已废弃)* 定义 AdBlue 条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~1"，水平范围 0 到 1）
- 1150 - 用于水温条的 ui_text_bar，文本根据当前水温裁剪
- 1155 - *(1.49 中已废弃)* 定义水温条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~130"，水平范围 0°C 到 130°C（32°F 到 266°F））
- 1160 - 瞬时消耗
- 1170 - 平均（行程）消耗
- 1180 - 用于制动踏板压力条的 ui_text_bar，文本根据当前压力裁剪
- 1185 - *(1.49 中已废弃)* 定义制动踏板压力条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~1"，水平范围 0 到 1）
- 1190 - 损坏警告图标，可以是 ui::group 或 ui::text 或任何其他可显示/隐藏的元素
- 1200 - 燃油不足警告图标，可以是 ui::group 或 ui::text 或任何其他可显示/隐藏的元素
- 1210 - 行程距离
- 1220 - 指南针，显示诸如 "N"、"E"、"SW" 的字符串。
- 1230 - 发动机制动图标
- 1240 - 巡航控制图标，可以是 ui::group 或 ui::text 或任何其他可显示/隐藏的元素。巡航控制速度（id 1100）明确可以为此组的子元素。
- 1250 - 巡航控制记忆图标，可以是 ui::group 或 ui::text 或任何其他可显示/隐藏的元素。
- 1260 - 气压过低警告图标
- 1270 - 驻车制动指示图标
- 1280 - 发动机运行时间
- 1290 - 缓速器图标
- 1300 - 变速箱挡位（原始值，不含模式信息）
- 1310 - 变速箱模式（不含挡位信息，A/M）
- 1320 - 蓄电池电压
- 1330 - 蓄电池电压表，应为 ui_gauge 元素类型
- 1340 - 机油温度表，应为 ui_gauge 元素类型
- 1350 - 用于瞬时油耗条的 ui_text_bar，文本根据当前值裁剪
- 1355 - *(1.49 中已废弃)* 定义瞬时油耗条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~5"，水平范围 0 到 5 km/l（11.8mpg））
- 1360 - 用于平均油耗条的 ui_text_bar，文本根据当前值裁剪
- 1365 - *(1.49 中已废弃)* 定义平均油耗条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~5"，水平范围 0 到 5 km/l（11.8mpg））
- 1370 - 气压值（仅 psi）
- 1380 - 变速箱模式，详细（D/N/R/M）
- 1390 - 行程时间
- 1400 - 行程平均速度（行程距离 / 行程时间）
- 1410 - 若 CC 已接合，则为智能巡航控制容差，否则隐藏该元素
- 1420 - 损坏停车图标，可以是 ui::group 或 ui::text 或任何其他可显示/隐藏的元素
- 1430 - 速度表，应为 ui_gauge 元素类型
- 1440 - 每分钟转数（rpm）表，应为 ui_gauge 元素类型
- 1450 - 巡航控制速度表，应为 ui_gauge 元素类型
- 1460 - 水温表，应为 ui_gauge 元素类型
- 1470 - 驻车灯图标，可以是 ui::group 或 ui::text 或任何其他可显示/隐藏的元素
- 1480 - 近光灯图标，可以是 ui::group 或 ui::text 或任何其他可显示/隐藏的元素
- 1490 - 差速锁图标，可以是 ui::group 或 ui::text 或任何其他可显示/隐藏的元素
- 1500 - 自上次行车电脑重置以来消耗的燃油
- 1510 - 油箱内剩余燃油百分比（范围 0-100）
- 1520 - 油箱内剩余 AdBlue 百分比（范围 0-100）
- 1530 - ETA（预计到达时间），时间不可用时隐藏（无送货任务、无导航等）
- 1540 - 距需要休息的时间，g_fatigue 为 0 时隐藏（疲劳选项已禁用）
- 1550 - 用于差速器温度条的 ui_text_bar，文本根据当前值裁剪
- 1555 - *(1.49 中已废弃)* 定义差速器温度条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~130"，水平范围 0°C 到 130°C（32°F 到 266°F））
- 1560 - 用于悬架载荷条的 ui_text_bar，文本根据当前值裁剪
- 1565 - *(1.49 中已废弃)* 定义悬架载荷条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~100000"，水平范围 0 到 100kN）
- 1570 - 左转向灯图标
- 1580 - 右转向灯图标
- 1590 - 远光灯图标
- 1600 - 用于机油温度条的 ui_text_bar，文本根据当前值裁剪
- 1605 - *(1.49 中已废弃)* 定义机油温度条尺寸、方向和范围的 ui::text（典型数据 "H~~0~~130"，水平范围 0°C 到 130°C（32°F 到 266°F））
- 1610 - 限速
- 1620 - 数字主后视镜，可以是任何可显示/隐藏的元素（当主后视镜通过摄像头单元前缀检测到数字主后视镜时显示）
- 1630 - 数字侧后视镜，可以是任何可显示/隐藏的元素（当侧后视镜通过摄像头单元前缀检测到数字侧后视镜时显示）
- 1640 - 数字前视镜，可以是任何可显示/隐藏的元素（当前视镜通过摄像头单元前缀检测到数字前视镜时显示）
- 1650 - 数字引擎盖后视镜，可以是任何可显示/隐藏的元素（当引擎盖后视镜通过摄像头单元前缀检测到数字引擎盖后视镜时显示）
- 1660 - 近距盲区指示灯（哪一侧取决于 `left_hand_traffic` 内饰数据属性），可以是任何可显示/隐藏的元素（当车辆左侧检测到障碍物时显示）
- 1670 - 远距盲区指示灯（哪一侧取决于 `left_hand_traffic` 内饰数据属性），可以是任何可显示/隐藏的元素（当车辆右侧检测到障碍物时显示）
- 1680 - 行程能量回收（回收的能量）
- 1690 - 用于功率消耗的 ui_text_bar，文本根据当前值裁剪（具体行为基于 Renaut E-Tech）
- 1700 - 用于 rpm 的 ui_text_bar，文本根据当前值裁剪（值为 RPM）
- 1710 - 用于速度的 ui_text_bar，文本根据当前值裁剪（值为 km/h）
- 1720 - 功率消耗表，应为 ui_gauge 元素类型（最大回收：-1，怠速：0，最大功率：1）
- 1730 - 发动机 RPM 除以 1000（四舍五入到一位小数）
- 1740 - 燃油表，应为 ui_gauge 元素类型（空油：0，满油：1）
- 1750 - 平均（行程）消耗表，应为 ui_gauge 元素类型（值为 l/100km）
- 1760 - 机油压力值

> **注意：** 在 1.49 中，文本条改为 ui_text_bar 元素。现在不需要额外数据，全部保存在常规成员中（vertical、min_size、max_size、min_value、max_value）。
>
> 旧系统（1.49 之前）使用次级文本字段。文本条的数据按 "H~~0~~130" 格式填写，H 表示文本条为水平方向（V 表示垂直方向），最左位置代表值 0，最右位置代表值 130。空文本默认为 "H~~0~~1"。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Truck_Interior_Animations_and_IDs | revision: 5808 | captured: 2026-10-21 23:56:14 -->
