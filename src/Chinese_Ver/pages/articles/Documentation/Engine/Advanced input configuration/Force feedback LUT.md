# 文档/引擎/高级输入配置/力反馈 LUT

在 1.42 游戏更新（ETS2 与 ATS）中，引擎获得了对自定义力反馈查找表（**L**ook **U**p **T**able）的支持，它可以改变方向盘输出力的线性度。其目的在于让用户能够克服某些方向盘硬件无法线性输出的局限，并按自己的喜好校准输出。

## 用法

要使用用户自定义的 FFB LUT，需要在配置文件文件夹中创建一个单元文件：

- 本地配置：`<game_user_path>/profiles/<profile_hash>/ffb_lut.sii`
- Steam 云配置：`<game_user_path>/steam_profiles/<profile_hash>/ffb_lut.sii`

当加载了已定义 `ffb_lut.sii` 的配置文件时，控制器设置中 **Overall gain** 选项旁会出现感叹号，标示该文件正在被使用。此外，如果文件已正确加载，则无论当前使用的是哪个方向盘，它都会始终被使用。因此，如果你有两个方向盘并在它们之间切换，那么自定义 ffb LUT 对两个方向盘都是相同的。

## 文件内容

自定义力反馈 LUT 是仅包含一个单元的文本文件：

```
SiiNunit
{
input_force_feedback_lut : ffb.lut {
	# This ffb LUT presents simple scaling by factor 0.5

	output_values[]: 0.0   # input value: 0.0; output value: 0.0
	output_values[]: 0.25  # input value: 0.5; output value: 0.25
	output_values[]: 0.5   # input value: 1.0; output value: 0.5
}
}
```

`input_force_feedback_lut` 单元包含一个名为 `output_values` 的数组变量，它为相应的输入值定义查找值。每个条目的输入值按如下方式计算：`<entry_index> / (<number_of_entries> - 1)`。介于其间的所有输入值都在最近的两个条目之间进行线性插值。

请注意，所有输出值都会被限制在 <0,1> 区间内，因为缩放超过 1.0 可能导致不可预测的行为。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Advanced_input_configuration/Force_feedback_LUT | revision: 5718 | captured: 2026-10-21 23:56:14 -->
