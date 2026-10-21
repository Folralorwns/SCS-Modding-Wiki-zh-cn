# Documentation/Engine/SDK/Telemetry/Changelog

## SDK 1.10

- 新增玩法事件支持。
- 卡车和挂车现在也会提供由配置给出的车牌信息。
- 挂车
  - 新增对多挂车的支持（最多 10 个）（参见通道与配置：trailer.[index]，为向后兼容，'trailer' 的数据与 'trailer.0' 相同）
  - 新配置属性
    - brand
    - name
    - chain.type
    - body.type
  - 新通道
    - trailer.wear.wheels - (float) 所有车轮配件的平均磨损。
    - trailer.cargo.damage - (float) 此挂车内货物的损坏程度。
  - 挂车现在还会报告可提升车轴的信息。
- 任务变更
  - 新配置属性
    - cargo.unit.mass - (float) 单个货物单元的质量，单位为 kg。
    - cargo.unit.count - (u32) 任务由多少个货物单元组成。
    - cargo.loaded - (bool) 货物是否已装载？
    - job.market - (string) 任务所属的市场（可能取值见注释）
    - special.job - (bool) 是否为特殊运输任务？
  - 新通道
    - job.cargo.damage - (float) 货物的总损坏程度。
  - 特殊运输任务现在会正确报告起点和目的地城市。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/SDK/Telemetry/Changelog | revision: 3928 | captured: 2026-10-21 23:56:14 -->
