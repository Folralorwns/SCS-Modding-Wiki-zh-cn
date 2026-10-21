# Documentation/Engine/Sound/Mixer

### 音频总线、路由与混音器

声音总线的定义及其路由是 Master Bank 中非常重要的一部分。

- 主总线<br>主总线会对所有路由到它的总线进行最终子混音，然后才将音频输出到扬声器声道。<br>所有总线、返回总线以及未分配到组的事件都会路由到主总线。
- 总线<br>总线是一种对象，用于将特定声音收集到组中，并集中控制其音量或静音状态。<br>游戏中的任何声音事件都应分配到相应的预备音频总线。
- 路由<br>通过混音器对事件和总线进行路由，有助于按组控制特定声音，并为整组声音一起应用效果（如混响）。

下表描述了我们的 Master Bank 中的混音器原则：

| 总线 | 路由到…… | 用于哪些声音…… | 备注 |
| --- | --- | --- | --- |
| master |  | *- 无 -* | 所有其他音频总线集中混音的目标。<br>"Master" 音量与静音状态（来自应用程序设置）会应用到此总线。 |
| <--- cabin | *master* | *- 无 -* |  |
| .....<--- interior | *cabin* | 单个卡车内饰声音，例如：<br>气压警告、转向灯、拨杆、驻车制动、雨刮器、车窗、座椅噪声…… |  |
| .....<--- window_left | *cabin* | *- 无 -* |  |
| .....<--- window_right | *cabin* | *- 无 -* |  |
| .....<--- window_out | *cabin* | *- 无 -* |  |
| <--- outside | *master* | *- 无 -* | 此总线不应包含任何声音。它只是在技术上用于收集来自外部世界的所有声音的组。 |
| ...<--- exterior | *outside* | *- 无 -* | 此总线不应包含任何声音。它只是在技术上用于收集所有外部声音的组。 |
| .....<--- traffic | *exterior* | 交通系统的声音。 |  |
| .....<--- trailer | *exterior* | 玩家的挂车声音。 |  |
| .....<--- truck_effects | *exterior* | 玩家的卡车效果音<br>（气压切断、气动换挡、挂钩、喇叭、倒车……）。 |  |
| .....<--- truck_engine | *exterior* | 玩家的卡车发动机。<br>（[参见：声音 - 卡车发动机](TruckEngine.md)） |  |
| .....<--- truck_exhaust | *exterior* | 玩家的卡车排气声。<br>（[参见：声音 - 卡车发动机](TruckEngine.md)） |  |
| .....<--- truck_turbo | *exterior* | 玩家的卡车涡轮声。<br>（[参见：声音 - 卡车发动机](TruckEngine.md)） |  |
| .....<--- truck_noise | *exterior* | 玩家的卡车噪声<br>（空气动力学噪声、悬架噪声……）。 |  |
| .....<--- world | *exterior* | 预制件声音、动画声音…… |  |
| ...<--- unprocessed | *outside* | *- 无 -* | 此总线不应包含任何声音。它只是在技术上用于收集所有不受声音处理（如混响）影响的外部声音的组。 |
| .....<--- ambient | *unprocessed* | 环境音与环境效果。 |  |
| <--- game | *master* | *- 无 -* |  |
| .....<--- music | *game* | 游戏内音乐（如“催促”旋律）。 |  |
| .....<--- navigation | *game* | 语音导航输出。 |  |
| .....<--- ui | *game* | 用户界面的声音<br>（点击、邮件、奖励、相机……）。 |  |
| .....<--- ui_music | *game* | UI 音乐（菜单、车库、服务……）。 |  |
| .....<--- voiceover | *game* | 保留供将来使用。 |  |
| <--- radio | *master* | 游戏内电台（用户音乐）播放器的输出。 |  |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/Mixer | revision: 5167 | captured: 2026-10-21 23:56:14 -->
