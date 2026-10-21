# Documentation/Engine/Sound/Modding

### 制作声音模组

FMOD 要求每个声音 bank 拥有自己的全局唯一标识符（GUID）。它还要求每个声音的 master bank 中的主混音总线具有相同的 GUID。<br> FMOD Studio 不提供用于编辑 GUID 的用户界面，因此为便于创建正确编写的第三方声音，我们提供 Master Bank 作为新声音项目的模板。<br> <br> 所有模组声音必须属于新的 FMOD bank，才能在游戏中使用。<br> 你需要安装 FMOD Studio 软件来为游戏创作新声音。<br> 始终使用（对应特定游戏版本的）声音 bank 模板来创建你的声音项目。<br> 访问 [Downloads](Downloads.md) 部分获取模板项目或声音示例。

## 创建自己的 bank - 分步操作

1. 下载 template.bank 项目。
2. 将项目解压到 'your new sound project' 文件夹。
3. 将 "template.fspro" 文件（位于项目根文件夹）重命名为 "[my project name].fspro"。<br>（*并非必需，但推荐。*）
4. 在 FMOD Studio 软件中打开你的项目（直接打开 [my project name].fspro 文件即可）。
5. 事件编辑器窗口中可能出现三种浏览器：事件浏览器、bank 浏览器和资源浏览器。<br>要创建新的 bank，请在 bank 浏览器的空白处右键单击，然后选择 "New Bank"。
6. 设置新 bank 的**名称**。<br>*bank 名称决定 bank 文件的名称，因此强烈建议使用与系统无关的名称（小写字符、不含空格等）。*
7. 就这样！<br>FMOD 会为新 bank 自动创建新的 GUID，因此你就拥有了自己的独立 bank，可用于游戏中的模组声音。

*说明：*<br> - *务必创建新的 bank，因为为 bank 创建新的 GUID 是必需的！*<br> - *如果你从其他模板（例如从你较早的项目）创建新项目，也始终要创建新的 bank。GUID 必须唯一！*<br> - *永远不要将 'master' bank 重命名为其他 bank！*<br> - *永远不要删除模板项目自带的标准总线！如果你删除它们并创建自己的总线，即使名称相同也无法正常工作！*

## 创建自己的声音 - 分步操作

如果你熟悉 FMOD Studio，这会非常简单。

1. 在 FMOD Studio 中打开你的项目进行编辑。<br>事件浏览器会显示项目的事件和事件文件夹。
2. 要在此浏览器中创建事件，请在空白处右键单击，然后从上下文菜单中选择 "New Event"。<br>这会打开一个子菜单，你可以在其中创建 3D 事件或 2D 事件（或自定义的默认事件）。
3. 根据你想要制作模组的声音选择 2D 或 3D 选项。
4. 为新事件设置名称。（*强烈建议使用与系统无关的名称。*）
5. 将事件分配到你的 bank。<br>右键单击 "new event"，选择 "Assign to Bank" 菜单，然后在子菜单中选择目标 bank。
6. 将事件分配到音频总线。<br>打开 "Mixer Routing" 窗口，将 "new event" 拖到目标音频总线。
7. 编辑你的声音……

*说明：*<br> - *务必创建新事件！*<br> - *如果你从其他模板（例如从你较早的项目）创建新项目，也始终要创建具有唯一 GUID 的新事件！*<br> - *'copy-paste' 过程会为事件创建新的 GUID，因此这是复制或移动声音事件的推荐方式。*<br> - *注意声音的各项能力——2D/3D、循环、控制参数。声音的特性取决于你所制作模组的声音类型。声音的某些能力对于正确播放声音是必需的。*

## 为游戏准备 bank - 分步操作

完成新声音的制作后，你应当为游戏准备声音 bank。

1. 构建 bank。<br>只需在 FMOD Studio 中选择菜单 File / Build...。<br>文件 "[bank name].bank" 应创建在项目的 "build" 子文件夹中。<br>*"master.bank" 和 "master.strings.bank" 文件可能也会被创建，请忽略它们。*
2. 导出 GUID。<br>在 FMOD Studio 中选择菜单 File / Export GUIDs...。<br>文件 "GUIDs.txt" 应创建在同一子文件夹中。<br>（*你应当能在 GUIDs.txt 文件内容的对象列表中看到你的新事件。*）
3. 将文件 "GUIDs.txt" 重命名为 "[bank name].bank.guids"。
4. 你可以通过只保留自己创建且仍属于新 bank 的对象来优化 guids 文件的内容。但这并非绝对必要。
5. 这两个文件（"[bank name].bank" 和 "[bank name].bank.guids"）就是你应在声音模组中使用的全部内容。
6. 编辑游戏的配置文件，加入指向你的音频事件的链接。
7. 享受新声音吧。

*说明：*<br> - *请注意你想在游戏中更改什么，并尽量减少文件覆盖。你应当为其他模组作者留出空间。*<br> - *如果你想更改 bank 中的所有声音，请创建同名的新 bank 并将其覆盖。*<br> - *如果你想更改全局或默认声音，请创建包含新事件的新 bank。然后仅覆盖 .soundref 文件，将声音事件重定向到你的新 bank 和事件。*<br> - *如果你想更改特定声音，请创建包含新事件的新 bank。然后覆盖指定部件或配件的配置文件，将声音重定向到你的事件。*

## 玩家制作的视频教程与信息

在这里你可以看到基本流程的各种方法或变体，相关内容保存在我们论坛 FMOD 主题帖的首帖中（帖子的其余部分是公测期间的学习与讨论）。对于某些人来说可能更容易理解，因为它是由最初不了解该系统的人创建的 - [https://forum.scssoft.com/viewtopic.php?f=178&t=281124](https://forum.scssoft.com/viewtopic.php?f=178&t=281124)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/Modding | revision: 5311 | captured: 2026-10-21 23:56:14 -->
