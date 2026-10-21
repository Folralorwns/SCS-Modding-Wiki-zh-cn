# Documentation/Engine/Units/package version info

**Package version info** is a [unit](../Units.md) containing workshop mod package information, such as the name of the folder or archive with content and the array of compatible game versions. It is used in each workshop mod's [versions.sii](../../Tools/SCS%20Workshop%20Uploader/versions.sii.md).

## Special Case: Universal Version

Each workshop mod's versions.sii file may have a *single* package version info without any defined compatible_versions, called the “universal version.” The associated package will be used for all game versions that are not defined by another package version info unit inside the versions.sii file.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Required/Optional | Description |
| --- | --- | --- | --- |
| package_name | string | Required | The name of the folder or archive with the version-specific mod content. For zip archives, package_name is just the file name without the extension. |
| compatible_versions | string array | Optional | The array containing the set of versions that are compatible with this version definition. If not specified this package will be used for all of the game versions not explicitly defined for other packages. <br>**Important:** Each workshop mod's versions.sii can only contain *one* `package_version_info` unit without this parameter specified. |
| informational | bool | Optional | When true, it indicates that the package contains information only. If unspecified, it defaults to false. |

## Raw Unit Definition

```
  "package_version_info":{
   "superclass":"unit",
   "attrs":{
    "package_name":{
     "type": "string"
    },
    "compatible_versions":{
     "type": "string_array"
    },
    "informational":{
     "type": "bool"
    }
   }
```

## See Also

[Tutorial: How to Use Mod Versioning](../../../Tutorials/SCS%20Workshop%20Uploader/How%20to%20use%20mod%20versioning.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/package_version_info | revision: 5191 | captured: 2026-10-21 23:56:14 -->
