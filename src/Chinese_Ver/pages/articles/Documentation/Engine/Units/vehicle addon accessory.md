# 文档/引擎/单元/车辆附加配件

**vehicle_addon_accessory** 单元类用于将附加配件、其数据以及带槽位的挂接点“附加”到车辆和挂车配置上。此类型的单元通常为无名单元，并在拥有/使用它们的配置所在的同一上下文中声明。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| wear | float | 0.0 | 此属性用于跟踪配件的损坏和磨损情况。0 对应未磨损状态，1 对应完全磨损状态。 |
| **data_path** | string |  | 包含合适配件数据单元的 SII 文件的完整路径。 |
| slot_name | array&lt;token&gt; |  | 配件模型中供挂接配件挂接到其上的模型定位器名称。有效名称以 `slot_` 开头。 |
| slot_hookup | array&lt;string&gt; |  | 要在对应 **slot_name** 中挂接的附加挂接点的单元名称。 |

> **注意：** **slot_name** 和 **slot_hookup** 数组通常定义为有序数组，以确保它们的索引相互对应。它们的长度必须始终相同。

## 槽位用法示例

以下示例展示了在卡车配置中，示廓灯如何挂接到 *cabflares* 配件上的槽位：

```
vehicle: .tdealer.peterbilt_4
{
    // ...
    accessories[]: .peterbilt_4.lights
    // ...
}
// ...
vehicle_addon_accessory : .peterbilt_4.lights {
    slot_name: 5
    slot_name[0]: slot_0
    slot_name[1]: slot_2
    slot_name[2]: slot_3
    slot_name[3]: slot_4
    slot_name[4]: slot_6
    slot_hookup: 5
    slot_hookup[0]: "light2.addon_hookup"
    slot_hookup[1]: "light2.addon_hookup"
    slot_hookup[2]: "light2.addon_hookup"
    slot_hookup[3]: "light2.addon_hookup"
    slot_hookup[4]: "light2.addon_hookup"

    wear: 0
    data_path: "/def/vehicle/truck/peterbilt.579/accessory/cabflares/shape01.sii"
}
// ...
```

## 适用的配件数据类型

以下配件数据类型可用于 **vehicle_addon_accessory** 的 **data_path** 属性：

- [accessory_addon_data](accessory%20addon%20data.md)
- [accessory_addon_int_data](accessory%20addon%20int%20data.md)
- [accessory_addon_patch_data](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/accessory_addon_patch_data&action=edit&redlink=1)

以下配件数据类型可挂接到该配件的槽位：

- [accessory_hookup_data](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/accessory_hookup_data&action=edit&redlink=1)
- [accessory_hookup_int_data](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/accessory_hookup_int_data&action=edit&redlink=1)
- [accessory_horn_hookup_data](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/accessory_horn_hookup_data&action=edit&redlink=1)

## 相关单元

- [traffic_trailer](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_trailer&action=edit&redlink=1)
- [traffic_vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/traffic_vehicle&action=edit&redlink=1)
- [trailer](trailer.md)
- [vehicle](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle&action=edit&redlink=1)
- [vehicle_accessory](vehicle%20accessory.md)
- [vehicle_paint_job_accessory](vehicle%20paint%20job%20accessory.md)
- [vehicle_sound_accessory](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/vehicle_sound_accessory&action=edit&redlink=1)
- [vehicle_wheel_accessory](vehicle%20wheel%20accessory.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/vehicle_addon_accessory | revision: 3320 | captured: 2026-10-21 23:56:14 -->
