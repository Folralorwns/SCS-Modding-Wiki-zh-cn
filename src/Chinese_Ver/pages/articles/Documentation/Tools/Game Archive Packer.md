# 文档/工具/游戏归档包打包器

ETS2/ATS 的 1.50 更新引入了 HashFS 格式的 v2 版本。该格式通过将资源元数据存储在内存中，可更高效地加载游戏数据。虽然所有旧格式仍受模组支持，但由于引擎假定元数据可立即获取，某些资源类型可能会出现卡顿。本工具支持创建和解包 .scs 打包文件。创建仅支持 v2，解包则同时支持 v1 和 v2。此前界面简化的仅解包版本仍然[可用](Game%20Archive%20Extractor.md)。

该格式将纹理作为单个对象处理。打包过程中遇到 tobj 时，工具会读取所有被引用的 dds 文件，并将结果存储为单个合并对象。未被引用的 dds 文件会被忽略。这意味着在制作纹理模组时，你需要同时包含 tobj 和所有被引用的 dds 文件。

## 归档包解包

要将内容解包到当前目录，请使用：

```
scs_packer extract archive.scs
```

要将内容解包到指定目录，请使用：

```
scs_packer extract archive.scs -root <directory>
```

## 归档包创建

要从指定目录的内容创建归档包，请使用：

```
scs_packer create archive.scs -root <directory>
```

工具会自动压缩所有兼容的文件。出于开发目的，通过指定 -nocompress 参数禁用压缩可能很有用，可加快整个流程。

## 下载

一般来说，较新版本的工具可以解包为较旧版本游戏创建的归档包。游戏应能够使用为较旧版本创建的归档包，但加载此类文件可能较慢，或可能导致卡顿。

- **[链接 (1.50-1.54)](https://download.eurotrucksimulator2.com/scs_packer_1_50.zip)**
- **[链接 (1.55+)](https://download.eurotrucksimulator2.com/scs_packer_1_55.zip)** - 64 位二进制文件。2025 年 9 月 12 日更新，修复了可能导致归档包损坏或崩溃的线程问题。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Game_Archive_Packer | revision: 5720 | captured: 2026-10-21 23:56:14 -->
