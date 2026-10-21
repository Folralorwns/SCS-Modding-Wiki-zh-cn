# 文档/工具/SCS Blender Tools/部件系统

![SCS_Tools_Object_Specials_-_Parts_05.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Part%20system/SCS_Tools_Object_Specials_-_Parts_05.280.png)

**部件**可在 Blender 属性窗口 *Object* 选项卡的 *SCS Object* 面板内的 *SCS Parts* 子面板中找到，它们为 Model 和[定位器](Locators.md)对象提供了一种分组系统。部件通常用于定义[变体](Variant%20system.md)，但在特殊情况下，也用于定义模型中将以不同于其余部分的方式处理的几何体。

场景中的每个对象都属于某个部件。即使在我们不需要使用部件的情况下，场景中的每个对象也始终会被分配一个部件名称。默认名称为 “defaultpart”，但可随时更改。如果活动对象未父级关联到任何 [SCS Root Object](Terminology%20and%20basics.md#SCS_Root_Object)，则无法为该对象设置部件名称，并且该面板不会显示。

## 部件列表

每个 SCS Root Object 都有一个 **Part List**，其中包含其对应 SCS Game Object 内使用的部件名称。

### 添加、移除、排序和重命名部件

你可以使用列表右侧的按钮 **+** ***Add*** 或 **−** ***Remove*** 在 **Part List** 中增加或移除名称。中间的按钮是 **🗘** ***Remove Unused***，它会自动移除所有未使用的部件名称。下方两个按钮 ⯅ 和 ⯆ 会改变当前选中部件的顺序。最后，要***重命名***现有部件，只需双击列表中的条目并输入新名称。

### 附加列表工具

**Part List** 中的每个条目还集成了一些附加工具，可用于轻松选择/取消选择（箭头图标 [![Blend_icon_restrict_select_off.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Part%20system/Blend_icon_restrict_select_off.png)](../../../../files/Blend%20icon%20restrict%20select%20off.png.md)）或隐藏/显示（眼睛图标 [![Blend_icon_restrict_view_off.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Part%20system/Blend_icon_restrict_view_off.png)](../../../../files/Blend%20icon%20restrict%20view%20off.png.md)）特定部件。它的作用类似于开关，因此反复按下它就会选中和取消选中，或隐藏和显示所有部件条目。按住 `⇧ Shift` 时，它会始终添加到现有选择中或始终显示部件条目；按住 `Ctrl` 时，它会始终从现有选择中减去或始终隐藏部件条目。

### 条目选择工具

如果活动对象是 Model、Model Locator 或 Collision Locator 对象，则会出现附加按钮：

- Assign - 将当前选中的部件名称分配给选中的对象。对于多选，所有选中对象必须属于同一个 SCS Root Object。

- Select - 选中活动 SCS Game Object 内所有使用相同部件名称的 Model、Model Locator 和 Collision Locator。

- Deselect - 取消选中活动 SCS Game Object 内所有使用相同部件名称的 Model、Model Locator 和 Collision Locator。

## 预定义部件名称

根据对象类型，具有某些预定义名称的部件会在游戏内应用一些特殊行为。

### 挂车

<table class="wikitable">
<tbody><tr>
<th>名称
</th>
<th>行为
</th>
<th>备注
</th></tr>
<tr>
<td>brace_on
</td>
<td>降下的支腿（静态）<br/>挂车分离时可见，以及在连接状态下支腿升起之前可见。
</td>
<td rowspan="2">对于挂车模型的所有变体，<i>brace_on</i> 部件都应处于激活状态，而 <i>brace_off</i> 部件应处于非激活状态。
<p>对于带有动画支腿的挂车，在支腿动画期间 <i>brace_on</i> 和 <i>brace_off</i> 均不可见。为获得最佳效果，这些部件应在视觉上与支腿动画的起始和结束关键帧相匹配。
</p>
</td></tr>
<tr>
<td>brace_off
</td>
<td>升起的支腿（静态）<br/>挂车连接后，在支腿升起之后可见。
</td></tr>
<tr>
<td>cables_off
</td>
<td>动态挂车线缆未连接时可见（版本 1.31+）
</td>
<td rowspan="2">对于挂车模型的所有变体，<i>cables_off</i> 部件都应处于激活状态，而 <i>cables_on</i> 部件应处于非激活状态。
</td></tr>
<tr>
<td>cables_on
</td>
<td>动态挂车线缆已连接时可见（版本 1.31+）
</td></tr></tbody></table>

### 地图对象

- *vis* - 用于模型的可见部分。
- *coll* - 用于碰撞几何体。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Part_system | revision: 4296 | captured: 2026-10-21 23:56:14 -->
