# 文档/引擎/单元/车辆动画数据

**vehicle_animation_data** 单元类用于定义单个动画，并包含动画正常运行所需的全部必要信息。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| model | string |  | 动画模型的模型描述符（.pmd）路径。*在 1.61 中添加* |
| anim | string |  | 动画的动画描述符（.pma）路径。*在 1.61 中添加* |
| type | enum | ignored_anim | 决定动画的类型，即在游戏内如何处理/播放动画。支持的动画类型有：suspension（动画悬挂，可用于车辆或挂车）*在 1.61 中添加* ignored_anim（不做任何事，仅作为默认值和回退值）*在 1.61 中添加* |
| wheel_index | unsigned | 0 | 此动画所属车轮的索引，对于不支持该属性的动画将被忽略。*在 1.61 中添加* |
| min | float | 0.0 | 动画起点所对应的值。取决于动画类型，单位可以是米、度，或根本不需要。*在 1.61 中添加* |
| range | float | 1.0 | 从 *min* 值起算的动画范围。取决于动画类型，单位可以是米、度，或根本不需要。*在 1.61 中添加* |
| default_position | float | 0.0 | 加载时为动画设置的默认位置。必须参照 *min* 和 *range* 值来设置。取决于动画类型，单位可以是米、度，或根本不需要。*在 1.61 中添加* |
| main_bone | token |  | 定义动画运动的骨骼的 token 名称，对于不需要它的动画将被忽略。*在 1.61 中添加* |

## 动画设置指南

关于如何设置这些动画的指南，日后将在此处添加更多动画。

### 悬挂动画

#### 模型设置

悬挂模型放置在 **susp_i** 定位器上，其中 **i** 是从 0 开始的车轴索引。这些定位器需放置在底盘模型中。给定车轴的悬挂模型应始终同时包含左侧和右侧悬挂，并且原点应相应设置为对应的 **susp_i** 定位器。

最重要的要求是动画从行程底部开始，到顶部结束。悬挂所需的运动范围将在数据定义部分中说明。

当为类型设置为 **axle_suspension_type[]: solidaxle** 的车轴创建悬挂动画时，还有一个额外要求。骨架必须包含一根骨骼，其位置正好在悬挂与车轴接触的点上。这可以确保悬挂不跟随车轮，而是跟随整体式车轴的接触点。该骨骼的名称稍后将在数据定义中用到。

[![Suspension_axle_contact_point.png](../../../../../../images/articles/Documentation/Engine/Units/vehicle%20animation%20data/Suspension_axle_contact_point.png)](../../../../files/Suspension%20axle%20contact%20point.png.md)

#### 数据定义

悬挂动画在 **accessory_chassis_data** 中如下定义：

```
SiiNunit
{	#start of SiiNunit global scope

#Example car uses suspension type wishbone/macpherson type for first axle, solidaxle for the second.
accessory_chassis_data : my.car.chassis
{
    ...
    animation[]: .susp_0
	animation[]: .susp_1
	animation[]: .susp_2
	animation[]: .susp_3
	...
}

vehicle_animation_data: .susp_0
{
	type: suspension
	wheel_index: 0
	model: "/vehicle/car/the_car/chassis/susp_0.pmd"
	anim: "/vehicle/car/the_car/chassis/susp_0_left_anim.pma"
	min: -11.0
	range: 22.0
}
vehicle_animation_data: .susp_1
{
	type: suspension
	wheel_index: 1
	model: "/vehicle/car/the_car/chassis/susp_0.pmd"
	anim: "/vehicle/car/the_car/chassis/susp_0_right_anim.pma"
	min: -11.0
	range: 22.0
}
vehicle_animation_data: .susp_2
{
	type: suspension
	wheel_index: 2
	model: "/vehicle/car/the_car/chassis/susp_1.pmd"
	anim: "/vehicle/car/the_car/chassis/susp_1_left_anim.pma"
	min: -11.0
	range: 22.0
	main_bone: axle_l
}
vehicle_animation_data: .susp_3
{
	type: suspension
	wheel_index: 3
	model: "/vehicle/car/the_car/chassis/susp_1.pmd"
	anim: "/vehicle/car/the_car/chassis/susp_1_right_anim.pma"
	min: -11.0
	range: 22.0
	main_bone: axle_r
}
}	#end of SiiNunit global scope
```

这些动画定义为 vehicle_animation_data 类型的单元，并存储在 animation[] 数组中。其中，**wheel_index** 指定此动画所代表的车轮。属性 **model** 和 **anim** 分别包含模型描述符（.pmd）和动画描述符（.pma）文件的路径。当为位于车轴模型上的车轮制作悬挂动画时（车轴模型在 **accessory_chassis_data** 的 **axle_model[]** 中定义），存在一个小的例外。在这种情况下，悬挂需要直接在车轴模型上制作动画，并且 **model** 属性将被忽略。

悬挂动画依赖以下属性被正确设置：

- min——这是动画的起点，也是最低点，以厘米为单位从车轮定位器算起（例如，-8.0 表示动画最多能到达车轮定位器下方 8cm 处），
- range——指定动画从最低点向上算起所能覆盖的实际行程量，它应恰好等于或略大于该车轴的 **2 * residual_travel**（转换为 cm），
- main_bone——此参数对整体式车轴悬挂至关重要，因为它指定悬挂与整体式车轴连接的确切点，使悬挂可以跟随该点而非跟随车轮本身；双横臂式和麦弗逊式悬挂不受此参数影响。

[![Suspension_animation_limits.png](../../../../../../images/articles/Documentation/Engine/Units/vehicle%20animation%20data/Suspension_animation_limits.png)](../../../../files/Suspension%20animation%20limits.png.md)

例如，如果动画的 **min = -8.0** 且 **range = 16.0**，那么只要车轮保持在定位器上方或下方 8cm 以内，动画就能跟随车轮。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/vehicle_animation_data | revision: 5807 | captured: 2026-10-21 23:56:14 -->
