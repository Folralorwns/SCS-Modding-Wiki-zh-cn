# Talk:Documentation/Engine/Units/accessory paint job data

## 必需属性

状态：未解决

属性若被标记为 *必需*，其名称需在名称列中以**粗体**显示。[Smarty](../../../../users/Smarty.md)（[讨论](../../../../user_talk/Smarty.md)）2016 年 9 月 22 日 21:15（CEST）

## Flipflake 模式/属性说明

状态：未解决

需要有更懂行的人来帮我理清 flipflake 相关的内容。我的理解是它会实现两种镜面效果：

- Clearcoat：主通道，基于使用顶点法线计算出的世界空间法线（若是 tsnmap 变体，则使用切线与 texture_nmap）
  - flake_clearcoat_rolloff：这一点我*真的*不确定。它是否影响 flake 镜面与 clearcoat 镜面的相对强度？
- Flake：较弱的通道，基于世界空间法线，并由 flake_noise 纹理以某种方式调节

此外还有一种效果，它会用 flip_color 为超出某个角度阈值（由 flip_strength 设定？）的区域着色

我理解得接近吗？[Smarty](../../../../users/Smarty.md)（[讨论](../../../../user_talk/Smarty.md)）2016 年 9 月 22 日 21:15（CEST）

<!-- source: https://modding.scssoft.com/wiki/Talk%3ADocumentation/Engine/Units/accessory_paint_job_data | revision: 2830 | captured: 2026-10-21 23:56:14 -->
