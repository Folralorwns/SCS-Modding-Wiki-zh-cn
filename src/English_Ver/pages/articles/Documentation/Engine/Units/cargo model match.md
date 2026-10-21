# Documentation/Engine/Units/cargo model match

With version 1.54 ETS2/ATS games got redefined cargo system. The **cargo_model_match** unit class is used to define the location of the cargo [accessory definition file](accessory%20cargo%20data.md) and other cargo loading/lashing related attributes so the new cargo system can load/lash cargo properly. Cargo model matches are placed inside folder `/def/vehicle/cargo/` where each cargo has its own sub-folder named by the cargo token, e.g. cargo `bricks` will have cargo model match and accessory inside `/def/vehicle/cargo/bricks/`.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| data_path | array&lt;string&gt; |  | Paths to definitions of cargo accessories with same model attributes so model that has same dimension, uses same loading type, uses same lashing type etc. Typically this is used to present models with different looks and small visual differences. Game will choose one item from the array pseudo-randomly during job generation. The unit type has to be [**accessory_cargo_data**](accessory%20cargo%20data.md). Typically, this will point to a SII file located in the same cargo folder e.g. `/def/vehicle/cargo/<cargo_name>/*.sii` |
| dimensions | float3 | (0.01, 0.01, 0.01) | Dimensions of the cargo model in meters using the format of W x H x L e.g. *(2.30, 2.63, 3.22)* |
| unit_volume_factor | float | 1.0 | Factor of the cargo unit volume that it represents. Used to distinguish different cargo model matches of the same cargo that have completely different visual and thus different ratio to the cargo unit volume defined in economy. |
| loading_method | token | none | The method the cargo will be loaded onto the trailer. **Note:** Valid loading method tokens from 1.54: *area, area_cont_20ft, area_cont_40ft, area_cont_45ft, area_cont_53ft, cont_2x20ft, area_cylinder, area_logger, auxiliary_only, bulk, custom, none* |
| lashing_method | token | none | The method used for lashing the cargo to the trailer. **Note:** Valid lashing method tokens from 1.54: *direct, top_over, none* |
| lashing_gear_type | token | none | Lashing device type to use telling the game which algorithm for lash generation it will use. **Note:** Valid lashing gear type tokens from 1.54: *chain, strap* |
| lashing_hook_angle_constraints | float3 | (90.0, 90.0, 90.0) | Angle constraint on each axis for hook on the cargo model in range between 0 and 90° from the rest placement. Beware this applies only on hooks that are placed on cargo model, so in case of `top_over` lashing method this constraint won't do anything. |

## Example SII File

This is an example of the unit class from 1.54 game files found at: `/def/vehicle/cargo/bricks/model_area.sii`

```
SiiNunit
{
cargo_model_match : .area
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
