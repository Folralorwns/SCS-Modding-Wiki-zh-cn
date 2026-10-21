# 文档/引擎/单元/雨刮器数据

**wiper_data** 单元类用于定义雨刮器，以清除内部视图中模拟玻璃窗格上的雨滴。每个雨刮器使用一个独立的单元。它们被定义为无名单元，通过 *wipers* 属性归属于 [glass_pane_data](glass%20pane%20data.md)，通常通过 **/def/vehicle/truck/<brand.model>/interior/glass.sui** 包含。

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| center_bone | string |  | 动画内饰模型骨架中用作雨刮器质心的骨骼名称。该骨骼的 Z 轴应指向玻璃窗格“内部”（大致与玻璃定位器的 Y 轴相反）。 |
| length | float | 0.0 | 沿 center_bone 的 X 轴的雨刮器“刮片”长度，单位为米。 |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/wiper_data | revision: 3276 | captured: 2026-10-21 23:56:14 -->
