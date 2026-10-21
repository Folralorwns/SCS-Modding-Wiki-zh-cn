# 文档/引擎/单元/配件声音数据

**accessory_sound_data** 单元类用于为[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)定义声音。此类型的单元通常位于 **/def/vehicle/truck/<brand.model>/sound/&lt;type&gt;/*.sii** 中。它们主要由指向 [sound_data](sound%20data.md)、[sound_engine_data](sound%20engine%20data.md) 和 [sound_noise_data](sound%20noise%20data.md) 单元的指针组成，这些单元既可以在行内定义，也可以通过[包含](../Units.md#Includes)从其他来源引入。一个有效的卡车配置将包含两个声音配件：一个用于外部声音，一个用于内部声音。这些单元的名称始终以 `.esound` 结尾（外部声音）或以 `.isound` 结尾（内部声音）。

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。标记为 *common* 的属性通常通过在 accessory_sound_data 单元定义中包含 `/def/vehicle/truck/common_sound_ext.sui` 或 `common_sound_int.sui`，以及在 SiiNunit 中包含 `/def/vehicle/truck/common_sound_ext_data.sui` 或 `common_sound_int_data.sui` 来定义。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 通用？ | 描述 |
| --- | --- | --- | --- | --- |
| exterior_sound | bool | false | 否 | 定义该单元包含的是外部声音（true）还是内部声音（false）。 |
| start | owner_ptr |  | 否 | 指向一个 **sound_data** 单元，该单元定义发动机启动时播放的声音。 |
| start_no_fuel | owner_ptr |  | 否 | 指向一个 **sound_data** 单元，该单元定义玩家在无燃油的情况下尝试启动发动机时播放的声音。 |
| stop | owner_ptr |  | 否 | 指向一个 **sound_data** 单元，该单元定义发动机停止时播放的声音。 |
| engine | array<owner_ptr> |  | 否 | 每个数组成员指向一个 **sound_engine_data** 单元，这些单元共同定义发动机在无负载时的声音（例如怠速、巡航、轻缓加速等）。 |
| engine_load | array<owner_ptr> |  | 否 | 每个数组成员指向一个 **sound_engine_data** 单元，这些单元共同定义发动机在负载下的声音（例如重加速、爬坡等）。 |
| engine_nofuel | array<owner_ptr> |  | 否 | 每个数组成员指向一个 **sound_engine_data** 单元，这些单元共同定义燃油被切断时发动机的声音（例如带挡滑行、限速器等）。 |
| engine_exhaust | array<owner_ptr> |  | 否 | 每个数组成员指向一个 **sound_engine_data** 单元，这些单元共同定义卡车排气管的共振声音。 |
| engine_brake | array<owner_ptr> |  | 否 | 每个数组成员指向一个 **sound_engine_data** 单元，这些单元共同定义使用发动机制动时发动机的声音。 |
| turbo | owner_ptr |  | 否 | 指向一个 **sound_data** 单元，该单元定义涡轮增压器的声音。 |
| retarder | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，该单元定义缓速器的声音。 |
| air_gear | array<owner_ptr> |  | 否 | 每个成员指向一个 **sound_data** 单元，定义换挡声音之一。换挡时会随机播放这些声音。 |
| air_brake | array<owner_ptr> |  | 否 | 每个成员指向一个 **sound_data** 单元，定义气动制动声音之一。松开行车制动时会随机播放这些声音。 |
| air_cutoff | array<owner_ptr> |  | **是** | 每个成员指向一个 **sound_data** 单元，定义一个在空气压缩机被调节器卸载时播放的声音。 |
| wheel_asphalt | array<owner_ptr> |  | **是** | 每个成员指向一个 **sound_noise_data** 单元，这些单元共同定义卡车在沥青路面上行驶时播放的声音。 |
| wheel_rumble | array<owner_ptr> |  | **是** | 每个成员指向一个 **sound_noise_data** 单元，这些单元共同定义卡车在震动带上行驶时播放的声音。 |
| wheel_gravel | array<owner_ptr> |  | **是** | 每个成员指向一个 **sound_noise_data** 单元，这些单元共同定义卡车在砾石路面上行驶时播放的声音。 |
| wheel_grass | array<owner_ptr> |  | **是** | 每个成员指向一个 **sound_noise_data** 单元，这些单元共同定义卡车在草地上行驶时播放的声音。 |
| aero_noise | owner_ptr |  | **是** | 指向一个 **sound_noise_data** 单元，该单元定义卡车的空气动力学噪声。 |
| gear_noise | array<owner_ptr> |  | **是** | 每个成员指向一个 **sound_data** 单元，定义齿轮损坏时的声音。 |
| gear_grind_loop | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义玩家试图挂入的挡位无法啮合时循环播放的声音（例如输入轴转速不匹配，或玩家未正确使用离合器）。 |
| seat_noise_threshold | float |  | **是** | 定义座椅悬架产生噪声所需的最小加速度（m/s<sup>2</sup>）。 |
| seat_noise | array<owner_ptr> |  | **是** |  |
| suspension_noise_threshold | float |  | **是** | 定义卡车悬架产生噪声所需的最小加速度（m/s<sup>2</sup>）。 |
| suspension_noise | array<owner_ptr> |  | **是** |  |
| lift_axle | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义卡车提升桥（如果有）升起或降下时播放的声音。 |
| horn | owner_ptr |  | 否 | 指向一个 **sound_data** 单元，定义卡车电喇叭/城市喇叭的声音。 |
| air_horn | owner_ptr |  | 否 | 指向一个 **sound_data** 单元，定义卡车气喇叭的默认声音。此声音会被任何挂接配件喇叭覆盖。如果未设置，则在没有挂接配件喇叭的情况下，卡车将没有气喇叭。 |
| reverse | owner_ptr |  | 否 | 指向一个 **sound_data** 单元，定义卡车倒车蜂鸣器的声音。 |
| air_warning | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义卡车低气压报警声音。 |
| crash_metal | array<owner_ptr> |  | **是** | 每个成员指向一个 **sound_data** 单元，这些单元共同定义 60-90 km/h 碰撞的声音。 |
| crash_hard | array<owner_ptr> |  | **是** | 每个成员指向一个 **sound_data** 单元，这些单元共同定义 30-59 km/h 碰撞的声音。 |
| crash_soft | array<owner_ptr> |  | **是** | 每个成员指向一个 **sound_data** 单元，这些单元共同定义 6-29 km/h 碰撞的声音。 |
| crash_scratch | array<owner_ptr> |  | **是** | 每个成员指向一个 **sound_data** 单元，这些单元共同定义刮擦碰撞的循环声音。 |
| blinker_on | owner_ptr |  | 否 | 指向一个 **sound_data** 单元，定义转向灯继电器闭合的声音。 |
| blinker_off | owner_ptr |  | 否 | 指向一个 **sound_data** 单元，定义转向灯继电器断开的声音。 |
| wipers_up | owner_ptr |  | 否 | 指向一个 **sound_data** 单元，定义雨刮器从停靠位置移动到伸展位置的声音。 |
| wipers_down | owner_ptr |  | 否 | 指向一个 **sound_data** 单元，定义雨刮器从伸展位置移动到停靠位置的声音。 |
| lights_stick | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义前照灯控制杆被拨动的声音。 |
| high_beam_stick | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义远光灯开关被激活的声音。 |
| light_horn_stick | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义电喇叭/城市喇叭被激活的声音。 |
| blinker_stick | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义转向灯拨杆被激活的声音。 |
| blinker_stick_off | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义转向灯拨杆被停用的声音。 |
| hazard_warning_stick | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义危险报警闪光灯/四向闪光灯控制被激活的声音。 |
| wipers_stick | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义雨刮器控制被激活的声音。 |
| retarder_stick | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义缓速器控制被激活的声音。 |
| park_brake_stick | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义驻车制动被接合的声音。 |
| park_brake_stick_off | owner_ptr |  | **是** | 指向一个 **sound_data** 单元，定义驻车制动被释放的声音。 |

## 相关单元

- [sound_data](sound%20data.md)
- [sound_engine_data](sound%20engine%20data.md)
- [sound_noise_data](sound%20noise%20data.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_sound_data | revision: 3325 | captured: 2026-10-21 23:56:14 -->
