# 文档/工具/SCS Blender Tools/转换助手

转换助手面板提供自动转换文件与打包模组的工具。包含转换助手的面板位于 Blender 属性窗口 *Output* 选项卡中的 [Export Panel](Export%20Panel.md) 下方。

不过，在使用转换助手之前，你应先下载适用于你所要制作模组的游戏的最新 [Conversion Tools](../Conversion%20Tools.md)，并在 *Conversion Tools Path* 下设置转换工具的路径。此外，请确保已查看 [Intended workflow](Intended%20workflow.md) 图片，以便更好地理解使用 SCS Blender Tools 与 Conversion Tools 时模组系统的工作方式。

[![SCS_Tools_Conv_Hlpr.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Conversion%20Helper/SCS_Tools_Conv_Hlpr.280.png)](../../../../files/SCS%20Tools%20Conv%20Hlpr.280.png.md)

位于 SCS Conversion Helper 面板标题右侧的小剃刀图标代表 **Clean Converted Data** 操作符。该操作符会立即清理你之前转换的内容，或此前遗留的内容。总的来说，这可确保你的模组在转换结果中不包含任何未使用的资源（残留的贴图、旧材质）。在使用 [Mod Packing](../Conversion%20Tools.md#Mod_Packing) 并启用 **Clean** 选项时，也可实现相同的操作。

转换助手还支持可切换的 **Custom Paths**。启用后，转换助手面板会如下方图片所示进行扩展。

[![SCS_Tools_Conv_Hlpr_Custom_Paths.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Conversion%20Helper/SCS_Tools_Conv_Hlpr_Custom_Paths.280.png)](../../../../files/SCS%20Tools%20Conv%20Hlpr%20Custom%20Paths.280.png.md)

## 自定义路径用法

自定义路径是一个列表属性，用于保存你希望同时转换的多个自定义路径。当你要合并自己 2 个或多个不同模组的资源时，请使用这些自定义路径。示例用法见 [Intended workflow#Usual mod combined with dependency mod (using custom paths)](Intended%20workflow.md#Usual_mod_combined_with_dependency_mod_(using_custom_paths))

在列表侧边，你可以找到用于管理自定义路径的操作符：

- **+** - 打开文件选择器，你需要在其中浏览以选择要使用的新自定义路径。
- **−** - 删除列表中当前选中的自定义路径。
- ⯅ - 将列表中当前选中的自定义路径上移。列表中的顺序不会影响转换结果，它只是让你可以按自己的喜好排列路径。
- ⯆ - 将列表中当前选中的自定义路径下移。列表中的顺序不会影响转换结果，它只是让你可以按自己的喜好排列路径。

## 手动转换

虽然使用 **Convert** 进行模组打包时已在打包前触发自动转换，但你仍可执行手动转换。目前共有三种不同方式：

- **CONVERT CURRENT SCS PROJECT** - 仅转换当前设置的 SCS Project Base Path 中资源的操作符。
- **CONVERT CUSTOM MAPS** *（仅在启用自定义路径时可见并可用）* - 仅转换已定义自定义路径中资源的操作符。
- **CONVERT ALL** *（仅在启用自定义路径时可见并可用）* - 转换自定义路径中的资源以及当前设置的 SCS Project Base Path 中资源的操作符。

当你打算稍后打包或手动打包模组时，建议使用手动转换。

## 模组打包

本节包含用于为 SCS 游戏打包模组的属性和操作符。

前两个选项用于指定目标位置和名称：

- **Mod Folder Path** - 保存模组应放置的文件夹的属性。在该属性侧边有搜索图标操作符，用于自动获取 Euro Truck Simulator 2 或 American Truck Simulator 的模组路径。
- **Mod Name** - 保存模组 ZIP 文件名称的属性。

第三行定义要用于模组包的压缩类型：

- **Folder** - 该选项会在所选模组目标位置内创建文件夹，并将 Conversion Tools 的转换结果复制到其中，而不会创建 ZIP 包。创建的文件夹名称与 ZIP 包相同，即由模组名称属性决定。
- **ZIP (Uncompressed)** - 将模组打包为未压缩的 ZIP 文件。
- **ZIP (Moderate)** - 将模组打包为压缩的 ZIP 文件（助手使用 deflate 压缩，SCS 游戏支持该格式）。

下一行包含可以在打包模组之前执行的自动操作开关：

- **Clean** - 如果你希望进行干净的转换、不残留之前打包或转换的内容，请启用此开关。
- **Export** - 如果你希望运行自动 Blender Tools 导出，请启用此开关。自动导出的内容范围由 [Export Panel](Export%20Panel.md) 中的 Export Scope 属性定义。
- **Convert** - 如果你希望在打包前转换资源，请启用此开关。该自动转换会转换 SCS Project Base Path 以及所有已定义的自定义路径。

### PACK MOD 又称魔法按钮

面板底部的最终魔法操作符是 **>>>> PACK MOD <<<<**。该操作符会先执行已启用的自动操作，最后将 Conversion Tools 的转换结果打包为 ZIP 包，并复制到所选的模组目标位置。

因此，如果你不想费心处理手动导出/转换，可按以下几步轻松操作：

1. 将模组文件夹路径设置为："[<Game User Path>](../../Engine/Game%20user%20path.md)/mod"
2. 填写模组名称
3. 启用所有选项
4. 按下 PACK MOD。
5. 打包完成后，运行游戏并试用你的模组！

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Conversion_Helper | revision: 4287 | captured: 2026-10-21 23:56:14 -->
