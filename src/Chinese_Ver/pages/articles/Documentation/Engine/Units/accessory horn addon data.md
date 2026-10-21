# 文档/引擎/单元/配件喇叭附加数据

**accessory_horn_addon_data** 单元类是 [**accessory_addon_data**](accessory%20addon%20data.md) 的扩展，专门用于气喇叭配件。其功能与 **accessory_addon_data** 相同，只是增加了 *sound_path* 属性，用于将喇叭声音事件绑定到配件。它最常用于[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)的定制。此单元类型于 1.38 中加入。

## 属性

许多通用属性继承自父类 [**accessory_addon_data**](accessory%20addon%20data.md) 和 [**accessory_data**](accessory%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| sound_path | string |  | 用于喇叭配件的声音库/事件或 soundref 的路径。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_horn_addon_data | revision: 4786 | captured: 2026-10-21 23:56:14 -->
