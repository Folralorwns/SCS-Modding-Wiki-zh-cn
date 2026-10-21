# 文档/引擎/单元/配件卡车数据

**accessory_truck_data** 单元类定义[玩家卡车](../Game%20data/Player%20trucks%20definitions.md)的基本信息、摄像机、回退规则以及必需配件。此类型的单元定义在 **/def/vehicle/truck/<brand.model>/data.sii** 中。

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。必需属性以**粗体**表示。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| **info** | array&lt;string&gt; |  | 此成员是 accessory data 的属性。这些条目通常为 **accessory_truck_data** 定义：info[]: "@@brand_peterbilt@@" // 卡车品牌 info[]: "@@series_peterbilt_579@@" // 卡车型号 info[]: "" // 可选描述（用于轿车） info[]: "" // 可选短品牌名（例如 Mercedes 使用） info[]: "" // 可选系列/驾驶室名称（例如 Iveco Hiway 使用） *在 1.61 中调整：新增描述作为第 3 个元素，两个备用名称分别从第 3、4 个元素移到第 4、5 个元素。* |
| require | array&lt;token&gt; |  | 无论车辆配置如何都应设为必需的配件类型，应在 **accessory_truck_data** 中定义。更多信息请参见 [accessory_data](accessory%20data.md)。 |
| **behind_camera** | link_ptr |  | 用于环绕（2）视图的摄像机单元名称。通常为 `camera.behind.basic`。 |
| **interior_camera** | link_ptr |  | 用于内饰（1）视图的摄像机单元名称。通常为 `camera.interior.<brand>.<model>`。 |
| **interior_camera_oculus** | link_ptr |  | 使用头戴式显示器时，用于内饰（1）视图的摄像机单元名称。通常为 `camera.interior.<brand>.<model>.oculus`。 |
| **window_camera** | link_ptr |  | 用于车窗（5）视图的摄像机单元名称。通常为 `camera.window.basic`。 |
| **bumper_camera** | link_ptr |  | 用于保险杠（6）视图的摄像机单元名称。通常为 `camera.bumper.basic`。 |
| **cabin_camera** | link_ptr |  | 用于驾驶室顶部（4）视图的摄像机单元名称。通常为 `camera.cabin.basic`，位于当前驾驶室配件 variant 的 *cam_cabin** 定位器处。 |
| **wheel_camera** | link_ptr |  | 用于车轮（7）视图的摄像机单元名称。通常为 `camera.wheel.basic`。 |
| **top_camera** | link_ptr |  | 用于俯视（3）视图的摄像机单元名称。通常为 `camera.top.basic`。 |
| top_fixed_camera | link_ptr |  | 通常未使用。 |
| **tv_camera** | link_ptr |  | 用于电视（8）视图的摄像机单元名称。通常为 `camera.tv.basic`。 |
| predefined_tv_camera | link_ptr |  | 通常未使用。 |
| side_camera | link_ptr |  | 通常未使用。 |
| wander_camera | link_ptr |  | 用于漫游模式的摄像机单元名称。通常为 `camera.wander`。玩家通常不会遇到此模式，因为它主要用于测试。 |
| **debug_camera** | link_ptr |  | 用于开发者/飞行摄像机（0）的摄像机单元名称。通常为 `camera.debug`。 |
| **fallback** | array&lt;string&gt; |  | 每个成员包含一个特殊格式的字符串，用于定义一种配件类型（token）以及指向已定义安全回退配件的 SII 文件的相对路径。因此，`chassis` 的回退规则可能如下所示：`fallback[]: "chassis\|4x2.sii"`；如果车辆当前分配的底盘配件出现问题而变得无效或无法加载，就会调用 */def/vehicle/truck/<make.model>/chassis/4x2.sii*。accessory 文件夹中的配件处理方式有些特殊。例如，`steering_w` 的规则如下所示：`fallback[]: "accessory\|steering_w/shape1.sii"`。**注意：** 共有 15 条*必需*的回退规则：chassis、cabin、engine、transmission、f_tire、f_disc、f_hub、f_nuts、r_tire、r_disc、r_hub、r_nuts、head_light、paint_job、interior。如果卡车配有可互换的方向盘，通常建议为 steering_w 添加一条规则。 |
| use_non_wheel_pin_placement_from_model | bool |  | 若为 true，则所有定位点（车轮定位点除外）的位置和朝向直接取自车辆模型中的定位器。只有 **double_sided** 标志始终取自 ui_truck_scene_config。*在 1.61 中添加。* |
| trims | array<owner_ptr> |  | 用于车辆名称可选部分的规则列表（*trim_rule* 单元）。每个元素定义一组配件（按文件名），这些配件是给定名称部分所必需的。第一个匹配的元素决定该名称部分。*在 1.61 中添加。* |

### 定位点覆盖 *(在 1.40 中添加)*

以下数组属性用于覆盖卡车配置场景或车辆模型（通过 use_non_wheel_pin_placement_from_model 定义）中配件定位点的位置、外观和朝向。它们的用法与 ui_truck_scene_config 单元中同名的属性相同，即每个数组的一个成员用于覆盖每个定位点的行为。在 accessory_truck_data 中定义的定位点覆盖将取代 ui_truck_scene_config 中针对相应卡车的数据。

| 名称 | [类型](../Units.md#Attribute_types) | 描述 |
| --- | --- | --- |
| pin_group | array&lt;token&gt; | 每个定位点覆盖所用的配件组名称 |
| pin_look | array&lt;token&gt; | 要使用的配件定位点外观——通常为 `custom_acc` |
| pin_offset | array&lt;float3&gt; | 将配件定位点从定位器偏移的向量 |
| pin_dir | array&lt;float3&gt; | 设置定位点方向的向量（与定位器朝向无关） |
| pin_dir_uk | array&lt;float3&gt; | 设置右舵车辆定位点方向的向量（与定位器朝向无关）。此属性在 ATS 中通常省略。 |
| double_sided | array&lt;bool&gt; | 为 true 时，定位点将沿卡车的 X 轴复制并镜像。 |

在第一个示例中，*sideskirt* 配件的定位点向定位器左侧偏移 1 米（-X），并同样指向左侧（-X）。它还会绘制在定位器右侧 1 米处，并指向右侧。

```
	pin_group[]: 	sideskirt
	pin_look[]: 	custom_acc
	pin_offset[]: 	(-1, 0, 0)
	pin_dir[]: 	(-1, 0, 0)
	pin_dir_uk[]: 	(-1, 0, 0)
	double_sided[]:	true
```

在此示例中，*exhaust* 配件的定位点将绘制在定位器处（无偏移），并指向卡车左后方 45°。它还会绘制在卡车右后方 45°。这样可以使定位点从车辆两侧和后部都完全可见。

```
	pin_group[]: 	exhaust
	pin_look[]: 	custom_acc
	pin_offset[]: 	(0, 0, 0)
	pin_dir[]: 	(-1, 0, 1)
	pin_dir_uk[]: 	(-1, 0, 1)
	double_sided[]:	true
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_truck_data | revision: 5783 | captured: 2026-10-21 23:56:14 -->
