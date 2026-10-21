# Documentation/Engine/Units/package version info

**Package version info** 是一个[单元](../Units.md)，包含创意工坊模组包的信息，例如内容所在文件夹或归档包的名称，以及兼容游戏版本的数组。它用于每个创意工坊模组的 [versions.sii](../../Tools/SCS%20Workshop%20Uploader/versions.sii.md) 中。

## 特殊情况：通用版本

每个创意工坊模组的 versions.sii 文件可以有*一个*不含任何已定义 compatible_versions 的包版本信息，称为“通用版本”。关联的包将用于 versions.sii 文件中未被其他包版本信息单元定义的所有游戏版本。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 必需/可选 | 描述 |
| --- | --- | --- | --- |
| package_name | string | 必需 | 包含特定版本模组内容的文件夹或归档包的名称。对于 zip 归档包，package_name 仅为不带扩展名的文件名。 |
| compatible_versions | string array | 可选 | 包含与此版本定义兼容的版本集合的数组。如果未指定，则此包将用于未为其他包显式定义的所有游戏版本。<br>**重要：** 每个创意工坊模组的 versions.sii 中只能包含*一个*未指定此参数的 `package_version_info` 单元。 |
| informational | bool | 可选 | 当为 true 时，表示该包仅包含信息。如果未指定，则默认为 false。 |

## 原始单元定义

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

## 另见

[教程：如何使用模组版本控制](../../../Tutorials/SCS%20Workshop%20Uploader/How%20to%20use%20mod%20versioning.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/package_version_info | revision: 5191 | captured: 2026-10-21 23:56:14 -->
