# 文档/引擎/单元/配件驾驶室数据

**accessory_cabin_data** 单元类配置[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)驾驶室的模型。此类型的单元位于 **/def/vehicle/truck/<brand.model>/cabin/** 中。

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| detail_model | string |  | 详细网格模型描述符（.pmd）的路径。此模型仅用于玩家使用的车辆。此外，它还用于车辆预览和浏览器窗口。 |
| model | string |  | 模型描述符（.pmd）的路径。如果只使用单个 LOD，则应将其设置为 **model**，并且不应定义其他属性（detail_model、lods）。 |
| lods | array&lt;string&gt; |  | 简化细节层级模型描述符（.pmd）的路径，按观察距离递增（模型复杂度递减）的顺序排列。 |
| collision | string |  | 碰撞描述符（.pmc）的路径。 |
| variant | token |  | 选择用于所有已定义模型/碰撞的 variant。如果驾驶室和底盘共用同一个模型（这是目前 ETS2 和 ATS 中的标准做法），则此项为必需。默认值为 *default*。**注意：** 为此 **accessory_cabin_data** 定义的所有模型都必须使用此 variant 名称。 |
| variant_uk | token |  | 选择用于右舵（RHD）车辆所有模型/碰撞的 variant。如果未设置，则默认为与 **variant** 相同的值。**注意：** 为此 **accessory_cabin_data** 定义的所有模型都必须使用此 variant 名称。 |
| look | token |  | 选择用于所有已定义模型的 look。默认值为 *default*。**注意：** 为此 **accessory_cabin_data** 定义的所有模型都必须使用此 look 名称。 |
| wiper_model | string |  | 动画雨刮器模型（.pmg）的路径。 |
| wiper_anim | resource_tie |  | 雨刮器动画（.pma）的路径。 |
| rear_wiper_anim | resource_tie |  | 后雨刮器动画（.pma）的路径。*在 1.61 中添加* |
| wiper_model_uk | string |  | 用于右舵车辆的动画雨刮器模型（.pmg）的路径。如果未设置，则默认为 **wiper_model** 的值。 |
| wiper_anim_uk | resource_tie |  | 用于右舵车辆的雨刮器动画（.pma）的路径。如果未设置，则默认为 **wiper_anim** 的值。 |
| drl_with_headlights | float | 0.0 | 设置前照灯开启时昼间行车灯的相对强度。若希望前照灯开启时昼间行车灯*关闭*，则使用值 0。若希望前照灯开启时昼间行车灯保持开启且不调暗，则使用值 1。中间值会在前照灯开启时调暗昼间行车灯，而大于 1 的值会在前照灯开启时增强昼间行车灯。ETS2 中的典型值为 0.4。 |
| suspension | bool | true | 为 true 时，启用驾驶室空气悬架的物理模拟。 |
| suspension_type | token | 4air | 如果启用了悬架，则定义驾驶室悬架的类型。可能的值为 *4air*（欧盟类型）和 *hinge2air*（美国类型）。*在 1.47 中添加* |
| sounds | array&lt;string&gt; |  | 每个条目使用“*sound_name\|sound_path*”[格式](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories)为某个功能分配一个 FMOD 事件。*在 1.39 中添加* 预期的声音事件名称为：horn、aero_noise 和 rain_noise。 |
| animation | array<owner_ptr> |  | 每个成员指向一个 [vehicle_animation_data](vehicle%20animation%20data.md) 单元的单元名称。*在 1.61 中添加* |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_cabin_data | revision: 5809 | captured: 2026-10-21 23:56:14 -->
