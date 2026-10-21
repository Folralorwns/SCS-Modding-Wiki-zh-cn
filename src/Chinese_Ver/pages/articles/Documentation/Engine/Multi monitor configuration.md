# Documentation/Engine/Multi monitor configuration

## 前提条件

仅支持以单个高分辨率虚拟屏幕的形式呈现给游戏的多显示器配置。你需要根据显卡芯片组类型使用 Nvidia Surround、AMD Eyefinity 或类似技术。按照下文说明以多个独立视图设置游戏时，应禁用基于驱动程序的边框校正（即显示驱动可能提供的那个），并改用相应的 cvar（游戏配置变量，见下文），让游戏自行处理边框间隙。

默认内饰摄像机略微向下，以便更清楚地看到卡车仪表盘。这在普通显示器上效果良好，但在多显示器设置的侧视图中会显得不正确。因此，建议在启动游戏前将 g_interior_camera_zero_pitch 设为 1，以在不修改游戏数据的情况下禁用此特性。

## 预定义模式

### 类型

游戏支持多种内置模式。这些模式通过 **r_multimon_mode** cvar 选择。请注意，所有内置模式都期望至少三台显示器，并且仅当分辨率的宽高比至少为 2.5:1 时才会真正启用。

支持以下模式：

- **0** - 单一视图，UI 覆盖整个区域。显示器被表示为单个超宽平面显示器，UI（用户界面）覆盖整个区域。这是默认值。缺点是由于 FOV（视场角）很宽，两侧图像会明显失真。

[![Multimon_schema_flat.png](../../../../../images/articles/Documentation/Engine/Multi%20monitor%20configuration/Multimon_schema_flat.png)](../../../files/Multimon%20schema%20flat.png.md)

- **1** - 单一视图覆盖整个区域，UI 元素位于第三台显示器的中央（例如三显示器设置中的中央显示器）。这与 **0** 类似，但 UI 只覆盖中央显示器的区域。
- **2** - 三台显示器三个独立视图。每台显示器都有自己的视图，默认水平 FOV 为 50 度。UI 位于中央显示器上。

[![Multimon_schema_3.png](../../../../../images/articles/Documentation/Engine/Multi%20monitor%20configuration/Multimon_schema_3.png)](../../../files/Multimon%20schema%203.png.md)

- **3** - 使用四显示器设置中最左侧的三台显示器显示与 **2** 相同的视图，最后一台显示器显示俯视仪表盘和方向盘的辅助视图。

[![Multimon_schema_31.png](../../../../../images/articles/Documentation/Engine/Multi%20monitor%20configuration/Multimon_schema_31.png)](../../../files/Multimon%20schema%2031.png.md)

### 附加配置

模式 **2** 和 **3** 的可视化还可通过以下 cvar 进一步控制：

- **r_multimon_border_fov_left** 和 **r_multimon_border_fov_right** - 中央显示器与左/右显示器之间由边框（例如显示器外框）覆盖的视角，单位为度。用于边框校正。
- **r_multimon_fov_horizontal** 和 **r_multimon_fov_vertical** - 每个视图使用的视场角。如果其中只有一个非零，另一个会按分辨率宽高比计算。如果两者都为零，则使用基于当前游戏内摄像机的默认 FOV 计算。
- **r_multimon_vert_offset_left** 和 **r_multimon_vert_offset_right** - 左/右显示器相对中央显示器的垂直偏移，单位为米。可用于上下移动左侧视图，以在垂直视场角有限的情况下改善后视镜的可见性。
- **r_multimon_rotation_center**、**r_multimon_rotation_left**、**r_multimon_rotation_right** 和 **r_multimon_rotation_aux** - 应用于各显示器视图的额外逆时针旋转。最可能使用值 90 或 -90，以补偿物理方向与显卡驱动中配置不同的显示器（例如纵向与横向）。这样即使驱动程序不支持，也能混用纵向和横向方向。
- **r_multimon_interior_in_main** - 控制主视图中驾驶室内饰的渲染。如果存在某种形式的实体内饰，可用于禁用内饰。
- **r_multimon_exterior_in_aux** - 控制辅助视图（模式 3）中外部场景的渲染。请注意，即使禁用了外部场景，阴影目前仍会更新。

## 自定义模式

此模式为 1-4 台显示器的设置提供了更大的灵活性。通过将 **r_multimon_mode** cvar 设为 4 来启用。请注意，与预定义模式不同，此模式不受显示器宽高比的限制。在此模式下，游戏从 **\Documents\<game name>\multimon_config.sii** 读取配置。如果该文件不存在，则会在游戏首次以此模式启动时创建。你既可以手动编辑该文件，也可以使用游戏内 [multimon](Console/Commands/multimon.md) 命令在运行时完成大部分调整。请注意，使用 **[multimon](Console/Commands/multimon.md)** 命令时，务必在退出游戏或通过游戏选项界面更改设置之前显式保存结果，否则这些更改将会丢失。

UI 和各显示器在驱动程序创建的虚拟显示中的位置使用归一化坐标指定，其中 [0,0] 对应左下角，[1,1] 对应右上角。整个显示器或 UI 必须位于 [0;1] 范围内，否则行为未定义。

### ui 的属性

- **normalized_ui_x** - UI 左下角在驱动程序创建的虚拟显示中的位置。
- **normalized_ui_width** - UI 在驱动程序创建的虚拟显示中的宽度。

### 单个显示器的属性

- **name** - 显示器名称，供 **[multimon](Console/Commands/multimon.md)** 命令使用。
- **normalized_x** 和 **normalized_y** - 显示器左下角在驱动程序创建的虚拟显示中的位置。
- **normalized_width** 和 **normalized_height** - 显示器视图在驱动程序创建的虚拟显示中的尺寸。
- **horizontal_fov_relative_offset** 和 **vertical_fov_relative_offset** - 该值乘以主显示器的视场角，并加到摄像机的偏航角和俯仰角上。当主显示器的 fov 自动计算时，可用于让显示器相对定位。
- **heading_offset**、**pitch_offset** 和 **roll_offset** - 加到摄像机朝向的旋转偏移，单位为度。可用于将视图指向所需的相对方向，或进行边框校正。
- **camera_space_offset** - 摄像机相对标准位置的偏移。可用于将摄像机移到某个特定位置，或在垂直方向上偏移它，以更好地匹配显示器的物理布局。
- **horizontal_fov_override** 和 **vertical_fov_override** - 覆盖相应的视场角。如果两个值都为零，则使用标准摄像机计算的角度。如果至少有一个非零，则直接使用该值，并按宽高比计算第二个角度。
- **render_interior** - 启用驾驶室内饰的渲染。如果你有实体驾驶室，可使用此项。
- **render_exterior** - 启用将外部场景（例如天空盒、世界以及卡车外部）渲染到视图。请注意，无论此设置如何，投射到该视图的阴影仍会包含外部场景。
- **frustum_subrect_x**、**frustum_subrect_y**、**frustum_subrect_width** 和 **frustum_subrect_height** - 允许指定完整视锥体中渲染到该显示器的部分。可用于将投影中心移到显示器中心之外。例如，当使用两台前置显示器表示卡车挡风玻璃而驾驶员坐在左侧那台之前时，可以移除视锥体的左侧部分，将投影中心移到驾驶员前方。请注意，更改该视图会改变有效宽高比，因此需要设置两个 fov 覆盖值来修正。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Multi_monitor_configuration | revision: 1686 | captured: 2026-10-21 23:56:14 -->
