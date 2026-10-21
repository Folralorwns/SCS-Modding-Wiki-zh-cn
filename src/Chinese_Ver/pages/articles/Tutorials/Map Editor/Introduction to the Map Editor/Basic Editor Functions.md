# 教程/地图编辑器/地图编辑器入门/编辑器基础功能

> [← 上一部分](Launching%20the%20Map%20Editor.md)[下一部分 →](Saving,%20Loading,%20Sectors,%20and%20Files.md)
>
> [所有步骤](../Introduction%20to%20the%20Map%20Editor.md)

<table class="wikitable tutorial_infobox" style="float: right" width="300px">
<tbody><tr>
<td colspan="2">编辑器基础功能
</td></tr>
<tr>
<td colspan="2"><span typeof="mw:File"><a class="mw-file-description" href="../../../../files/Editor%20toolbar%20full.png.md"><img class="mw-file-element" data-file-height="39" data-file-width="2362" decoding="async" height="5" src="../../../../../images/thumb/7/7c/Editor_toolbar_full.png/300px-Editor_toolbar_full.png" srcset="../../../../../images/thumb/7/7c/Editor_toolbar_full.png/450px-Editor_toolbar_full.png 1.5x, ../../../../../images/thumb/7/7c/Editor_toolbar_full.png/600px-Editor_toolbar_full.png 2x" width="300"/></a></span>
</td></tr>
<tr class="info">
<td class="row_name" width="50px"><b>主题：</b>
</td>
<td>地图编辑器入门 第 2 部分
</td></tr>
<tr class="info">
<td class="row_name" width="50px"><b>难度：</b>
</td>
<td>简单
</td></tr>
<tr class="info">
<td class="row_name" width="50px"><b>工具：</b>
</td>
<td><a href="../../../Documentation/Tools/Map%20Editor.md" title="Documentation/Tools/Map Editor">地图编辑器</a>
</td></tr></tbody></table>

现在地图编辑器已经加载完毕，我将说明主工具栏中每个按钮的作用及其一些常见用法，还会介绍一些有用的快捷键和实用提示。高级内容以及编辑器工具的说明将在后续教程中介绍。

|  |  |
| --- | --- |
| **地图** | [![Editor_toolbar_map.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_map.png)](../../../../files/Editor%20toolbar%20map.png.md) |

|  |  |
| --- | --- |
| **新建地图** | 新建一张地图 |
| **加载地图** | 加载现有地图 |
| **保存地图** | 保存当前地图 |
| **导出地图** | 用于将地图中的选定内容导出为 Selection Binary Data（SBD）或 OBJ（在建模程序中很有用）。这可用于复制地图的某些部分，或辅助制作自定义预制件或模型对象。参见高级教程以了解更多 |
| **导入地图** | 将 SBD 导入当前加载的地图 |
| **运行地图** | 关闭编辑器，并以预览配置启动游戏，以测试当前打开的地图 |

|  |  |
| --- | --- |
| **编辑模式** | [![Editor_toolbar_editmode.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_editmode.png)](../../../../files/Editor%20toolbar%20editmode.png.md) |

|  |  |
| --- | --- |
| **新建项** | 根据所选项类型打开相应的对话框，以添加新项 |
| **移动项** | 用于项的移动工具，可沿 X、Y、Z 轴移动 |
| **缩放项** | 用于适用项的缩放工具，可沿 X、Y、Z 轴缩放 |
| **删除项** | 删除所选的一个或多个项 |
| **项属性** | 根据所选项类型打开相应的对话框，以修改整个项 |
| **节点属性** | 显示所选节点的信息，包括类型、UID、旋转、位置、锁定、自由旋转等 |
| **放置起点** | 放置用于预览地图的起点（ETS2 中为粉色小车，ATS 中为粉色卡车） |
| **高度** | 沿 Z 轴移动所选对象 |
| **绕 X 轴旋转** | 沿 X、Y、Z 轴旋转所选项 |
| **绕 Y 轴旋转** | 沿 X、Y、Z 轴旋转所选项 |
| **绕 Z 轴旋转** | 沿 X、Y、Z 轴旋转所选项 |
| **笔刷** | 用于在地形和道路项的地形上绘制纹理，以及移除植被 |
| **标尺** | 用于以米为单位测量距离的工具，可多次单击以绘制线段 |
| **地形拾取器** | &lt;已废弃&gt; |
| **场景预览** | &lt;已废弃&gt; |
| **交通工具** | 用于检查 AI 交通流量，也可帮助发现道路连接错误、查看限速 |
| **顶点工具** | 用于操作地形四边形上的顶点；可塑造地形外观并封闭缝隙 |
| **静音所有声音** | 静音所有声音 |

|  |  |
| --- | --- |
| **吸附** | [![Editor_toolbar_snap.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_snap.png)](../../../../files/Editor%20toolbar%20snap.png.md) |

|  |  |
| --- | --- |
| **吸附到节点** | 节点将吸附到其他节点；用于连接道路/预制件部件或堆叠模型 |
| **吸附到顶点** | 顶点将吸附到其他顶点；与顶点工具配合使用 |
| **吸附到网格** | 项将吸附到编辑器网格上的点 |
| **吸附到地面** | 项将落到地面或其他最低点；忽略其他对象的碰撞 |
| **吸附到所有静态碰撞** | 项将落到地面或其他对象的碰撞模型上；例如将两个模型堆叠在一起 |

|  |  |
| --- | --- |
| **选择** | [![Editor_toolbar_selection.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_selection.png)](../../../../files/Editor%20toolbar%20selection.png.md) |

|  |  |
| --- | --- |
| **框选** | 通过单击并拖动方框圈选来选中项。按住 CTRL 可将项添加到选择中，按住 ALT 可将项从选择中移除 |
| **套索选择** | 通过单击并绘制围绕项的自由形状来选中项。按住 CTRL 可将项添加到选择中，按住 ALT 可将项从选择中移除 |

|  |  |
| --- | --- |
| **相机** | [![Editor_toolbar_camera.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_camera.png)](../../../../files/Editor%20toolbar%20camera.png.md) |

|  |  |
| --- | --- |
| **俯视相机** | 世界的俯视视图，用于把握整体情况并创建区域的一般布局；只有在此模式下才能看到网格 |
| **自由相机** | 允许你使用 W、A、S、D、Q、E 和滚轮向上/向下在地图中飞行 |
| **冻结相机视图** | 作用与游戏中的暂停选项类似；在相机解冻之前，使用自由相机飞行或新放置的对象都不会渲染 |

|  |  |
| --- | --- |
| **工具** | [![Editor_toolbar_tools.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_tools.png)](../../../../files/Editor%20toolbar%20tools.png.md) |

|  |  |
| --- | --- |
| **内容浏览器** | 此窗口按类别显示游戏中的所有资源；可在此查看有关特定资源的大量信息——更多信息请参阅高级教程 |
| **天气编辑器** | 允许你编辑天气、阳光、颜色、云层和 DOF |
| **设置** | 编辑器设置，包括比例、缩放速度和自动保存时间 |
| **查找** | 用于按各类标识符（扇区、UID、城市、位置等）查找各类项的对话框 |

|  |  |
| --- | --- |
| **项类型** | [![Editor_toolbar_item_type.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_item_type.png)](../../../../files/Editor%20toolbar%20item%20type.png.md) |

|  |  |
| --- | --- |
| **贝塞尔面片** | 可放置的地形块，可通过几种方式进行配置；适合修补地形中的异常孔洞 |
| **建筑** | 用于装饰和功能的模型线（隐形墙、树墙、栅栏等） |
| **相机路径** | 过场动画相机沿其移动的路径 |
| **相机点** | 相机环绕的固定点，例如第一个车库、第一辆卡车等 |
| **城市** | 定义城市名称和城市规模的项；新城市必须在游戏 DEF 文件中设置 |
| **曲线** | 与建筑项类似，但这些项具有更多选项，且视项而定，在复杂情况下更灵活 |
| **切割平面** | 性能项，用于控制平面两侧对象的可见性 |
| **过场动画** | 用于控制游戏、地图和过场动画事件的项 |
| **远景模型** | 性能项，控制项在一定距离处的可见性 |
| **渡轮** | 铁路/渡轮项，用于按照游戏 DEF 文件中的定义将玩家从一个点传送到另一个点 |
| **大门** | 按特定参数或触发器运作的动画大门 |
| **挂接** | 放置模型挂接项；请参阅关于挂接的教程 |
| **地图区域** | 用 3 个或更多点绘制的项，用于在 GPS 上定义某些区域或“虚拟”道路/预制件 |
| **地图叠加层** | 在地图上放置叠加层的项——图标、地标、文字等 |
| **模型** | 来自 */def/world/model.sii* 的模型项 |
| **移动对象** | 来自 */def/world/mover.sii* 的移动对象项；一种会播放动画或沿路径移动的对象，例如火车、动物、人 |
| **无天气区域** | 定义的天气受影响区域；例如用于标记隧道内或建筑物内不下雨等 |
| **预制件** | 具有高级用途、复杂布局和部件的模型；公司、服务设施、加油站、高速公路立交、接缝、十字路口、路口等 |
| **道路** | 用于将项相互连接的主要项，并提供连接地形的选项 |
| **标志牌** | 可编辑的标志牌/看板以及静态（不可编辑）标志牌 |
| **地形** | 与道路块类似，但没有道路 |
| **交通区域** | 用 3 个或更多点绘制的项，用于定义某些区域，以规定特定情况下的交通行为 |
| **轨迹** | 影响车辆在特定情况下行为的项；主要用于超限运输任务和其他道路事件 |
| **触发器** | 用 2 个或更多点绘制的项，用于定义触发某些对象、脚本或事件的区域，例如睡眠区域 |
| **可见性区域** | 性能项，用于管理玩家能看到什么以及在哪里看到；与切割平面配合使用 |

|  |  |
| --- | --- |
| **网格** 定义网格大小，单位为米 <br> **提示：** 网格仅在俯视相机视图中可见 | [![Editor_toolbar_grid.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_grid.png)](../../../../files/Editor%20toolbar%20grid.png.md) |

|  |  |
| --- | --- |
| **旋转** 对象的旋转步长，单位为度；按住 Shift 生效 | [![Editor_toolbar_rotation.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_rotation.png)](../../../../files/Editor%20toolbar%20rotation.png.md) |

|  |  |
| --- | --- |
| **操纵器** | [![Editor_toolbar_gizmo.png](../../../../../../images/articles/Tutorials/Map%20Editor/Introduction%20to%20the%20Map%20Editor/Basic%20Editor%20Functions/Editor_toolbar_gizmo.png)](../../../../files/Editor%20toolbar%20gizmo.png.md) |

|  |  |
| --- | --- |
| **全局** | 将移动/旋转操纵器对齐为指向北方 |
| **局部** | 将移动/旋转操纵器对齐为相对于对象指向 |
| **视图** | 将移动/旋转操纵器对齐为相对于相机视图指向 |
| **曲线** | &lt;已废弃&gt; |
| **圆形** | 使移动/旋转操纵器沿圆形移动；适用于道路和其他曲线对象 |

以上就是主工具栏的全部内容，应能帮助你朝正确方向起步。在后续教程中，我们将研究更高级的工具和地图调试项。

## 实用提示

**F1 键** - 打开帮助对话框，你可以在其中找到各种按键快捷键，让操作更轻松，还有一些快速参考<br> **F5 键** - 在编辑器右上角打开小地图视图，帮助你可视化当前操作<br> *我的项去哪了？* - 多按几次 A 键，在显示背景地图、项以及地图 + 项之间切换<br> *救命！我在编辑器里无法单击项，也无法打开控制台/对话框* - 最小化编辑器并返回桌面。再回到编辑器时，一切应恢复正常<br> *我的编辑器随机崩溃，或在保存/加载时崩溃* - 检查 editor.log.txt 以了解崩溃的性质

> [← 上一部分](Launching%20the%20Map%20Editor.md)[下一部分 →](Saving,%20Loading,%20Sectors,%20and%20Files.md)
>
> [所有步骤](../Introduction%20to%20the%20Map%20Editor.md)

<!-- source: https://modding.scssoft.com/wiki/Tutorials/Map_Editor/Introduction_to_the_Map_Editor/Basic_Editor_Functions | revision: 5504 | captured: 2026-10-21 23:56:14 -->
