# Documentation/Tools/SCS Blender Tools/Supported shaders

With version 1.0 Blender Tools are presenting flavors in materials. Flavors are used for common passes in more shaders. Depending on each shader different flavors can be enabled on it.

Shader preset list now includes only base shader types, which can be later altered with switching different flavors on and off. That's why this page now resembles base shader types and flavors description.

## Base Shader Types

### building.add.env.day

Use this material if you want your building windows to reflect at day-time and be lit at night. It shall be more or less used on distant "panorama" buildings as they don't need advanced features from window.day / window.night.

It effectively switches two materials depending on the time of the day. During the day it uses dif.spec.add.env material with texture for reflections and at night switches to dif.lum.spec in order for windows to be lit at night.

The texture must have alpha channel on places where it should have reflections and light at night.

### building.day

Same as building.add.env.day without reflection component.

It effectively switches two materials depending on the time of the day. During the day it uses dif.spec material where alpha is used as specular map and at night switches to dif.lum.spec in order for windows to be lit at night.

### building.lvcol.day

Same as building.day with extra multiplication of vertex color.

During the day vertex color is multiplying specular map, on the other hand during the night vertex color is multiplying luminance.

### decalshadow

Used for transparent static baked shadows. Color of surfaces is put together from the base texture multiplied with material diffuse and vertex color.

On the other hand transparency is donated by multiplication of vertex color alpha and base texture alpha channel.

### dif

This is one of the most basic shader with diffuse and specular light featuring one texture. Specular light is used directly from value specified in material.

#### Useful flavor combinations

1. **"dif.a"** - the areas on geometries where texture has alpha value 0 will be transparent. Example usage: grills, railings and ladders on far buildings.
2. **"dif.shadow"** - uses geometry also as shadow caster. This type of shader shall be used only in the case of complex animated geometries, because cost of animation calculation may be greater than calculating shadows directly on high poly mesh.
3. **"dif.shadow.a"** - is a combination of "dif.shadow" and "dif.a" which means that areas of geometry which will be transparent also won't cast shadows. This shader may be used for fences models which shall beside begin transparent also cast shadows.
4. **"dif.over"** - in this case alpha map represent transparency blending of material, where alpha with value 0 means completely transparent and alpha with value 255 means non transparent.

### dif.anim

Same as dif with extra behaviour of blending over time between base and over texture.

Extra auxiliary setting in this shader defines animation speed, meaning how quickly textures are switched.

### dif.lum

Same as dif with additional linear interpolation calculation between "dif" shader result and base texture RGB colors by factor of base texture alpha channel. As a result this shader will give you lit surfaces during the night, where amount of surface lit is donated by base texture alpha channel.

Example usage of this shader are dashboard and gps surfaces in truck inside Euro Truck Simulator 2 game.

#### Useful flavor combinations

1. **"dif.lum.decal.over"** - decal part of shader name donates ability to use lightning model from the surfaces lying behind geometries using this shader and over part of shader name represent transparency blending of material, where alpha with value 0 means completely transparent and alpha with value 255 means non transparent. Example usage of this shader are lit icons on buttons in truck cabin which shall be:
  - lit to reflect effect of back light,
  - transparent around icon to blend on the button below,
  - use the lightning model from the surface below again for blending on the button surface.

### dif.lum.spec

Similar as dif.lum with difference that surface has additional specular map shading as dif.spec.

### dif.spec

Basic shader with diffuse and specular light featuring one texture. Alpha of the texture represents intensity of specular light.

#### Useful flavor combinations

1. **"dif.spec.a"** - making transparent areas where texture has alpha with value 0.
2. **"dif.spec.over"** - texture alpha channel also represent transparency blending of material, where alpha with value 0 means completely transparent and alpha with value 255 means non transparent.
3. **"dif.spec.shadow"** - uses geometry also as shadow caster. This type of shader shall be used only in the case of complex animated geometries, because cost of animation calculation may be greater than calculating shadows directly on high poly mesh.
4. **"dif.spec.shadow.a"** - with enabled shadow calculations over alpha channel which means that areas of geometry which will be transparent also won't cast shadows.
5. **"dif.spec.tsnmap.shadow"** - with extra texture defining normal maps and using geometries for shadow casters. Both textures are using same UV layer. This type of shader shall be used only in the case of complex animated geometries, because cost of animation calculation may be greater than calculating shadows directly on high poly mesh.

### dif.spec.add.env

Same as dif.spec with additional reflection pass and texture.

#### Useful flavor combinations

1. **"dif.spec.add.env.paint"** - with usage of extra color defined in definition files. All areas on the base texture will be multiplied with extra color while in game. This shader is either used for AI cars or truck parts which should be painted with base truck color.

### dif.spec.add.env.nofresnel

Same as dif.spec.add.env without fresnel attribute and computation, therefore is slightly cheaper to compute.

### dif.spec.fade.dif.spec

Shader mostly used for rocks where one texture can be used as base and detail one.

Shader is fading between base and detail texture with assumption that detail texture is representing details of base texture (sounds like fractals). Therefore base and detail textures should use same texture file which has to be self-similar.

However blending details are defined with auxiliary values where:

- From - detail texture fade out start, represented as z-distance in meters
- Range - detail texture fade range, represented in meters
- Bias - strength of detail texture mixing with base texture
- UV Scale - UV layer scale factor for detail layer (as shader shall be using same textures for base and detail, this factor comes handy as user can use only one UV layer for base & detail and then this factor represents how UV layer will be rescaled for detail texture)

### dif.spec.mult.dif.spec

Same as dif.spec with one more texture which color and alpha is multiplied with base texture.

Example usage in Euro Truck Simulator 2 is trailer where company texture is multiplied with base texture of the trailer.

#### Useful flavor combinations

1. **"dif.spec.mult.dif.spec.tsnmap.shadow"** - beside normal maps geometries with this material will also cast shadows. This type of shader shall be used only in the case of complex animated geometries, because cost of animation calculation may be greater than calculating shadows directly on high poly mesh.

### dif.spec.mult.dif.spec.add.env

Same as dif.spec.mult.dif.spec with additional reflection pass and texture.

### dif.spec.mult.dif.spec.iamod.dif.spec

Special use shader based on dif.spec.mult.dif.spec and is usually used for building walls.

Shader is combining two multiplied opaque textures with third inverse-vertex-alpha (iamod) texture. The third texture should represent decal/dirt/wear layer where texture alpha channel and vertex alpha controls how strong this decal application is. Vertex color alpha with value 0 will apply the most and value 0.5 won't apply third layer at all.

### dif.spec.oclu

Behaves in similar way as dif.spec.mult.dif.spec but the second texture in this case is using gray-scale image (only one channel) which results in better performance.

General usage of this shader is as recognized as using dif.spec with "ambient occlusion" texture.

### dif.spec.oclu.add.env

Same as dif.spec.oclu with additional reflection pass and texture.

### dif.spec.over.dif.opac

Same as dif.spec with extra mask texture which color is mixed with base texture color by factor of alpha from mask texture.

### dif.spec.weight

Same as dif.spec with modified specular light.

It's mostly used for roads and asphalts, due to the distinct feel of specularity and diffuse properties of such surfaces.

### dif.spec.weight.add.env

Same shader as dif.spec.weight with additional reflection pass and texture.

### dif.spec.weight.mult2

Special case shader created mostly for road surfaces combining base texture with "smeared top layer". Smeared layer is donated by multiplication texture and mixed by both textures alpha channels.

This shader shall be replaced with simple dif.spec.weight instead if possible.

### dif.spec.weight.mult2.weight2

Transition shader between two shaders of dif.spec.weight.mult2 for simulating transitional areas (usually road shoulders).

Fading between first and second shader is done by vertex color alpha, where value 0 will use only first layer and value 0.5 will use only second layer, any value in-between will mix both layers respectively.

This shader shall be replaced with dif.spec.weight.weight.dif.spec.weight instead if possible.

### dif.spec.weight.weight.dif.spec.weight

Transition shader between two shaders of dif.spec.weight, where texture for first shader is presented as base and texture for second shader as over texture.

Fading between the two is done by vertex color alpha, where value 0 will use only base texture layer and value 0.5 will use only over texture layer, any value in-between will mix both layers respectively.

Additionally this shader also supports secondary specular (color and shininess), so even shaders with different specular behaviour can be transitioned.

This shader is usually primary choice when creating roads with transition to road shoulder.

### dif.weight.dif

Transition shader between two shaders of dif where base texture presents texture for first shader and over texture presents texture for second shader.

Fading between the two is done by vertex color alpha, where value 0 will use only base texture layer and value 0.5 will use only over texture layer, any value in-between will mix both layers respectively.

### fakeshadow

Geometry with this material is used to outline contour of the vehicle from which casting of shadow volume begins. Due wheels vertical motion this material is required to be present in the wheel scene as well. It must outline the contour of the whole wheel.

### flare

Shader for simulating light scatter or/and retina glare.

Result of the shader is additive non-lit surface which color part consist of base texture multiplied by vertex color and diffuse material attribute, on the other hand alpha part consists of multiplication between texture alpha channel and vertex color alpha.

### glass

Glass material which uses base texture alpha for specular map and it's also controlled by tint parameters:

- Tint - color for glass
- Tint Opacity - mixing factor between transparent and opaque glass

Depending on the type of glass and its usage user should properly choose reflection texture.

### grass

Shader used in special cases for static not moving grass.

Its result is the same as dif with transparency controlled by multiplication between vertex alpha color and base texture alpha channel.

Normals on the meshes using this shader are ignored as shader always uses normals up as lighting applied to mesh should more-or-less match the ground (assuming ground is flat).

### lamp

Lamp material used for vehicle lights, auxiliary lights and traffic lights. With the second mask texture this material defines masking areas for situations when particular light is turned on.

More about lamps in [Lamp system](Materials/Lamp%20system.md).

#### Useful flavor combinations

1. **"lamp.add.env"** - with additional reflection pass and texture.

### light.tex

Light map shader which is behaving as a fake light source by adding diffuse and specular to surfaces beneath. This shader variant has light map always on independent on day/night.

Example usage would be creation of light map shining on the ground emitted from lights inside the building.

### lightmap.night

It is night variant of light.tex, meaning surface with this shader will be visible only during the night. During the day this light map will be switched off.

### mlaaweight

Geometries with this shader won't be visible, instead they will switch off MLAA processing on the geometries beneath surfaces using this shader.

Example usage is to place simple plane with material of this shader above truck dashboard so that the textures presenting speed text, rpm text, etc. stays sharp.

### none

Special case void shader. Surfaces with this shader won't be drawn in game, might be useful only for testing purposes.

### reflective

Special additive surface simulating reflective surface reaction from players truck lights.

This shader is primarily used for street reflectors or any reflective areas on the vehicles.

### shadowmap

Used for transparent static baked shadows. Color of surfaces is put together from the base texture multiplied with material diffuse. Transparency of shadow map is donated by base texture alpha channel.

### shadowonly

Presents shadow caster material and it's used on geometry for casting sun shadows.

### sign

Special case shader used for sign surfaces. Similarly as reflective this shader simulates interaction with player's headlights.

### sky

Special shader used only for skyboxes. Basically this shader combines three textures with blending defined by Layer Blend factor and is changing during the day night cycle.

### truckpaint

Truckpaint shader as the name suggests is the shader for truck color paint. Shader features combination of base and paintjob textures. The final result of this shader is dependent on configuration of the truck paint inside definition files as the shader supports different output types. If the truck is driven by the player, shader is configured by "paint job" definition file of the truck, otherwise truck paint is configured from AI truck colors palette.

#### Paintjob modes

Additionally "aux" parameters inside material are used only for preview purposes. Their usage in 3D view is dependent on truckpaint mode:

1. "Default" mode (when neither "colormask" or "airbrush" flavor is used) with no additional color settings. Paintjob texture is there only for export porpuses so that proper UV mapping for paintjob can be set.
2. "Color mask" mode (when "colormask" flavor is used) where paintjob texture RGB channels are used to color mask base truckpaint output. Auxiliary attributes are used in 3D viewport as follows:
  - Paintjob R Color -> color masked with B channel of paintjob texture,
  - Paintjob G Color -> color masked with G channel of paintjob texture,
  - Paintjob B Color -> color masked with R channel of paintjob texture,
  - Paintjob Base Color -> base paintjob color.
3. "Airbrush" mode (when "airbrush" flavor is used) uses paintjob texture as airbrush mask on base truckpaint output. Auxiliary attributes are used in 3D viewport as follows:
  - Paintjob Base Color -> base paintjob color.

> > **Note:** There are two more modes "flipflake" and "airbrush.flipflake" which are not yet implemented inside 3D viewport but they can be defined inside definition files anyway, because no additional data have to be exported for them.

#### Useful flavor combinations

1. **"truckpaint.altuv"** - exports alternative UV layer for paint job. Alternative UV layer has to be specified in paintjob texture. > > **Note:** Not using this extension alternative UV won't be exported and thus can not be used in definition files for paint job.
2. **"truckpaint.airbrush"** - uses paint job as airbrush mask. Paintjob texture is multiplied with base truck paint color by factor of paintjob texture alpha channel. > > **Note:** May or may not be used, shader will give the same result as usage of this extension is specified in definition files and the extension doesn't effect exported data.
3. **"truckpaint.airbrush.altuv"** - combined "truckpaint.altuv" and "truckpaint.airbrush" extensions.
4. **"truckpaint.tsnmap"** - with extra texture defining normal maps. Both textures are using same UV layer.
5. **"truckpaint.tsnmap.altuv"** - with extra texture defining normal maps. Both textures are using same UV layer. Beside normal maps shader also features "truckpaint.altuv" extension.
6. **"truckpaint.tsnmap.airbrush"** - with extra texture defining normal maps. Both textures are using same UV layer. Beside normal maps shader also features "truckpaint.airbrush" extension.
7. **"truckpaint.tsnmap.airbrush.altuv"** - with extra texture defining normal maps. Both textures are using same UV layer. Beside normal maps shader also features "truckpaint.altuv" and "truckpaint.airbrush" extensions.
8. **"truckpaint.tsnmapuv"** - with extra texture defining normal maps using its own UV layer.
9. **"truckpaint.tsnmapuv.altuv"** - with extra texture defining normal maps using its own UV layer. Beside normal maps shader also features "truckpaint.altuv" extension.
10. **"truckpaint.tsnmapuv.airbrush"** - with extra texture defining normal maps using its own UV layer. Beside normal maps shader also features "truckpaint.airbrush" extension.
11. **"truckpaint.tsnmapuv.airbrush.altuv"** - with extra texture defining normal maps using its own UV layer. Beside normal maps shader also features "truckpaint.altuv" and "truckpaint.airbrush" extensions.

### unlit.tex

Shader which is drawing surfaces after world has been lit, meaning surfaces using this shader will result into direct texture color multiplied by diffuse material parameter without any lighting applied.

### unlit.vcol.tex

Similar to unlit.tex with additional multiplication by vertex color.

As for transparent flavor combinations this shader uses vertex color alpha multiplied with base texture alpha channel.

#### Useful Flavor Combinations

- **"unlit.vcol.tex.a.over"** - is useful for animated indicators of dashboard inside truck in [Euro Truck Simulator 2](../../../Games.md), as alpha over flavor combination makes transparent areas where texture alpha channel or vertex color is 0.

### water

Shader composed of two independently scrolling water wave layers with added environmental reflection and near/horizon water color interpolation. First water wave is defined with layer0 texture, second with layer1 texture.

However shader also features a lot of extra parameters:

1. Distances:
  - Near - distance of interpolation start
  - Far - distance of horizon
  - Scramble - water surface distorts the reflection and scramble factor tells the amount of distortion
2. Near Color - base water color
3. Horizon Color - water color on horizon
4. Layer0 - first wave settings:
  - Yaw - wave layer orientation defined by counter-clockwise degree rotation around vertical axis
  - Speed - wave layer flow speed in meters per second
  - ScaleX - wave layer texture generation U scale factor
  - ScaleY - wave layer texture generation V scale factor
5. Layer1 - second wave settings:
  - Yaw - wave layer orientation defined by counter-clockwise degree rotation around vertical axis
  - Speed - wave layer flow speed in meters per second
  - ScaleX - wave layer texture generation U scale factor
  - ScaleY - wave layer texture generation V scale factor

### window.day

Day variation of window effect intended to be used for window interiors on building models. Main feature of this shader is interior mapping which is offsetting when viewing angle change (player gets feeling of moving interior behind the window). The amount of offsetting is defined by UV mapping on base texture. This variant is previewing day variant which uses only base texture.

As day/night variant is switched automatically in game so it doesn't really matter which variant is used and exported.

### window.night

Night variation of window effect intended to be used for window interiors on building models. Main feature of this shader is interior mapping which is offsetting when viewing angle change (player gets feeling of moving interior behind the window). The amount of offsetting is defined by UV mapping on base texture. This variant is previewing night variant which uses multiplication between base & lightmap texture.

As day/night variant is switched automatically in game so it doesn't really matter which variant is used and exported.

## Flavors

### a

Flavor enables alpha test on shader, meaning surfaces will be transparent where opacity value is greater than 0. Opacity is usually donated by base texture alpha channel.

### add.env

Flavor enabling extra reflection pass on shader. This will add reflection texture and environment factor parameter to shader, which controls type of environmental cube map texture and amount of added environment lighting.

### altuv

Special flavor used only on truckpaint shader type. It tells shader to use second UV mapping for paintjob texture.

### airbrush

Special flavor used only for truckpaint shader type. It tells shader that paintjob texture should be applied as airbrush paintjob.

For more information on airbrush paintjob behaviour see: Paintjob modes

### asafew

Flavor for safe-weighted alpha test, allowing the base texture alpha channel to encode both the opacity [0,32] and the specular map [32,255]. The shader will remap alpha values [32,255] as [0, 255] for the specular map. It is currently supported for dif.spec, dif.spec.weight and dif.lum.spec.

> **Note:** The "a" flavor must still be specified to enable alpha test behavior.

Photoshop curve presets for converting specular maps to/from the compressed asafew space: [File:Asafew spec remap curves.zip](../../../../files/Asafew%20spec%20remap%20curves.zip.md)

### awhite

Special flavor used only for unlit.vcol.tex, moreover should be used only in combination with multiplication blending mode (See #add & over & mult).

This particular combination will blend out to white color where base texture alpha channel is 0.

### add & over & mult

Flavor defining special blending modes of shader. All of the three modes switches to transparent mode of shader and blend it with the surfaces beneath:

1. **Add** - will result as summary of accumulation buffers and surface using this blending mode,
2. **Over** - will just overlay opaque areas of surfaces using this blending mode over accumulation buffers,
3. **Mult** - will multiply accumulation buffers and surface using this blending mode.

### colormask

Special flavor used only for truckpaint shader type. It tells shader that paintjob texture should be applied as colormask paintjob.

For more information on color mask paintjob behaviour see: Paintjob modes

### decal

Flavor marking surfaces using this flavor to be drawn after all others. So all shaders using this flavor will be drawn as last.

This behaviour somehow reassembles z-depth sorting among normal and shaders with decal flavor, thus this flavor shall be used on more or less any shader using blending mode (see #add & over & mult).

### flat

Flavor removing global specular and diffuse lighting calculation on shader using this flavor, which will result in flat shaded surfaces and most probably in better performance.

### indenv

Special flavor used on dif.spec.add.env marking independent environment reflection from material specular color.

This gives user ability to use reflections also on surfaces where specular light is not reaching the surfaces. Example usage for this in [Euro Truck Simulator 2](../../../Games.md) would be any part of reflective interior where sun never shines.

### linv

Flavor inverting luminance mixing used on luminance shaders of dif.lum.spec.

Luminance shaders usually illuminate surfaces where base texture alpha channel is 255 and don't on surfaces with alpha value 0. This flavor inverts that behavior so that an alpha value of 0 gives full illumination and an alpha value of 255 gives no illumination.

### lvcol

Flavor enabling luminance multiplication with vertex color used on luminance shaders: dif.lum or dif.lum.spec.

### tsnmap & tsnmap16 & tsnmapuv & tsnmapuv16

Flavors adding extra shader pass for normal maps:

1. **tsnmap** - adds extra texture slot for 8-bit normal maps texture and uses same UV mapping as base texture,
2. **tsnmap16** - adds extra texture slot for 16-bit normal maps texture and uses same UV mapping as base texture,
3. **tsnmapuv** - adds extra texture slot for 8-bit normal maps texture and uses its own UV mapping layer,
4. **tsnmapuv16** - adds extra texture slot for 16-bit normal maps texture and uses its own UV mapping layer.

### nocull

Special flavor switching off backface culling of shadow casters on shaders: shadowonly or fakeshadow.

Basically this means shadow casters will cast shadows on both sides, not only on the one where surface normals are directed.

### paint

Flavor enabling additional color masking of surfaces with game defined color.

Usually used on shaders for AI cars, which are painted with different color during the game play.

### shadow

Flavor enabling shadow casting pass on shader.

As there is separate shadow caster shader named shadowonly, this flavor should be used exceptionally. Usually can be used on animated models where cost of animation calculation on extra shadow caster mesh may be greater then calculating shadow caster directly from "high" poly mesh.

### tg0

Flavor for automatic global texture mapping generation and use it on first texture slot. Enabling this flavor will ignore any set UV mapping and will use automatically generated planar UVs.

This mode is usually used for tiled terrain textures, like grass or asphalt.

### tg1

Flavor for automatic global texture mapping generation and use it on second texture slot. Enabling this flavor will ignore any set UV mapping and will use automatically generated planar UVs.

This mode is usually used for tiled terrain textures, like grass or asphalt.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Supported_shaders | revision: 5676 | captured: 2026-10-21 23:56:14 -->
