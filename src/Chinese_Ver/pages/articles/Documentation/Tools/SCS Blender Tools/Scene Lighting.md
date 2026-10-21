# 文档/工具/SCS Blender Tools/场景光照

SCS Lighting 面板可利用游戏中的太阳配置数据轻松设置场景光照，并可用于复现 SCS 游戏中一天里的不同时段。该面板可在 Blender 属性窗口的 *World* 选项卡下找到。

如果 SCS Lighting 已禁用（面板标题左侧的复选框未勾选），Blender 会为 SCS 材质使用功能齐全的参考光照，代表一天正午时的中性光照。但如果你想使用自己的设置，或与游戏相同的太阳配置数据，请勾选标题中的复选框，然后要么在 **Active Sun Profile Settings** 子面板中更改数值以自行设置参考配置，要么搜索太阳配置的 SII 定义文件（通常位于游戏结构中的：“/def/climate/<climate_type>/<weather_type>.sii”）。在列表中选择所需的太阳配置条目，其设置便会应用到 Blender 场景光照。

[![SCS_Blender_Tools_Lighting.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Scene%20Lighting/SCS_Blender_Tools_Lighting.280.png)](../../../../files/SCS%20Blender%20Tools%20Lighting.280.png.md)

## 太阳配置库

*[“*.sii” 文件，指向 'SCS Project Base Path' 的绝对或相对路径]*

表示包含太阳配置的 SII 定义文件的路径。指定后，下方列表将填入该文件中找到的所有太阳配置。

## SCS Lighting 东向

定义东向天空方向的属性。更改此属性会使整个光照场景绕全局 Z 轴旋转——从而指定太阳光的方向。

东向光照旁还有一个锁定选项：[![Blend_icon_lock_east.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Scene%20Lighting/Blend_icon_lock_east.png)](../../../../files/Blend%20icon%20lock%20east.png.md)。此选项会强制灯光在 3D 视图中绕全局 Z 轴跟随摄像机的旋转。一旦取消勾选该选项，灯光便会保持在原位。因此，你可以轻松用此选项在 3D 视图中按自己的喜好旋转东向光照。

## 活动太阳配置设置

此区域显示列表中当前选中太阳配置的光照数值。更改此区域中的任何数值，场景光照都会相应地按当前设置的数值更新。

任何选中太阳配置的设置都可以自由更改，但它们不会保存回 SII 定义文件，因此如果你重新加载太阳配置库，所做的所有更改都会丢失。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Scene_Lighting | revision: 4289 | captured: 2026-10-21 23:56:14 -->
