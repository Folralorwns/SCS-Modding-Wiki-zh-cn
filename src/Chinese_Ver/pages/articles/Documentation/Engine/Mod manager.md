# 文档/引擎/模组管理器

新的模组管理器引入了包的概念。包可以是：

- zip 归档包 - 与你之前使用 .scs 或 .zip 扩展名时所用的完全相同。
- 普通目录 - 其中每个目录代表一个单独的模组。

我们建议在模组开发阶段使用普通目录，在模组发布时使用 zip 归档包，以使模组体积更小、对最终用户更方便（一个文件相对于一个充满文件的目录）。在包内你可以定义包含模组元数据的 manifest 文件。元数据由模组管理器使用，用于向用户显示你的模组。你可以指定描述、图标图像以及更多内容。

自 ETS2 与 ATS 1.48 版本起，你可以使用这样的模组：其中包含仅在拥有同名 DLC 时才会挂载的子目录或文件。如果模组根目录包含目录 “base”、zip 归档包 “base.zip”、以 “dlc_” 为前缀的目录或 zip 归档包，游戏只会挂载模组中与已拥有 DLC 对应的部分。“base” 部分始终会被挂载（如果存在）。模组 manifest 和其他元数据仍保留在模组根目录中。

## 使用 manifest

要设置全部元数据信息，你需要在模组包中创建包含 “mod_package” 单元定义的 “manifest.sii” 文件。示例 “manifest.sii” 文件：

```
SiiNunit
{
# ".package_name" does not matter as the dot at the beginning of the file means
# that this unit is anonymous. Please keep this form to not make any conflicts
# with other mod packages (name collisions).
mod_package : .package_name
{
        # Package version can be any string with any length.
        package_version: "1.0 Release 3"

        # Display name can be any string with any length.
        display_name: "My mod"

        # Author can be any string with any length.
        author: "My Nick"

        # Categories is an array of strings.
        category[]: "ui"
        category[]: "truck"

        # Icon inside the root directory of the mod.
        icon: "mod_icon.jpg"

        # Description file inside the root directory of the mod.
        description_file: "mod_description.txt"

        # compatible_versions[]: "1.19.*" # Mod is compatible with 1.19.X..

        # dlc_dependencies[]: "dlc_north"
        # dlc_dependencies[]: "dlc_east"
}
}
```

**注意：** 我们不限制属性的长度，但显示这些元数据的某些位置空间有限。为避免出现问题，我们会截断取值以适配 UI。截断只是在某处截断字符串，并在字符串末尾添加 “..”，以表示还有更多内容但无法容纳。

- **package_version**
  - 类型：string
  - 模组包的版本。
- **display_name**
  - 类型：string
  - 模组的显示名称。如果未指定，则使用不含扩展名的包名称。**注意：** 当你想创建 Steam 创意工坊模组时，此字符串不是必需的。你可以在 SCS Workshop Uploader 的上传过程中指定模组名称。
- **author**
  - 类型：string
  - 作者名称。
- **category**
  - 类型：字符串数组
  - 类别列表。目前每个模组最多限制 2 个类别。如果使用的类别超过两个，则只会使用前两个。如果未指定，模组会被归入 “Others” 类别。你只能使用“可使用的类别”一节中定义的类别
- **icon**
  - 类型：string
  - 模组包目录根目录下包含图标图像的文件名。只能是尺寸恰好为 276x162px 的 .jpg 文件
- **description_file**
  - 类型：string
  - 模组包目录根目录下包含描述文本的文件名。描述文件必须是扩展名为 .txt 并以 UTF-8 编码保存的简单文本文件。描述文件的内容显示在模组详情窗口中，应包含有关模组用途的信息、所含模组的额外致谢等。关于可能的文本格式，请参见“模组的描述”一节 > **提示：** 自 ETS 2 1.23 起，你可以指定本地化描述文件，更多信息请查看：本地化描述。
- **compatible_versions（不适用于 Steam 创意工坊模组）**
  - 类型：字符串数组
  - 兼容游戏版本列表。如果该列表存在，且游戏版本与该列表中的任何版本都不匹配，用户将无法使用该模组，只能等待作者更新。仅应用于可能会失效的模组，例如地图模组。 <br>**注意：** 如果你希望模组与所有版本兼容，只需跳过此参数。另请注意，带 “s” 后缀的 Steam 版本格式（例如：1.18.1s）在此版本编号中并不存在，因此请勿使用。 <br>列表中的每一项都支持如下所示通配符格式： <br><code>compatible_versions[]: "1.19.*"</code> 这表示该模组与所有 “1.19.x” 版本兼容，即所有编号以 1.19 开头的补丁都兼容。下表中的示例展示了字符串 “1.19.*” 的兼容游戏版本： | **版本** | **兼容？** | | --- | --- | | 1.18.1 | 否 | | 1.19.1 | 是 | | 1.19.1.3 | 是 | | 1.19.4 | 是 | | 1.20.4 | 否 |你还可以只指定支持游戏的某一个修订版本，但不推荐这样做，因为在小版本补丁之间我们不会对游戏做太多改动。<br>例如： <br><code>compatible_versions[]: "1.19.1"</code>这种做法并不可取，因为你的模组只能与 1.19.1 版本配合使用。<br>如果我们发布某些热修复，你的模组就会与之不兼容。<br>你也可以使用多个兼容版本定义，如下所示： <br><code>compatible_versions[]: "1.19.*"<br>compatible_versions[]: "1.20.*"</code>这样你就能同时支持 1.19 和 1.20 补丁。<br>**请记住！如果你指定非常受限的版本集合，即使你的模组与最新版本 100% 兼容，模组用户也可能要等待你发布针对该模组的修复补丁。**
  - 模组类型及其配置：
    - 地图模组 <br><code>compatible_versions[]: "X.X.*"</code>只需检查游戏主版本号部分是否匹配。我们可能会在主版本补丁之间破坏地图兼容性（例如 1.17 > 1.18），因此你必须从地图编辑器重新导出地图模组。在补丁之间（例如 1.18.1 > 1.18.2），我们引入会破坏兼容性的关键地图格式改动的可能性非常小。
    - 调校部件、卡车、模型集以及任何其他内容 <br>最好的做法是不要使用此变量，因为你的模组失效的可能性非常小。
- **dlc_dependencies（可选）**
  - 类型：字符串数组
  - 自 **ETS2 1.26** 和 **ATS 1.5** 起，你可以在 manifest 文件中指定模组需要安装的 DLC 列表。当用户缺少所需 DLC 之一时，此功能会阻止在模组管理器中激活该模组。要指定依赖项，你需要编辑模组的 manifest.sii 文件并添加以下内容：<br><code>dlc_dependencies[]: "package_name"</code>其中 package_name 是 DLC 包的名称 - 你可以在游戏目录中找到包名称，例如，如果你的模组需要 DLC Scandinavia - 其归档包名为 dlc_north.scs，那么包名称就是不含扩展名的归档包名称，因此在本例中为 dlc_north。
- **mp_mod_optional（可选）**
  - 类型：bool
  - 指定在安装了此模组的情况下玩家能否加入多人游戏，即使服务器或其他玩家没有该模组。设为 true 时，该模组在多玩家兼容性方面被视为可选。此类模组不得以要求所有参与者都安装它的方式影响玩法。地图模组将忽略此参数。
  - 服务器必须显式允许使用可选模组。否则所有模组都被视为必需。
  - 客户端必须在会话浏览器过滤器中显式允许带有可选模组的服务器。

## 可使用的类别

“category” 数组条目中可以使用 18 个有效类别：

- truck
- trailer
- interior
- tuning_parts
- ai_traffic
- sound
- paint_job
- cargo_pack
- map
- ui
- weather_setup
- physics
- graphics
- models
- movers
- walkers
- prefabs
- other

## 模组的描述

描述文本长度不受限制。此外，你还可以使用颜色标签为模组描述着色。

可用的颜色标签列表：

| 标签 | 结果颜色 |
| --- | --- |
| [red] | #FF2626 |
| [green] | #75FF00 |
| [blue] | #12ABE5 |
| [normal] | UI 中使用的默认字体颜色 |
| [white] | #FFFFFF |
| [orange] | #FFAE00 |

**例如：**

```
[red]Hello [green]Wor[orange]ld
```

结果为：**Hello World**

### 本地化描述

同样从 **1.23** 版本起，你可以本地化模组描述。要使用此功能，你需要为每种语言分别创建描述文件 - 文件名格式为 `description_file_name.[locale].txt`，例如如果 description_file 属性设为 “description.txt”：

- `description.en_gb.txt`
- `description.cz_cz.txt`
- `description.ru_ru.txt`
- `description.pl_pl.txt`

如果游戏找不到合适的语言文件，将使用 description.txt 文件。

## 示例模组

你可以[在此处](http://eurotrucksimulator2.com/modding/sample_mod.zip)下载带有 manifest 的示例模组。

## 此处未描述的其他问题

如果你在将模组适配新标准时遇到任何问题，欢迎到我们论坛的[模组论坛版块](http://forum.scssoft.com/viewforum.php?f=24)发帖。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Mod_manager | revision: 5726 | captured: 2026-10-21 23:56:14 -->
