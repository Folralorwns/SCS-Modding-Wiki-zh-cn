# Tutorials/Advanced/Extended Shadows

[Template:Construction](https://modding.scssoft.com/index.php?title=Template:Construction&action=edit&redlink=1)

This tutorial will provide a brief overview of the extended shadow effect used for player trucks and trailers, and guide you through correctly setting up your model for it.

## Overview

The extended shadow effect is used to draw a shadow volume underneath the player's truck and trailer. A grayscale texture is used to define the strength of the shadow volume along its length and width. Within the model, two locators are used to define the shadow volume and a surface is used to define the limit of the effect in the vertical direction. The effect can be fine tuned in the corresponding [chassis definition](../../Documentation/Engine/Units/accessory%20chassis%20data.md).

![Ext_shadow_001.jpg](../../../../../images/articles/Tutorials/Advanced/Extended%20Shadows/300px-Ext_shadow_001.jpg)

![Ext_shadow_002.jpg](../../../../../images/articles/Tutorials/Advanced/Extended%20Shadows/300px-Ext_shadow_002.jpg)

### Locators

The origin locator (shadow_x_ori, shd_x_ori1, shd_x_ori2, etc) defines the upper boundary, center, direction, and orientation of the shadow volume. This locator should generally always be oriented so that it points down (i.e. rotated so that the locator **+y** points in global **-Z**) and rotated so that its **+z** points in global **-Y**. The corner locator (shadow_x_crn, shd_x_crn1, shd_x_crn2, etc) defines the width, length, and lower boundary of the shadow volume.

### *Fakeshadow* Surface

A surface using the *fakeshadow* effect is used to limit where shading is applied within the shadow volume. By default, the extended shadow texture is projected vertically within the entire shadow volume, shading all of the geometry within. When a *fakeshadow* surface is present, only the volume 'outside' of the surface relative to the shadow volume origin will be shaded. So, typically, the normals of any fakeshadow surface will point toward the ground. It is also important that the *fakeshadow* surface covers the entire length and width of the shadow volume, or there may be undesirable shading in the uncovered areas.

## Model Set-Up

### Placing the Locators

Typically, the same texture will be used for both the extended shadow and the UI shadow model of a truck or trailer. In this case, the extended shadow locators must be placed in reference to the UI shadow model so that the texture will project onto the shadow volume the same way it's mapped to the UI shadow.

1. Place the origin locator (shadow_x_ori) using `⇧ Shift`+`A` so that it sits in the bounding box center of your UI shadow model when viewed from above. Its position in Z is the top of the shadow volume/the highest point that would be darkened by the extended shadow.<br> ![Ext_shadow_3.jpg](../../../../../images/articles/Tutorials/Advanced/Extended%20Shadows/Ext_shadow_3.jpg)
2. Rotate the origin locator to the standard orientation: `R`, `X`, -90; `R`, `Z`, 180. Its orientation in the Transform panel should look like this:<br> ![Ext_shadow_3b.jpg](../../../../../images/articles/Tutorials/Advanced/Extended%20Shadows/Ext_shadow_3b.jpg)
3. Place the corner locator (shadow_x_crn) at the front left (+Y, -X) extreme of your UI shadow model when viewed from above. Usually, it is placed it below ground level so that the shadow doesn't disappear awkwardly when the player goes over a dip. A reasonable value is around -65cm. (If it is very low, the shadow volume will extend below bridges, etc)<br> ![Ext_shadow_4.jpg](../../../../../images/articles/Tutorials/Advanced/Extended%20Shadows/Ext_shadow_4.jpg)

### Making the *Fakeshadow* Surface

Select the extended shadow origin locator (shadow_x_ori or shd_x_ori) and snap the 3D cursor to it (`⇧ Shift`+`S` → *Cursor to Selected*). Add a plane to the scene (`⇧ Shift`+`A` → Mesh → Plane). This plane will become your fakeshadow surface!

Enable snapping (`⇧ Shift`+`Tab ↹`), select vertex mode, and use the *Closest* target mode. Make sure the corner locator (shadow_x_crn or shd_x_crn) is visible.

Select the plane you created, enter Edit mode, and select all. Scale the plane in *X* and then in *Y*, snapping to the corner locator each time. Flip the normals of the plane so that they face down, using `Ctrl`+`F` → Flip Normals.

Assign your fakeshadow surface an SCS Material using the *fakeshadow* effect. [Parent](https://docs.blender.org/manual/en/dev/editors/3dview/object/properties/relations/parents.html) the plane to your vehicle's SCS root locator.

At this point, your vehicle has a functional fakeshadow surface! However, it may not fit very well yet. The surface can be subdivided and manipulated as needed. Be careful to ensure that the outside edges still cover the entire shadow volume.

> **TIP:** The [Loop Cut](https://docs.blender.org/manual/en/dev/modeling/meshes/editing/subdividing/loop.html) tool is useful for quickly subdividing the fakeshadow surface.

### Creating the Shadow Texture

## Definitions Set-Up

## Troubleshooting

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Advanced/Extended_Shadows | revision: 5346 | captured: 2026-10-21 23:56:14 -->
