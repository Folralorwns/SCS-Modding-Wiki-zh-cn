# Documentation/Engine/Units/sound engine data

**sound_engine_data** 单元类用于定义发动机声音。此单元通常用于数组中，各成员之间的 *min_rpm* 和 *max_rpm* 范围相互重叠，以实现交叉淡化。

## 用途

- [accessory_sound_data](accessory%20sound%20data.md)（engine、engine_load、engine_nofuel、engine_exhaust、engine_brake）

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| name | string |  | 声音片段的路径（例如 `name: "/sound/truck/default/int/unloaded_1.ogg"`） |
| looped | bool | false | 当为 true 时，声音片段将在激活期间循环播放。当为 false 时，它将在触发时播放一次。对于发动机声音应始终为 true。 |
| is_2d | bool | false |  |
| volume | float | 0.0 | 相对于录制电平的播放音量（0.0 为完全衰减，1.0 为原样输出，2.0 为两倍响度） |
| pitch_reference | float | 0.0 | 录音的参考发动机转速。 |
| min_rpm | float | 0.0 | 播放此片段的最低转速。 |
| max_rpm | float | 0.0 | 播放此片段的最高转速。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/sound_engine_data | revision: 3275 | captured: 2026-10-21 23:56:14 -->
