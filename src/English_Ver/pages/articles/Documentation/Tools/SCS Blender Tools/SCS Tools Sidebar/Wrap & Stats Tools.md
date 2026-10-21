# Documentation/Tools/SCS Blender Tools/SCS Tools Sidebar/Wrap & Stats Tools

Almost all shaders inside SCS Game engine are using vertex colors. That's why it's very important how you set them.

If shader explicitly doesn't specify otherwise, then vertex colors with values 0.5 are actually neutral colors and won't change the look of resulting mesh inside game. If vertex colors are below 0.5 it will "darken" the model and what will be above 0.5 will result in "brighter" mesh.

## Wrap Tool

In addition to this there is Wrap Tool which helps you wrap vertex colors of active vertex color layer on specified interval. So if you baked or painted your model on the range from 0 to 1 you can easily use this tools to scale this interval to the one you define in operator properties (advised interval is from 0.4 to 0.6). Tool can be found in SCS Tools shelf if current object is in "Vertex Paint" mode.

[![SCS_Tools_Sidebar_-_Wrap_Tool.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20Sidebar/Wrap%20&%20Stats%20Tools/SCS_Tools_Sidebar_-_Wrap_Tool.280.png)](../../../../../files/SCS%20Tools%20Sidebar%20-%20Wrap%20Tool.280.png.md)

- **Wrap All** - wrap vertex colors on all vertices.
- **Wrap Selected** - wrap vertex colors only on selected vertices.

## Stats Tool

As Blender doesn't have any proper number statistics over currently set vertex colors, this tool enables you to print out minimum, maximum and average vertex colors values for the mesh.

[![SCS_Tools_Sidebar_-_Stats_Tool.280.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20Sidebar/Wrap%20&%20Stats%20Tools/SCS_Tools_Sidebar_-_Stats_Tool.280.png)](../../../../../files/SCS%20Tools%20Sidebar%20-%20Stats%20Tool.280.png.md)

- **Get Statistics** - output statistic to console and Blender status bar.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/SCS_Tools_Sidebar/Wrap_%26_Stats_Tools | revision: 4353 | captured: 2026-10-21 23:56:14 -->
