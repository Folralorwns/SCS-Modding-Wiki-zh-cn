# Documentation/Engine/Units/vehicle animation data

The **vehicle_animation_data** unit class is used to define a single animation with all the necessary information needed for the animation to function properly.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| model | string |  | Path to the model descriptor (.pmd) of the animated model. *Added in 1.61* |
| anim | string |  | Path to the animation descriptor (.pma) of the animation. *Added in 1.61* |
| type | enum | ignored_anim | Determines the type of the animation, i.e., how it is handled/played in-game. Supported animation types are: suspension (animated suspension, can be used on vehicles or trailers) *Added in 1.61* ignored_anim (does nothing, only serves as a default value and a fallback) *Added in 1.61* |
| wheel_index | unsigned | 0 | Index of the that this animation belongs to, ignored for animations that don't support it. *Added in 1.61* |
| min | float | 0.0 | Value that the start of the animation corresponds to. Depending on the animation, it can be in meters, degrees or not needed at all. *Added in 1.61* |
| range | float | 1.0 | Range of the animation measured from the *min* value. Depending on the animation, it can be in meters, degrees or not needed at all. *Added in 1.61* |
| default_position | float | 0.0 | Default position that the animation is set to upon loading. Must be set with regards to *min* and *range* values. Depending on the animation, it can be in meters, degrees or not needed at all. *Added in 1.61* |
| main_bone | token |  | Token name of the bone that defines the animation motion, ignored for animations that don't need it. *Added in 1.61* |

## Animation setup guides

Guides on how to setup the animations, future animations will be added here.

### Suspension animation

#### Model setup

Suspension models are placed on the **susp_i** locator where **i** is the axle index starting from 0. These locator are to be placed in the chassis model. The suspension model should always contain the left and right suspension for a given axle and the origin should be set accordingly to the corresponding **susp_i** locator.

The most important requirement is that the animation starts at the bottom of the travel and ends at the top. The required range of motion for the suspension is described in the data definition paragraph.

There is an extra requirement when creating a suspension animation for an axle that has its type set to **axle_suspension_type[]: solidaxle**. The skeleton has to have a bone, that is located at the exact point at which the suspension contacts the axle. This ensures, that the suspension does not track the wheel, but tracks the solid axle contact point instead. The name of this bone will be needed later for the data definition.

[![Suspension_axle_contact_point.png](../../../../../../images/articles/Documentation/Engine/Units/vehicle%20animation%20data/Suspension_axle_contact_point.png)](../../../../files/Suspension%20axle%20contact%20point.png.md)

#### Data definition

Suspension animations are defined in **accessory_chassis_data** like so:

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

The animations are defined as a unit type vehicle_animation_data and are stored in the array animation[]. Here, **wheel_index** specifies the wheel, that this animation is representing. Attributes **model** and **anim** contain the paths to the model descriptor (.pmd) and the animation descriptor (.pma) files, respectively. There is a slight exception when animating suspension for a wheel that is located on an axle model (defined in **accessory_chassis_data** in **axle_model[]**). In this case, the suspension needs to be animated directly on the axle model and the **model** attribute will be ignored.

Suspension animations rely on the following attributes to be set correctly:

- min - this is the starting as well as the lowest point of the animation, it is in centimeters mesured from the wheel locator (e.g., -8.0 means that the animation is able to reach at maximum 8cm below the wheel locator),
- range - this specifies the amount of actual travel that the animation can cover measured from the lowest point up, it should be exactly the same or slightly bigger than **2 * residual_travel** (converted to cm) for that axle,
- main_bone - this parameter is critical for solid axle suspension as it specifies the exact point at which the suspension is attached to the solid axle so the suspension can track that instead of tracking the wheel itself, double wishbone and MacPherson suspension remain unaffected by this parameter.

[![Suspension_animation_limits.png](../../../../../../images/articles/Documentation/Engine/Units/vehicle%20animation%20data/Suspension_animation_limits.png)](../../../../files/Suspension%20animation%20limits.png.md)

For example, if the animation has **min = -8.0** and **range = 16.0**, then the animation will be able to track the wheel as long as it stays 8cm above or below the wheel locator.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/vehicle_animation_data | revision: 5807 | captured: 2026-10-21 23:56:14 -->
