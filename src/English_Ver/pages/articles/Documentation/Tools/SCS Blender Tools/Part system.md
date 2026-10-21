# Documentation/Tools/SCS Blender Tools/Part system

![SCS_Tools_Object_Specials_-_Parts_05.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Part%20system/SCS_Tools_Object_Specials_-_Parts_05.280.png)

**Parts** can be found in *SCS Parts* sub-panel inside *SCS Object* panel in *Object* tab of Blender properties window and provide a kind of grouping system for Model and [Locator](Locators.md) objects. They are usually used in defining [Variants](Variant%20system.md) but, in special cases, they are also used to define parts of the geometry that will be treated differently than the rest of the model.

Every object in a scene belongs to some Part. Even in cases when we don't need to use Parts, there is always a Part name assigned to every object in a scene. The default name is “defaultpart”, but it can be changed any time. If the active object is not parented to any [SCS Root Object](Terminology%20and%20basics.md#SCS_Root_Object), then it is not possible to set the Part name for that object and panel won't be visible.

## Part list

There is a **Part List** for each SCS Root Object which contains the Part names used within its respective SCS Game Object.

### Add, Remove, Order and Rename Parts

You can **+** ***Add*** or **−** ***Remove*** names from the Part list using the buttons on the right side of the list. The middle button here is a **🗘** ***Remove Unused*** button, which will automatically remove any unused Part names. Lower two buttons ⯅ & ⯆ will change order of currently selected part. Lastly to ***Rename*** the existing Part just double click the item in the list and type a new name.

### Additional list tools

There are also some additional tools integrated for each item in the Part list which can be used for easy selection/deselection (arrow icon [![Blend_icon_restrict_select_off.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Part%20system/Blend_icon_restrict_select_off.png)](../../../../files/Blend%20icon%20restrict%20select%20off.png.md)) or hiding/showing (eye icon [![Blend_icon_restrict_view_off.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Part%20system/Blend_icon_restrict_view_off.png)](../../../../files/Blend%20icon%20restrict%20view%20off.png.md)) of particular Parts. It works like a switches, so if it is pressed repeatedly it will select and deselect or hide and show all the Part items. With `⇧ Shift` pressed it will always add to the existing selection or always show the Part items and with `Ctrl` it will always subtract from existing selection or always hide the Part items.

### Item-selection tools

If the active object is Model, Model Locator or Collision Locator object additional buttons appear:

- Assign - assigns currently selected Part name to selected object(s). For multiple selections, all selected objects must belong to the same SCS Root Object.

- Select - selects all Models, Model Locators and Collision Locators within active SCS Game Object which uses the same Part name.

- Deselect - deselects all Models, Model Locators and Collision Locators within active SCS Game Object which uses the same Part name.

## Predefined Part Names

Some special behaviors are applied in-game to Parts with certain predefined names, based on the type of object.

### Trailers

<table class="wikitable">
<tbody><tr>
<th>Name
</th>
<th>Behavior
</th>
<th>Notes
</th></tr>
<tr>
<td>brace_on
</td>
<td>Lowered landing gear (static)<br/>Visible when trailer is detached, and before landing gear is raised when attached.
</td>
<td rowspan="2">The <i>brace_on</i> part should be active for all variants of the trailer model, and the <i>brace_off</i> part should be inactive.
<p>For trailers with animated landing gear, both <i>brace_on</i> and <i>brace_off</i> are invisible during the landing gear animation. For best results, these parts should visually match the start and end keyframes of the landing gear animation.
</p>
</td></tr>
<tr>
<td>brace_off
</td>
<td>Raised landing gear (static)<br/>Visible when trailer is attached, after landing gear is raised.
</td></tr>
<tr>
<td>cables_off
</td>
<td>Visible when dynamic trailer cables are not connected (version 1.31+)
</td>
<td rowspan="2">The <i>cables_off</i> part should be active for all variants of the trailer model, and the <i>cables_on</i> part should be inactive.
</td></tr>
<tr>
<td>cables_on
</td>
<td>Visible when dynamic trailer cables are connected (version 1.31+)
</td></tr></tbody></table>

### Map Objects

- *vis* - used for the visible part of the model.
- *coll* - used for the collision geometry.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Part_system | revision: 4296 | captured: 2026-10-21 23:56:14 -->
