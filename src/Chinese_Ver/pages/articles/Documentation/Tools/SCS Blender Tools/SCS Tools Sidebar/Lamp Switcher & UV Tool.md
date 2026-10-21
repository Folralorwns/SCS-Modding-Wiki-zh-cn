# 文档/工具/SCS Blender Tools/SCS Tools 侧边栏/灯光切换器与 UV 工具

任何使用灯光着色器的材质都有特定的纹理与 UV 映射配置（参见 [灯光系统](../Materials/Lamp%20system.md)）。

因此 Blender Tools 提供了这两个额外工具，以便轻松将 UV 映射对应到正确的纹理区块，并预览预期结果。

## 灯光切换器

灯光切换器是一种预览工具，用于开启和关闭当前所有已创建材质中的不同类型灯光。

开启任一类型的灯光后，使用灯光材质的网格上会出现变亮的表面。如果在 3D 视图中看不到任何变化，则可能是网格的 UV 映射有问题，或者遮罩纹理未正确创建。灯光切换器位于 3D 视图的 SCS Tools 面板下，包含三个分组：

- **Vehicle** - 用于切换车辆灯光
- **Auxiliary** - 用于切换车辆辅助灯光
- **Traffic Lights** - 用于切换交通信号灯

[![SCS_Tools_Sidebar_-_Lamp_Switcher.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20Sidebar/Lamp%20Switcher%20&%20UV%20Tool/SCS_Tools_Sidebar_-_Lamp_Switcher.280.png)](../../../../../files/SCS%20Tools%20Sidebar%20-%20Lamp%20Switcher.280.png.md)

## 灯光 UV 工具

灯光 UV 工具是用于定位选中面 UV 映射的辅助工具。该工具会在灯光材质中遮罩纹理所使用的 UV 层上重新定位映射。

该工具只能在网格对象的 “Edit Mode” 下使用。按下任一按钮后，工具会根据所选的车辆侧位、辅助灯颜色或交通信号灯颜色，自动将选中面的 UV 映射重新定位到正确的纹理区块：

- **Vehicle** - UV 映射根据车辆侧位进行定位。
- **Auxiliary** - UV 映射根据辅助灯的亮起颜色进行定位。
- **Traffic Lights** - UV 映射根据交通信号灯的颜色进行定位。

[![SCS_Tools_Sidebar_-_Lamp_UV_Tool.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20Sidebar/Lamp%20Switcher%20&%20UV%20Tool/SCS_Tools_Sidebar_-_Lamp_UV_Tool.280.png)](../../../../../files/SCS%20Tools%20Sidebar%20-%20Lamp%20UV%20Tool.280.png.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/SCS_Tools_Sidebar/Lamp_Switcher_%26_UV_Tool | revision: 4349 | captured: 2026-10-21 23:56:14 -->
