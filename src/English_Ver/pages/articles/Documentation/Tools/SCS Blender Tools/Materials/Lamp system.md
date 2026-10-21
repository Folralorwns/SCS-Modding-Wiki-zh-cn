# Documentation/Tools/SCS Blender Tools/Materials/Lamp system

Lamp system uses "lamp" material effect to visualize extra lit surfaces by second mask texture or by alpha channel of base texture. This system is used on vehicle lights, vehicle auxiliary lights and traffic lights.

For easy usage of lamp system Blender Tools has included [Lamp Switcher & UV Tool](../SCS%20Tools%20in%20Tool%20Shelf/Lamp%20Switcher%20&%20UV%20Tool.md) which will help you with UV mappings tiling and previewing of lit surfaces directly in Blender 3D viewport.

## Vehicle lights

<table class="wikitable" style="text-align:center;float:right;">
<caption>Vehicle Lights Quick-Reference
</caption>
<tbody><tr>
<th rowspan="2">UV Tile
</th>
<th rowspan="2">Corresponding<br/>Position
</th>
<th colspan="4">Color Channel
</th></tr>
<tr>
<td style="background-color:#FF2222;"><b>R</b>
</td>
<td style="background-color:#22FF22;"><b>G</b>
</td>
<td style="background-color:#2222FF;"><b>B</b>
</td>
<td><b>A</b>
</td></tr>
<tr>
<td>0
</td>
<td>Front Left
</td>
<td style="background-color:#ffb44a;">Left Blinker
</td>
<td rowspan="2">High Beam
</td>
<td rowspan="2">Low Beam
</td>
<td rowspan="2" style="background-image:linear-gradient(to right,#ffb44a,rgba(255,255,255,0));">Positional*
</td></tr>
<tr>
<td>1
</td>
<td>Front Right
</td>
<td style="background-color:#ffb44a;">Right Blinker
</td></tr>
<tr>
<td>2
</td>
<td>Rear Left
</td>
<td style="background-image:linear-gradient(to right,#ff4a4a,#ffb44a);">Left Blinker**
</td>
<td rowspan="2" style="background-color:#ff4a4a;">Brake
</td>
<td rowspan="2">Reverse
</td>
<td rowspan="2" style="background-color:#ff4a4a;">Positional
</td></tr>
<tr>
<td>3
</td>
<td>Rear Right
</td>
<td style="background-image:linear-gradient(to right,#ff4a4a,#ffb44a);">Right Blinker**
</td></tr>
<tr>
<td>4
</td>
<td>Middle or DRL
</td>
<td>
</td>
<td>
</td>
<td>DRL
</td>
<td style="background-color:#ffb44a;">Positional
</td></tr>
<tr>
<td colspan="6"><i>*Front positional lights are white in ETS2, and orange in ATS by default as of 1.39. <br/>**Rear blinkers are orange in ETS2, and red in ATS by default.</i>
</td></tr></tbody></table>

Vehicle lights use a second RGBA mask texture from which each channel defines a luminance mask for a particular type of light:

- R - left blinker, right blinker
- G - high beam, brake
- B - low beam, reverse, daytime running (DRL)
- A - positional

The second requirement for vehicle lights to work correctly is to use a separate UV layer for the lamp mask texture and proper tile offset of the mappings. Tiling is applied on the right side of the texture in the following order:

0. original texture - front left side of vehicle
1. first texture tile - front right side of vehicle
2. second texture tile - rear left side of vehicle
3. third texture tile - rear right side of vehicle
4. fourth texture tile - middle of vehicle and DRL

## Auxiliary lights

Auxiliary lights on vehicles can also have separate second mask texture but they use only two channels from light mask texture:

- R - dimmed beam
- G - full beam
- B - not used and must be zero (black)
- A - not used and must be zero (black)

There is also possible to use two different colors for auxiliary lights with offsetting UV mappings for second mask texture. Tile offset here is also done on the right side of the texture:

0. original texture - white color
1. first texture tile - orange color

## Traffic lights

Traffic lights don't use extra second mask texture as they are using alpha channel of base texture for proper lit of traffic lights. But they still use tile offset on UV mappings to properly lit up different color in traffic light. Tile offset here is done on right up side of the texture in the following order:

0. first texture tile - red color of traffic light
1. second texture tile - yellow color of traffic light
2. third texture tile - green color of traffic light

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Materials/Lamp_system | revision: 4815 | captured: 2026-10-21 23:56:14 -->
