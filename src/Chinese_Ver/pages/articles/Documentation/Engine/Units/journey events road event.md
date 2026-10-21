# Documentation/Engine/Units/journey events road event

**journey_events_road_event** 单元类用于定义[随机道路事件](../Random%20Road%20Events.md)。

所有过场动画属性（**start_cutscene**、**end_cutscene**、**layer_cutscenes**、**mirror_cutscenes**、**signs_cutscenes_inner** 和 **signs_cutscenes_outer**）均使用 [**journey_events_cutscene**](journey%20events%20cutscene.md) 的链接指针，将过场动画数据链接到每个随机事件。

### 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| name | string |  | 道路事件的名称（描述）。 |
| set_idx | unsigned |  | 索引，用于确定所使用的“主”属性集合，例如“最小生成距离”或“概率”（参见 /def/world/journey_road_event_master.sii）。 |
| start_cutscene | link_ptr | NULL | 道路事件的开始过场动画。 |
| end_cutscene | link_ptr | NULL | 道路事件的结束过场动画。 |
| layer_cutscenes | array<link_ptr> |  | 放置在开始与结束过场动画之间的过场动画数组。当将多种类型的过场动画彼此前后叠放时，此数组包含多个元素。例如：道路施工的第一层应为标志牌，第二层为实际施工。层的用法见下文：#道路事件的构成 |
| mirror_cutscenes | array<link_ptr> |  | 与 **layer_cutscenes** 类似，只是用于相反方向的道路。更多信息请查看 **mirror_active** 属性。 |
| layer_min_curve | array&lt;float&gt; |  | 分层过场动画允许的道路最小曲率（单位为度）。必须为 **layer_cutscenes** 数组的每一项定义。 |
| layer_max_curve | array&lt;float&gt; |  | 分层过场动画允许的道路最大曲率（单位为度）。必须为 **layer_cutscenes** 数组的每一项定义。 |
| min_length | float | -1.0 | 整个随机事件的最小长度（单位：米）。 |
| max_length | float | 10000.0 | 整个随机事件的最大长度（单位：米）。 |
| min_shoulder_space | float | -1.0 | 道路的最小路肩空间（单位：米）。与 road look 的 shoulder_space_left/shoulder_space_right 属性进行比较。 |
| max_shoulder_space | float | 100.0 | 道路的最大路肩空间（单位：米）。与 road look 的 shoulder_space_left/shoulder_space_right 属性进行比较。 |
| traffic_block | bool | false | 是否需要封闭最外侧车道？ |
| weight | float | 1.0 | 此道路事件生成概率的权重。 |
| countries | array&lt;token&gt; |  | 此道路事件允许国家的 token 数组，空数组表示无限制。使用完整名称，例如 'france'。 |
| excluded_countries | array&lt;token&gt; |  | 此道路事件排除国家的 token 数组。 |
| min_time_constraint | unsigned | 0 | 此道路事件生成所允许的最小时间（单位为一天中的游戏分钟数）。 |
| max_time_constraint | unsigned | 24 * 60 | 此道路事件生成所允许的最大时间（单位为一天中的游戏分钟数）。 |
| min_duration | unsigned | 0 | 事故的最短持续时间。即使道路已解除封闭，事故也将至少在此时间内保持激活（单位：游戏分钟）。 |
| area_tag | token | NULL | 将道路事件限制为具有特定标签的交通区域（无标签表示无限制）。 |
| slow_down_passing | bool | false | 从相邻车道经过道路事件的 AI 车辆是否应减速？ |
| centerline_displacement | bool | false | AI 车辆在经过道路事件时是否应靠近中心线行驶？ |
| bridge_forbidden | bool | false | 是否禁止此道路事件在桥梁上生成？ |
| tunnel_forbidden | bool | false | 是否禁止此道路事件在隧道中生成？ |
| left_hand_traffic | bool | false | false 表示右侧通行，true 表示左侧通行。 |
| allowed_lane_types | array&lt;token&gt; |  | 允许的车道类型数组。如果车道类型的单元名称包含此数组中的某些 token，则该车道类型被允许。空数组表示所有车道均被允许（但仍可通过 **excluded_lane_types** 数组排除）。 |
| excluded_lane_types | array&lt;token&gt; |  | 排除的车道类型数组。如果车道类型的单元名称包含数组中的某些 token，则该车道类型被排除。 |
| allowed_road_looks | array&lt;token&gt; |  | 允许的 road look 数组。以 road look 单元的后缀 token 表示。空数组表示所有 road look 均被允许。 |
| remove_map_sign | bool |  | 如果为 true，则移除地图上与道路事件重叠的冲突标志牌（限速标志）。 |
| inner_lane_allowed | bool | false | 是否允许道路事件出现在最内侧车道？ |
| center_lane_allowed | bool | false | 是否允许道路事件出现在某些中间车道？ |
| outer_lane_allowed | bool | false | 是否允许道路事件出现在最外侧车道？ |
| allowed_lanes_count | array&lt;unsigned&gt; |  | 允许的道路车道数量数组。空数组表示无限制。 |
| mirror_active | bool | false | 道路事件是否也应在相反方向生成？相反方向必须满足道路事件的所有条件。但在相反方向中将使用 **mirror_cutscenes** 而不是 **layer_cutscenes**。 |
| forward_allowed | bool | true | 是否允许道路事件在正向（nodes[0] -> nodes[1]）出现？ |
| backward_allowed | bool | true | 是否允许道路事件在反向（nodes[1] -> nodes[0]）出现？ |
| signs_cutscenes_outer | array<link_ptr> |  | 最外侧车道标志牌的过场动画数组。更多信息：[Documentation/Engine/Random Road Events#Signage](../Random%20Road%20Events.md#Signage)。 |
| signs_distances_outer | array&lt;float&gt; |  | 与 **signs_cutscenes_outer** 大小相同的数组，定义最外侧车道标志牌的距离；正值将标志牌放置在道路事件之前，负值将其放置在之后。更多信息：[Documentation/Engine/Random Road Events#Signage](../Random%20Road%20Events.md#Signage)。 |
| signs_cutscenes_inner | array<link_ptr> |  | 最内侧车道标志牌的过场动画数组。更多信息：[Documentation/Engine/Random Road Events#Signage](../Random%20Road%20Events.md#Signage)。 |
| signs_distances_inner | array&lt;float&gt; |  | 与 **signs_cutscenes_inner** 大小相同的数组，定义最内侧车道标志牌的距离；正值将标志牌放置在道路事件之前，负值将其放置在之后。更多信息：[Documentation/Engine/Random Road Events#Signage](../Random%20Road%20Events.md#Signage)。 |
| parent | link_ptr | NULL | 道路事件的父级，所有未显式定义的值均从父级继承。 |

## 道路事件的构成

[![道路事件中的层](../../../../../../images/articles/Documentation/Engine/Units/journey%20events%20road%20event/1024px-Engine_random_event_composition.jpg)](../../../../files/Engine%20random%20event%20composition.jpg.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/journey_events_road_event | revision: 5045 | captured: 2026-10-21 23:56:14 -->
