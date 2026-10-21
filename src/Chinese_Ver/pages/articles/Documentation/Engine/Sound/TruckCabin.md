# Documentation/Engine/Sound/TruckCabin

## 声音 - 卡车驾驶室

另一组卡车声音是与卡车驾驶室相关的声音。

### 喇叭

喇叭的声音。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。事件必须循环播放。此声音的 3D 位置（默认）为卡车模型的坐标原点。

### 气喇叭

气喇叭的声音。它必须是 3D 事件。该事件应路由到 "truck_effects" 音频总线。事件必须循环播放。此声音的 3D 位置（默认）位于卡车模型坐标原点上方 1 米处。

### 气动噪声

气流绕过驾驶室时产生的噪声。它必须是 3D 事件。该事件应路由到 "truck_noise" 音频总线。事件必须循环播放。

以下事件参数必须存在：

- aero_speed - 取值范围为 <0 - 200>，表示流动空气的速度（单位为 km/h）
- aero_wnd - 取值范围为 <0 - 2>，表示车窗的状态：
  - 0 ... 效果已禁用
  - (0 - 1> ... 车窗开度的指示值（状态）
  - 2 ... 摄像机位于驾驶室外部

游戏中该事件有两个实例。每个实例分别位于（左侧 / 右侧）车窗附近。每个实例的参数相互独立。

### 雨声

雨滴落在卡车驾驶室上的音效。它必须是 3D 事件。该事件应路由到 "truck_noise" 音频总线。事件必须循环播放。

以下事件参数必须存在：

- rain_int - 取值范围为 <0 - 1>，表示相对的降雨强度

此声音的 3D 位置（默认）位于驾驶室内。

## 声音配置

该组声音的配置存储在 "accessory_cabin_data" 数据中。

没有强制事件，但也没有默认事件。只会播放已定义的声音。数组 "sounds" 包含事件的定义：

- horn
- air_horn
- aero_noise
- rain_noise

### 示例

在文件夹 "/def/vehicle/truck/peterbilt.579/cabin" 中有 "Peterbilt 579" 的底盘配置文件。

每个配件都包含 *@include "sound.sui"* 文件，该文件间接定义了事件：

```
	sounds[]: "horn|/sound/truck/horn/horn_01.soundref"
	sounds[]: "air_horn|/sound/truck/air_horn/air_horn_04.soundref"
	sounds[]: "aero_noise|/sound/truck/default/noise_aero.soundref"
	sounds[]: "rain_noise|/sound/truck/default/noise_rain.soundref"
```

### 声音位置

声音位置可通过 .soundref 文件修改。（参见 [声音参考文件](../Sound.md#Sound_reference_file)）

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/TruckCabin | revision: 4805 | captured: 2026-10-21 23:56:14 -->
