# Documentation/Tools/SCS Blender Tools/SCS Tools in Tool Shelf/VColoring

![SCS_Tools_VColoring.png](../../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/SCS%20Tools%20in%20Tool%20Shelf/VColoring/SCS_Tools_VColoring.png)

Special tool for compositing final vertex color from 4 independent layers. Tool can be found inside [SCS Tools in Tool Shelf](../SCS%20Tools%20in%20Tool%20Shelf.md) under button named **VColoring**.

Purpose of this operator is to have 4 separated channels: Color, Decal, AO and AO2 which are mixed in real time to final vertex color. So this gives you ability to have different kind of information saved separately. Each channel is usually used like this:

- **Color** - this layer should be saving only color information.
- **Decal** - this layer defines alpha channel which is in some shaders used to blend between different textures or materials.
- **AO** - this layer should be incorporating fake global illumination ambient occlusion. So usually it consists of gradient where bottom is dark and top is brighter.
- **AO2** - this layer should be used for micro shadows, actual ambient occlusion.

This tool was designed for map assets creation as their pipeline is very much depended on vertex color, however one can still use this tool for any other model too.

## Usage

Once you enter VColoring you will see four buttons: "**Edit Color**", "**Edit Decal**", "**Edit AO**" and "**Edit AO2**" with which you select currently active layer for painting. Currently active layer is marked with dot.

To exit editing you can either use "**Exit**" button or press ESC.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/SCS_Tools_in_Tool_Shelf/VColoring | revision: 3448 | captured: 2026-10-21 23:56:14 -->
