# Documentation/Engine/Units/accessory paint job data

The **accessory_paint_job_data** unit class is used to define paint jobs for trucks and trailers (as of ETS2 [1.25](../../../Games/ETS2/Modding%20guides/1.25.md)/ATS 1.4).

## Usage

### Airbrush

In the airbrush mode, the RGB of **paint_job_mask** is blended with the base color, using the alpha channel as the blend factor. This mode is active when the attribute **airbrush** is *true*.

### Colormask

In the colormask mode, each of **paint_job_mask**'s color channels (RGB) acts as a mask for a color being blended over the base texture. They are applied in the order *blue*, *green*, and *red*. So the red channel has the highest “priority”, followed by green and then blue.

> **TIP:** Texture compression can lead to some minor aliasing at sharp boundaries between the mask channels. To avoid colors ‘bleeding through’ at these boundaries, try blending some of the lower-priority channel ‘under’ the higher-priority channel along their shared boundary. For example, at a sharp boundary between the *red* (255, 0, 0) and *green* (0, 255, 0) channels, a thin line of the base color may be visible. This can be mitigated by extending the edge of the lower-priority mask ‘under’ the higher-priority mask. So in the case where there is a sharp line between the red mask and the green mask, the green mask should be extended slightly into the area of the red mask. The resultant color looking at the RGB image would be yellow (255, 255, 0).

## Attributes

Many common attributes are inherited from [**accessory_data**](accessory%20data.md).

<table class="wikitable">
<tbody><tr>
<th>Name
</th>
<th><a href="../Units.md#Attribute_types" title="Documentation/Engine/Units">Type</a>
</th>
<th>Default Value
</th>
<th>Modes
</th>
<th>Description
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
<td rowspan="3">Defines the default color applied to each channel of the color mask.
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
<td>Defines the default color of the paint job.
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
<td rowspan="3">When false, the player may change each channel's color via the color picker.
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
<td>When false, the player may change the base color via the color picker.
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
<td>When false, the player may change the flip color via the color picker.
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
<td>When false, the player may change the flake color via the color picker.
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
<td>Defines the color of the flip effect.
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
<td>Defines the relative strength of the flip effect.
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
<td>Defines the color of the flake effect.
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
<td>Defines how many times the flake_noise texture repeats within one UV tile. (Another way to think of this is that the UV coordinates are divided by this factor when addressing flake_noise.)
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
<td>Defines how 'tight' the flake effect is to the specular highlight. Higher values result in a smaller area of the flake effect, while smaller values result in a broad area having it.
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
<td>Adjusts the sharpness of the clearcoat specular highlight. Higher values yield sharper edges.
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
<td>Path to the flipflake texture. The RGB component multiplies the flake_color, and the A component masks the flake effect.
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
<td>When true, flipflake (metallic/pearlescent) behavior and attributes are enabled. Cannot be used with colormask.
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
<td>When true, airbrush behavior and attributes are enabled. Cannot be used with colormask.
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
<td>When true, the resulting material will have the <i>altuv</i> flavor. This triggers usage of the alternate UV layout, if configured.
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
<td>Defaults to <b>false</b>. This was previously used to mark paintjobs available when purchasing a truck when true, and only available from the upgrade shop when false. Currently must be set to <b>false</b> to avoid undesirable behavior.
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
<td>Defines the path to the texture resource (.tobj) to be used for color masking (colormask) or for blending (airbrush). If empty, mask is ignored and final result is composed purely from color attributes.
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
<td>Defines the path to a texture resource (.tobj) to override the base texture of the truckpaint material(s). If empty, the base texture will be used as defined in the truckpaint material(s). This is useful for overriding the alpha channel of the base texture if a different specularity is desired.
</td></tr></tbody></table>

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_paint_job_data | revision: 5079 | captured: 2026-10-21 23:56:14 -->
