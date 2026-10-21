# Documentation/Engine/Sound/TruckEngine

### 声音 - 卡车发动机

卡车发动机的声音是一种非常特殊的声音。<br> 发动机声音对声源之间的平衡非常敏感。<br> <br> 因此，发动机声音有以下几条规则：

- 卡车发动机的每个声音都应位于单独的 bank 中。
- 只有四个事件，且都应实现在同一个 bank 中。
- 不建议为发动机声音混合使用不同 bank 的事件。

## 发动机声音事件

- 所有事件都应位于事件浏览器中的 "engine" 文件夹内。
- 这些事件应存在于该 bank 中：<br>**engine/engine**<br>**engine/exhaust**<br>**engine/turbo** *（自 1.39 起）*<br>**engine/start_bad**

### 事件 "engine"

事件 "engine" 播放发动机的声音。<br> 它必须是 3D 事件。该事件应路由到 "truck_engine" 音频总线。<br> 事件必须循环播放，其生命周期由 "play" 参数控制（见下文）。<br> <br> 以下事件参数必须存在：

- engine/play<br>参数 "play" 控制事件的生命周期：<br>值 play = 1 表示 - 声音正在播放<br>值 play = 0 表示 - 声音应停止
- engine/brake<br>取值范围为 <0 - 1>，表示发动机制动的动作
- engine/load<br>取值范围为 <0 - 1><br>该值表示发动机负荷<br>值 < 0.05 表示发动机怠速声音
- engine/rpm<br>取值范围为 <0 - 3000><br>该值表示发动机每秒的转数

### 事件 "exhaust"

事件 "exhaust" 播放排气的声音。<br> 它必须是 3D 事件。该事件应路由到 "truck_exhaust" 音频总线。<br> 事件必须循环播放，其生命周期由 "play" 参数控制。<br> <br> 以下事件参数必须存在：

- exhaust/load
- exhaust/play
- exhaust/rpm

这些参数的用途与 "engine" 事件相同（参见事件 "engine"）。

### 事件 "turbo"

事件 "turbo" 播放涡轮的声音。<br> 它必须是 3D 事件。该事件应路由到 "truck_turbo" 音频总线。<br> 事件必须循环播放，其生命周期由 "play" 参数控制。<br> <br> 以下事件参数必须存在：

- engine/turbo<br>取值范围为 <0 - 1>，表示涡轮系统的动作

### 事件 "start_bad"

事件 "start_bad" 播放发动机启动失败的声音。<br> 它必须是 3D 事件。该事件应路由到 "truck_engine" 音频总线。<br> 该事件是一次性声音（不循环）。<br> 该事件没有其他参数。<br> 可以使用 FMOD Studio 支持的素材随机化功能。

## 发动机声音配置

发动机声音的配置存储在 "accessory_engine_data" 数据中。<br> 数组 "sounds" 包含发动机必需事件的定义。<br> 这意味着每种类型的发动机都可以分配自己的声音 bank。<br> <br> 示例：<br> 在文件夹 "\def\vehicle\truck\peterbilt.579\engine" 中有 "Peterbilt 579" 的发动机配置文件。<br> 每个发动机都包含 *@include "sound.sui"* 文件，其中间接定义了事件：

```
	sounds: 4
	sounds[]: "engine|/def/vehicle/truck/peterbilt.579/engine/sound_engine.soundref"
	sounds[]: "exhaust|/def/vehicle/truck/peterbilt.579/engine/sound_exhaust.soundref"
	sounds[]: "start_bad|/def/vehicle/truck/peterbilt.579/engine/sound_start_bad.soundref"
	sounds[]: "turbo|/def/vehicle/truck/peterbilt.579/engine/sound_turbo.soundref"
```

每个事件都有一个 .soundref 文件，用于指定声音的 bank 和 FMOD 事件。

sound_engine.soundref 的内容为：

```
source="/sound/truck/peterbilt_579.bank#engine/engine"
```

在任意发动机配置文件中写入记录<br>sound: *"/sound/truck/peterbilt_579.bank"*<br>即可将声音 bank 分配给该发动机。

## 发动机声音位置

发动机声音的 3D 位置（默认）位于卡车第一根车桥上方 1 米处。<br> 该位置可通过 .soundref 文件修改。（参见 [声音参考文件](../Sound.md#Sound_reference_file)）

## 发动机声音示例

访问 [下载](Downloads.md) 页面以获取模板工程或声音示例。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/TruckEngine | revision: 5773 | captured: 2026-10-21 23:56:14 -->
