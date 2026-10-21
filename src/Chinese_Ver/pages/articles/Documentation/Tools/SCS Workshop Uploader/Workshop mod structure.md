# 文档/工具/SCS Workshop Uploader/Workshop 模组结构

标准模组是单个 **包**，其中包含 manifest.sii 文件、描述与图标文件以及模组数据文件。Workshop 模组可以、也应该由多个 **包** 组成 - 该选项使你能够借助一个 Workshop 模组，为使用不同游戏版本的用户提供模组的多个版本。在 **[versions.sii](versions.sii.md)** 文件中，你指定在使用特定的游戏更新时应使用哪个 **包**。但请记住 - 这种布局仅对 Workshop 模组正确。标准模组仍使用单包方式。

[![Mod_layout_explanation.jpg](../../../../../../images/articles/Documentation/Tools/SCS%20Workshop%20Uploader/Workshop%20mod%20structure/Mod_layout_explanation.jpg)](../../../../files/Mod%20layout%20explanation.jpg.md)

这些包中的每一个都直接包含模组元数据（manifest.sii、描述、图标）以及模组数据文件。

[![Package_with_mod_metadata_and_mod_data_files.jpg](../../../../../../images/articles/Documentation/Tools/SCS%20Workshop%20Uploader/Workshop%20mod%20structure/Package_with_mod_metadata_and_mod_data_files.jpg)](../../../../files/Package%20with%20mod%20metadata%20and%20mod%20data%20files.jpg.md)

自 SCS Workshop Uploader 1.0.38 版本起，包中可以包含仅在拥有同名 DLC 时才会挂载的子目录或文件。如果模组根目录包含目录 "base"、zip 归档包 "base.zip"、以 "dlc_" 为前缀的目录或 zip 归档包，游戏只会挂载模组中与已拥有 DLC 对应的部分。"base" 部分始终会被挂载（如果存在）。模组 manifest 和其他元数据仍保留在包内。

[![Package_with_zip_files.jpg](../../../../../../images/articles/Documentation/Tools/SCS%20Workshop%20Uploader/Workshop%20mod%20structure/Package_with_zip_files.jpg)](../../../../files/Package%20with%20zip%20files.jpg.md)

[![Package_with_subdirectories.jpg](../../../../../../images/articles/Documentation/Tools/SCS%20Workshop%20Uploader/Workshop%20mod%20structure/Package_with_subdirectories.jpg)](../../../../files/Package%20with%20subdirectories.jpg.md)

使用新式包时，每个目录或 zip 归档包都会单独校验，并且校验时仅挂载游戏基础数据和同名 DLC。如果你需要挂载其他 DLC，请在 manifest 的 **dlc_dependencies** 数组中列出它们。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Workshop_Uploader/Workshop_mod_structure | revision: 5288 | captured: 2026-10-21 23:56:14 -->
