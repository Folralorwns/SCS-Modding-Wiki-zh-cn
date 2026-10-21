# 文档/引擎/单元/配件发动机数据

**accessory_engine_data** 单元类用于定义[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)的发动机特性，以及自动变速器驾驶体验中的部分升挡与降挡特性。此类型的单元通常定义在 **/def/vehicle/truck/<brand.model>/engine/*.sii** 中

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| info | array&lt;string&gt; |  | 此成员是 accessory data 的属性，不过通常为 **accessory_engine_data** 定义三个 **info** 成员。info[]: "197 @@hp@@ (147@@kw@@)" // 第一项为额定功率 info[]: "550 @@lb_ft@@ (782 @@nm@@)" // 第二项为峰值扭矩 info[]: "1@@dg@@200 @@rpm@@" // 第三项为峰值扭矩转速 **注意：** info 属性对发动机模拟没有影响。它用于 UI 显示，以及附加到 World of Trucks 的个人资料卡车上传中。**提示：** 由 *@* 包围的字符串用于本地化——`@@hp@@` 显示本地化的马力缩写，`@@dg@@` 显示本地化的千位分隔符，等等。 |
| type | token | diesel | 定义发动机、动力总成以及车辆其他一些方面的类型与行为。可接受的值为 **diesel**、**electric** 或 **petrol**。其他任何值（或未设置）都会默认为 **diesel**。*（1.50 中加入，petrol 于 1.61 加入）* |
| engine_aspiration | token | turbocharger | 发动机进气类型。可接受的值为 **natural**、**turbocharger** 或 **supercharger**。对于 **electric** 发动机，此属性会被忽略（强制为 **natural**）。 |
| torque | float | 0.0 | 定义发动机的最大扭矩输出，单位为 N·m。 |
| secondary_torque | float | 0.0 | 如果为正值且大于零，则定义多扭矩发动机的次级最大扭矩输出，单位为 N·m。*（1.30 中加入）* |
| secondary_torque_gear_ratio | float | 1.0 | 定义变速器齿轮比，低于该值时多扭矩发动机将使用 **secondary_torque**。*（1.30 中加入）* |
| torque_curve | array&lt;float2&gt; | *见描述* | 定义发动机在不同转速下的扭矩输出，相对于 **torque** 中定义的最大扭矩。如果未设置，则使用默认曲线：torque_curve[]: (300, 0) torque_curve[]: (440, 0.5) torque_curve[]: (1000, 1) torque_curve[]: (1300, 1) torque_curve[]: (1900, 0.77) torque_curve[]: (2400, 0.4) torque_curve[]: (2600, 0) 扭矩输出在数据点之间进行线性插值。对于超出数据点范围的转速，输出会被钳制到最高/最低转速点处的值。扭矩输出的有效范围为 0-1。 |
| secondary_torque_curve | array&lt;float2&gt; | *见描述* | 定义多扭矩发动机在不同转速下的次级扭矩输出，相对于 **secondary_torque** 中定义的最大扭矩。如果未设置，则改为使用 **torque_curve**。语法与 **torque_curve** 相同。*（1.30 中加入）* |
| power | float | 0 | 这是简化的定义值。仅用于 **electric** 发动机，且仅在未定义 **torque_curve** 时使用。此时会生成 **torque_curve**，从 0 rpm 到发动机输出达到给定 **power** 的转速点产生标称扭矩。在更高转速下，扭矩会逐渐降低，以便在直至最大转速的范围内将输出保持在给定 **power**。*（1.60 中加入）* |
| secondary_power | float | 0 | 这是简化的定义值。仅用于 **electric** 发动机，且仅在未定义 **secondary_torque_curve** 与 **torque_curve** 时使用。此时会生成 **secondary_torque_curve**，从 0 rpm 到发动机达到给定 **secondary_power** 的转速点产生标称扭矩。在更高转速下，扭矩会逐渐降低，以便在直至最大转速的范围内保持给定的 **secondary_power**。*（1.60 中加入）* |
| resistance_torque | float | -1 | 这是 2000rpm 时的阻力扭矩，单位为 N·m，用于被动发动机制动和燃油消耗。*（ETS 1.27/ATS 1.6 起新增）* **注意：** 当未设置，或设置为任何负值时，resistance_torque 按（*volume* × 20.0）计算。 |
| rpm_idle | float | 550 | 这是无油门输入时虚拟发动机控制器将尝试维持的发动机转速。有效范围为 500-850 rpm。 |
| rpm_limit | float | 2500 | 这是虚拟发动机控制器允许的最大发动机转速，但发动机被车轮带动的情况除外（例如车辆在下坡时失控滑行，或玩家进行了不明智的降挡）。 |
| rpm_limit_hysteresis | float | 0.0 | **rpm_limit** 限制器的迟滞（单位 RPM）。当大于零时，使用硬切断式限制器，而非默认的软限制器。不能为负值。 |
| rpm_limit_neutral | float | 2500 | 这是变速器处于空挡时虚拟发动机控制器允许的最大发动机转速——除非 **rpm_limit** 更低，此时该值会被钳制。 |
| rpm_limit_neutral_hysteresis | float | 0.0 | **rpm_limit_neutral** 限制器的迟滞（单位 RPM）。当大于零时，使用硬切断式限制器，而非默认的软限制器。不能为负值。 |
| rpm_range_low_gear | float2 | (700, 1500) | 定义低挡区内的降挡和升挡发动机转速（自动变速器）。 |
| rpm_range_high_gear | float2 | (1000, 1350) | 定义高挡区内的降挡和升挡发动机转速——通常为峰值扭矩区间（自动变速器）。*（1.38 中调整）* |
| rpm_range_power | float2 | (1400, 1900) | 在请求更大功率时定义大致的转速范围——用于坡道行驶或自适应换挡，尤其是动力模式（自动变速器）。*（1.37 中加入，1.38 中调整）* |
| *rpm_range_power_boost* | float2 | (550, 450) | *（1.37 中废弃）* 在请求更大功率时，定义对 **rpm_range_low_gear** 和 **rpm_range_high_gear** 的粗略转速范围*变化量*——用于坡道行驶或自适应换挡，尤其是动力模式。（自动变速器）。**提示：** 注意将 **rpm_range_power_boost** 加到 **rpm_range_*_gear** 后得到的结果值不要超过 **rpm_limit**，否则变速器在自适应自动模式下可能无法正确换挡。 |
| rpm_range_engine_brake | float2 | (1500, 2500) | 定义发动机制动工作时的降挡和升挡发动机转速。（自动变速器） |
| engine_brake | float | 1.0 | 发动机制动扭矩，相对于相同 **volume** 的发动机上的典型排气制动器而言。 |
| engine_brake_downshift | bool | true | 为 true 时，自动变速器会在发动机制动开始时降挡，以将转速保持在 **rpm_range_engine_brake** 范围内。为 false 时，保持常规转速。 |
| engine_brake_positions | uint | 3 | 定义发动机制动的强度级别数量。每个位置的制动扭矩基于该数量线性分配。因此对于 `engine_brake_positions: 3`，第一个位置将具有全强度的 <sup>1</sup>⁄<sub>3</sub>，第二个位置将具有全强度的 <sup>2</sup>⁄<sub>3</sub>，最高位置则具有全强度。 |
| auxiliary_brakes | array&lt;float3&gt; |  | 设置后，将覆盖发动机制动控制，使其同时控制发动机制动和缓速器（如果存在）。各分量为（发动机制动强度、强制降挡、缓速器强度）。**engine_brake_positions** 的值必须与 auxiliary_brakes 的成员数量一致。*（1.40 中加入）* 例如：engine_brake_positions: 5 auxiliary_brakes[]: (0.3, 0, 0) // 仅 30% 发动机制动 auxiliary_brakes[]: (0.6, 0, 0) // 仅 60% 发动机制动 auxiliary_brakes[]: (1.0, 0, 0) // 仅 100% 发动机制动 auxiliary_brakes[]: (1.0, 1, 0) // 100% 发动机制动并降挡 auxiliary_brakes[]: (1.0, 1, 1) // 100% 发动机制动、降挡以及 100% 缓速器 |
| volume | float | 0.0 | 发动机的排量，单位为升。用于基础燃油消耗计算、发动机质量与惯性计算，以及默认的 **resistance_torque** 计算。可接受的最小发动机排量为 0.8。 |
| consumption_coef | float | 1.0 | 用于相对于游戏计算值缩放发动机的燃油消耗。 |
| cold_start_rpm | float | *见描述* | 发动机冷态（约 20°C）时的怠速转速。如果未设置（负值），则默认为 **rpm_idle**。不能低于 **rpm_idle**。*（1.61 中加入）* |
| flywheel_inertia | float | *见描述* | 发动机飞轮的惯性，单位为 kg·m²。如果未设置（负值），则根据 **volume** 估算。*（1.61 中加入）* |
| adblue_consumption | float | 0.05 | 每消耗一升燃油所消耗的 AdBlue（柴油机尾气处理液）升数。**提示：** 对于不使用 AdBlue 的较旧发动机，此属性应设置为 0。 |
| no_adblue_power_limit | float | 1.0 | 当 AdBlue 罐为空时，发动机功率会按此系数缩放。 |
| sound | string |  | 卡车[发动机声音库](../Sound/TruckEngine.md)的路径（格式如 "/sound/truck/engine.bank"）。*（已废弃，由 **sounds** 取代。1.39 中移除。）* |
| sounds | array&lt;string&gt; |  | 每一项使用“*sound_name\|sound_path*” [格式](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories)将 FMOD 事件分配给一个发动机功能。*（1.39 中加入）* 预期的声音事件名称为：engine、exhaust、exhaust_ignite、start_bad 和 turbo。 |
| sound_location_engine | token | front | 发动机声源相对于车辆的位置。可接受的值为 **front** 或 **rear**；其他任何值都会默认为 **front**。 |
| sound_location_exhaust | token | front | 排气声源相对于车辆的位置。可接受的值为 **front** 或 **rear**；其他任何值都会默认为 **front**。 |

## 相关单位换算与公式

### 立方英寸转换为升

1 cu·in = 0.0164 L

### 磅-英尺转换为牛顿-米

1 lb<sub>f</sub>·ft = 1.3558 N·m

### 马力转换为千瓦

1 hp = 0.7457 kW

### 由功率和转速计算扭矩（公制单位）

T [N·m] = ( P [kW] × 9549 ) ÷ N [RPM]

### 由功率和转速计算扭矩（英制单位）

T [lb<sub>f</sub>·ft] = ( P [hp] × 5252 ) ÷ N [RPM]

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_engine_data | revision: 5792 | captured: 2026-10-21 23:56:14 -->
