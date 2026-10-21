# Documentation/Engine/Detours

![Engine_detour1.jpg](../../../../../images/articles/Documentation/Engine/Detours/512px-Engine_detour1.jpg)

*绕行预览 1*

![Engine_detour2.jpg](../../../../../images/articles/Documentation/Engine/Detours/512px-Engine_detour2.jpg)

*绕行预览 2*

绕行（DE）是动态生成的情境，会导致整条道路封闭。

DE 由程序化生成，无需为特定绕行定义专门的数据。你唯一需要提供的数据是用于道路封闭、路障以及绕行起因事件的过场动画。

## 工作原理

生成绕行必须满足若干条件。

- 玩家必须接取离线任务。
- 距上次绕行必须已过去足够长的时间。
- 任务的 GPS 路线必须包含适合封闭的道路。

当玩家接取离线任务时，游戏会分析找到的 GPS 路线，若发现任何有效的绕行，便会选择它。当存在多个有效绕行时，游戏会随机选择其中一个。

你可能已经注意到这里没有提到过场动画。这是因为分析算法不会考虑所提供的用于封闭可视化的过场动画（出于性能原因）。过场动画会在玩家接近封闭处时生成，并且只有在这时游戏才会查找合适的过场动画。

## 数据单元

与道路事件类似，绕行使用一个主单元来描述该功能的总体行为，然后使用若干单元来描述不同车道和道路上的封闭与事件可视化。

### 主数据单元

此类型只能有一个单元。它位于 **/def/world/journey_detour_master.sii**

```
SiiNunit
{
journey_events_detour_data : .master
{
    min_game_time_delay:	2400		// 4 (hours) * 60 (hour2min) * 20 (map scale) / 2 (some time spend in city)
    max_game_time_delay:	4800		// 8 (hours) * 60 (hour2min) * 20 (map scale) / 2 (some time spend in city)
    minimal_level:              2
}
}
```

属性：

- **min_game_time_delay** 距上次绕行的最短游戏时间。若距上次绕行的时间低于此属性，则不会生成绕行。
- **max_game_time_delay** 距上次绕行的最长游戏时间。若距上次绕行的时间大于此属性，则总会生成绕行。（前提是其他条件也满足）
- **minimal_level** 生成绕行所需的最低等级。

其余情况是距上次绕行的时间介于 **min_game_time_delay** 与 **max_game_time_delay** 之间。此时，绕行将按与这些时间之间**一次**绕行的均匀分布相对应的概率生成。

### 绕行数据单元

这些单元定义绕行可视化的各个部分将使用哪个过场动画。

位于 **/def/world/journey_detours.sii** 的绕行数据单元示例

```
journey_events_detour : j_dt.1_cl_ri1
{
	cutscene:		j_cut.1_cl_ri1
	lane_idx:		1
	lane_count:		1
	type:			road_block_right
}
```

属性：

- **cutscene** 使用的过场动画。见下文。
- **type** 可视化类型。
  - ***closed_road*** 绕行的源头。该过场动画将在绕行起点处生成。（绕行预览 2 图中的**第 4 辆车**（车辆））
  - ***border_prefab_node*** 这些过场动画将生成在每一个封闭预制件（交通被改道的预制件）与封闭道路之间。（绕行预览 2 图中的**第 3 辆车**）
  - ***road_block_right*** 这些过场动画将生成在封闭预制件之前的封闭车道上。交通从左侧绕行。
  - ***road_block_left*** 这些过场动画将生成在封闭预制件之前的封闭车道上。交通从右侧绕行。（绕行预览 2 图中的**第 1 辆**（*lane_idx* = 2）**车**和**第 2 辆**（*lane_idx* = 1）**车**）
- **lane_count** 过场动画只会在车道数为此数值的道路上生成。
- **lane_idx** 仅对 *road_block_* 类型有效。仅当到最近空闲车道的距离与此数值相同时，才会为该路障生成过场动画。

### 过场动画数据单元

由于 DE 属于旅程事件框架的一部分，它们使用与随机道路事件相同的过场动画单元。可在此处查看过场动画单元的详细说明：[Documentation/Engine/Random Road Events#Cutscenes_for_random_events](Random%20Road%20Events.md#Cutscenes_for_random_events)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Detours | revision: 5312 | captured: 2026-10-21 23:56:14 -->
