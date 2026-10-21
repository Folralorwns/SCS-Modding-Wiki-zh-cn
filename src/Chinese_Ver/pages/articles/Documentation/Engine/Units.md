# Documentation/Engine/Units

## What is unit?

Units are objects inside SCS game engine. One of their core abilities is so they can be serialized or deserialized making it a perfect tool to give content creators a way to define various parts of the games.

Unit has:

- Name - units can be nameless or have some specified name. Unit names are divided into components which are 12-char tokens separated by dot - for example correct unit name will be `vehicle.dummy.truck` incorrect will be `vehicledummytruck` however in most cases you should not use them, in case some mod is using name `vehicle.dummy.truck` and you will also use this your mod will fail to load. To create nameless unit simply use dot as the prefix for your unit name for example `.my_mod.nameless.units`
- Attributes - attributes are set of the data that unit can store, it can be number, text, other unit connection, set of them etc.

### SII files

Units are stored in SII files. There are two versions of this file supported by the game engine: plain-text and binary. However, only the plain-text format is used for definitions.

#### Structure

The magic mark – used to check if the file is a real SII file or not.

```
SiiNunit
```

The opening bracket used to explicitly show the global file scope start

```
{
```

Here you put your unit definitions

```
some_unit : .my_mod.unit
{
    attribute_number: 40
    attribute_string: "TEST STRING"
    attribute_unit: test.unit
    attribute_float3: (1.0, 1.0, 1.0)
    attribute_float_number_ieee754: &40490f5a
}
```

The closing bracket for the SiiNunit

```
}
```

It's always good to add one blank line at the end of the file.

#### Unit definition entry

Unit definition entry format is:

```
class name : unit name
{
    attributes
}
```

#### Comments

You can comment some of your data using C-like multi-line comments syntax starting from `/*` and ending with `*/`.

**Example:**

```
/* Definition of some unit.
 *
 * Author: You */
some_unit : .my_mod.unit
{
}
```

Also you can use one-line comments which start from `#` or `//`.

**Example:**

```
some_unit : .my_mod.unit // Some unit
{
    # This value should be tweaked after users feedback
    some_value: 45.875
}
```

#### Includes

You can also include the contents of other files using the SII preprocessor directive - `@include`. The contents of the included file will be read as if they were in the file itself.

**Example:**<br> *some_file_using_include.sii*

```
SiiNunit
{
example: doing.includes
{
    foo: "bar"
    over: 9000
@include "some_file_to_include.sui"
}
}
```

*some_file_to_include.sui:*

```
    ninjas: true
```

*How the game “sees” some_file_using_include.sii:*

```
SiiNunit
{
example: doing.includes
{
    foo: "bar"
    over: 9000
    ninjas: true
}
}
```

You may notice usage of the new extension - **.sui**. It's used for unit serialized files without magic mark `SiiNunit` that are included somewhere in different files. We recommend you also use this extension.

> **Note:** The `@include` directive must appear at the beginning of a new line with no whitespace (space, tab, etc) before it. The following examples will **not** work:
>
> ```
> SiiNunit
> {
> bad_examples: just.the.worst {
>     foo: "bar"
>     @include "dont_get_too_attached_to_indents.sui"
>
>     foo: @include "you_definitely_cannot_use_it_inline.sui"
> }
> }
> ```

### Attribute types

| Type | Value | Example | Notes |
| --- | --- | --- | --- |
| string | "x" | attribute: "String value" |  |
| float | x | attribute: 1.0 // Using normal float-notation<br>attribute: &3f800000 // using ieee754 hexa notation |  |
| float2 | (x, y) | attribute: (1.0, 2.0) |  |
| float3 | (x, y, z) | attribute: (1.0, 5.0, 3.0) |  |
| float4 | (x, y, z, w) | attribute: (1.0, 5.0, 3.0, 9.0) |  |
| placement | (x, y, z) (w; x, y, z) | attribute: (0, 0, 0) (1; 0, 0, 0) |  |
| fixed | x | attribute: 10 |  |
| fixed2 | (x, y) | attribute: (10, 22) |  |
| fixed3 | (x, y, z) | attribute: (10, 22, 33) |  |
| fixed4 | (x, y, z, w) | attribute: (10, 22, 33, 44) |  |
| int2 | (x, y) | attribute: (20, 69) |  |
| quaternion | (w, x, y, z) | attribute: (1.0, 0.0, 0.0, 0.0) |  |
| s16 | x | attribute: -15 |  |
| s32 | x | attribute: -15 |  |
| s64 | x | attribute: -15 |  |
| u16 | x | attribute: 15 |  |
| u32 | x | attribute: 15 |  |
| u64 | x | attribute: 15 |  |
| bool (boolean) | x | attribute: true attribute: false |  |
| token | x | attribute: value | Token is a string of maximum length of 12 characters, only lowercase alphanumeric characters and underscore can be used [`a-z0-9_`] |
| owner pointer (owner_ptr) | x | attribute: .some.nameless.unit | **owner_ptr** refers to unit defined within the same SiiNunit (eg. `.trailer.tchassis`) |
| link pointer (link_ptr) | x | attribute: some.named.unit | **link_ptr** refers to a named unit that is defined elsewhere (eg. `cabin_a.brand.model.cabin`) |
| resource_tie | "x" | attribute: "path/to/some/resource.pma" | **resource_tie** is typically used to bind animations to animated models. The syntax is the same as for 'string' type attributes. |

#### Arrays

You can also use arrays of the values. The array syntax is:

```
attribute_name[]: value
attribute_name[]: value2
attribute_name[]: value3
```

In some cases you may notice fixed-arrays written in this format:

```
attribute_name: 3           <-- Size of the array.
attribute_name[0]: 1        <-- 1st element
attribute_name[1]: 5        <-- 2nd element
attribute_name[2]: 9        <-- 3rd element
```

## Documented Unit Types

- [accessory addon data](Units/accessory%20addon%20data.md)
- [accessory addon int data](Units/accessory%20addon%20int%20data.md)
- [accessory addon int ui data](Units/accessory%20addon%20int%20ui%20data.md)
- [accessory addon tank data](Units/accessory%20addon%20tank%20data.md)
- [accessory addon trailer cables data](Units/accessory%20addon%20trailer%20cables%20data.md)
- [accessory cabin data](Units/accessory%20cabin%20data.md)
- [accessory cargo data](Units/accessory%20cargo%20data.md)
- [accessory chassis data](Units/accessory%20chassis%20data.md)
- [accessory data](Units/accessory%20data.md)
- [accessory engine data](Units/accessory%20engine%20data.md)
- [accessory horn addon data](Units/accessory%20horn%20addon%20data.md)
- [accessory interior data](Units/accessory%20interior%20data.md)
- [accessory paint job data](Units/accessory%20paint%20job%20data.md)
- [accessory rim data](Units/accessory%20rim%20data.md)
- [accessory sound data](Units/accessory%20sound%20data.md)
- [accessory trailer body data](Units/accessory%20trailer%20body%20data.md)
- [accessory transmission data](Units/accessory%20transmission%20data.md)
- [accessory truck data](Units/accessory%20truck%20data.md)
- [accessory wheel data](Units/accessory%20wheel%20data.md)
- [cargo data](Units/cargo%20data.md)
- [cargo def](Units/cargo%20def.md)
- [cargo model match](Units/cargo%20model%20match.md)
- [company def](Units/company%20def.md)
- [company permanent](Units/company%20permanent.md)
- [dynamic cargo data](Units/dynamic%20cargo%20data.md)
- [glass pane data](Units/glass%20pane%20data.md)
- [journey events cutscene](Units/journey%20events%20cutscene.md)
- [journey events road event](Units/journey%20events%20road%20event.md)
- [package version info](Units/package%20version%20info.md)
- [sound data](Units/sound%20data.md)
- [sound data voice navigation](Units/sound%20data%20voice%20navigation.md)
- [sound engine data](Units/sound%20engine%20data.md)
- [sound noise data](Units/sound%20noise%20data.md)
- [trailer](Units/trailer.md)
- [trailer cable data](Units/trailer%20cable%20data.md)
- [trailer configuration](Units/trailer%20configuration.md)
- [trailer def](Units/trailer%20def.md)
- [transmission names](Units/transmission%20names.md)
- [vehicle accessory](Units/vehicle%20accessory.md)
- [vehicle addon accessory](Units/vehicle%20addon%20accessory.md)
- [vehicle animation data](Units/vehicle%20animation%20data.md)
- [vehicle paint job accessory](Units/vehicle%20paint%20job%20accessory.md)
- [vehicle wheel accessory](Units/vehicle%20wheel%20accessory.md)
- [wiper data](Units/wiper%20data.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units | revision: 5765 | captured: 2026-10-21 23:56:14 -->
