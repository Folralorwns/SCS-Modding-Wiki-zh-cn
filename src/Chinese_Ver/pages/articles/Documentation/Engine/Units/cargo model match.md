# 文档/引擎/单元/货物模型匹配

在 1.54 版本中，ETS2/ATS 游戏重新定义了货物系统。**cargo_model_match** 单元类用于定义货物[配件定义文件](accessory%20cargo%20data.md)的位置以及其他与货物装载/捆扎相关的属性，以便新的货物系统能够正确装载/捆扎货物。货物模型匹配文件放置在 `/def/vehicle/cargo/` 文件夹中，每种货物都有以货物 token 命名的子文件夹，例如货物 `bricks` 的货物模型匹配和配件位于 `/def/vehicle/cargo/bricks/` 中。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| data_path | array&lt;string&gt; |  | 指向模型属性相同的货物配件定义的路径，这些模型具有相同尺寸、使用相同装载类型、使用相同捆扎类型等。通常用于呈现具有不同 look 和细小视觉差异的模型。游戏在生成任务时会从数组中伪随机选择一个条目。单元类型必须为 [**accessory_cargo_data**](accessory%20cargo%20data.md)。通常，这会指向位于同一货物文件夹中的 SII 文件，例如 `/def/vehicle/cargo/<cargo_name>/*.sii` |
| dimensions | float3 | (0.01, 0.01, 0.01) | 货物模型的尺寸，单位为米，格式为宽 x 高 x 长，例如 *(2.30, 2.63, 3.22)* |
| unit_volume_factor | float | 1.0 | 此模型对应的货物单位体积系数。用于区分同一货物的不同货物模型匹配，这些模型外观完全不同，因而与 economy 中定义的货物单位体积之比也不同。 |
| loading_method | token | none | 将货物装载到挂车上的方式。**注意：** 从 1.54 起有效的装载方式 token：*area, area_cont_20ft, area_cont_40ft, area_cont_45ft, area_cont_53ft, cont_2x20ft, area_cylinder, area_logger, auxiliary_only, bulk, custom, none* |
| lashing_method | token | none | 用于将货物捆扎到挂车上的方式。**注意：** 从 1.54 起有效的捆扎方式 token：*direct, top_over, none* |
| lashing_gear_type | token | none | 要使用的捆扎装置类型，用于告知游戏将使用哪种捆扎生成算法。**注意：** 从 1.54 起有效的捆扎装置类型 token：*chain, strap* |
| lashing_hook_angle_constraints | float3 | (90.0, 90.0, 90.0) | 货物模型上挂钩在各轴上的角度约束，范围为相对于静止放置位置的 0 至 90°。请注意，此约束仅适用于放置在货物模型上的挂钩，因此对于 `top_over` 捆扎方式，此约束不会产生任何效果。 |

## 示例 SII 文件

以下是 1.54 游戏文件中该单元类的示例，位于：`/def/vehicle/cargo/bricks/model_area.sii`

```
SiiNunit
{
cargo_model_match : .area
{
	data_path[]: "/def/vehicle/cargo/bricks/accessory_bricks.sii"

	dimensions: (1.19, 0.97, 0.80)

	loading_method: area
	lashing_method: top_over
	lashing_gear_type: strap
}
}
‎
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/cargo_model_match | revision: 5737 | captured: 2026-10-21 23:56:14 -->
