# Documentation/Engine/Units/transmission names

The **transmission_names** unit class is used to define custom names for the gears of a transmission which are displayed in the UI and dashboard. Units of this type are usually defined in **/def/vehicle/truck/<make.model>/transmission/*.sii** or included from a Serialized Unit Includes (.sui) file and are usually nameless (the unit name is prefixed by a dot like `.names` or `.foo.bar.names`). They are assigned to a transmission accessory via the likewise-named *transmission_names* attribute of the [accessory_transmission_data](accessory%20transmission%20data.md) unit class.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Description |
| --- | --- | --- |
| neutral | string | The gear name to be displayed when the transmission is in neutral. |
| reverse | array&lt;string&gt; | The gear names to be displayed for reverse gears. The array indices correspond to those in the *ratios_reverse* attribute of the parent *accessory_transmission_data* unit. |
| forward | array&lt;string&gt; | The gear names to be displayed for reverse gears. The array indices correspond to those in the *ratios_forward* attribute of the parent *accessory_transmission_data* unit. |

> **Note:** While not a hard limit, it is advisable to keep the length of the gear names within three characters to avoid truncation, etc when displayed.

## Example of an Embedded *transmission_names* Unit

The most typical usage is to embed the **transmission_names** within the same file as the **accessory_transmission_data** unit it belongs to. Here's an example of an *8LL* (8 + 2 crawler gears) using custom gear names within the same SiiNunit.

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

## Example of an Included *transmission_names* Unit

If a project is going to have a large number of transmissions using custom gear names and many will use the same custom gear names, it may be convenient to instead write a single .sui file with all unique instances of *transmission_names* and [include](../Units.md#Includes) it in the transmission definitions as needed. Let's say the earlier, embedded example is part of a larger set of transmissions using a handful of custom gear name sets.

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

> **Note:** Observe that the include occurs *outside* the scope of the *accessory_transmission_data* unit, but *within* the scope of the SiiNunit.

> **TIP:** It is helpful in this case to use more descriptive (but still nameless) unit names for the *transmission_names* units so that it's still possible to intuit which unit is being assigned to the transmission definition without needing to open the included file.

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

> **Note:** Because the *transmission_names* units are nameless, the "gear_names.sui" file can be included in many transmission definitions without fear of namespace collisions because nameless units only exist within the scope of the SiiNunit in which they are declared. However, nameless units *within* an SiiNunit **must** have unique names within that scope.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/transmission_names | revision: 3176 | captured: 2026-10-21 23:56:14 -->
