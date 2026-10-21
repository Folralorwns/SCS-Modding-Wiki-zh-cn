# 文档/引擎/单元/配件附加数据

**accessory_addon_data** 单元类用于为车辆添加可见组件的车辆配件。它最常用于[玩家车辆](../Game%20data/Player%20trucks%20definitions.md)的定制。它定义可见模型的路径及其配置（variant、look、排除的视图），并在适用时定义碰撞网格的路径。此类型的单元位于 **/def/vehicle/truck/<brand.model>/accessory/&lt;type&gt;/*.sii** 中。

> **注意：** 一些不直接与玩家交互的旧版配件（例如徽标）由于历史原因也可能位于 **def/vehicle/truck/<brand.model>/&lt;type&gt;/*.sii** 中。因此，在创建新类型时，请始终将其创建在 **accessory** 子文件夹内。

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| exterior_model | string |  | 要在外部视图中显示的模型对应的模型描述符（.pmd）路径（如果适用）。 |
| exterior_model_uk | string |  | 右舵车辆要在外部视图中显示的模型对应的模型描述符（.pmd）路径（如果适用）。如果未设置，则默认为 **exterior_model**。 |
| interior_model | string |  | 要在内部视图中显示的模型对应的模型描述符（.pmd）路径（如果适用）。 |
| interior_model_uk | string |  | 右舵车辆要在内部视图中显示的模型对应的模型描述符（.pmd）路径（如果适用）。如果未设置，则默认为 **interior_model**。 |
| coll | string |  | 配件的碰撞描述符（.pmc）路径（如果适用）。 |
| look | token | default | 用于此配件所有描述符的 look 名称。**注意：** 一个配件的所有模型必须具有相同的 look 集合。 |
| variant | token | default | 用于此配件所有描述符的 variant 名称。**注意：** 一个配件的所有模型必须具有相同的 variant 集合。 |
| hide_in | u32 | 0 | 用于在特定视图中“隐藏”配件使其不被绘制的标志。有效值可在[此处](http://eurotrucksimulator2.com/modding_changes_114.php#Hide%20following%20views)计算。**注意：** 其模型引用的纹理包含镜面反射（例如后视镜本身）的配件**必须**标记为在后视镜中不可见。此前有专门的机制来处理这一点，但现在游戏完全依赖 hide_in 属性来处理。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_addon_data | revision: 5347 | captured: 2026-10-21 23:56:14 -->
