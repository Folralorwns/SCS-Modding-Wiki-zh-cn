# 文档/引擎/单元/配件变速箱数据

**accessory_transmission_data** 单元类用于定义[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)的变速箱特性以及差速比。此类型的单元通常定义在 **/def/vehicle/truck/<brand.model>/transmission/*.sii** 中，有效的单元名称以 `.transmission` 结尾。

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| stall_torque_ratio | float | -1.0 | 如果存在液力变矩器/扭矩倍增器，则为扭矩比乘数。任何正值都会用作较低转速下扭矩的乘数。 |
| differential_ratio | float | 1.0 | 定义变速箱输出轴与车轮之间的差速/主减速比。 |
| torque_converter_lock_gear | uint | 2 | 液力变矩器（如果存在，参见 **stall_torque_ratio**）从该挡位（从 1 开始计数）起锁止。零表示液力变矩器从不锁止。 |
| transmission_class | token | heavy | 变速箱类别，用于换挡行为/声音选择。可接受的值为 **heavy** 或 **standard**；任何其他值都将默认为 **heavy**。 |
| torque_converter_crawl | bool | false | 为 true 时，允许在不踩油门的情况下利用液力变矩器（如果存在）爬行。 |
| retarder | uint | 0 | 缓速器的输出挡数（如适用）。如果为零，则该变速箱禁用缓速器行为。 |
| auxiliary_brakes | array&lt;float3&gt; |  | 设置后，将覆盖缓速器控制，使其同时控制缓速器和发动机制动。各分量为（缓速器强度、发动机制动强度、强制降挡）。retarder 的值必须与 auxiliary_brakes 的成员数量一致。*在 1.28 中添加* 例如：retarder: 5 auxiliary_brakes[]: (0.3, 0, 0) // 仅 30% 缓速器 auxiliary_brakes[]: (0.6, 0, 0) // 仅 60% 缓速器 auxiliary_brakes[]: (1.0, 0, 0) // 仅 100% 缓速器 auxiliary_brakes[]: (1.0, 1, 0) // 100% 缓速器与 100% 发动机制动 auxiliary_brakes[]: (1.0, 1, 1) // 100% 缓速器、100% 发动机制动并降挡 |
| ratios_reverse | array&lt;float&gt; |  | 按减速比递减的顺序定义倒挡传动比。这些值应为负数。例如：ratios_reverse[0]: -11.002 ratios_reverse[1]: -8.875 |
| ratios_forward | array&lt;float&gt; |  | 按减速比递减的顺序定义前进挡传动比。这些值应为正数。例如：ratios_forward[0]: 11.32 ratios_forward[1]: 9.132 ratios_forward[2]: 7.207 ...等... |
| transmission_names | owner_ptr |  | 指向一个 [transmission_names](transmission%20names.md) 类型的单元，通常为无名单元，且位于同一单元定义文件中，或通过 Serialized Unit Include（.sui）类型文件[包含](../Units.md#Includes)。此项用于为自动和顺序模式下的每个挡位分配自定义名称（这些名称会被 H 挡换挡模式定义覆盖）。 |
| auto_mode_name | string | A | 自动变速箱模式下，仪表盘显示（元素 ID 1310）中挡位编号的前缀。*在 1.35 中添加* |
| manual_mode_name | string | M | 手动变速箱模式下，仪表盘显示（元素 ID 1310）中挡位编号的前缀。*在 1.35 中添加* |
| crawls | uint | 0 | 在 UI 显示中作为爬行挡处理的 ratios_forward 数量。*在 ETS2 [1.27.2](../../../Games/ETS2/Modding%20guides/1.27.2.md#Transmission_Data) 中添加* |
| reverse_crawls | uint | 0 | 在 UI 显示中作为爬行挡处理的 ratios_reverse 数量。*在 1.60 中添加* |
| shift_time | float | 1.0 | 在自动换挡中换挡所需的时间，单位为秒。*在 1.31 中添加* |
| sounds | array&lt;string&gt; |  | 每个条目使用“*sound_name\|sound_path*”[格式](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories)为某个功能分配一个 FMOD 事件。*在 1.39 中添加* 预期的声音事件名称为：air_gear、retarder、gear_grind 和 gear_wrong。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_transmission_data | revision: 5786 | captured: 2026-10-21 23:56:14 -->
