# 文档/引擎/单元/配件车轮数据

**accessory_wheel_data** 单元类用于为大多数车辆类型定义车轮，并为[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)定义轮胎。它定义可见模型的路径、所使用的 look、是否可涂装，以及轮胎的一些物理特性（针对可驾驶车辆）。此类型的单元通常位于：

- **/def/vehicle/ai_wheel/*.sii**（用于 AI 车辆的车轮）
- **/def/vehicle/f_tire/*.sii**（可驾驶卡车的前轮胎）
- **/def/vehicle/f_wheel/*.sii**（AI 卡车的前轮）
- **/def/vehicle/r_tire/*.sii**（可驾驶卡车的后轮胎）
- **/def/vehicle/r_wheel/*.sii**（AI 卡车的后轮）
- **/def/vehicle/tr_wheel/*.sii**（挂车的车轮）
- **/def/vehicle/trailer_wheel/f_tire/*.sii**（自有挂车的前轮胎）
- **/def/vehicle/trailer_wheel/r_tire/*.sii**（自有挂车的后轮胎）

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。必需属性以**粗体**表示。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| **model** | string |  | 有效车轮模型的描述符（.pmd）路径。有效的车轮模型具有 *left* 和 *right* 两种变体，以及一个用于设置滚动/碰撞半径的 *bb* 模型定位器。 |
| look | token | default | 选择要使用的 look。 |
| paintable | boolean | false | 为 true 时，在车库、卡车浏览器等界面启用颜色选择器。涂装颜色会应用到 **model** 中材质使用 [paint](../../Tools/SCS%20Blender%20Tools/Supported%20shaders.md#paint) 特性的部件上。**注意：** 与其他配件不同，车轮配件不会继承其所属车辆的涂装颜色。 |
| default_color | float3 | (1.0, 1.0, 1.0) | 设置车轮配件的默认颜色。 |
| roll_resistance | float | 5.5 | 轮胎滚动阻力，单位为 kg/t（欧盟轮胎标签法规 1222/2009） |
| wet_grip | float | 1.0 | 轮胎湿滑路面抓地性能（欧盟轮胎标签法规 1222/2009） |
| grip_factor | float | 1.0 | 用作摩擦力乘数的抓地系数。 |
| noise_volume | float | 75.0 | 轮胎滚动噪声，单位为 dB（欧盟轮胎标签法规 1222/2009） |
| wheel_shift | float | 0.0 | 轮胎中心线相对于模型原点的偏移（基于左侧变体），用于正确生成车轮碰撞。请确保 'bb' 定位器位于轮胎外缘。 |
| sounds | array&lt;string&gt; |  | 每个条目使用“*sound_name\|sound_path*”[格式](../../../Games/ETS2/Modding%20guides/1.39.md#Accessories)为一种轮胎滚动路面材质分配一个 FMOD 事件。预期的声音事件名称为：asphalt、rumble、gravel、grass 和 snow。 |

## 卡车与客车（C3）轮胎的欧盟轮胎标签字母等级

*摘自 [ETRMA Industry Guidelines Version 4](http://www.etrma.org/uploads/Modules/Documentsmanager/2012-07-05--industry-guideline-on-tyre-labelling-(vers4).pdf)（2012 年 7 月 5 日）*

在没有数值数据的情况下，以下表格有助于将轮胎标签上的字母等级转换为用于 **roll_resistance** 和 **wet_grip** 的数值。

### 滚动阻力

| 等级 | RRC（kg/t） |
| --- | --- |
| A | RRC ≤ 4.0 |
| B | 4.1 ≤ RRC ≤ 5.0 |
| C | 5.1 ≤ RRC ≤ 6.0 |
| D | 6.1 ≤ RRC ≤ 7.0 |
| E | 7.1 ≤ RRC ≤ 8.0 |
| F | RRC ≥ 8.1 |
| G | 空 |

### 湿滑抓地

| 等级 | *G* |
| --- | --- |
| A | *G* ≥ 1.25 |
| B | 1.10 ≤ *G* ≤ 1.24 |
| C | 0.95 ≤ *G* ≤ 1.09 |
| D | 0.80 ≤ *G* ≤ 0.94 |
| E | 0.65 ≤ *G* ≤ 0.79 |
| F | *G* ≤ 0.64 |
| G | 空 |

## 根据 RPM 或 RPK 计算滚动半径

要获得正确的滚动半径以确保性能准确，可以使用轮胎制造商公布的每英里转数（RPM）或每公里转数（RPK）数据。该数据用于设置车轮模型中 *bb* 定位器的位置。

### 根据 RPM

滚动半径（米）由下式给出：

```
rrolling = 1609.34 ÷ ( RPM × 2 × π )
```

### 根据 RPK

滚动半径（米）由下式给出：

```
rrolling = 1000 ÷ ( RPK × 2 × π )
```

## 相关类

- [accessory_rim_data](accessory%20rim%20data.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_wheel_data | revision: 5787 | captured: 2026-10-21 23:56:14 -->
