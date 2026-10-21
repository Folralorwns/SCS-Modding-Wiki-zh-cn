# 文档/工具/SCS Blender Tools/全局设置

全局设置包含适用于整个 SCS Blender Tools 插件的通用设置，并根据用户的选择按机器或按 Blender 文件定义。

***SCS Global Settings*** 面板可在属性窗口的 ***Workspace*** 设置中找到。

[![SCS_Tools_Globals_01.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Global%20Settings/SCS_Tools_Globals_01.280.png)](../../../../files/SCS%20Tools%20Globals%2001.280.png.md)

共有三个子面板，将各项属性按合适的布局归类。

## Path Settings

在开始使用这些工具之前，必须指定数据源的访问位置，这些数据源用于填充部分库菜单以及寻址纹理。

首先，你需要设置包含项目的主文件夹。请将其填入 “SCS Project Base Path” 条目。其他路径通常以该位置为起点，因此可以以相对路径的形式保存。不过这并不总是必须遵循的规则，因此 SCS Tools 中的路径选择机制将始终自行决定合适的路径形式。

路径设置是否正确可从其背景颜色清楚地看出——如果某个条目有误，其背景为红色，需要将其设置为有效位置或有效的库文件。

[![SCS_Tools_Globals_Path_01.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Global%20Settings/SCS_Tools_Globals_Path_01.280.png)](../../../../files/SCS%20Tools%20Globals%20Path%2001.280.png.md)

### SCS Project Base Path

*[文件夹，始终为绝对路径]*

***这是最重要的路径，它指向你在任何 SCS 游戏中模组的 “base” 根目录。由于纹理和定义文件使用相对寻址，base 目录必须始终具有特定的结构。*** 因此，后续所有库的路径都应从该位置延续，并应为相对形式。不过，如果你希望这些库使用其他位置，也可以这样设置，路径形式将被自动选择。

> > **注意：** 若要导入示例模型，请确保将 SCS Project Base Path 设置为已下载 SCS Blender Tools 包中 “data” 目录内的某个示例 base 文件夹。

### Trigger Action Library

*[“*.sii” 文件，相对于 'SCS Project Base Path' 的绝对或相对路径]*

预定义触发动作的库。你可以将它们分配给 Trigger Prefab Locators，后者在游戏中用于触发各种动作（例如睡眠区域）。

### Sign Library

*[“*.sii” 文件，相对于 'SCS Project Base Path' 的绝对或相对路径]*

预定义交通标志的库。你可以将它们分配给 Sign Prefab Locators，后者在游戏中用于创建交通标志或任何定义为标志的模型。其中大多数会被 AI 车辆遵守，并为玩家设定交通规则。

### Semaphore Library

*[“*.sii” 文件，相对于 'SCS Project Base Path' 的绝对或相对路径]*

预定义交通信号灯配置文件的库。你可以将它们分配给 Traffic Semaphore Prefab Locators，后者在游戏中用于创建交通信号灯。这些信号灯会被 AI 车辆遵守，玩家同样应当遵守。

### Traffic Rules Library

*[“*.sii” 文件，相对于 'SCS Project Base Path' 的绝对或相对路径]*

预定义交通规则的库。你可以将它们分配给 Navigation Point Prefab Locators，后者在游戏中用于创建交通路线。这些规则主要由 AI 车辆使用。

### Hookup Library

*[文件夹，相对于 'SCS Project Base Path' 的绝对或相对路径]*

包含预定义 Hookup 文件的目录。你可以将它们分配给 Model Locators，后者在游戏中用于在当前模型内实例化其他游戏模型。

### Mat Substance Library

*[“*.db” 文件，相对于 'SCS Project Base Path' 的绝对或相对路径]*

材质物质（Material Substance）的库，用于定义材质的物理行为。你可以将它们分配给材质。

### Shader Presets Library

*[“*.txt” 文件，绝对文件路径]*

Shader Presets 库会加载所有可在 SCS 材质中使用的特效。默认情况下该路径为空，因为 SCS Blender Tools 使用内置的着色器预设库；但如果你希望使用自定义库，请务必勾选文件路径左侧的复选框，然后查找你的自定义着色器预设库。

## Display Settings

“Display Settings” 子面板汇集了属于 SCS Blender Tools 的所有特殊元素的视觉设置。此处可以找到 Locators、其 Curves、Preview Models 以及其他特定元素的视觉设置，详细说明见下文。

[![SCS_Tools_Globals_Display.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Global%20Settings/SCS_Tools_Globals_Display.280.png)](../../../../files/SCS%20Tools%20Globals%20Display.280.png.md)

### Drawing Mode

自定义元素（即 Locators 和 Connections）的绘制模式。它可在 Normal 与 X-Ray 模式之间切换。Normal 模式使用常规深度测试绘制，因此所有自定义元素与其他对象一样在场景中绘制；而 X-Ray 模式使用 X-Ray 绘制，使所有自定义元素显示在其他对象之上。

### Icon Theme

在这里你可以选择用于 SCS Blender Tools 自定义图标的图标主题，以最契合你的 Blender 主题。默认使用 White 主题。

### Display Info Texts

切换是否在 3D 视图中直接显示 Locators 的各种附加信息文本。这在处理预制件模型时非常有用。例如，你可以只显示 Locator 名称，或边界车道（Boundary Lanes）或节点（Nodes）。

### Info Text Color

信息文本的自定义颜色。

### Base Paint Color

为增加 SCS 游戏中的多样性，提供了可涂装功能，它通常用于 AI 交通车辆，使每辆车根据其在 SII 文件中的配置使用不同的颜色。然而由于 Blender Tools 不读取这类 SII 文件，所有带有 “paint” 风格的着色器在预览时都会使用此基础涂装颜色属性。

如果你不希望此功能改变着色器的外观，请确保显示设置中的此属性设置为纯白色 RGB(1.0, 1.0, 1.0)。

### Show Preview Models

打开或关闭 Locators 的预览模型显示。

### Locators Display (Subpanel)

打开或关闭 Locators 自定义表示形式的显示。这在调整导航曲线时尤其有用。

### Locator Size

Locators 自定义表示形式的绘制尺寸。

### Locator Empty Object Size

Locators 中可选择的 Empty 对象的绘制尺寸比例。如果你在选择 Locators 时遇到困难，可以调整此项。

### Prefab Loc Color

预制件 Locators 的自定义颜色。

### Model Loc Color

Model Locators 的自定义颜色。

### Collider Loc Wire Color

Collider Locators 线框的自定义颜色。

### Collider Loc Face Color

Collider Locators 面的自定义颜色。

### Connections Display (Subpanel)

打开或关闭 Locators 连接——曲线与直线——的显示。

### Optimized Connections Draw

仅在数据更新时绘制连接。关闭此项可能会提高 FPS（每秒帧数），尤其是在复杂的预制件场景中。

### Curve Segments

导航曲线的分段数量。它可以提升 3D 视图的更新速度。

### Nav Curves Color

导航曲线的自定义颜色。

### Map Line Color

Map Lines 的自定义颜色。

### Trigger Line Color

Trigger Lines 的自定义颜色。

## Other Settings

[![SCS_Tools_Globals_Other.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Global%20Settings/SCS_Tools_Globals_Other.280.png)](../../../../files/SCS%20Tools%20Globals%20Other.280.png.md)

### Copy BT Log To Clipboard

将 Blender Tools 日志复制到剪贴板的简易工具。剪贴板将包含自 Blender 启动以来的完整 Blender Tools 日志。

当你想要报告使用 Blender Tools 时遇到的问题时，可使用此工具轻松抓取日志。

### Log Level

设置 Blender 控制台内的日志记录级别。正常使用的推荐级别为 2，但在尝试排查缺陷或错误时，使用最高到级别 4 的日志记录会很有帮助。

### Use Global Settings

设置全局设置的存储位置：

1. ***From Common Config File*** - 会将全局设置保存到同一个 config.txt 文件中，因此该选项会让你处理的所有 Blender 文件使用相同的设置（按机器的全局设置）。> > **注意：** 更改的条目会立即写入设置文件（config.txt），因此下次启动 Blender 时所有设置都会被保留，即使应用程序遭遇崩溃。如果你想将设置重置为默认值，请在文件浏览器中找到已安装的 Blender Tools，删除 “io_scs_tools/config.txt” 文件并重新启动 Blender。
2. ***From Blend File*** - 会直接将全局设置保存到 blend 文件中，使你保存的每个 Blender 文件都可以拥有自己的设置（按 blend 文件的全局设置）。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Global_Settings | revision: 5675 | captured: 2026-10-21 23:56:14 -->
