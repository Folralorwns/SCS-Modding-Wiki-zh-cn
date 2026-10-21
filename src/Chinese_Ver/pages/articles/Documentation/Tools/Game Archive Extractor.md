# 文档/工具/游戏归档包解包器

你可以使用提供的解包器解压游戏归档包，以开发游戏模组。完成模组后，若要重新打包归档包，可使用任意标准 ZIP 工具，例如 [7-Zip](https://www.7-zip.org/)。

## 用法

```
scs_extractor archive.scs [output_path]
```

你也可以将 .scs 文件拖放到 SCS Extractor 上以解包文件。将 **base.scs** 文件拖放到 SCS Extractor 上，会将其包含的所有文件解包到 SCS Extractor 的当前位置。为避免解包内容落入游戏的原始目录，你应创建一个单独的文件夹，并将 SCS Extractor 的副本放入其中。然后只需将游戏文件拖放到解包器上即可。所有文件解包完成后，控制台窗口会关闭。

## 下载

一般来说，较新版本的工具可以解包为较旧版本游戏创建的归档包。

- **[链接 (1.50-1.54)](https://download.eurotrucksimulator2.com/scs_extractor_1_50.zip)**
- **[链接 (1.55+)](https://download.eurotrucksimulator2.com/scs_extractor_1_55.zip)** - 64 位二进制文件，1.55+ 版本（包括测试版）必需

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Game_Archive_Extractor | revision: 5756 | captured: 2026-10-21 23:56:14 -->
