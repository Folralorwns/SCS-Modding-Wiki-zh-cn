# Documentation/Engine/Units/sound data

**sound_data** 单元类用于定义声音。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| name | string |  | 声音片段的路径（例如 `name: "/sound/environment/timmys_ducks.ogg"`） |
| looped | bool | false | 当为 true 时，声音片段将在激活期间循环播放。当为 false 时，它将在触发时播放一次。 |
| is_2d | bool | false | 当为 true 时，声音忽略任何空间特征（位置、朝向、距离、移动）。 |
| volume | float | 1.0 | 相对于录制电平的播放音量（0.0 为完全衰减，1.0 为原样输出，2.0 为两倍响度） |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/sound_data | revision: 4187 | captured: 2026-10-21 23:56:14 -->
