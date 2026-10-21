# Documentation/Engine/Units/dynamic cargo data

**dynamic cargo data** 单元类包含与动态货物装载功能相关的所有必需数据。此类型的单元位于 **/def/vehicle/cargo/<cargo_name>/** 中，通常与 [accessory cargo data](accessory%20cargo%20data.md) 位于同一文件。这样的配件货物数据随后包含一个指向其动态货物数据的指针。

出于调试目的，最好不要让此单元保持无名。但请谨慎选择名称以避免冲突！SCS 货物的命名约定为 *dyn.cargo.data.<cargo_name>*，其中将 <cargo_name> 替换为你所添加的货物。例如 *dyn.cargo.data.potatoes_b*。

## 属性

许多属性可以省略。从 1.56 起，动态货物装载/卸载共有三种类型：

- **Particles** - 1.51 中新增的谷物漏斗车动态货物装载/卸载。对此类型，其他必需属性为 **trailer_particle**、**world_particle** 和 **material_path**。要使动态货物数据被视为正确，你必须能够装载它（world_particle）、卸载它（trailer_particle），并在挂车内的货堆网格上显示材质（material_path）。
- **Mover** - 1.52 中新增的原木挂车动态货物装载/卸载。此类型忽略所有粒子属性，并且自 1.54 起，如果支持 loading_method: cylinder，它会使用来自 [accessory cargo data](accessory%20cargo%20data.md) 的货物模型。
- **Mover_bulk** - 1.56 中新增的废金属动态货物装载/卸载。此类型使用 mover 装载货物，但挂车内部有一个网格，其增长方式与基于粒子的装载相同，只是以增量方式进行。

条目标记说明：

- p - 基于粒子的散货装载/卸载所必需。
- m - 基于 mover 的圆柱体装载/卸载所必需。
- b - 基于 mover 的散货装载所必需。

如果未标注字母，则表示该属性为可选项。

| 名称 | [类型](../Units.md#Attribute_types) | 必需 | 描述 |
| --- | --- | --- | --- |
| type | enum | pmb | 动态货物数据的类型，目前存在三种（见上文）。particles mover mover_bulk |
| trailer_particle | string | p | 动态货物卸载期间从挂车发出的粒子效果（particle_set）的[单元名称](../Units.md)。 |
| trailer_particle_night | string |  | 动态货物卸载期间从挂车发出的粒子效果的单元名称。（夜间变体） |
| impact_particle | string |  | 在装载粒子效果（world_particle）接触挂车处发出的粒子效果的单元名称。 |
| impact_particle_night | string |  | 在装载粒子效果（world_particle）接触挂车处发出的粒子效果的单元名称。（夜间变体） |
| world_particle | string | p | 动态货物装载期间从地图中的货物粒子挂接点发出的粒子效果的单元名称。 |
| world_particle_night | string |  | 动态货物装载期间从地图中的货物粒子挂接点发出的粒子效果的单元名称。（夜间变体） |
| material_path | string | pb | 用于表示挂车内货堆的网格所用材质的路径。 |
| cargo_slope_angle | float |  | 货物装入挂车时的[休止角](https://en.wikipedia.org/wiki/Angle_of_repose)。换言之，即装载时货堆的陡峭程度。*默认值：* 25.0。 |
| loading_sound | string |  | 在装载阶段/当装载机将货堆放入挂车内时，挂车在货物流触及货堆处发出的声音的路径。 |
| unloading_sound_default | string |  | 在卸载阶段/当装载机从挂车中取出货堆时，挂车在货物流离开挂车处发出的声音的路径。 |
| pile_model | string | b | 抓斗内部用作货堆的静态模型的路径。 |
| grab_types | array&lt;token&gt; | mb | 可装载/卸载此货物的抓斗名称的 token 数组。可以重复，用于定义 *variants* 属性。 |
| variants | array&lt;token&gt; | b | *pile_model* 的变体名称的 token 数组。你必须定义与 *grab_types* 数量相同的变体，从而将它们与抓斗一一对应。 |
| variant_radius | array&lt;float&gt; | b | *pile_model* 各变体的“假半径”数组。你必须定义与 *grab_types* 数量相同的变体，从而将它们与抓斗一一对应。此半径用于控制抓斗围绕货物闭合的程度，必须反复调整才能获得完美贴合。 |

##### 关于可选属性的说明

如果未定义粒子的夜间变体，则使用普通（日间）变体。

可为任何装载类型定义声音，但其行为略有不同。对于基于粒子的装载，声音会在挂车装载/卸载期间持续播放。对于基于 mover 的装载，当货物从抓斗“弹入”挂车或反向弹出时，声音只播放一次。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/dynamic_cargo_data | revision: 5732 | captured: 2026-10-21 23:56:14 -->
