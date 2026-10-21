# 文档/工具/SCS Blender Tools/SCS Tools 工具架/灯光切换器与 UV 工具

任何使用灯光着色器的材质都有特定的纹理配置和 UV 映射（参见[灯光系统](../Materials/Lamp%20system.md)）。

因此 Blender Tools 提供了这两个附加工具，以便轻松地将 UV 映射对应到正确的纹理图块，并预览所需的结果。

## 灯光切换器

灯光切换器是一个预览工具，用于在当前创建的所有材质中开启和关闭不同类型的灯光。

开启任一类型的灯光时，你会看到使用灯光材质的网格表面变亮。如果你在 3D 视图中看不到任何变化，则可能是网格的 UV 映射有问题，或遮罩纹理创建不正确。灯光切换器可在 3D 视图的 SCS Tools 面板下找到，包含三个分组：

- **Vehicle** - 用于切换车辆灯光
- **Auxiliary** - 用于切换车辆辅助灯光
- **Traffic Lights** - 用于切换交通信号灯

> > **注意：** 要在 3D 视图中看到变化，你应使用 GLSL 着色模式，并在至少一个对象上使用至少一个灯光材质。

[![SCS_Tools_Shelf_-_Lamp_Switcher.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/Lamp%20Switcher%20&%20UV%20Tool/SCS_Tools_Shelf_-_Lamp_Switcher.png)](../../../../../files/SCS%20Tools%20Shelf%20-%20Lamp%20Switcher.png.md)

## 灯光 UV 工具

灯光 UV 工具是用于定位选中面 UV 映射的辅助工具。该工具会在灯光材质中遮罩纹理所使用的 UV 层上重新放置映射。

你只能在网格对象的 “Edit Mode” 中使用此工具。按下任一按钮，该工具都会根据所选车辆侧面、辅助灯颜色或交通信号灯颜色，自动将选中面的 UV 映射重新放置到正确的纹理图块：

- **Vehicle** - UV 映射会根据车辆侧面放置。
- **Auxiliary** - UV 映射会根据辅助灯的亮起颜色放置。
- **Traffic Lights** - UV 映射会根据交通信号灯的颜色放置。

[![SCS_Tools_Shelf_-_Lamp_UV_Tool.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/Lamp%20Switcher%20&%20UV%20Tool/SCS_Tools_Shelf_-_Lamp_UV_Tool.png)](../../../../../files/SCS%20Tools%20Shelf%20-%20Lamp%20UV%20Tool.png.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/SCS_Tools_in_Tool_Shelf/Lamp_Switcher_%26_UV_Tool | revision: 2890 | captured: 2026-10-21 23:56:14 -->
