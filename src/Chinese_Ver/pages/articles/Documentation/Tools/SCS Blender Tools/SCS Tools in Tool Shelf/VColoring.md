# 文档/工具/SCS Blender Tools/SCS Tools 工具架/VColoring

![SCS_Tools_VColoring.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/VColoring/SCS_Tools_VColoring.png)

用于将 4 个独立层合成为最终顶点颜色的专用工具。该工具可在 [SCS Tools 工具架](../SCS%20Tools%20in%20Tool%20Shelf.md) 中名为 **VColoring** 的按钮下找到。

此操作符的用途是提供 4 个分离的通道：Color、Decal、AO 和 AO2，它们会被实时混合为最终顶点颜色。这样你就能将不同种类的信息分别保存。每个通道通常这样使用：

- **Color** - 该层应只保存颜色信息。
- **Decal** - 该层定义 alpha 通道，某些着色器用它来在不同纹理或材质之间进行混合。
- **AO** - 该层应包含伪造的全局光照环境光遮蔽。因此它通常由渐变构成，底部较暗、顶部较亮。
- **AO2** - 该层应用于微小阴影，即真实的环境光遮蔽。

此工具是为地图资产创作而设计的，因为其流程非常依赖于顶点颜色，不过你也可以将其用于任何其他模型。

## 用法

进入 VColoring 后，你会看到四个按钮：“**Edit Color**”、“**Edit Decal**”、“**Edit AO**” 和 “**Edit AO2**”，用它们选择当前用于绘制的活动层。当前活动层以圆点标记。

要退出编辑，你可以使用 “**Exit**” 按钮，或按 ESC 键。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/SCS_Tools_in_Tool_Shelf/VColoring | revision: 3448 | captured: 2026-10-21 23:56:14 -->
