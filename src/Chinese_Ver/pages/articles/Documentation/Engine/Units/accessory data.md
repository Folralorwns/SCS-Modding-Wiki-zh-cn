# 文档/引擎/单元/配件数据

**accessory_data** 单元类是所有 *accessory_*_data* 类的超类，它定义了基本的 UI 属性以及配件之间的兼容性/交互。它通常不会*直接*使用，因为它既不影响车辆的外观，也不影响车辆的物理特性。相反，更专门的子类从它派生而来，以定义特定的配件类型。基本上，可以把 **accessory_data** 视为所有 *accessory_*_data* 类所派生的模板。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| name | string |  | 用于 UI 显示的配件完整名称。 |
| short_name | string |  | 用于在空间有限或完整名称不适用的场景中 UI 显示的配件简略名称。 |
| icon | string |  | 相对于 `/material/ui/accessory/` 的配件图标路径，省略文件扩展名。例如，`icon: "truck_name/fancy_doodad"` 将指向 `/material/ui/accessory/truck_name/fancy_doodad.mat`。 |
| info | array&lt;string&gt; |  | 关于配件的附加信息。仍使用此项进行 UI 显示的配件类型很少（例如发动机）。 |
| price | s64 | 0 | 商店中配件的价格，以基础货币计（ETS2 → EUR，ATS → USD）。如果为零，玩家将看不到该配件。 |
| unlock | uint | 0 | 配件在商店中可用之前玩家必须达到的最低等级。 |
| part_type | token | `unknown` | 它定义配件上显示的图标和工具提示。可用的值为 `factory`、`aftermarket`、`licensed` 或 `unknown`。*在 1.44 中添加。* |
| suitable_for | array&lt;string&gt; |  | 每个数组成员指定一个单元名称——或使用通配符（*）的模式——该单元必须存在于车辆上，此配件才会在商店中可见并可应用于车辆。 |
| conflict_with | array&lt;string&gt; |  | 每个数组成员指定一个单元名称——或使用通配符（*）的模式——此配件与之不兼容。如果应用此配件，冲突的配件将从车辆上移除。 |
| defaults | array&lt;string&gt; |  | 每个数组成员指定一个配件定义文件的路径，如果车辆上不存在同类型的其他合适配件，则将该文件应用于车辆。 |
| overrides | array&lt;string&gt; |  | 每个数组成员指定一个配件定义文件的路径，该文件会应用于车辆；如果车辆上已存在同类型的其他配件，则会覆盖它们。这在大多数情况下消除了对 suitable_for/defaults 关系的需求（例如发动机徽标和声音）。*在 ETS 1.27/ATS 1.6 中添加。* |
| require | array&lt;token&gt; |  | 每个数组成员指定一个配件类型，在安装此配件时该类型必须存在于车辆上。例如，如果卡车有独立的挡泥板和挡泥板支架配件，每个支架配件可能会声明 `require[]: mudflaps`，以禁止卡车有挡泥板支架但没有挡泥板的状态。该 token 是每个单元名称的最后一段，因此匹配的配件其单元名称会类似 `foo.bar.mudflaps`。**注意：** 每个 *require*d 配件类型都**始终**应该在 *defaults* 中有该类型的对应配件！ |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_data | revision: 5078 | captured: 2026-10-21 23:56:14 -->
