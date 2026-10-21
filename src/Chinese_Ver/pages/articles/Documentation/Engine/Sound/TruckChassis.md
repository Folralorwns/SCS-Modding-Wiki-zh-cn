# Documentation/Engine/Sound/TruckChassis

## 声音 - 卡车底盘

另一组卡车声音是与卡车底盘相关的声音。

### 空气制动

制动排气音效。松开行车制动时会随机播放。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。这是一个简单的（"one shot"）事件。建议使用 FMOD Studio 支持的素材随机化功能。

以下事件参数必须存在：

- air_pressure - 取值范围为 <0 - 1>，表示空气系统的相对压力

### 空气切断

空气切断音效。当调压器使空气压缩机卸载时播放的声音。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。这是一个简单的（"one shot"）事件。建议使用 FMOD Studio 支持的素材随机化功能。

### 倒车

倒车提示音。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。事件必须循环播放。

### 提升桥

提升桥的音效。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。事件必须循环播放，也可以是 "one shot" 声音，但长度要足够。

### 挂钩连接

连接挂钩的音效。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。这是一个简单的（"one shot"）事件。

### 挂钩分离

分离挂钩的音效。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。这是一个简单的（"one shot"）事件。

### 挂车线缆

连接挂车线缆的音效。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。这是一个简单的（"one shot"）事件。

## 声音配置

该组声音的配置存储在 "accessory_chassis_data" 数据中。

没有强制事件，但也没有默认事件。只会播放已定义的声音。数组 "sounds" 包含事件的定义：

- air_brake
- air_cutoff
- reverse
- lift_axle
- hook_attach
- hook_detach
- trailer_cables

### 示例

在文件夹 "/def/vehicle/truck/peterbilt.579/chassis" 中有 "Peterbilt 579" 的底盘配置文件。

每个配件都包含 *@include "sound.sui"* 文件，该文件间接定义了事件：

```
	sounds[]: "air_brake|/sound/truck/default/effects_air_brake.soundref"
	sounds[]: "air_cutoff|/sound/truck/default/effects_air_cutoff.soundref"
	sounds[]: "reverse|/sound/truck/default/effects_reverse.soundref"
	sounds[]: "lift_axle|/sound/truck/default/effects_lift_axle.soundref"
	sounds[]: "hook_attach|/sound/truck/default/effects_hook_attach.soundref"
	sounds[]: "hook_detach|/sound/truck/default/effects_hook_detach.soundref"
	sounds[]: "trailer_cables|/sound/truck/default/effects_trailer_cables.soundref"
```

### 声音位置

此声音的 3D 位置（默认）与发动机相同。<br> 该位置可通过 .soundref 文件修改。（参见 [声音参考文件](../Sound.md#Sound_reference_file)）

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/TruckChassis | revision: 5613 | captured: 2026-10-21 23:56:14 -->
