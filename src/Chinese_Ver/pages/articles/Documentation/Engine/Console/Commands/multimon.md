# Documentation/Engine/Console/Commands/multimon

虽然 **multimon** 命令允许在运行时动态更改显示器视图的尺寸，但增大尺寸并不能使最大有效渲染分辨率超过游戏启动时最大视图所用的分辨率。这种情况下，更改后的视图尺寸会正确，但其内容可能显得模糊。要解决此问题，请重启游戏，或先使用 **multimon save** **保存**配置，再在显示选项中临时更改（并应用）vsync 设置。

多显示器支持假定图形驱动程序提供了跨越所有物理显示器的虚拟屏幕。

支持以下命令：

### init

语法：multimon init <setup_name>

示例：multimon init three

此命令使用预定义方案之一初始化运行时配置。支持以下方案：

- **empty** - 无视图，UI 覆盖整个屏幕。这是构建更复杂自定义方案的便捷起点。
- **one** - 创建单个宽视图，UI 覆盖整个屏幕。这与预定义模式 **0** 类似，但它允许在需要时禁用内饰渲染。
- **three** - 对应预定义模式 **2** 的设置
- **three_with_dash** - 对应预定义模式 **3** 的设置

使用 **three** 或 **three_with_dash** 初始化时，初始化时刻对应的微调 cvar 状态会被应用到运行时配置。这可用于在预定义模式下用 cvar 完成基本设置，然后使用自定义模式仅微调结果。

### reload

语法：multimon reload

示例：multimon reload

使用 **multimon_config.sii** 的内容替换运行时配置

### save

语法：multimon save

示例：multimon save

将当前运行时配置保存到 **multimon_config.sii**。为使更改在游戏重启或显示设置更改后仍然保留，**必须**使用此命令。

### add

语法：multimon add &lt;name&gt; &lt;x&gt; &lt;y&gt; &lt;width&gt; &lt;height&gt;

示例：multimon add left 0.25 0 0.5 1

在输出分辨率的指定区域中定义显示器，并将其与指定名称关联。注意，名称 ui 保留用于特殊用途。

### remove

语法：multimon remove &lt;name&gt;

示例：multimon remove left

移除与指定名称关联的显示器。

### make primary

语法：multimon make_primary &lt;name&gt;

示例：multimon make_primary center

将指定显示器标记为主显示器。主显示器用作某些相对属性的基准值来源，HDR 眼睛适应也以此显示器为基准计算。这对应于配置文件中定义的第一个显示器。

### list

语法：multimon list

示例：multimon list

列出所有已定义显示器的名称

### set

语法：multimon set &lt;name&gt; &lt;attribute&gt; &lt;value&gt;

示例：multimon set left horizontal_fov_override 60

为指定显示器设置指定属性。特殊显示器名称 ui 可用于更改 UI 本身的位置。

### get

语法：multimon get &lt;name&gt; [<attribute_prefix>]

示例：multimon get left normalized_

输出指定显示器中名称以指定前缀开头的所有属性的值。与 set 一样，ui 提供对 UI 本身的访问。

## **get** 和 **set** 支持的属性

| 名称 | 示例 | 描述 |
| --- | --- | --- |
| `normalized_ui_x` | `normalized_ui_x: 0.333333` | 0 到 1 之间的小数。在整个虚拟屏幕中开始绘制 UI 的水平位置。例如，在 3 显示器设置中，第二个显示器为 **0.333333**。第三个显示器为 **0.666666**。在两显示器设置中，若 UI 应绘制在最右侧显示器上，则为 **0.5**。 |
| `normalized_ui_width` | `normalized_ui_width: 0.333333` | 0 到 1 之间的小数。UI 在整个虚拟屏幕中应占用的宽度。对于 3 显示器设置中的单个显示器，为 **0.333333**（整个区域的 1/3）；2 显示器则为 **0.5**。要占据所有显示器的空间，此值应为 **1.0**，且上面的 **normalized_ui_x** 应为 **0.0**。 |
| `name` | `name: middle` | 字符串。显示器的标识名，用于 `multimon get` 和 `multimon set`。**ui** 名称保留。 |
| `normalized_x` | `normalized_x: 0.333333` | 0 到 1 之间的小数。整个虚拟屏幕中与此显示器左边缘对应的 x 轴（水平）位置。在 3 显示器设置中，第 1 个显示器为 **0.0**，第 2 个为 **0.333333**，第 3 个为 **0.666666**。2 显示器：分别为 **0.0** 和 **0.5**。 |
| `normalized_y` | `normalized_y: 0.5` | 0 到 1 之间的小数。整个虚拟屏幕中与此显示器下边缘对应的 y 轴（垂直）位置。对于 2 行显示器设置（各显示器分辨率与尺寸相同），第 1 个显示器应为 **0.0**，第 2 个显示器为 **0.5**。在单行设置中，应为 **0.0**。 |
| `normalized_width` | `normalized_width: 0.333333` | 0 到 1 之间的小数。显示器在整个虚拟屏幕中沿 x 轴（水平）的长度。对于 3 显示器设置（各显示器分辨率与尺寸相同），所有显示器均应为 **0.333333**；而 2 显示器设置则为 **0.5**。 |
| `normalized_height` | `normalized_height: 0.5` | 0 到 1 之间的小数。显示器在整个虚拟屏幕中沿 y 轴（垂直）的长度。对于 2 行显示器设置（各显示器分辨率与尺寸相同），所有显示器均应为 **0.5**。在单行设置中，应为 **1.0**。 |
| `heading_offset` | `heading_offset: -2.0` | 介于 -180.0 与 180.0 之间的小数。为此显示器渲染内容时添加到相机的航向角（单位为度）。 |
| `pitch_offset` | `pitch_offset: -15.0` | 介于 -90.0 与 90.0 之间的小数。为此显示器渲染内容时添加到相机的俯仰角（单位为度），用于补偿其倾斜、角度或旋转。 |
| `roll_offset` | `roll_offset: -15.0` | 介于 -180.0 与 180.0 之间的小数。为此显示器渲染内容时添加到相机的整体横滚角（单位为度），用于补偿其角度或旋转。 |
| `horizontal_fov_relative_offset` | `horizontal_fov_relative_offset: 1.0` | 小数值。为此显示器渲染内容时添加到相机的额外航向角。与 **heading_offset** 不同，此值以渲染主显示器所用相机的水平 FOV 的倍数表示。对于主显示器应设为 0.0。 |
| `vertical_fov_relative_offset` | `vertical_fov_relative_offset: 0.0` | 小数值。为此显示器渲染内容时添加到相机的额外俯仰角。与 **pitch_offset** 不同，此值以渲染主显示器所用相机的垂直 FOV 的倍数表示。对于主显示器应设为 0.0。 |
| `camera_space_offset` | `camera_space_offset: (0.000000, 0.000000, 0.000000)``multimon set left camera_space_offset 0.0 0.0 0.0` | 由 x（水平，左右）、y（垂直，上下）、z（深度，前后）坐标的小数值组成的三元组。为此显示器渲染内容时添加到相机位置的偏移量。注意，在配置文件中语法为 **(x, y, z)**（由括号字符包裹，以逗号分隔），而在控制台中为 **x y z**（以空格分隔的序列）。 |
| `horizontal_fov_override` | `horizontal_fov_override: 85.0` | 介于 0.0 与 178.0 之间的小数。覆盖此显示器的水平 FOV。值 **0.0** 表示**未覆盖**。如果该显示器的水平与垂直 FOV 均未被覆盖，则 FOV 取自默认相机，并可使用“seat adjuster”UI 调整。否则，seat adjuster 中的滑块将被忽略。如果该显示器只有一个 FOV 被覆盖，则未覆盖的 FOV 将根据被覆盖的那一个计算，以保持宽高比。 |
| `vertical_fov_override` | `vertical_fov_override: 72.3` | 介于 0.0 与 178.0 之间的小数。覆盖此显示器的垂直 FOV。更多信息参见 **horizontal_fov_override** |
| `frustum_subrect_x` | `frustum_subrect_x: 0.3` | 0 到 1 之间的小数。设置用于渲染此显示器的视锥体可见部分的左边缘。生成的视锥内容会被拉伸以适配由 **normalized_*** 设置定义的屏幕区域。可用于创建非对称 FOV。 |
| `frustum_subrect_y` | `frustum_subrect_y: 0.3` | 0 到 1 之间的小数。设置用于渲染此显示器的视锥体可见部分的下边缘。参见 **frustum_subrect_x** |
| `frustum_subrect_width` | `frustum_subrect_width: 0.3` | 0 到 1 之间的小数。设置用于渲染此显示器的视锥体可见部分的宽度。参见 **frustum_subrect_x** |
| `frustum_subrect_height` | `frustum_subrect_height: 0.3` | 0 到 1 之间的小数。设置用于渲染此显示器的视锥体可见部分的高度。参见 **frustum_subrect_x** |
| `render_interior` | `render_interior: true``multimon set middle render_interior 1` | 布尔值 true/false（1/0）。是否渲染内饰（仪表盘）。注意，配置文件中接受 **true** 和 **false**。在控制台中，应分别使用 **1** 和 **0**。 |
| `render_exterior` | `render_exterior: true``multimon set middle render_exterior 1` | 布尔值 true/false（1/0）。是否渲染外观（实际上即仪表盘之外的所有内容）。注意，配置文件中接受 **true** 和 **false**。在控制台中，应分别使用 **1** 和 **0**。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Console/Commands/multimon | revision: 5612 | captured: 2026-10-21 23:56:14 -->
