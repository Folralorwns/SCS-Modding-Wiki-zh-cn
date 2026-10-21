# 文档/引擎/单元/挂车线缆数据

> **注意：** 本文仍在编写中，尚未经过 SCS 员工审阅。部分信息可能不完整或不准确。

**trailer_cable_data** 单元类用于定义车辆与其挂车之间的动态挂车线缆连接。此类型的单元通常没有名称，并与 **[accessory_addon_trailer_cables_data](accessory%20addon%20trailer%20cables%20data.md)** 单元内联定义。*此单元类型在 1.31 中添加，在 1.32 之前名为 **physics_trailer_cable_data**。*

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| locator_prefix | token |  | 车辆和挂车上用于连接线缆的定位器名称。 |
| rest_locator_prefix | token |  | 车辆上用作线缆挂车端静置位置的定位器名称，在未连接挂车时使用。如果没有静置定位器，则除非线缆已连接，否则不会绘制线缆。 |
| vehicle_plug_model | string |  | 线缆车辆端所用模型的描述符（.pmd）路径。此模型将挂接到 **locator_prefix** 中定义的定位器，并朝向该定位器。如果未定义模型，线缆将直接挂接到车辆上的定位器。 |
| vehicle_plug_model_variant | token | default | 要使用的 **vehicle_plug_model** 的 variant。 |
| vehicle_plug_model_look | token | default | 要使用的 **vehicle_plug_model** 的 look。 |
| vehicle_plug_model_offset | float3 | (0.0, 0.0, 0.0) | 线缆车辆端所连接位置相对于 **vehicle_plug_model** 原点的偏移（以局部空间计）。 |
| trailer_plug_model | string |  | 线缆挂车端所用模型的描述符（.pmd）路径。当连接挂车时，此模型将挂接到 **locator_prefix** 中定义的定位器并朝向该定位器；当未连接挂车时，则挂接到 **rest_locator_prefix** 中定义的定位器。如果未定义模型，线缆将直接挂接到挂车上的定位器。 |
| trailer_plug_model_variant | token | default | 要使用的 **trailer_plug_model** 的 variant。 |
| trailer_plug_model_look | token | default | 要使用的 **trailer_plug_model** 的 look。 |
| trailer_plug_model_offset | float3 | (0.0, 0.0, 0.0) | 线缆挂车端所连接位置相对于 **trailer_plug_model** 原点的偏移（以局部空间计）。 |
| ring_count | int |  | 线缆螺旋部分的环数。（最小 2） |
| ring_resolution | int |  | 每个环的边数。（最小 3） |
| diameter | float |  | 线缆螺旋部分的直径。（最小 0.02） |
| width | float |  | 线缆本身的直径。（最小 0.001，不能超过 **diameter**） |
| straight_cable_length | float | 0 | 直线线缆的长度，单位为米，若大于零则使用。否则线缆为螺旋状。 |
| back_faces | boolean | false | 当为 true 时，会绘制直线线缆的“内侧”面。在线缆上使用透明材质时会很有用，这样线缆内壁也会可见（例如，目前交通车辆的新挂车线缆就使用了背面）。 |
| material | string | "/material/ropes/cable_white.mat" | 用于渲染线缆的材质。 |
| color | float3 | (0.5, 0.5, 0.5) | 应用于线缆模型的顶点颜色（在线性色彩空间中）。 |
| resolution | int |  | 线缆模拟的纵向分段数。（最小 2） |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/trailer_cable_data | revision: 4038 | captured: 2026-10-21 23:56:14 -->
