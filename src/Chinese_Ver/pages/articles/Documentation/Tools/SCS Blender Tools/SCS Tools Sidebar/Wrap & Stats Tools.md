# 文档/工具/SCS Blender Tools/SCS Tools 侧边栏/包裹与统计工具

SCS 游戏引擎中几乎所有着色器都使用顶点颜色。因此如何设置它们非常重要。

如果着色器没有明确另行指定，那么值为 0.5 的顶点颜色实际上是中性色，不会改变网格在游戏中的最终外观。如果顶点颜色低于 0.5，模型会“变暗”；高于 0.5 则会使网格“变亮”。

## 包裹工具

除此之外还有包裹工具，它可帮助你将活动顶点颜色层的顶点颜色包裹到指定区间。因此，如果你在 0 到 1 的范围内烘焙或绘制了模型，就可以轻松用该工具将此区间缩放到你在操作符属性中定义的区间（建议区间为 0.4 到 0.6）。若当前对象处于 “Vertex Paint” 模式，可在 SCS Tools 工具架中找到该工具。

[![SCS_Tools_Sidebar_-_Wrap_Tool.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20Sidebar/Wrap%20&%20Stats%20Tools/SCS_Tools_Sidebar_-_Wrap_Tool.280.png)](../../../../../files/SCS%20Tools%20Sidebar%20-%20Wrap%20Tool.280.png.md)

- **Wrap All** - 包裹所有顶点上的顶点颜色。
- **Wrap Selected** - 仅包裹选中顶点上的顶点颜色。

## 统计工具

由于 Blender 没有针对当前所设顶点颜色的合适数值统计，此工具可让你输出网格顶点颜色值的最小值、最大值和平均值。

[![SCS_Tools_Sidebar_-_Stats_Tool.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20Sidebar/Wrap%20&%20Stats%20Tools/SCS_Tools_Sidebar_-_Stats_Tool.280.png)](../../../../../files/SCS%20Tools%20Sidebar%20-%20Stats%20Tool.280.png.md)

- **Get Statistics** - 将统计信息输出到控制台和 Blender 状态栏。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/SCS_Tools_Sidebar/Wrap_%26_Stats_Tools | revision: 4353 | captured: 2026-10-21 23:56:14 -->
