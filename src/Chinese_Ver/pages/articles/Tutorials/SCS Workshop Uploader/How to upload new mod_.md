# 教程/SCS Workshop Uploader/如何上传新模组？

## 简介

在本教程中，我们将逐步向你展示如何准备模组，以便将其上传到创意工坊。

### 创意工坊模组的文件与目录布局

首先 - 你的模组布局会稍有变化。要查看 Steam 创意工坊模组的结构，请点击[此处](../../Documentation/Tools/SCS%20Workshop%20Uploader/Workshop%20mod%20structure.md)。

### 逐步准备待上传的模组

|  |  |  |
| --- | --- | --- |
| **1** | [![0002_create_folder.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0002_create_folder.jpg)](../../../files/0002%20create%20folder.jpg.md) | 准备模组的第一步是创建文件夹。你将在其中放置模组与 Steam 创意工坊兼容所需的所有文件和文件夹。 |
| **2** | [![0003_create_latest_folder.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0003_create_latest_folder.jpg)](../../../files/0003%20create%20latest%20folder.jpg.md) | 创建该文件夹后，打开它并在其中再创建一个名为 **universal** 的文件夹。（除了文件夹，你也可以创建包含游戏数据的 ZIP 归档包） |
| **3** | [![Universal_directory_content.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-Universal_directory_content.jpg)](../../../files/Universal%20directory%20content.jpg.md) | universal 目录（或归档包）应包含标准模组包的全部内容，即：manifest.sii 文件、描述文件、图标文件和模组内容。**注意：** 请记住！在创意工坊模组中，manifest.sii、描述文件和图标文件都是必需的！[在此处查看更多信息](../../Documentation/Engine/Mod%20manager.md) |
| **4** | [![0004_open_text_editor_and_create_versions_sii.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0004_open_text_editor_and_create_versions_sii.jpg)](../../../files/0004%20open%20text%20editor%20and%20create%20versions%20sii.jpg.md) | 打开你常用的文本编辑器并创建名为 versions.sii 的文件 - 将其保存在创建 **universal** 文件夹的同一文件夹中 |
| **5** | [![0005_fill_versions_sii_with_magic_and_global_sii_scope.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0005_fill_versions_sii_with_magic_and_global_sii_scope.jpg)](../../../files/0005%20fill%20versions%20sii%20with%20magic%20and%20global%20sii%20scope.jpg.md) | 将 sii 文件框架添加到你的 versions.sii 文件中。SiiNunit { } |
| **6** | [![0006_add_package_version_info_for_latest_version.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0006_add_package_version_info_for_latest_version.jpg)](../../../files/0006%20add%20package%20version%20info%20for%20latest%20version.jpg.md) | 添加 universal 版本单元的定义。SiiNunit { package_version_info : .universal { } } |
| **7** | [![0007_add_folder_attribute_to_latest_info.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0007_add_folder_attribute_to_latest_info.jpg)](../../../files/0007%20add%20folder%20attribute%20to%20latest%20info.jpg.md) | 将 **package_name** 设置为包含模组数据的文件夹或 ZIP 归档包的名称。SiiNunit { package_version_info : .universal { package_name: "universal" } } |

完成这些步骤并把游戏内容放入包中后，如果你不想支持特定的游戏更新，可以跳过后续步骤，直接前往“上传”部分。

### 支持指定的游戏版本

|  |  |  |
| --- | --- | --- |
| **1** | [![0008_create_folder_for_122_content.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0008_create_folder_for_122_content.jpg)](../../../files/0008%20create%20folder%20for%20122%20content.jpg.md) | 如果你拥有仅支持某一个特定游戏版本的数据，就需要创建用于存放该内容的文件夹或归档包。 <br> **提示：** 为更好地组织目录，我们建议将此文件夹命名为 *122_content* - 其中 122 代表 1.22。例如 - 对于 1.23 更新，它将是 123，对于 1.6 则是 16，以此类推。 |
| **2** | [![0009_add_new_unit_to_versions_sii_with_122_content_step_1.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0009_add_new_unit_to_versions_sii_with_122_content_step_1.jpg)](../../../files/0009%20add%20new%20unit%20to%20versions%20sii%20with%20122%20content%20step%201.jpg.md) | 打开文本编辑器，并执行与为模组的 universal 版本添加定义时完全相同的步骤（只是这次要使用不同的文件夹名和单元名）。SiiNunit { package_version_info : .universal { package_name: "universal" } package_version_info : .122_content { package_name: "122_content" } } |
| **3** | [![0010_add_new_unit_to_versions_sii_with_122_content_step_2.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0010_add_new_unit_to_versions_sii_with_122_content_step_2.jpg)](../../../files/0010%20add%20new%20unit%20to%20versions%20sii%20with%20122%20content%20step%202.jpg.md) | 现在你还需要完成另外几个步骤：设置 compatible_versions 属性的值。由于我们要为 1.22 更新提供数据，请写入 "1.22.*"。取值形式与 manifest.sii 中的 compatible_versions 数组类似。如果你希望此包仅用于 1.23 版本，则需要写入：compatible_versions: "1.23.*" 如果你只想支持单一版本（不推荐），则应写入：compatible_versions[]: "1.22.1" 该属性的值可以包含数字、点号 "."（位于数字之间）和星号 "*"（位于末尾）。如果你只写入 "1.35.1"，你的模组将仅与该特定版本兼容。使用 "1.35.*" 会让你的模组与 1.35 版本的所有小型更新兼容（推荐）。SiiNunit { package_version_info : .universal { package_name: "universal" } package_version_info : .122_content { package_name: "122_content" compatible_versions[]: "1.22.*" } } |
| **4** | [![0011_create_multiversion_folder.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0011_create_multiversion_folder.jpg)](../../../files/0011%20create%20multiversion%20folder.jpg.md) | 如果你想支持多个特定版本，就需要为其设置文件夹。 <br> **提示：** 我们建议使用与“指定单个版本内容”类似的命名语法，但使用下划线 "_" 来分隔版本。例如，如果内容同时供 1.23 和 1.24 使用，内容包将命名为 "123_124_content"；如果你希望内容包用于 1.24、1.25.0 和 1.25.2 更新，内容包将命名为 "124_1250_1252_content"。 |
| **5** | [![0012_add_another_unit_to_versions_sii.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0012_add_another_unit_to_versions_sii.jpg)](../../../files/0012%20add%20another%20unit%20to%20versions%20sii.jpg.md) | 再次为该单元添加相同的定义。SiiNunit { package_version_info : .universal { package_name: "universal" } package_version_info : .122_content { package_name: "122_content" compatible_versions[]: "1.22.*" } package_version_info : .120_121_content { package_name: "120_121_content" } } |
| **6** | [![0013_add_first_version_attribute.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0013_add_first_version_attribute.jpg)](../../../files/0013%20add%20first%20version%20attribute.jpg.md) | 为你支持的某一个更新添加 compatible_version 值。SiiNunit { package_version_info : .universal { package_name: "universal" } package_version_info : .122_content { package_name: "122_content" compatible_versions[]: "1.22.*" } package_version_info : .120_121_content { package_name: "120_121_content" compatible_versions[]: "1.20.*" } } |
| **7** | [![0014_add_second_version_attribute.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0014_add_second_version_attribute.jpg)](../../../files/0014%20add%20second%20version%20attribute.jpg.md) | 再为你想要支持的第二个更新添加 compatible_version 值。SiiNunit { package_version_info : .universal { package_name: "universal" } package_version_info : .122_content { package_name: "122_content" compatible_versions[]: "1.22.*" } package_version_info : .120_121_content { package_name: "120_121_content" compatible_versions[]: "1.20.*" compatible_versions[]: "1.21.*" } } |

## 上传

> **实用链接：** 如果你尚未安装 SCS Workshop Uploader - 请查看此教程 - [如何下载并安装 SCS Workshop Uploader？](How%20to%20download%20the%20tool_.md)

[![Scs_workshop_uploader_tutorial_preview.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/Scs_workshop_uploader_tutorial_preview.jpg)](../../../files/Scs%20workshop%20uploader%20tutorial%20preview.jpg.md)

- 从你的 Steam 客户端运行 **SCS Workshop Uploader** 工具。

1. 选择与你的模组兼容的**游戏**。
2. 从下拉菜单中选择 **New**。启动工具时它应默认处于选中状态。
3. 在 **Mod data** 部分 - 浏览选择你的**模组数据文件夹**。该文件夹应包含你的包和 version.sii 文件。
4. 如果你选择文件夹，请浏览选择**模组预览图像**。
5. 在下一步中填写**模组名称**。
6. 在 Steam 创意工坊中选择**模组可见性**。可以是 **Private**、**Friends only** 或 **Public**。
7. 填写你的**模组描述**，它将显示在你的物品创意工坊页面上。**（最少 50 个字符）**
8. 如果你想了解可用的格式，请点击问号按钮。
9. 现在，你必须为模组选择**类型标签**。
10. 如果适用，你还可以选择 **truck parts** 和 **brand** 标签。
11. 现在你可以填写模组的**更改说明**。如果需要让编辑框更大，只需调整工具窗口的大小。由于这是首次上传，你很可能什么都不写 - 或者写类似 *“初次上传。”* 的内容。
12. 完成所有这些步骤后，直接点击 **Upload** 按钮。在实际执行上传操作之前，工具会检查你的模组是否包含正确的数据。

> **注意：** 你可能会注意到，使用非 [ASCII 字符](https://en.wikipedia.org/wiki/ASCII)时，计数器减少的量会超过一。这是因为这些字符占用的空间大于一个字节。计数器统计的是描述和标题所占用的字节空间 - 而非字符数量

### 验证

- 如果出现任何验证错误，你会看到此对话框。

[![0025_in_case_of_error_you_will_get_this_dialog.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0025_in_case_of_error_you_will_get_this_dialog.jpg)](../../../files/0025%20in%20case%20of%20error%20you%20will%20get%20this%20dialog.jpg.md)

点击 **OK** 后，你会看到包含验证期间出现的所有错误和警告的日志对话框。如果只有警告，你既可以继续操作，也可以中止操作。如果出现错误，你**必须**在上传前修复它们。

> **实用链接：** 如果你需要帮助解决验证错误，请点击**[此处](../../Documentation/Tools/SCS%20Workshop%20Uploader/Validation%20errors%20and%20solutions%20for%20them.md)**

[![Validation_result_window.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/Validation_result_window.jpg)](../../../files/Validation%20result%20window.jpg.md)

1. 这一行是验证的摘要 - 错误和警告的数量。
2. 此区域是验证日志。所有日志条目的格式如下：***[TYPE] [CODE] (file): Message***
3. 下方有两个复选框，你可以在这里隐藏警告或错误。
4. 如果至少存在一个错误，你只能点击 Abort。此按钮会直接中止上传。
5. 如果验证未报告任何错误，你可以点击此按钮并继续上传模组。如果存在错误，你将无法继续 - 必须修复这些问题。

### 成功

如果没有错误，上传将继续进行；如果一切顺利，你会看到此对话框。

[![0026_upload_success.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/0026_upload_success.jpg)](../../../files/0026%20upload%20success.jpg.md)

不过，上传过程中也可能出现某些失败 - 此时你会看到带有错误信息的对话框。如果你在解决问题时遇到困难，请在**[我们的论坛](http://forum.scssoft.com/viewforum.php?f=24)**发帖

## Steam 创意工坊服务条款

如果这是你的第一个模组，并且你从未为其他游戏制作过模组，你很可能会遇到关于未接受 Steam 创意工坊服务条款的错误 - 若出现这种情况，工具会向你显示相应的提示信息，并在你的默认浏览器中打开 Steam 创意工坊服务条款 - 你需要登录 Steam 账户、阅读并接受服务条款，完成后只需返回工具并重新尝试上传模组。同意这些条款是**强制性的**。

<!-- source: https://modding.scssoft.com/wiki/Tutorials/SCS_Workshop_Uploader/How_to_upload_new_mod%3F | revision: 4564 | captured: 2026-10-21 23:56:14 -->
