# Documentation/Engine/Sound/SoundWorld

世界的声音系统中有几种类型的声音和声音效果：

- 3d 声音（在世界中）
- 环境音
- 混响效果
- 对象（预制件）上的 3d 声音
- 动画（mover）

### 编辑器中的声音图层

现在地图上有专门的声音图层（至 1.40 版本）。声音图层编辑器只是地图编辑器的一种特殊模式，可通过以下命令行激活：

```
eurotrucks.exe -nosingle -edit -sound
```

在声音图层中只能在地图上放置一种对象："sound item"。不过，该对象以 3 种不同模式工作：

- **3d 声音** - 显示一个圆形的声音区域，其大小由可听度限制决定。
- **环境区域** - 表示用户定义的区域，是指定环境音的来源。
- **混响区域** - 表示用户定义的区域，是混响效果的来源。

### 声音图层的配置

共有 3 个配置文件（位于 */base/def/world* 文件夹中）：

- sound_item_data.sii

```
Contains a 3d sound definition with these parameters:
sound_item_data : sound.<id token of the sound item>
{
	name: "user friendly name (editor only) in format 'sound group name/sound name' "
	sound_path: "path to the sound event"
	max_dist: maximum sound distance (should be equal to or greater than the maximum audibility of the FMOD event)
	item_color: editor item color in RGBA format (0xAABBGGRR)
}
The sound is triggered on if the actor camera is in the range of the 'sound item' object. The audibility of the sound is given only by the setting of the 3D event in FMOD.
```

- sound_item_ambient.sii

```
Contains an ambient area definition with these parameters:
sound_item_data : ambient.<id token of the ambient sound>
{
	name: "user friendly name (editor only) in format 'sound group name/sound name' "
	sound_path: "path to the sound event"
	max_dist: maximum ambient sound distance
	item_color: editor item color in RGBA format (0xAABBGGRR)
	reverb: reverb.<id token of the reverb effect - Default reverb effect for the area.>
}
The sound is triggered when the actor camera is near the area.
The area on the map represents the 'full audibility' area of the ambient sound. The sound is automatically fade in/out beyond the edge of the area depending on the 'max distance' parameter.
The default reverb effect is applied only if there is no other reverb defined in the area.
```

- sound_item_reverb.sii

```
Contains a reverb area definition with these parameters:
sound_item_reverb : reverb.<id token of the reverb effect>
{
	name: "user friendly name (editor only)"
	max_dist: maximum effect distance
	item_color: editor item color in RGBA format (0xAABBGGRR)
	ceiling: true/false If true the effect is activate only if camera is under the 'sound item' object (eg under a bridge, tunnel).
	decay_time: Decay Time: Reverberation decay time at low-frequencies in milliseconds.  Ranges from 100.0 to 20000.0. Default is 1500.
	early_delay: Early Delay: Delay time of first reflection in milliseconds.  Ranges from 0.0 to 300.0.  Default is 20.
	late_delay: Reverb Delay: Late reverberation delay time relative to first reflection in milliseconds.  Ranges from 0.0 to 100.0.  Default is 40.
	hf_reference: HF Reference: Reference frequency for high-frequency decay in Hz.  Ranges from 20.0 to 20000.0. Default is 5000.
	hf_decay_ratio: Decay HF Ratio: High-frequency decay time relative to decay time in percent.  Ranges from 10.0 to 100.0. Default is 50.
	diffusion: Diffusion: Reverberation diffusion (echo density) in percent.  Ranges from 0.0 to 100.0.  Default is 100.
	density: Density: Reverberation density (modal density) in percent.  Ranges from 0.0 to 100.0.  Default is 100.
	low_shelf_frequency: Low Shelf Frequency: Transition frequency of low-shelf filter in Hz.  Ranges from 20.0 to 1000.0. Default is 250.
	low_shelf_gain: Low Shelf Gain: Gain of low-shelf filter in dB.  Ranges from -36.0 to 12.0.  Default is 0.
	high_cut: High Cut: Cutoff frequency of low-pass filter in Hz.  Ranges from 20.0 to 20000.0. Default is 20000.
	early_late_mix: Early/Late Mix: Blend ratio of late reverb to early reflections in percent.  Ranges from 0.0 to 100.0.  Default is 50.
	wet_level: Wet Level: Reverb signal level in dB.  Ranges from -80.0 to 20.0.  Default is -6.
	dry_level: Dry Level: Dry signal level in dB.  Ranges from -80.0 to 20.0.  Default is 0.
}
The effect is activated when the actor's camera enters to the defined area. (Now independent on max distance.)
But the parameters of the reverb effect are adjusted slidingly over time.
```

*备注：如果你想添加新条目，请不要修改这些文件。请在此目录中创建新文件 "<base_name>.&lt;idofyourmod&gt;.sii"，其中 <base_name> 是不含扩展名的基础文件名（例如 "/def/city.sii" 对应的 "city"），而 &lt;idofyourmod&gt; 是某个不太可能与其他模组冲突的字符串。*

### 声音事件

（参见 [声音示例](Downloads.md)）

## 3d 声音

- 此声音事件表示来自地图上静态放置的特定声源的 3d 声音。
- 事件通常是标准 FMOD 音频 3d 事件中的无限音频循环。
- 音频可听度由 FMOD 空间化器控制。（这必须与音频配置中的 'max distance' 设置一致。）
- 全局参数可用于修改循环声音。
- 声音应为单声道（首选）或立体声采样。

*注意：在我们的示例中，使用了由 'daytime' 参数控制的餐厅声音。该示例演示了在一天中不同时段使用声音变体的方式。*

## 环境音

- 此声音事件用作世界中环境区域的声音。
- 事件通常是标准 FMOD 音频 **2d 事件**中的无限音频循环。（不包含 3d 空间化器。）
- 音频可听度由游戏控制。（完全可听音量应在 FMOD 中设置。）
- 全局参数可用于修改循环声音。
- **循环的首选格式为 5.1。**
- 循环中可以包含随机事件。
- 事件应路由到 'outside/unprocessed/ambient' 总线。

*注意：在我们的示例中，(forest_warm_con_2) 是对森林昼夜声音的模拟，包含随机事件。*

## 世界中的其他声音

为完整起见：游戏世界中还有其他声音。所有这些声音都是标准的 3d FMOD 事件，可以像 '3d sound' 事件一样创建（见上文）。

它们是：

- 分配给特定游戏对象/预制件的声音（定义于 base\unit\hookup\sound_prefab.sii）
- 分配给动画 / 'mover' 的声音（作为 mover 定义的一部分定义在 base\def\world\mover.sii 中）

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/SoundWorld | revision: 5213 | captured: 2026-10-21 23:56:14 -->
