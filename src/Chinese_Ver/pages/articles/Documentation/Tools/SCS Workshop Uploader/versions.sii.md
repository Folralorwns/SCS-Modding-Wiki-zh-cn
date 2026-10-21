# Documentation/Tools/SCS Workshop Uploader/versions.sii

In the Steam Workshop mods you need to have unit file "versions.sii" containing definitions which content folder should be used for which game version.

This file contains set of [package_version_info](../../Engine/Units/package%20version%20info.md) serialized unit informations with proper set of the attributes.

- Example file:

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
