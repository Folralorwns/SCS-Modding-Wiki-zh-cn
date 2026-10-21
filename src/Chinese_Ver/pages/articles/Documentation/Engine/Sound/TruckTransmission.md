# Documentation/Engine/Sound/TruckTransmission

## 声音 - 卡车变速箱与缓速器

卡车的下一组声音是变速箱与缓速器的声音。

### 缓速器

"retarder" 事件播放缓速器的声音。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。

该事件必须循环播放，且必须存在以下事件参数：

- retarder - 取值范围为 <0 - 1>，表示缓速器的活动程度
- trans_rpm - 取值范围为 <0 - 3000>，表示变速箱的转速

### 气动换挡（噪声）

变速箱的排气声效果。这是变速箱换挡时播放的噪声。例如欧洲电控气动 ATM 变速箱在该时刻会发出其典型声音。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。可以使用 FMOD Studio 支持的资源随机化。

这是一个简单（"one shot"）事件。

### 齿轮打齿

变速箱齿轮打齿的声音。主要用作全手动换挡时转速错误的提示。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。

该事件必须循环播放。没有参数。

### 挡位错误

变速箱挂挡不正确的声音效果。即使在自动换挡时，也用作变速箱损坏的提示。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。

这是一个简单（"one shot"）事件。

## 声音配置

该组声音配置存储在 "accessory_transmission_data" 数据中。

没有强制事件，但也没有默认事件。只有已定义的声音会被播放。存在数组 "sounds"，其内容为事件的规格说明：

- retarder
- air_gear
- gear_grind
- gear_wrong

### 示例

"Peterbilt 579" 的变速箱配置文件位于文件夹 "/def/vehicle/truck/peterbilt.579/transmission" 中。

每个配件都包含 *@include "sound.sui"* 文件，其中包含事件的间接定义：

```
	sounds[]: "retarder|/sound/truck/default/retarder.soundref"
	sounds[]: "air_gear|/sound/truck/default/effects_air_gear.soundref"
	sounds[]: "gear_grind|/sound/truck/default/effects_gear_grind.soundref"
	sounds[]: "gear_wrong|/sound/truck/default/effects_gear_wrong.soundref"
```

### 声音位置

这些声音的 3D 位置（默认）与发动机相同。<br> 该位置可由 .soundref 文件修改。（见 [声音引用文件](../Sound.md#Sound_reference_file)）

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/TruckTransmission | revision: 4799 | captured: 2026-10-21 23:56:14 -->
