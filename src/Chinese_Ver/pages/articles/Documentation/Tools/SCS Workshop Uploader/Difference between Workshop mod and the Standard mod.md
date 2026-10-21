# Documentation/Tools/SCS Workshop Uploader/Difference between Workshop mod and the Standard mod

### 独立模组与创意工坊模组之间的差异

- 创意工坊模组具有特定的布局。详情见 [Workshop mod Structure](Workshop%20mod%20structure.md) 页面。
  - 一个包含 [versions.sii](versions.sii.md) 文件的根目录。
  - 由 [versions.sii](versions.sii.md) 文件指向的、包含模组每个版本的子目录，实际的模组文件位于其中。
  - 当模组与游戏新版本引入的改动不再兼容时，应创建新的版本子目录，以便为使用旧版本的用户保持向后兼容。

- 应从版本子目录的 [manifest.sii](../../Engine/Mod%20manager.md#Using_the_manifest) 文件中移除以下配置指令：
  - **compatible_versions**：继承自 [versions.sii](versions.sii.md) 文件
  - **display_name**：使用在 [SCS Workshop Uploader](../../Tools.md#SCS_Workshop_Uploader) 工具中配置的名称

- 标准模组需要自行处理分发，用户需在新版本发布后手动更新。
- 上传新版本后，Steam 创意工坊模组会自动更新到订阅者处。
- 在存在相应版本时，Steam 创意工坊模组还能选择已知可在特定游戏版本中运行的特定模组版本，从而实现自动向后兼容。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Workshop_Uploader/Difference_between_Workshop_mod_and_the_Standard_mod | revision: 5750 | captured: 2026-10-21 23:56:14 -->
