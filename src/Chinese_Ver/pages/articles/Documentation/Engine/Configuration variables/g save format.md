# 文档/引擎/配置变量/g save format

|  |  |
| --- | --- |
| **名称：** | g_save_format |
| **用途：** | 用于存储游戏存档的格式。 |
| **配置：** | global |
| **值：** | integer - format |

## format：

| 值 | 说明 |
| --- | --- |
| 0 | 默认模式，游戏视为默认的方式可能随构建或测试状态而变化 |
| 1 | 强制仅二进制 |
| 2 | 强制仅文本 **（见下方提示）** |
| 3 | 为调试目的同时创建二进制存档与文本存档 **（见下方提示）** |

> **提示：** 文本格式（选项 2 和 3）保存耗时明显更长，并可能在自动保存时造成卡顿尖峰。请谨慎使用！

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Configuration_variables/g_save_format | revision: 3688 | captured: 2026-10-21 23:56:14 -->
