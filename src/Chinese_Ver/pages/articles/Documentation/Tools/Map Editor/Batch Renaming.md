# 文档/工具/地图编辑器/批量重命名

编辑器现在支持根据配置文件对某些类型的对象进行批量重命名。首先你需要准备描述应应用哪些更改的配置文件（见下文）。之后你需要在编辑器中加载地图，按 **F3** 打开替换对话框，按 **批量替换** 按钮并确认更改。之后应保存并重新加载地图。

该操作要求操作期间新旧名称对应的单元都存在，因此你需要分步执行：先向定义中添加使用新名称的单元，然后执行重命名，之后再从定义中移除使用旧名称的单元。

配置文件必须保存为 **Documents\Euro Truck Simulator 2\replace.sii** 或 **Documents\American Truck Simulator\replace.sii**。该文件必须包含一个类型为 **editor_search_replace** 的单元。该单元包含字符串数组属性 **sectors**，其中必须包含要应用更改的所有扇区的名称。扇区名称对应存储该扇区的文件的基础名称（例如 sec+0001-0001）。该单元还包含定义替换的其他字符串数组属性。替换字符串的格式为 “old_name|new_name”。支持以下数组：

> **注意：** 请在批准前补充任何新的数组，例如我在 ATS 的替换文件中见过 *road_template* 和 *prefab_model*。

- **ter_material** - 地形材质
- **road_material** - 道路材质
- **sidewalk_material** - 人行道材质
- **bld_scheme** - 建筑方案
- **model** - 模型
- **mover** - 移动对象
- **walker** - 步行者/行人
- **vegetation** - 植被
- **road_look** - 道路外观
- **ter_profile** - 地形轮廓
- **railing** - 道路上的护栏
- **sign** - 道路旁的路灯/护柱

替换文件示例：

```
SiiNunit
{
editor_search_replace : .edit_replace
{
# List of sectors where the search replace should be performed
# If you want to search everywhere in the map use the wildcard character "*"

sectors[]: "sec-0002-0007"
sectors[]: "sec-0002-0008"

# Terrain material replacement old terrain material unit suffix | new terrain material unit suffix

ter_material[]: "24|121"
ter_material[]: "103|129"

# Building scheme replacement old scheme unit suffix | new scheme unit suffix

bld_scheme[]: "22|2sc"

# Model replacement old model unit suffix | new model unit suffix

model[]: "122|1sc"
model[]: "757|2sc"
model[]: "56a|3sc"
}
}
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/Batch_Renaming | revision: 3380 | captured: 2026-10-21 23:56:14 -->
