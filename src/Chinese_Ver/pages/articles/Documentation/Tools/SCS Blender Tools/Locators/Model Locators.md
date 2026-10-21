# 文档/工具/SCS Blender Tools/定位器/模型定位器

模型定位器可用于将现有的游戏模型放置到其他游戏模型中，而无需将其数据实际包含在宿主文件中。简单来说，这些模型仅在宿主文件中被引用。例如，这样你就可以在卡车模型中定义一些位置，游戏中的后视镜或其他升级件将按玩家的意愿出现在这些位置。

[![SCS_Tools_Locators_-_Model_02.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Locators/Model%20Locators/SCS_Tools_Locators_-_Model_02.280.png)](../../../../../files/SCS%20Tools%20Locators%20-%20Model%2002.280.png.md)

### 名称

此处的属性与 Blender 对象的名称相同，并将由游戏引擎使用（例如在 ETS2 的轮胎/车轮模型中，“bb” 是表示车轮尺寸的定位器名称）。

### 挂接

此属性可根据 “Hookup Library” 中的记录进行设置（参见 [Global Settings](../Global%20Settings.md) 中的 “Path Settings” 一章）。而挂接属性则用于将其他游戏对象绑定到当前对象。挂接的示例包括：车灯的光晕、在预制件上生成行人、预制件上的公司标志等。

此外，左侧还有两个按钮：

- **🗘** 按钮可即时重新加载挂接库，无需导航到全局设置面板，
- **⌕** 按钮可选择与当前定位器具有相同挂接值的模型定位器。

> > **注意：** 模型定位器也可以使用 “Preview Model” 功能（参见 [Preview Models](../Locators.md#Preview_Models_on_Locators) 一章）。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Locators/Model_Locators | revision: 4312 | captured: 2026-10-21 23:56:14 -->
