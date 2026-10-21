# 文档/工具/SCS Workshop Uploader/versions.sii

在 Steam Workshop 模组中，你需要有单元文件 "versions.sii"，其中包含定义：应为哪个游戏版本使用哪个内容文件夹。

此文件包含一组 [package_version_info](../../Engine/Units/package%20version%20info.md) 序列化单元信息，并带有相应的一组属性。

- 示例文件：

```
SiiNunit
{
package_version_info : .latest {
	package_name: "latest"
}

package_version_info : .122.content {
	package_name: "content_122"
	compatible_versions[]: "1.22.*"
}

package_version_info : .120and121.content {
	// No special difference between 1.20 and 1.21
	package_name: "content_120_121"
	compatible_versions[]: "1.20.*"
	compatible_versions[]: "1.21.*"
}
}
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Workshop_Uploader/versions.sii | revision: 1648 | captured: 2026-10-21 23:56:14 -->
