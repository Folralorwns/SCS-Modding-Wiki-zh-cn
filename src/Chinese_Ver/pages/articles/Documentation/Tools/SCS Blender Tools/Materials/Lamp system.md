# 文档/工具/SCS Blender Tools/材质/灯光系统

灯光系统使用“lamp”材质效果，通过第二张遮罩纹理或基础纹理的 alpha 通道来表现额外的受光表面。该系统用于车辆灯光、车辆辅助灯和交通信号灯。

为便于使用灯光系统，SCS Blender Tools 内置了 [Lamp Switcher & UV Tool](../SCS%20Tools%20in%20Tool%20Shelf/Lamp%20Switcher%20&%20UV%20Tool.md)，它可帮助你进行 UV 映射平铺，并直接在 Blender 3D 视口中预览受光表面。

## 车辆灯光

<table class="wikitable" style="text-align:center;float:right;">
<caption>车辆灯光速查表
</caption>
<tbody><tr>
<th rowspan="2">UV 平铺
</th>
<th rowspan="2">对应<br/>位置
</th>
<th colspan="4">颜色通道
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
<td>左前
</td>
<td style="background-color:#ffb44a;">左转向灯
</td>
<td rowspan="2">远光灯
</td>
<td rowspan="2">近光灯
</td>
<td rowspan="2" style="background-image:linear-gradient(to right,#ffb44a,rgba(255,255,255,0));">位置灯*
</td></tr>
<tr>
<td>1
</td>
<td>右前
</td>
<td style="background-color:#ffb44a;">右转向灯
</td></tr>
<tr>
<td>2
</td>
<td>左后
</td>
<td style="background-image:linear-gradient(to right,#ff4a4a,#ffb44a);">左转向灯**
</td>
<td rowspan="2" style="background-color:#ff4a4a;">刹车灯
</td>
<td rowspan="2">倒车灯
</td>
<td rowspan="2" style="background-color:#ff4a4a;">位置灯
</td></tr>
<tr>
<td>3
</td>
<td>右后
</td>
<td style="background-image:linear-gradient(to right,#ff4a4a,#ffb44a);">右转向灯**
</td></tr>
<tr>
<td>4
</td>
<td>中部或 DRL
</td>
<td>
</td>
<td>
</td>
<td>DRL
</td>
<td style="background-color:#ffb44a;">位置灯
</td></tr>
<tr>
<td colspan="6"><i>*自 1.39 起，ETS2 中前位置灯默认为白色，ATS 中默认为橙色。 <br/>**ETS2 中后转向灯默认为橙色，ATS 中默认为红色。</i>
</td></tr></tbody></table>

车辆灯光使用第二张 RGBA 遮罩纹理，其中每个通道为特定类型的灯光定义亮度遮罩：

- R - 左转向灯、右转向灯
- G - 远光灯、刹车灯
- B - 近光灯、倒车灯、日间行车灯（DRL）
- A - 位置灯

车辆灯光正常工作的第二项要求是：为灯光遮罩纹理使用单独的 UV 层，并为映射设置正确的平铺偏移。平铺按以下顺序应用在纹理右侧：

0. 原始纹理 - 车辆左前侧
1. 第一块纹理 - 车辆右前侧
2. 第二块纹理 - 车辆左后侧
3. 第三块纹理 - 车辆右后侧
4. 第四块纹理 - 车辆中部和 DRL

## 辅助灯

车辆上的辅助灯也可以使用单独的第二张遮罩纹理，但它们只使用灯光遮罩纹理中的两个通道：

- R - 低亮度光束
- G - 全亮度光束
- B - 未使用，必须为零（黑色）
- A - 未使用，必须为零（黑色）

辅助灯还可以使用两种不同颜色，为此需要为第二张遮罩纹理偏移 UV 映射。此处的平铺偏移同样位于纹理右侧：

0. 原始纹理 - 白色
1. 第一块纹理 - 橙色

## 交通信号灯

交通信号灯不使用额外的第二张遮罩纹理，而是使用基础纹理的 alpha 通道来正确点亮信号灯。但它们仍会在 UV 映射上使用平铺偏移，以正确点亮信号灯中的不同颜色。此处的平铺偏移位于纹理右上方，顺序如下：

0. 第一块纹理 - 信号灯红色
1. 第二块纹理 - 信号灯黄色
2. 第三块纹理 - 信号灯绿色

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Materials/Lamp_system | revision: 4815 | captured: 2026-10-21 23:56:14 -->
