# Documentation/Engine/Sound/Tires

### 声音 - 轮胎

本节介绍轮胎在不同路面材质上的声音。

## 轮胎声音事件

卡车轮胎和挂车轮胎的轮胎声音是分开保存的，但二者具有相同的事件和参数。<br> 目前支持 4 种路面材质，每种都有自己的声音事件：

- asphalt
- rumble
- gravel
- grass<br>

### 轮胎声音参数

声音参数：

- <name_of_event>/speed<br>参数 "speed"（km/h）控制该路面材质声音的音高和音量。
- skid_speed<br>参数 "skid_speed"（m/s）表示任一方向上车轮打滑的速度。
- note<br>参数 "note" 仅存在于 "rumble" 路面材质中。<br>它是一个频率乘数，应用于根音 G，并形成“会唱歌的路面”的旋律。

## 引擎声音配置

卡车轮胎的声音路径存储在这 4 个 soundref 中：

```
	sound/tires/rumble.soundref
	sound/tires/grass.soundref
	sound/tires/gravel.soundref
	sound/tires/asphalt.soundref
```

挂车则为这 4 个：

```
	sound/trailer/tires/rumble.soundref
	sound/trailer/tires/grass.soundref
	sound/trailer/tires/gravel.soundref
	sound/trailer/tires/asphalt.soundref
```

示例：

"sound/tires/rumble.soundref" 的内容为：

```
source="/sound/tires/tires.bank#rumble"
```

卡车的声音 bank 位置：*"/sound/tires/tires.bank"*<br> 挂车的声音 bank 位置：*"/sound/trailer/tires/tires.bank"*

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/Tires | revision: 5294 | captured: 2026-10-21 23:56:14 -->
