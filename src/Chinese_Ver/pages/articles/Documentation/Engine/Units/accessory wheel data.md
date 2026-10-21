# Documentation/Engine/Units/accessory wheel data

The **accessory_wheel_data** unit class is used to define wheels for most vehicle types, and tires for the [player's vehicle](../Game%20data/Player%20trucks%20definitions.md). It defines the path to the visible model, the look used, whether it is paintable, and some physical characteristics of the tire (for playable vehicles). Units of this type are typically found in:

- **/def/vehicle/ai_wheel/*.sii** (wheels used for AI vehicles)
- **/def/vehicle/f_tire/*.sii** (front tires for playable trucks)
- **/def/vehicle/f_wheel/*.sii** (front wheels for AI trucks)
- **/def/vehicle/r_tire/*.sii** (rear tires for playable trucks)
- **/def/vehicle/r_wheel/*.sii** (rear wheels for AI trucks)
- **/def/vehicle/tr_wheel/*.sii** (wheels for trailers)
- **/def/vehicle/trailer_wheel/f_tire/*.sii** (front tires for owned trailers)
- **/def/vehicle/trailer_wheel/r_tire/*.sii** (rear tires for owned trailers)

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md). Required attributes are **bolded**.

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| **model** | string |  | Path to the descriptor (.pmd) of a valid wheel model. Valid wheel models have *left* and *right* variants and a *bb* model locator which sets the rolling/collision radius. |
| look | token | default | Selects the look to be used. |
| paintable | boolean | false | When true, enables the color picker on the garage, truck browser, etc screens. The paint color is applied to pieces of the **model** whose materials use the [paint](../../Tools/SCS%20Blender%20Tools/Supported%20shaders.md#paint) flavor. **Note:** Unlike other accessories, wheel accessories do not inherit the paint color(s) of the vehicle they belong to. |
| default_color | float3 | (1.0, 1.0, 1.0) | Sets the default color for the wheel accessory. |
| roll_resistance | float | 5.5 | Tire rolling resistance in kg/t (EU Tyre Labelling Regulation 1222/2009) |
| wet_grip | float | 1.0 | Tire wet grip performance (EU Tyre Labelling Regulation 1222/2009) |
| grip_factor | float | 1.0 | Grip factor used as a friction multiplier. |
| noise_volume | float | 75.0 | Tire rolling noise in dB (EU Tyre Labelling Regulation 1222/2009) |
| wheel_shift | float | 0.0 | Offset of the tire centerline from the model origin (based on the left side variant) to correctly generate the wheel collision. Make sure that the 'bb' locator is positioned at the outer edge of the tire. |
| sounds | array&lt;string&gt; |  | Each item assigns an FMOD event to a tire rolling substance, using the "*sound_name\|sound_path*" [format](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories). Expected sound event names are: asphalt, rumble, gravel, grass, and snow. |

## EU Tire Label Letter Grades for Truck and Bus (C3) Tires

*From [ETRMA Industry Guidelines Version 4](http://www.etrma.org/uploads/Modules/Documentsmanager/2012-07-05--industry-guideline-on-tyre-labelling-(vers4).pdf) (5 July, 2012)*

Where numerical data is not available, the following tables are useful to translate letter grades from tire labels to the values used for **roll_resistance** and **wet_grip**.

### Rolling Resistance

| Class | RRC in kg/t |
| --- | --- |
| A | RRC ≤ 4.0 |
| B | 4.1 ≤ RRC ≤ 5.0 |
| C | 5.1 ≤ RRC ≤ 6.0 |
| D | 6.1 ≤ RRC ≤ 7.0 |
| E | 7.1 ≤ RRC ≤ 8.0 |
| F | RRC ≥ 8.1 |
| G | Empty |

### Wet Grip

| Class | *G* |
| --- | --- |
| A | *G* ≥ 1.25 |
| B | 1.10 ≤ *G* ≤ 1.24 |
| C | 0.95 ≤ *G* ≤ 1.09 |
| D | 0.80 ≤ *G* ≤ 0.94 |
| E | 0.65 ≤ *G* ≤ 0.79 |
| F | *G* ≤ 0.64 |
| G | Empty |

## Calculating Rolling Radius from RPM or RPK

To get a correct rolling radius for accurate performance, it is possible to use the Revolutions per Mile (RPM) or per Kilometer (RPK) figure published by the tire manufacturer. This is used to set the position of the *bb* locator in the wheel model.

### From RPM

The rolling radius in meters is given by:

```
rrolling = 1609.34 ÷ ( RPM × 2 × π )
```

### From RPK

The rolling radius in meters is given by:

```
rrolling = 1000 ÷ ( RPK × 2 × π )
```

## Related Classes

- [accessory_rim_data](accessory%20rim%20data.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_wheel_data | revision: 5787 | captured: 2026-10-21 23:56:14 -->
