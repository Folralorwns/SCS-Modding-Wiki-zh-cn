# 文档/引擎/字体

本文介绍 1.43 版本中字体生成与渲染系统所做的更改。

## 简介

![Font_tech_comparison.png](../../../../../images/articles/Documentation/Engine/Fonts/300px-Font_tech_comparison.png)

*左侧为 SDF 字体，右侧为旧的栅格字体。上方为屏幕上的字体质量，下方为内部纹理表示。*

到目前为止，我们的所有文本渲染都是使用普通栅格字体完成的。这种做法在多年前或许还算够用，但在 4K 分辨率与高 DPI 的时代，它已无法满足当今现代游戏所要求的标准。解决方案是[有向距离场](https://steamcdn-a.akamaihd.net/apps/valve/2007/SIGGRAPH2007_AlphaTestedMagnification.pdf)。纹理不再像图像那样直接存储栅格信息，而是编码与最近边缘的距离，从而在渲染时能够近似出字形的实际形状。这项技术的主要优势在于，字形理论上可以无限缩放，同时无论屏幕上的尺寸如何都能应用一致的抗锯齿效果。它还允许我们在运行时应用多种效果，例如描边或发光。

虽然由此单独生成的图集在体积上可能更大，但我们只需生成一次即可覆盖所有可能的字体字号。例如在 ATS/ETS2 中，我们不再需要为 **normal**、**normal_o**、**title**、**big**、**small** 这些基础字体准备多套纹理，因为它们都基于同一个源 TTF 文件。此外，我们还可以借此以几乎零额外成本创建同一字体的多种效果变体。

## Sii 定义

新的字体定义格式基于旧格式。虽然新增了一些参数，但旧定义仍与[新生成器](https://modding.scssoft.com/index.php?title=Documentation/Tools/fontgen/Download&action=edit&redlink=1)基本兼容。

主要变更：

- 纹理中字形的大小不再与屏幕上文本的大小有任何关系。字形应当足够大，以编码足够的细节，并在我们预期屏幕上会出现的所有尺寸下都不产生伪影。因此，**width** 与 **height** 参数已被单个 **size** 参数取代，而 **scale_width**、**scale_height** 仍然保留，用于在渲染时为每个图集附加缩放。请注意，我们现在会在所有生成的字体中存储每个图集的尺寸信息，因此就文本尺寸而言，一切都应如你在屏幕上所预期的那样显示。
- 新增的可选 **texture_size** 参数可用于直接指定生成纹理的尺寸，以提高或降低文本质量。默认情况下，该值由生成器根据所请求的尺寸规格自动选择；不过，如果你觉得结果不够理想，可以手动使用该参数强制生成器创建更大的纹理。你也可以在视觉质量影响可忽略的前提下缩小纹理以节省存储空间。
- 生成器现在还支持 OTF 字体。

```
texture_size: (256, 256) # Force the generator to create a 256x256 texture for this atlas.
```

> **注意：** 提示：为获得最佳的尺寸/质量比，你应从较小的纹理尺寸开始，逐步增大，直到字体达到期望的质量。

- 可选参数 **sdf_range** 用于指定距离场的大小，该值需要足够大，以便我们正确渲染基于边缘的效果，例如抗锯齿、柔和阴影、描边等。生成器会根据需求自动计算该值。你唯一可能需要自行指定它的情况，是使用在多个字体之间共享的图集时——子字体所使用的效果可能不兼容父字体提供的 SDF 范围，此时生成器会告知你父字体为满足需要而必须使用的最小 SDF 范围。请注意，增大 SDF 范围会降低质量，因为可用于编码精细细节的数据变少，因此你可能需要指定更大的纹理尺寸来补偿。
- **antialias**/**gradient** 参数已被移除，因为它们要么不再需要，要么根本未被使用。

使用单个图集的字体定义示例：

```
SiiNunit
{
configuration : .cfg
{
	base: "../../base"
	output: "/font/normal"
	char_config[]: .cfg0
    line_spacing: 2
    vertical_span_bias: 1
    include_escaped_charset: false
}

char_set_config : .cfg0
{
    # Base atlas parameters based on the old format
  	font_file:"papyrus_regular.ttf"
  	character_set_file: "charset.txt"
  	size: 38              # EM size
	scale_width: 1.0        # X-scaling factor (applied when rendering)
	scale_height: 1.0       # Y-scaling factor (applied when rendering)

	# Optional: base color
    base_color: (1.0, 0.0, 0.0, 1.0)    # default is (1, 1, 1, 1)

	# Optional: kerning bias
	kerning_bias: 2         # glyph kerning bias (px) at full scale

	# Optional: thickness bias
	thickness_bias: 1       # glyph thickness_bias (px) at full scale

	# Optional: outline parameters
    outline_width: 1        # outline width (px) at full scale
    outline_color: (0.0, 0.5, 0.0, 1.0) # default is (0, 0, 0, 1)

    # Optional: drop shadow parameters
    shadow_angle: -45       # shadow angle in degrees
	shadow_distance: 2.0    # shadow distance (px) at full scale
	shadow_alpha: 0.4       # shadow alpha (0-1)
	shadow_size: 2          # shadow size (px) at full scale (0 - hard shadow, >0 - softer, spread out shadow)

    # Optional: glow parameters
    glow_color: (0.0, 1.0, 0.0)
    glow_size: 5            # glow size (px) at full scale

    # Optional: bevel parameters
    bevel_angle: -45        # bevel angle in degrees (should be same as shadow for consistent lighting)
    bevel_alpha: 0.5        # bevel alpha (0-1)
    bevel_size: 1.5         # bevel size (px) at full scale

    # Optional: additional MSDFGen parameters
    # Expert-only, see \etc\font\msdf-atlas-gen.exe -help for more info.
    additional_msdfgen_parameters: "-errorcorrection full-auto"
}

}
```

#### 走捷径

默认情况下，我们使用三个颜色通道来编码距离场信息（这种方法称为 MSDF）。这样可以保留锐利的转角，代价是存储需求增加。

如果你不需要锐利的转角，和/或需要减小文件体积，可以在图集定义中使用以下参数：

```
sharp_corners: false
```

> **注意：** 如果你使用的字体本身就是圆角的，也应考虑这样做。

这会使内存需求降低 66%，代价是所有内容看起来更圆滑一些。请注意，这样做还允许你使用更大的纹理尺寸，同时仍能节省一些内存；我们目前在不需要锐利转角的 CJK 字体中就采用了这一做法。

### 图集共享

**normal.sii:**

```
SiiNunit
{
configuration : normal.cfg # parent font configuration can't be nameless!
{
	base: "../../base"
	output: "/font/normal"
	char_config[]: .cfg0
	char_config[]: .cfg1
	char_config[]: .cfg2
	char_config[]: .cfg3
	char_config[]: .cfg4
	char_config[]: .cfg5
	line_spacing: 0
	default_scale: 0.83
	include_escaped_charset: true
}

char_set_config : .cfg0
{
  	font_file:"arialbd.ttf"
  	character_set_file: "charset.txt"

	scale_width: 0.96
	size: 17
	scale_height: 0.96
    texture_size: (1024, 512)
    sdf_range: 8
}

...
```

**normal_o.sii:**

```
SiiNunit
{
configuration : .cfg
{
	base: "../../base"
	output: "/font/normal_o"
	char_config[]: .cfg0
	char_config[]: .cfg1
	char_config[]: .cfg2
	char_config[]: .cfg3
	char_config[]: .cfg4
    char_config[]: .cfg5 # number of atlases needs to match!
	line_spacing: 0
    atlas_source: "./normal.sii"
}

char_set_config : .cfg0
{
    # source ttf and charset data automatically pulled from normal.sii
	size: 14
	scale_width: 1.0
	scale_height: 1.0
	outline_width: 2
}

...
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Fonts | revision: 5026 | captured: 2026-10-21 23:56:14 -->
