# 文档/引擎/单元

## 什么是单元？

单元是 SCS 游戏引擎内部的对象。其核心能力之一是能够被序列化或反序列化，这使其成为让内容创作者定义游戏各个部分的理想工具。

单元具有：

- 名称——单元可以无名，也可以带有指定名称。单元名称被划分为多个组件，这些组件是以点分隔的 12 字符 token——例如正确的单元名称是 `vehicle.dummy.truck`，错误的则是 `vehicledummytruck`；不过在大多数情况下你不应使用它们，因为如果某个模组使用了 `vehicle.dummy.truck` 这一名称，而你也使用了，你的模组将无法加载。要创建无名单元，只需为单元名称加上点作为前缀，例如 `.my_mod.nameless.units`
- 属性——属性是单元可以存储的一组数据，可以是数字、文本、与其他单元的连接、这些内容的集合等。

### SII 文件

单元存储在 SII 文件中。游戏引擎支持两种版本的此类文件：纯文本和二进制。不过，定义只使用纯文本格式。

#### 结构

魔法标记——用于检查文件是否为真正的 SII 文件。

```
SiiNunit
```

左花括号，用于明确表示全局文件作用域的开始

```
{
```

在此处放置你的单元定义

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

SiiNunit 的右花括号

```
}
```

始终最好在文件末尾添加一个空行。

#### 单元定义条目

单元定义条目的格式为：

```
class name : unit name
{
    attributes
}
```

#### 注释

你可以使用类似 C 的多行注释语法来注释部分数据，注释以 `/*` 开头，以 `*/` 结尾。

**示例：**

```
/* Definition of some unit.
 *
 * Author: You */
some_unit : .my_mod.unit
{
}
```

此外，你还可以使用以 `#` 或 `//` 开头的单行注释。

**示例：**

```
some_unit : .my_mod.unit // Some unit
{
    # This value should be tweaked after users feedback
    some_value: 45.875
}
```

#### 包含

你还可以使用 SII 预处理器指令 `@include` 来包含其他文件的内容。被包含文件的内容会像它原本就在该文件中一样被读取。

**示例：**<br> *some_file_using_include.sii*

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

*游戏“看到” some_file_using_include.sii 的样子：*

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

你可能会注意到使用了新的扩展名——**.sui**。它用于不含魔法标记 `SiiNunit` 的单元序列化文件，这些文件会被包含在其他不同文件中。我们也建议你使用这一扩展名。

> **注意：** `@include` 指令必须出现在新行的开头，其前面不能有任何空白字符（空格、制表符等）。以下示例**不会**生效：
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

### 属性类型

| 类型 | 值 | 示例 | 备注 |
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
| token | x | attribute: value | token 是长度不超过 12 个字符的字符串，只能使用小写字母数字字符和下划线 [`a-z0-9_`] |
| 所有者指针（owner_ptr） | x | attribute: .some.nameless.unit | **owner_ptr** 指向在同一 SiiNunit 中定义的单元（例如 `.trailer.tchassis`） |
| 链接指针（link_ptr） | x | attribute: some.named.unit | **link_ptr** 指向在其他位置定义的有名单元（例如 `cabin_a.brand.model.cabin`） |
| resource_tie | "x" | attribute: "path/to/some/resource.pma" | **resource_tie** 通常用于将动画绑定到动画模型。其语法与 'string' 类型属性相同。 |

#### 数组

你也可以使用值的数组。数组语法为：

```
attribute_name[]: value
attribute_name[]: value2
attribute_name[]: value3
```

在某些情况下，你可能会看到以这种格式编写的固定数组：

```
attribute_name: 3           <-- Size of the array.
attribute_name[0]: 1        <-- 1st element
attribute_name[1]: 5        <-- 2nd element
attribute_name[2]: 9        <-- 3rd element
```

## 已记录的单元类型

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
