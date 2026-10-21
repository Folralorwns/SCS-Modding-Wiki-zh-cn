# 文档/引擎/单元/配件涂装数据

**accessory_paint_job_data** 单元类用于为卡车和挂车定义涂装（自 ETS2 [1.25](../../../Games/ETS2/Modding%20guides/1.25.md)/ATS 1.4 起）。

## 用法

### Airbrush

在 airbrush 模式下，**paint_job_mask** 的 RGB 会与基色混合，alpha 通道用作混合系数。当属性 **airbrush** 为 *true* 时，此模式生效。

### Colormask

在 colormask 模式下，**paint_job_mask** 的每个颜色通道（RGB）都作为在基色纹理上混合某种颜色的遮罩。它们按 *蓝*、*绿*、*红* 的顺序应用。因此红色通道的“优先级”最高，其次是绿色，最后是蓝色。

> **提示：** 纹理压缩可能会在遮罩通道之间的锐利边界处造成轻微的锯齿。为避免颜色在这些边界处“渗过”，可尝试沿共享边界将优先级较低的通道在优先级较高的通道“下方”进行混合。例如，在 *红*（255, 0, 0）与 *绿*（0, 255, 0）通道之间的锐利边界处，可能会看到一条基色的细线。可以通过将优先级较低的遮罩边缘“延伸”到优先级较高的遮罩下方来缓解。因此，当红色遮罩与绿色遮罩之间存在锐利分界线时，绿色遮罩应略微延伸进红色遮罩的区域。此时从 RGB 图像上看到的最终颜色将是黄色（255, 255, 0）。

## 属性

许多通用属性继承自 [**accessory_data**](accessory%20data.md)。

<table class="wikitable">
<tbody><tr>
<th>名称
</th>
<th><a href="../Units.md#Attribute_types" title="Documentation/Engine/Units">类型</a>
</th>
<th>默认值
</th>
<th>模式
</th>
<th>描述
</th></tr>
<tr>
<td>mask_r_color
</td>
<td rowspan="3">float3
</td>
<td>(1, 0, 0)
</td>
<td rowspan="3">colormask
</td>
<td rowspan="3">定义应用于颜色遮罩每个通道的默认颜色。
</td></tr>
<tr>
<td>mask_g_color
</td>
<td>(0, 1, 0)
</td></tr>
<tr>
<td>mask_b_color
</td>
<td>(0, 0, 1)
</td></tr>
<tr>
<td>base_color
</td>
<td>float3
</td>
<td>(1, 1, 1)
</td>
<td>all
</td>
<td>定义涂装的默认颜色。
</td></tr>
<tr>
<td>mask_r_locked
</td>
<td rowspan="3">bool
</td>
<td>true
</td>
<td rowspan="3">colormask
</td>
<td rowspan="3">为 false 时，玩家可通过颜色选择器更改每个通道的颜色。
</td></tr>
<tr>
<td>mask_g_locked
</td>
<td>true
</td></tr>
<tr>
<td>mask_b_locked
</td>
<td>true
</td></tr>
<tr>
<td>base_color_locked
</td>
<td>bool
</td>
<td>true
</td>
<td>all
</td>
<td>为 false 时，玩家可通过颜色选择器更改基色。
</td></tr>
<tr>
<td>flip_color_locked
</td>
<td>bool
</td>
<td>true
</td>
<td>flipflake
</td>
<td>为 false 时，玩家可通过颜色选择器更改翻转色。
</td></tr>
<tr>
<td>flake_color_locked
</td>
<td>bool
</td>
<td>true
</td>
<td>flipflake
</td>
<td>为 false 时，玩家可通过颜色选择器更改闪片色。
</td></tr>
<tr>
<td>flip_color
</td>
<td>float3
</td>
<td>(1, 0, 0)
</td>
<td>flipflake
</td>
<td>定义翻转效果的颜色。
</td></tr>
<tr>
<td>flip_strength
</td>
<td>float
</td>
<td>0.27
</td>
<td>flipflake
</td>
<td>定义翻转效果的相对强度。
</td></tr>
<tr>
<td>flake_color
</td>
<td>float3
</td>
<td>(0, 1, 0)
</td>
<td>flipflake
</td>
<td>定义闪片效果的颜色。
</td></tr>
<tr>
<td>flake_uvscale
</td>
<td>float
</td>
<td>32.0
</td>
<td>flipflake
</td>
<td>定义 flake_noise 纹理在一个 UV 瓦片内重复的次数。（另一种理解方式是，在采样 flake_noise 时，UV 坐标会除以该系数。）
</td></tr>
<tr>
<td>flake_density
</td>
<td>float
</td>
<td>1.0
</td>
<td>flipflake
</td>
<td>定义闪片效果相对于高光反射的“紧密”程度。数值越大，闪片效果覆盖的面积越小；数值越小，覆盖面积越大。
</td></tr>
<tr>
<td>flake_shininess
</td>
<td>float
</td>
<td>50.0
</td>
<td>flipflake
</td>
<td>
</td></tr>
<tr>
<td>flake_clearcoat_rolloff
</td>
<td>float
</td>
<td>2.2
</td>
<td>flipflake
</td>
<td>调整清漆高光的锐利程度。数值越大，边缘越锐利。
</td></tr>
<tr>
<td>flake_noise
</td>
<td>string
</td>
<td>"/material/custom/flake_noise.tobj"
</td>
<td>flipflake
</td>
<td>flipflake 纹理的路径。RGB 分量与 flake_color 相乘，A 分量对闪片效果进行遮罩。
</td></tr>
<tr>
<td>flipflake
</td>
<td>bool
</td>
<td>false
</td>
<td>
</td>
<td>为 true 时，启用 flipflake（金属/珠光）行为及相关属性。不能与 colormask 一起使用。
</td></tr>
<tr>
<td>airbrush
</td>
<td>bool
</td>
<td>false
</td>
<td>
</td>
<td>为 true 时，启用 airbrush 行为及相关属性。不能与 colormask 一起使用。
</td></tr>
<tr>
<td>alternate_uvset
</td>
<td>bool
</td>
<td>false
</td>
<td>all
</td>
<td>为 true 时，生成的材质将带有 <i>altuv</i> 变体。如果已配置备用 UV 布局，这会触发对其的使用。
</td></tr>
<tr>
<td>stock
</td>
<td>bool
</td>
<td>false
</td>
<td>all
</td>
<td>默认为 <b>false</b>。此前当为 true 时，用于标记涂装在购买卡车时即可用，而为 false 时仅可从改装店获得。目前必须设为 <b>false</b>，以避免出现不良行为。
</td></tr>
<tr>
<td>paint_job_mask
</td>
<td>string
</td>
<td>
</td>
<td>all
</td>
<td>定义用于颜色遮罩（colormask）或混合（airbrush）的纹理资源（.tobj）路径。若为空，则忽略遮罩，最终结果完全由颜色属性构成。
</td></tr>
<tr>
<td>base_texture_override
</td>
<td>string
</td>
<td>
</td>
<td>all
</td>
<td>定义一个纹理资源（.tobj）路径，用于覆盖 truckpaint 材质的基色纹理。若为空，则使用 truckpaint 材质中定义的基色纹理。当需要不同的镜面反射程度时，这可用于覆盖基色纹理的 alpha 通道。
</td></tr></tbody></table>

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_paint_job_data | revision: 5079 | captured: 2026-10-21 23:56:14 -->
