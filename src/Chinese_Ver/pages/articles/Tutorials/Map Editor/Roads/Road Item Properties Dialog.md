# 教程/地图编辑器/道路/道路项属性对话框

> [← 上一部分](Road%20Item%20Default%20Properties%20Dialog.md)[下一部分 →](Creating%20a%20Simple%20Road.md)
>
> [所有步骤](../Roads.md)

如果我们点击项属性（*P 键*），然后点击道路块，就会得到一个新的对话框，其中显示我们道路的所有选项。此处列出的大多数选项与上一个对话框类似。下面列出的是新增项。

![Road_item_properties.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_item_properties.png)

## 主对话框

|  |  |
| --- | --- |
| **可视距离**（*滑块*） | 对象可见的距离，单位为米 |

![Road_prop_checkboxes.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/768px-Road_prop_checkboxes.png)

|  | 复选框 |
| --- | --- |
| **高多边形道路** | 启用更多地形的四边形；适合使用笔刷工具混合地形 |
| **低多边形植被** | 为提升性能而使用的低质量植被 |
| **超精细** | &lt;已废弃&gt; |
| **隧道道路** | &lt;已废弃&gt; 请使用 `Weather area` |
| **无碰撞** | 关闭道路块的碰撞 |
| **忽略切割平面** | 道路项忽略切割平面并照常加载 |
| **地形阴影** | 地形在道路块上投射阴影 |
| **在 UI 地图中显示** | 在 GPS 上显示道路并启用导航 |
| **水面反射** | 道路在水面上产生反射 |
| **平滑细节植被** | 地形与笔刷之间的平滑过渡 |
| **无 AI 车辆** | 禁用所选道路的 AI 交通 |
| **左侧通行** | 为左侧通行的交通反转道路上的 AI 路径 |
| **GPS 避让** | 游戏在导航时会忽略该道路块 |
| **无边界** | 移除道路周围的无形墙 |
| **拉伸地形** | &lt;已废弃&gt; |
| **秘密道路** | 道路只有被发现后才会显示在 GPS 上 |

![Road_prop_terrain_size.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/Road_prop_terrain_size.png)

|  |  |
| --- | --- |
| **地形尺寸** | 地形从道路模型向外延伸的尺寸，单位为米 |
| **道路高度偏移** | 地形的高度偏移，单位为米 |
| **路肩受阻** | 禁止在靠近道路边缘处生成项 |

![Road_prop_profile.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/Road_prop_profile.png)

|  |  |
| --- | --- |
| **轮廓** | 预定义的地形形状 |

## 植被选项卡

![Road_properties_vegetation.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_properties_vegetation.png)

3 个下拉框，用于选择 `/def/world/vegetation.sii` 中定义的 3 种不同植被模型

|  |  |
| --- | --- |
| **稀疏度** | 植被的密度；数值越低 = 密度越高 |
| **从/到** | 所选植被模型在地形上出现的距离区间，单位为米 |

## 模型选项卡

![Road_properties_model.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_properties_model.png)

2 个用于选择模型的下拉框；这些模型会作为按距离间隔重复的对象使用，例如路灯、标志牌、立柱等。

## 护栏选项卡

![Road_properties_railing.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_properties_railing.png)

3 个用于选择模型的下拉框；这些模型会作为连续对象使用，例如护栏、隧道墙、桥梁墙等。

## 覆盖选项卡

![Road_prroperties_overrides.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_prroperties_overrides.png)

用于覆盖道路块上的变体和边缘，为同一道路块添加多种外观/边缘

## 杂项选项卡

![Road_properties_misc.png](../../../../../../images/articles/Tutorials/Map%20Editor/Roads/Road%20Item%20Properties%20Dialog/1024px-Road_properties_misc.png)

可在此开启/关闭道路模型支持的其他部件

> [← 上一部分](Road%20Item%20Default%20Properties%20Dialog.md)[下一部分 →](Creating%20a%20Simple%20Road.md)
>
> [所有步骤](../Roads.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Roads/Road_Item_Properties_Dialog | revision: 5458 | captured: 2026-10-21 23:56:14 -->
