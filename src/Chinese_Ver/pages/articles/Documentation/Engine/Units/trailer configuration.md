# 文档/引擎/单元/挂车配置

**trailer_configuration** 单元类用于收集可拥有挂车某一配置的底盘，定义哪些车身组对该配置有效，并定义在挂车配置用途下哪些配置是“等效”的。此类型的单元通常位于 **/def/vehicle/trailer_owned/<brand.model>/configurations/**

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| **name** | string |  | 用于 UI 显示的配置完整名称。 |
| icon | string |  | 配件图标相对于 `/material/ui/accessory/` 的路径，省略文件扩展名。例如，`icon: "truck_name/fancy_doodad"` 将指向 `/material/ui/accessory/truck_name/fancy_doodad.mat`。 |
| **chain_type** | token |  | 定义链类型（例如 single、double、rmdouble 等） |
| equivalency | token |  | 具有相同 **equivalency** token 的挂车配置可在游戏过程中通过挂车配置菜单切换。此属性必须显式设置——equivalency 属性为空的配置不会相互匹配。 |
| **chassis** | array&lt;string&gt; |  | 挂车配置的底盘定义路径数组（例如 `chassis[]: "/def/vehicle/trailer_owned/scs.box/chassis/ch_45_f.sii"`）。期望的单元类型为 [accessory_chassis_data](accessory%20chassis%20data.md)。 |
| **body_sets** | array<owner_ptr> ([trailer_body_set](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/trailer_body_set&action=edit&redlink=1)) |  | 与此配置兼容的 **trailer_body_set** 数组。此数组通常从与基础配置文件同名的子文件夹中自动收集（文件名取到第一个点为止，因此配置 "single3.sii" 或 "single3.mymod.sii" 的车身组应位于文件夹 "/def/vehicle/trailer_owned/<brand.model>/configurations/single3" 中）。车身组也可以在配置定义中显式定义并链接。每个挂车配置必须至少有一个有效的车身组。 |

## 相关单元

- [trailer_body_set](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/trailer_body_set&action=edit&redlink=1)
- [accessory_chassis_data](accessory%20chassis%20data.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/trailer_configuration | revision: 4067 | captured: 2026-10-21 23:56:14 -->
