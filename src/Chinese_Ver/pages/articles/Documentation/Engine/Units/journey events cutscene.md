# Documentation/Engine/Units/journey events cutscene

**journey events cutscene** 单元类用于为[随机道路事件](../Random%20Road%20Events.md)定义过场动画。

此单元汇集多个过场动画，并将它们与本单元的属性绑定。因此，具有相同辅助数据的过场动画可以定义在一个 journey events cutscene 单元中，这使得更多图形变体能够包装在同一个 journey events cutscene 之下。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| cutscene_tokens | array&lt;token&gt; |  | 此单元应汇集的所有过场动画的 token 名称数组（token 名称通过单元名称的最后一个 token 与“**/def/camera/cutscene.sii**”中定义的过场动画相匹配）。 |
| left_width | float | -1.0 | 由给定 token 名称汇集的过场动画左侧的宽度。更多信息：[Documentation/Engine/Random_Road_Events#Cutscene_width](../Random%20Road%20Events.md#Cutscene_width)。 |
| right_width | float | -1.0 | 由给定 token 名称汇集的过场动画右侧的宽度。更多信息：[Documentation/Engine/Random_Road_Events#Cutscene_width](../Random%20Road%20Events.md#Cutscene_width)。 |
| sequence_mode | int | simple | 如果此过场动画数据汇集了多个过场动画，游戏将如何选择过场动画 token。**simple** - 序列中的每个过场动画（当多个 layer_cutscenes 前后放置时）均被随机且独立地选择。**pseudo** - 序列中的每个过场动画（当多个 layer_cutscenes 前后放置时）按如下方式选择：每个 N 元组（其中 N 为 token 名称汇集的过场动画数量）以随机顺序包含所有过场动画。**fixed** - 整个序列只使用一个随机的过场动画。 |
| lane_height | float | -1.0 | 由 token 名称汇集的过场动画的高度。值 >= 0.0 表示可以在与车道方向垂直的方向上应用随机偏移（如果有足够空间） |
| align_buildings | bool | false | 建筑物是否应与可行驶曲线对齐？为 true 时，所有建筑节点与曲线的距离都等于其与过场动画原点的 X 轴距离。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/journey_events_cutscene | revision: 3880 | captured: 2026-10-21 23:56:14 -->
