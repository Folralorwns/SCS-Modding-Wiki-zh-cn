# Documentation/Engine/Sound

> **注意：** **声音系统与当前页面处于"开发中"状态。我们将持续更新站点内容和音频数据结构。**

## FMOD®

FMOD® 系统现在（从 1.37 版本起）作为游戏中的核心声音引擎使用。<br> 你应根据游戏版本选择使用的 FMOD® Studio 版本，可在[此处](Sound/Downloads.md)找到。

*参阅 FMOD 文档（[www.fmod.com](http://www.fmod.com)）以更好地理解声音系统。*

## 声音与声音库

每个声音都由声音 **事件** 表示。事件是 FMOD Studio 项目中可实例化的声音单元。所有声音/事件均由声音库提供。最终的声音库由 FMOD Studio 构建。

FMOD Studio 为声音项目中的每个库构建 "[bank name].bank" 文件。它是游戏中用于声音播放的事件与参数的集合。

## 主声音库

主声音库是声音系统的主要声音库。该库中没有事件。

**主声音库定义了：**

- 声音总线<br>FMOD Studio 中的事件并非孤立存在。它们的输出被路由到项目混音器。事件必须路由到主声音库中注册的某个总线。对于每个用作声音事件路由目标的总线，用户可以在应用设置中设置声音音量和静音状态。
- 混音器与路由<br>项目混音器由若干相互连接的总线组成。音频总线之间的连接描述了声音事件在声音系统中的流动。
- 全局参数<br>事件包含并主要由轨道和参数组成。部分参数在主声音库中定义。这些参数是全局的，可用于跨所有库对事件进行自动化与调制。

主声音库是声音系统的基础构件，因此：**切勿修改主声音库！**

只有当你完全确定自己在做什么，并且正在重写游戏中的所有声音时，才可以修改它。

## 声音定义

游戏中的常见声音是 FMOD Studio 项目中的 **事件**。FMOD 系统使用的每个对象（库、总线、事件、参数等）都有一个全局唯一标识符 - **GUID**。<br>（*GUID 类似于这样：{1315eda7-1829-4dd8-9d1a-176f65637ab2}*）

声音系统内部使用 GUID 处理对象。这一点非常重要。如果你在声音项目中删除一个对象（总线、事件等）并创建一个新对象，即使名称相同，它也会是另一个对象，因为该对象的 GUID 不同。

FMOD Studio 会将 GUID 导出到 txt 文件。

1. 使用 FMOD Studio 菜单命令：File / Export GUIDs...
2. 新文件 GUIDS.txt 会写入项目主文件夹的 "build" 子文件夹。
3. 该文件必须重命名为 "[bank filename].guids"，并放置在对应 "bank" 文件旁边。它是库中对象名称与其 GUID 之间的"字典"。

游戏使用两种方式定义声音对象的使用：

1. 直接使用 'sound id'：<br>"Sound id" 是格式为 "[bank filename]#[event name]" 的字符串。其中 [bank filename] 是相对于游戏 "base" 文件夹的库文件，[event name] 是 FMOD Studio 项目中事件的名称。<br>示例：*"/sound/ui/ui.bank#click"*
2. 声音引用文件：<br>声音引用文件用作声音规格的链接。它使用指向 soundref 文件的简单路径（例如 *"/sound/ui/ui_click.soundref"*）。

## 声音引用文件

我们更倾向并推荐使用声音引用文件。

- 配置声音的可能性更多。
- 更容易更改 / 模组化单个声音。

**声音引用文件结构：**

Soundref 文件是文本文件（采用 UTF-8 编码）。

- 其内容是一行 'sound id'，格式如下：source="[bank filename]#[event name]"。
- 文件中可以更改声音相对于默认位置的 3D 定位。格式如下，单独一行："position_offset=-left/+right;-down/+up;-front/+back"（单位：米）。

文件 *"ui_click.soundref"* 的内容示例：`source="/sound/ui/ui.bank#click"`

## 声音文档

- [音频总线、路由与混音器](Sound/Mixer.md)
- (WIP) 全局参数
- [声音 - 卡车发动机](Sound/TruckEngine.md)
- [声音 - 卡车变速箱与缓速器](Sound/TruckTransmission.md)
- [声音 - 卡车底盘](Sound/TruckChassis.md)
- [声音 - 卡车驾驶室（喇叭与噪声）](Sound/TruckCabin.md)
- [声音 - 卡车驾驶室过滤（内/外、车窗）](Sound/TruckCabinFiltering.md)
- [声音 - 远程卡车（多人游戏）](Sound/TruckRemote.md)
- (WIP) 声音 - 卡车内饰
- [声音 - 轮胎](Sound/Tires.md)
- (WIP) 声音 - 碰撞
- (WIP) 声音 - 交通
- [声音 - 世界](Sound/SoundWorld.md)
- (WIP) 声音 - 游戏 UI 与音乐
- [制作声音模组](Sound/Modding.md)
- [下载（模板、示例）](Sound/Downloads.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound | revision: 5784 | captured: 2026-10-21 23:56:14 -->
