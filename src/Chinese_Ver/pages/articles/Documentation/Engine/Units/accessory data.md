# Documentation/Engine/Units/accessory data

The **accessory_data** unit class is the superclass for all *accessory_*_data* classes and defines basic UI attributes and compatibility/interactions between accessories. It is generally not used *directly* because it doesn't affect the vehicle visually or physically. Instead, more specialized subclasses have been derived from it to define specific accessory types. Basically, think of **accessory_data** as a template from which all *accessory_*_data* classes have been derived.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| name | string |  | Full name of the accessory for UI display. |
| short_name | string |  | Condensed name of the accessory for UI display in contexts with limited space or where full names are otherwise ill-suited. |
| icon | string |  | Path relative to `/material/ui/accessory/` to the icon for the accessory, omitting the file extension. For example, `icon: "truck_name/fancy_doodad"` would point to `/material/ui/accessory/truck_name/fancy_doodad.mat`. |
| info | array&lt;string&gt; |  | Additional information about the accessory. Few accessory types still use this for UI display (e.g. engine). |
| price | s64 | 0 | The price of the accessory in the store in the base currency (ETS2 → EUR, ATS → USD). If zero, the accessory will not be visible to the player. |
| unlock | uint | 0 | The minimum level the player must achieve before the accessory becomes available in the store. |
| part_type | token | `unknown` | It defines icon and tooltip shown on accessory. Available values are `factory`, `aftermarket`, `licensed` or `unknown`. *Added in 1.44.* |
| suitable_for | array&lt;string&gt; |  | Each array member specifies a unit name — or a pattern using wildcards (*) — which must be present on the vehicle for this accessory to become visible in the store and applicable to the vehicle. |
| conflict_with | array&lt;string&gt; |  | Each array member specifies a unit name — or a pattern using wildcards (*) — with which this accessory is incompatible. The conflicting accessories will be removed from the vehicle if this accessory is applied. |
| defaults | array&lt;string&gt; |  | Each array member specifies a path to an accessory definition file which is applied to the vehicle if no other suitable accessory of the same type exists on the vehicle. |
| overrides | array&lt;string&gt; |  | Each array member specifies a path to an accessory definition file which is applied to the vehicle, overriding other accessories of the same type if one already exists on the vehicle. This eliminates the need for suitable_for/defaults relationships in most cases (e.g. engine badges and sounds). *Added in ETS 1.27/ATS 1.6.* |
| require | array&lt;token&gt; |  | Each array member specifies an accessory type that must exist on the vehicle while this accessory is installed. For example, if a truck has separate accessories for mudflaps and mudflap hangers, each hanger accessory might declare `require[]: mudflaps` to disallow a state where the truck has mudflap hangers but no mudflaps. The token is the final segment of each unit name, so matching accessories would have unit names like `foo.bar.mudflaps`. **Note:** Every *require*d accessory type should **always** have a corresponding accessory of that type in *defaults*! |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_data | revision: 5078 | captured: 2026-10-21 23:56:14 -->
