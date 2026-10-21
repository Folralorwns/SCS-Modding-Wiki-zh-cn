# 文档/引擎/单元/配件轮辋数据

**accessory_rim_data** 单元类用于为[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)定义车轮（轮辋）、轮毂、螺母和轮罩。它定义可见模型的路径、所使用的 look、是否可涂装，以及轮胎相对于默认位置的水平偏移量。此类型的单元通常位于：

- **/def/vehicle/f_cover/*.sii**（可驾驶卡车的前轮毂罩）→ 有效的单元名称为 `*.fcover`
- **/def/vehicle/f_disc/*.sii**（可驾驶卡车的前轮）→ 有效的单元名称为 `*.fdisc`
- **/def/vehicle/f_hub/*.sii**（可驾驶卡车的前轮毂）→ 有效的单元名称为 `*.fhub`
- **/def/vehicle/f_nuts/*.sii**（可驾驶卡车的前螺母）→ 有效的单元名称为 `*.fnuts`
- **/def/vehicle/r_cover/*.sii**（可驾驶卡车的后轮毂罩）→ 有效的单元名称为 `*.rcover`
- **/def/vehicle/r_disc/*.sii**（可驾驶卡车的后轮）→ 有效的单元名称为 `*.rdisc`
- **/def/vehicle/r_hub/*.sii**（可驾驶卡车的后轮毂）→ 有效的单元名称为 `*.rhub`
- **/def/vehicle/r_nuts/*.sii**（可驾驶卡车的后螺母）→ 有效的单元名称为 `*.rnuts`

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。必需的属性以**粗体**表示。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| **model** | string |  | 有效轮辋模型的模型描述符（.pmd）路径。有效的轮辋模型具有 *left* 和 *right* 变体。 |
| look | token | default | 所用 look 的名称。 |
| tire_shift | float | 0.0 | 轮胎模型向车辆中心线偏移的距离（米）。仅应为 **fdisc** 和 **rdisc** 类型的配件定义此项。 |
| paintable | boolean | false | 为 true 时，在车库、卡车浏览器等界面启用颜色选择器。涂装颜色会应用到 **model** 中材质使用 [paint](../../Tools/SCS%20Blender%20Tools/Supported%20shaders.md#paint) 特性的部件上。**注意：** 与其他配件不同，轮辋配件不会继承其所属车辆的涂装颜色。每个实例可以有自己的涂装颜色。 |
| default_color | float3 | (1.0, 1.0, 1.0) | 设置轮辋配件的默认颜色。 |

## 相关类

- [accessory_wheel_data](accessory%20wheel%20data.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_rim_data | revision: 3266 | captured: 2026-10-21 23:56:14 -->
