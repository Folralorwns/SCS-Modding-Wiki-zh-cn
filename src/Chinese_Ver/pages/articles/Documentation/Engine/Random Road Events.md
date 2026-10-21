# Documentation/Engine/Random Road Events

![Engine_random_event.jpg](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/400px-Engine_random_event.jpg)

*随机事件预览*

![Engine_random_event_composition.jpg](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/400px-Engine_random_event_composition.jpg)

*道路事件的构成*

道路事件（RE）是 ETS2 和 ATS 中在道路上动态生成的情境。

RE 由沿道路放置的若干过场动画定义。RE 区分 3 种过场动画：

- **起始过场动画** - RE 的第一个过场动画，每个 RE 只有一个。
- **结束过场动画** - RE 的最后一个过场动画，每个 RE 只有一个。
- **层过场动画** - 起始与结束过场动画之间的过场动画。

根据 RE 的长度以及各过场动画的长度，起始与结束过场动画之间的空间由层过场动画填充。

## 道路事件创建流程

要制作可用的道路事件，我们需要：

1. 从地图编辑器导出一个或多个过场动画 - #Cutscene export。
2. 定义步骤 1 中导出的过场动画 - #Cutscene definition。
3. 以步骤 2 中定义的过场动画单元名称的最后一个标记，定义旅程过场动画 - #Defining journey cutscenes。
4. 最后在其中定义道路事件，并链接步骤 3 中的旅程过场动画 - #Defining random events。

### 随机事件的过场动画

RE 中使用的基本元素是过场动画。过场动画是导出的地图，可被动态插入游戏。

#### 过场动画导出

过场动画从编辑器导出为标准地图 SBD 文件。但对于 RE，每个导出的过场动画都必须有一个带 ***cutscene*** 标签的 **camera_point_item**。在 RE 上放置过场动画时，该点充当过场动画的起点（位置和旋转）。

带相机点项目的 RE 过场动画示例：

[![带相机点项目的道路事件过场动画](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/800px-Engine_random_event_cutscene_origin.jpg)](../../../files/Engine%20random%20event%20cutscene%20origin.jpg.md)

> **注意：** 从示例中可以看出，相机点被放在导航线上，这是有意为之，因为 RE 的过场动画沿导航线放置。这样就能在道路上妥善设置过场动画，而无需猜测它之后会如何放置。

#### 过场动画定义

所有过场动画都在 "**/def/camera/cutscene.sii**" 中定义，并用于不同目的。

对于 RE，需要这样定义过场动画：

```
//                            ----- Cutscene token
//                           |
//                           v
cutscene_data: cutscene.acc_stop_lii
{
    objects_path: "/map/scenes/accident_stop_lights_in.sbd"
}
```

其中 **objects_path** 属性指向导出的过场动画，单元名称中的最后一个标记表示“过场动画标记”。过场动画标记（示例中为“***acc_stop_lii***”）是之后通过 **cutscene_tokens** 属性在旅程事件过场动画中收集过场动画时使用的名称：[Documentation/Engine/Units/journey_events_cutscene](Units/journey%20events%20cutscene.md)。

### 定义旅程过场动画

RE 的所有过场动画属性：**start_cutscene**、**end_cutscene**、**layer_cutscenes**、**mirror_cutscenes**、**signs_cutscenes_inner** 和 **signs_cutscenes_outer** 都使用相同的单元类型：[**journey_events_cutscene**](Units/journey%20events%20cutscene.md)，它们列在/定义在 "**/def/world/journey_cutscene.sii**" 中。

这些过场动画随后通过其单元名称链接到 RE。

**journey_cutscene.sii** 文件定义示例：

```
SiiNunit
{
# For modders: Please do not modify this file if you want to add a new entry. Create in
# this directory a new file "<base_name>.<idofyourmod>.sii" where <base_name> is name of
# base file without the extension (e.g. "city" for "/def/city.sii") and <idofyourmod> is
# some string which is unlikely to conflict with other mod.
#
# Warning: Even if the units are specified in more than one source file, they share the
# same namespace so suffixes or prefixes should be used to avoid conflicts.

journey_events_cutscene : j_cut.acc_stop_li
{
    cutscene_tokens[]:     acc_stop_li1   // Last token from unit names defined in "/def/camera/cutscene.sii"
    cutscene_tokens[]:     acc_stop_li2

    left_width:             80.0       // [m]
    right_width:            5.0        // [m]
    sequence_mode:          pseudo
}
journey_events_cutscene : j_cut.acc_mid
{
    cutscene_tokens[]:     acc_mid_1
    cutscene_tokens[]:     acc_mid_2
    cutscene_tokens[]:     acc_mid_3

    left_width:             15.0       // [m]
    right_width:            15.0       // [m]
    sequence_mode:          pseudo
}
journey_events_cutscene : j_cut.acc_plane
{
    cutscene_tokens[]:     acc_rare_1

    left_width:             35.0       // [m]
    right_width:            25.0       // [m]
    sequence_mode:          pseudo
}
}
```

#### 过场动画宽度

对于 RE，[journey_events_cutscene](Units/journey%20events%20cutscene.md) 类型的过场动画定义还会使用 **left_width** 和 **right_width** 属性，它们定义了过场动画的长度。这两个属性非常重要，因为它们决定了不同过场动画之间有多少空间、整个 RE 中能放置多少个层过场动画，以及交通阻挡物会放置在何处。

要确定左右宽度，需要：

1. 在道路的某一段上添加过场动画。
2. 在地图编辑器中旋转过场动画，使行驶方向为从右到左：<br> ![随机事件过场动画的左右宽度](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/Engine_random_event_cutscene_widths.jpg) *随机事件过场动画的左右宽度*
3. 当看到如图所示的过场动画后，使用地图编辑器中的标尺工具测量从过场动画原点向两侧的距离。
4. 在旅程事件过场动画定义中使用测量得到的宽度。

### 定义随机事件

所有 RE 都以 [**journey_events_road_event**](Units/journey%20events%20road%20event.md) 单元列表的形式存储在 "**/def/world/journey_road_event.sii**" 中。

**journey_road_event.sii** 文件定义示例：

```
SiiNunit
{
# For modders: Please do not modify this file if you want to add a new entry. Create in
# this directory a new file "<base_name>.<idofyourmod>.sii" where <base_name> is name of
# base file without the extension (e.g. "city" for "/def/city.sii") and <idofyourmod> is
# some string which is unlikely to conflict with other mod.
#
# Warning: Even if the units are specified in more than one source file, they share the
# same namespace so suffixes or prefixes should be used to avoid conflicts.

journey_events_road_event : j_re.acc_uni_p
{
    signs_distances_outer[]: 50

    layer_min_curve[]: 0.0
    layer_max_curve[]: 15.0

    max_length: 55.0
    min_length: 55.0
}
journey_events_road_event : j_re.acc_plane
{
    start_cutscene: j_cut.acc_stop_li    // From example above cutscene "j_cut.acc_stop_li" is featured as start cutscene here.
    layer_cutscenes[]: j_cut.acc_mid
    end_cutscene: j_cut.acc_plane

    min_shoulder_space: 3.0
    outer_lane_allowed: true
    centerline_displacement: true

    layer_max_curve[]: 2.0

    weight: 10.0

    parent: j_re.acc_spec_p

    name: "Accident country specific plane (1)"
}
}
```

#### 总长度

RE 的总长度定义为：

```
total_length = (distance between start cutscene placement and end cutscene placement) + (start cutscene right width) + (end cutscene left width)
```

取决于所定义的 **max/min_length**，生成 RE 时可能出现三种情况：

- **max_length** 未定义 - 起始与结束过场动画的放置方式使 **total_length** 与 RE 所占据的道路长度相同。
- **max_length** < **total_length** - 起始与结束过场动画的位置会相互靠拢，使计算出的 **total_length** 等于 **max_length**。
- **min_length** 已定义且 **min_length** > **total_length** - 不会生成 RE。

> **注意：** 在路段非常短的情况下，可能没有任何层过场动画能放入中间，因此可以用 **min_length** 来避免此情况。

> **注意：** 如果 **traffic_block** 设为 true，则 RE 前后必须有 **35m 无中断**的道路，否则事件不会生成。

#### 曲率

由于道路通常不是直的，RE 也必须能生成在弯曲道路上，这一点至关重要。这由 **layer_min_curve** 和 **layer_max_curve** 属性控制，它们必须为所有层过场动画定义（这些数组中的元素数量必须相同）。这些数值确定同一层内相邻过场动画之间允许的最小和最大曲率。

[![Engine_random_event_curvature.jpg](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/600px-Engine_random_event_curvature.jpg)](../../../files/Engine%20random%20event%20curvature.jpg.md)

上例展示了由两个路障过场动画组成的一层，以及它们放置的方向向量（蓝色箭头）。曲率随后按这些向量之间的角度计算，由此可得到最小和最大弯曲角度。

#### 标志牌

由于 RE 会改变交通流向甚至封锁车道，我们必须支持在事件前后放置警告标志牌。警告标志牌由以下属性定义：

- **signs_cutscenes_inner** 和 **signs_distances_inner** - 定义最内侧车道上的标志牌及其距离。
- **signs_cutscenes_outer** 和 **signs_distances_outer** - 定义最外侧车道上的标志牌及其距离。

在两种情况下，标志牌过场动画数组给出用于警告标志牌的过场动画，距离数组则给出它们的放置位置（这也意味着过场动画数组与距离数组的大小必须相同）。

正距离将标志牌过场动画放在道路事件之前，负距离将其放在道路事件之后（下例展示的是放置在事件之前的内侧标志牌）。因此，RE 要生成，事件前后必须有足够长的无中断道路（至少与所提供的最大距离一样长）。

[![Engine_random_event_cutscene_signs.jpg](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/800px-Engine_random_event_cutscene_signs.jpg)](../../../files/Engine%20random%20event%20cutscene%20signs.jpg.md)

#### 同步

从 **start_cutscene**、**end_cutscene** 和 **layer_cutscene** 中生成哪个过场动画的选择是相互独立的。但有时让它们之间存在一定依赖关系会很有用。因此游戏可以同步它们的选择。同步会在以下 2 种情况下发生：

1. RE 同时具有 **start_cutscene** 和 **end_cutscene**。如果这些过场动画的 **cutscene tokens** 数量相同，游戏将为它们随机选择同一个索引。
  - 此外，如果 RE 的 **layer_cutscene** 使用 **fixed** 序列模式，且其 **cutscene tokens** 数量与 **start_cutscene** 和 **end_cutscene** 的 tokens 数量相同，那么它们选定的索引也会用于该 **layer_cutscene**。
2. RE 只有 **start_cutscene** 或 **end_cutscene** 之一。如果 RE 的 **layer_cutscene** 使用 **fixed** 序列模式，且其 **cutscene tokens** 数量与 **start_cutscene** 或 **end_cutscene** 的 tokens 数量相同，那么为 **start_cutscene** 或 **end_cutscene** 选定的索引也会用于该 **layer_cutscene**。

[![Engine_random_event_sync1.png](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/1000px-Engine_random_event_sync1.png)](../../../files/Engine%20random%20event%20sync1.png.md)

[![Engine_random_event_sync2.png](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/1000px-Engine_random_event_sync2.png)](../../../files/Engine%20random%20event%20sync2.png.md)

两个 RE 变体的示例，其 **start_cutscene**、**end_cutscene** 与第一个 **layer_cutscene** 已同步。

## 另见

- [Documentation/Engine/Units/journey_events_cutscene](Units/journey%20events%20cutscene.md)
- [Documentation/Engine/Units/journey_events_road_event](Units/journey%20events%20road%20event.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Random_Road_Events | revision: 3655 | captured: 2026-10-21 23:56:14 -->
