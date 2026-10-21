# Documentation/Engine/Units/sound data voice navigation

**声音数据 - 语音导航包**

每个语音导航语音包都定义在单独的配置文件中。配置文件位于以下游戏数据文件夹：

```
    /base/sound/navigation
```

文件可以任意命名，但良好的约定是 "language_actor".sii

文件是非常简单的单元，包含以下属性：

## 属性

| 名称 | [类型](../Units.md#Attribute_types) | 默认值 | 描述 |
| --- | --- | --- | --- |
| pack_name | string |  | 包的名称（在游戏中显示）。格式为 "`Language` - `Actor name` (`Optional Variant`)"（例如 `"English - Skye (UK)"`） |
| pack_dir | string |  | 包含声音文件的文件夹名称。（例如 `pack_dir: "/sound/navigation/english_skye_uk"`） |

良好的做法是让配置单元文件与声音数据文件夹使用相同的名称。

## 声音数据文件夹

文件夹中的文件为 ogg 格式（扩展名为 .ogg）。文件内容由文件名前缀决定（参见下表）。

具有相同前缀的文件用于同一命令，其使用是随机的。

(*我们强烈建议每个交通命令只使用一个文件。此处的随机化非常不直观。*)

| 文件前缀 | 命令（英语） | 备注 |
| --- | --- | --- |
| turn_left | "Turn left." |  |
| turn_right | "Turn right." |  |
| keep_left | "Keep left." |  |
| keep_right | "Keep right." |  |
| exit_left | "Exit left." |  |
| exit_right | "Exit right." |  |
| go_straight | "Go straight on." |  |
| roundabout_1 | "At the roundabout take the first exit." |  |
| roundabout_2 | "At the roundabout take the second exit." |  |
| roundabout_3 | "At the roundabout take the third exit." |  |
| roundabout_4 | "At the roundabout take the fourth exit." |  |
| roundabout_5 | "At the roundabout take the fifth exit." |  |
| roundabout_6 | "At the roundabout take the sixth exit." |  |
| exit_now | "Exit now." | *用于环形交叉路口。* |
| prepare_turn_left | "Get ready to turn left." |  |
| prepare_turn_right | "Get ready to turn right." |  |
| prepare_exit_left | "Get ready to exit left." |  |
| prepare_exit_right | "Get ready to exit right." |  |
| compound_turn_left | "Turn left ..." | *复合命令的第一部分。* |
| compound_turn_right | "Turn right ..." | *复合命令的第一部分。* |
| compound_keep_left | "Keep left ..." | *复合命令的第一部分。* |
| compound_keep_right | "Keep right ..." | *复合命令的第一部分。* |
| compound_exit_left | "Exit left ..." | *复合命令的第一部分。* |
| compound_exit_right | "Exit right ..." | *复合命令的第一部分。* |
| compound_go_straight | "Go straight on ..." | *复合命令的第一部分。* |
| and_then_turn_left | "... and then turn left." | *复合命令的第二部分。* |
| and_then_turn_right | "... and then turn right." | *复合命令的第二部分。* |
| and_then_keep_left | "... and then keep left." | *复合命令的第二部分。* |
| and_then_keep_right | "... and then keep right." | *复合命令的第二部分。* |
| and_then_exit_left | "... and then exit left." | *复合命令的第二部分。* |
| and_then_exit_right | "... and then exit right." | *复合命令的第二部分。* |
| and_then_go_straight | "... and then continue straight on." | *复合命令的第二部分。* |
| start | 例如 "OK, here we go!" | *新路线的开始。适合随机化。* |
| finish | 例如 "Here we are..." | *路线的终点。适合随机化。* |
| recomputing | 例如 "Recomputing..." | *当玩家偏离所选路线时使用。适合随机化。* |
| u_turn | "Make a u-turn." | *适合随机化。* |
| speed_signal | (*仅声学信号，无语音命令。*) |  |
| speed_warning | "Caution, please mind the speed limit." | *超过速度时的警告。* |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/sound_data_voice_navigation | revision: 4186 | captured: 2026-10-21 23:56:14 -->
