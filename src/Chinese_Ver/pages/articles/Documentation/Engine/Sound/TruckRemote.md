# Documentation/Engine/Sound/TruckRemote

### 声音 - 远程卡车

远程卡车的声音原则上与玩家卡车的发动机声音非常相似。<br> （请参阅 [声音 - 卡车发动机](TruckEngine.md) 以更好地理解。）<br> <br> 不过，有几点关键差异需要注意：

- 发动机声音被整合到一个事件中（通常为 remote / engine），包括排气和涡轮声音。
- 出于性能考虑，远程卡车的声音需要大幅简化。

### 事件 "(remote/)engine"

事件 "engine" 播放远程卡车的发动机声音。<br> 它必须是 3D 事件。该事件应路由到 "traffic" 音频总线。<br> 事件必须循环播放，其生命周期由 "play" 参数控制（见下文）。<br> <br> 以下事件参数必须存在：

- play<br>参数 "play" 控制事件的生命周期：<br>值 play = 1 表示 - 声音正在播放<br>值 play = 0 表示 - 声音应停止
- brake<br>取值范围为 <0 - 1>，表示发动机制动的动作
- load<br>取值范围为 <0 - 1><br>该值表示发动机负荷<br>值 < 0.05 表示发动机怠速声音
- rpm<br>取值范围为 <0 - 3000><br>该值表示发动机每秒的转数
- turbo<br>取值范围为 <0 - 1>，表示涡轮系统的动作

## 远程发动机声音配置

发动机声音的配置存储在 "accessory_engine_data" 数据中。<br> 数组 "sounds" 包含发动机必需事件的定义。<br> 这意味着每种类型的发动机都可以分配自己的声音 bank。<br> 已为远程发动机声音添加了 "remote" 项（自 1.42 版本起） <br> 示例：<br> 在文件夹 "\def\vehicle\truck\peterbilt.579\engine" 中有 "Peterbilt 579" 的发动机配置文件。<br> 每个发动机都包含 *@include "sound.sui"* 文件，其中包含事件的定义：

```
	sounds: 5
	sounds[]: "engine|/def/vehicle/truck/peterbilt.579/engine/sound_engine.soundref"
	...
	sounds[]: "remote|/def/vehicle/truck/peterbilt.579/engine/sound_engine_rm.soundref"
```

每个事件都有一个 .soundref 文件，用于指定声音的 bank 和 FMOD 事件。

sound_engine_rm.soundref 的内容为：

```
source="/sound/truck/peterbilt_579_rm.bank#remote/engine"
```

## 发动机声音示例

访问 [下载](Downloads.md) 页面以获取模板工程或声音示例。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/TruckRemote | revision: 5761 | captured: 2026-10-21 23:56:14 -->
