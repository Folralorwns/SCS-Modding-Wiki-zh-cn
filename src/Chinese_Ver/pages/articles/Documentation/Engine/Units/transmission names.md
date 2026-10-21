# 文档/引擎/单元/变速箱名称

**transmission_names** 单元类用于为变速箱的挡位定义自定义名称，这些名称会显示在 UI 和仪表盘中。此类型的单元通常定义在 **/def/vehicle/truck/<make.model>/transmission/*.sii** 中，或通过 Serialized Unit Includes（.sui）文件包含，并且通常为无名单元（单元名称以点号开头，如 `.names` 或 `.foo.bar.names`）。它们通过 [accessory_transmission_data](accessory%20transmission%20data.md) 单元类中同名的 *transmission_names* 属性分配给变速箱配件。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 描述 |
| --- | --- | --- |
| neutral | string | 变速箱处于空挡时显示的挡位名称。 |
| reverse | array&lt;string&gt; | 倒挡要显示的挡位名称。数组索引与父级 *accessory_transmission_data* 单元的 *ratios_reverse* 属性中的索引相对应。 |
| forward | array&lt;string&gt; | 前进挡要显示的挡位名称。数组索引与父级 *accessory_transmission_data* 单元的 *ratios_forward* 属性中的索引相对应。 |

> **注意：** 尽管并非硬性限制，但建议将挡位名称的长度控制在三个字符以内，以避免显示时出现截断等情况。

## 内嵌 *transmission_names* 单元示例

最常见的用法是将 **transmission_names** 嵌入到其所属 **accessory_transmission_data** 单元的同一文件中。以下是一个 *8LL*（8 + 2 个爬行挡）在同一 SiiNunit 内使用自定义挡位名称的示例。

**/vehicle/truck/<foo.bar>/transmission/rt8ll.sii:**

```
SiiNunit
{
accessory_transmission_data : rt8ll.foo.bar.transmission
{
	name: "Example 8LL with custom gear names"

	price: 8750
	unlock: 0
	icon: "transmission_generic"
	transmission_names: .names
	# RT-8908LL
	# ---
	# SQHD Differential Ratios: 3.70, 4.11, 4.33, 4.44, 4.63, 4.88, 5.29
	differential_ratio: 4.11
	# reverse gear
	ratios_reverse[0]: -20.47
	ratios_reverse[1]: -13.24
	ratios_reverse[2]: -3.89
	# forward gears
	ratios_forward[0]: 19.58
	ratios_forward[1]: 12.67
	ratios_forward[2]: 8.39
	ratios_forward[3]: 6.23
	ratios_forward[4]: 4.58
	ratios_forward[5]: 3.41
	ratios_forward[6]: 2.46
	ratios_forward[7]: 1.83
	ratios_forward[8]: 1.35
	ratios_forward[9]: 1.0
}
transmission_names: .names
{
	neutral: "N"
	forward[0]: "LL"
	forward[1]: "L"
	forward[2]: "1"
	forward[3]: "2"
	forward[4]: "3"
	forward[5]: "4"
	forward[6]: "5"
	forward[7]: "6"
	forward[8]: "7"
	forward[9]: "8"

	reverse[0]: "RLL"
	reverse[1]: "RL"
	reverse[2]: "RH"
}
}
```

## 包含的 *transmission_names* 单元示例

如果某个项目将有大量使用自定义挡位名称的变速箱，并且其中许多会使用相同的自定义挡位名称，那么更方便的做法可能是：编写一个包含所有唯一 *transmission_names* 实例的 .sui 文件，并按需将其[包含](../Units.md#Includes)到变速箱定义中。假设前面那个内嵌示例属于一个使用少量自定义挡位名称集的更大变速箱集合。

**/vehicle/truck/<foo.bar>/transmission/rt8ll.sii:**

```
SiiNunit
{
accessory_transmission_data : rt8ll.foo.bar.transmission
{
	name: "Example 8LL with custom gear names"

	price: 8750
	unlock: 0
	icon: "transmission_generic"
	transmission_names: .8ll.names
	# RT-8908LL
	# ---
	# SQHD Differential Ratios: 3.70, 4.11, 4.33, 4.44, 4.63, 4.88, 5.29
	differential_ratio: 4.11
	# reverse gear
	ratios_reverse[0]: -20.47
	ratios_reverse[1]: -13.24
	ratios_reverse[2]: -3.89
	# forward gears
	ratios_forward[0]: 19.58
	ratios_forward[1]: 12.67
	ratios_forward[2]: 8.39
	ratios_forward[3]: 6.23
	ratios_forward[4]: 4.58
	ratios_forward[5]: 3.41
	ratios_forward[6]: 2.46
	ratios_forward[7]: 1.83
	ratios_forward[8]: 1.35
	ratios_forward[9]: 1.0
}
@include "gear_names.sui"
}
```

> **注意：** 请注意，包含操作发生在 *accessory_transmission_data* 单元的作用域*之外*，但位于 SiiNunit 的作用域*之内*。

> **提示：** 在这种情况下，为 *transmission_names* 单元使用更具描述性（但仍为无名）的单元名称会很有帮助，这样无需打开被包含的文件，也能直观看出哪个单元被分配给了变速箱定义。

**/vehicle/truck/<foo.bar>/transmission/gear_names.sui:**

```
transmission_names: .8ll.names
{
	neutral: "N"
	forward[0]: "LL"
	forward[1]: "L"
	forward[2]: "1"
	forward[3]: "2"
	forward[4]: "3"
	forward[5]: "4"
	forward[6]: "5"
	forward[7]: "6"
	forward[8]: "7"
	forward[9]: "8"

	reverse[0]: "RLL"
	reverse[1]: "RL"
	reverse[2]: "RH"
}

transmission_names: .other.names
{
	# Other units can be defined in the same file as long as there are no namespace collisions!
}
```

> **注意：** 由于 *transmission_names* 单元是无名单元，因此可以把“gear_names.sui”文件包含到许多变速箱定义中，而不必担心命名空间冲突，因为无名单元仅存在于声明它们的 SiiNunit 的作用域内。但是，同一 SiiNunit *内部*的无名单元**必须**在该作用域内具有唯一的名称。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/transmission_names | revision: 3176 | captured: 2026-10-21 23:56:14 -->
