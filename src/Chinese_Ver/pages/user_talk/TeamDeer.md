# 用户讨论:TeamDeer

你好 TeamDeer，

本页面将作为与你交流你所做贡献的专用沟通渠道。

## 地图编辑器教程

教程完成后请在此告知我，之后我会给你反馈，因为我们需要做一些一致性调整，以便采用与现有格式相似甚至相同的格式。也就是更好的页面命名、尽可能加入上一页/下一页链接等。

---

你好！以下教程已由我完成。也许我们可以替换掉其他一些过时的地图编辑器教程？这样大概也会让新教程的命名更容易。

: [https://modding.scssoft.com/wiki/Tutorials/Map_Editor/00_-_Launching_the_Map_Editor_(2024)](../articles/Tutorials/Map%20Editor/00%20-%20Launching%20the%20Map%20Editor%20(2024).md)

: [https://modding.scssoft.com/wiki/Tutorials/Map_Editor/01_-_Basic_Editor_Functions_(2024)](../articles/Tutorials/Map%20Editor/01%20-%20Basic%20Editor%20Functions%20(2024).md)

: [https://modding.scssoft.com/wiki/Tutorials/Map_Editor/02_-_Saving,_Loading,_Sectors,_and_Files_(2024)](../articles/Tutorials/Map%20Editor/02%20-%20Saving,%20Loading,%20Sectors,%20and%20Files%20(2024).md)

另外，你们能否顺便在 wiki 上启用可视化编辑器扩展？这样写教程会容易一些，不必每次都写代码。（[https://www.mediawiki.org/wiki/Extension:VisualEditor](https://www.mediawiki.org/wiki/Extension:VisualEditor)）

---

嗯，我看到你在这些主题上进展很快。在你进一步深入之前，我想先讨论一下你的计划，因为我越是浏览你的主题，越觉得它们更像文档而非教程。从我看到的内容来看，你似乎在展示地图编辑器中特定工具的工作原理。如果是这样，我们就会把它移到文档部分。如果不是，那我们需要稍微整理一下这些主题，使它们整体上成为一个教程，即“如何从 A 到 Z 创建你的第一张地图”，并为它们取合适的标题，以便教程主页上的自动列表能按预期工作。

所以能否请你先列一份你想创建的内容清单并发布在本页，谢谢。

---

感谢你的反馈！其实我关注这个 wiki 已经很久了（自 2018 年初起），并注意到从那时起它并没有太大变化。你说得对，我的教程目前确实很像文档（说明）。我认为好的教程不应只由步骤 1、2、3 组成，而应是“这里，这个项目是这样工作的，原因如下，这里是支撑它的文档”，然后才是制作该项目（道路片段、预制件等）所涉及的基本步骤。 <br> <br> 在 TruckersMP，我用类似的教程和说明教过许多团队成员，并取得了非常成功的成果，把对地图编辑器 / Blender 零基础的人培养成了知识丰富的模组制作者。我观察到卡车模拟社区认为 SCS wiki 非常过时且帮助不大，因为其方法过于简化且信息不足。举个例子，目前的地图编辑器教程就已非常过时（1 年以上）。我计划通过我的教程，为想要进行 ETS2 / ATS 基础到高级模组制作的人提供简单易行的方法，帮助他们学习并提升技能与理解。话虽如此，我认为先做说明再给教程，对于建立对某个主题的理解和技能很重要。过去 3 年里，我在 Discord 和 Steam 上被问过近 1,000 个关于地图/Blender 的问题。我尝试用我在这里使用的简化教程方法来解答所有这些问题。 <br> <br> 另外，我一直以为这个 wiki 的文档部分（以及其他部分）是 SCS 面向模组制作者对所用项目的关联与说明。基本上，我以为文档部分只供 SCS 使用，而教程部分也只由 SCS 编写。（我们可以怪现代世代不懂 wiki 如何运作）例如，人们想知道 ETS2 2023 年冬季传送门是如何工作的，但 SCS 尚未分享其工作原理。许多人认为 SCS wiki 已经死了。我曾多年编辑 Valve software 的 Source Engine wiki，帮助模组制作者为该游戏制作模组——看看它现在的样子！总之，我认为整个教程部分都应进行修订，以适应更现代的时代。 <br> <br> 抱歉我的消息可能有点东拉西扯，我上夜班，而且在美国，所以我现在有点累，但能为支持的游戏和社区做点牺牲是值得的。总之，以下是我的教程基本大纲，当然，随着情况变化或我对相关主题的兴趣/学习深入或减退，我会更新它 <br> <br> 地图编辑器

1. 入门（设置、加载、保存、运行、基本信息）
2. 道路
3. 预制件
4. 附加项目（天气区域、模型、建筑、曲线）
5. 性能项目（可视区域、裁剪平面）
6. 外部地图

处理 SII 文件

1. 创建自定义卡车经销商
2. 创建自定义挂车经销商
3. 渡轮/铁路连接
4. 自定义城市
5. 自定义挂车部件与链类型

共享内容（Blender/SII/地图编辑器）

1. 自定义公司（2 种类型）
2. 模型外观 #color_variants 及更多
3. AI 导航网络（路径）
4. Mover 模型
5. 内饰动画（仪表盘）
6. 自定义车辆（truckersmp 侦察车）
7. 建议的工作文件与文件夹结构
8. 使用 SCS 模型制作静态停放车辆（truckersmp）
9. 涂装与涂装设置 + 涂装配件
10. 自定义配件
11. 修改（hack）游戏中间格式以生成文件体积更小的模组改动
12. 公司传送门（2023 年圣诞）
13. 车轮设置/配置
14. 本地文件模组制作（truckersmp）（车队模式）
15. 单元挂接

Blender

1. 创建基础预制件（公司）
2. 自定义道路片段
3. 自定义预制件（接缝、分叉、纹理、alpha 混合、挂接点）
4. 如何设置 Blender（现代版本）
5. 外观与变体系统示例
6. 使用 Blender 为模型制作基础 AO
7. SCS Blender RFX 设置的实用方法

FMOD

1. 创建新的环境音与点音源
2. 创建配件音效（喇叭）
3. 创建发动机音效（完整）

目前大致就是这些。我欢迎反馈，如果你们想修改我的教程，或对这类信息应放在哪里有何建议，我也很欢迎。对了，可视化编辑器扩展怎么样？我目前正在写另一个教程：道路。请告诉我，这是否就是你所指的符合标准以及分部描述？

---

嚯，计划很大，不错，那我们逐步推进：

1. 地图编辑器部分没问题，只要你像道路教程那样组织。是的，你创建的道路教程就是我所指的拆分为更多部分。
  1. 不过道路教程仍然缺少前往教程上一部分和下一部分的链接，请看一下：[Tutorials/Beginners/Simple_cube/1._How_to_prepare_tools_for_mod_creation](../articles/Tutorials/Beginners/Simple%20cube/1.%20How%20to%20prepare%20tools%20for%20mod%20creation.md) 的顶部和底部，你会找到导航元素 <- 上一步 | 所有步骤 | 下一步 ->。
  2. 此外，桥梁与隧道应作为教程的额外部分，或从道路教程主页中移除。
  3. 创建入门教程，把你现有的以 00 开头的教程移入其中，并尽可能从标题中去掉数字前缀。（是的，我知道其中一些是原有的，待你的教程准备好获批后，它们会被移到废弃区或重命名）
2. Blender 和 FMOD 部分应该也可以，那就动手吧！其余部分我需要先弄清楚如何放在当前教程主页中，我相信等所有地图编辑器、Blender 和 FMOD 教程完成时，我就会知道其余部分该放在哪里了。

[50keda](https://modding.scssoft.com/index.php?title=User:50keda&action=edit&redlink=1)

---

听起来不错！

1. 入门教程现在应该已集中在一个页面，就像我做道路教程那样，并添加了页面链接
2. 道路教程应该有页面链接
3. 你第 2 点是什么意思？我是应该把桥梁和隧道单独移出来，放在道路之下？去掉“高级道路施工”，基本上让道路/隧道各有自己的页面？

目前我正在写预制件教程。 <br> [TeamDeer](../users/TeamDeer.md)

---

1. 好的，我会批准这些并进行小幅修正。
2. 好的，也会批准它们，并在需要时修正。
3. 我会修正。我的意思只是，在 [教程/地图编辑器/道路](../articles/Tutorials/Map%20Editor/Roads.md) 页面上不应有额外的链接部分。这类页面只应使用 TutorialPartEntry 模板，不要自定义链接。
4. 现在检查完教程后，我注意到两件事：
  1. `<br>` 标签，请完全不要使用；如果需要换行，用两次回车实现。自定义间距是我们尽量避免的做法，原因在于格式一致性和未知的显示故障。所以请检查你的页面，将所有 br 标签移除/替换为两次回车，或在需要时使用新段落。如有需要，请毫不犹豫地使用三级标题。
  2. `<big>` 标签，请也将它们移除，文本不应通过标签进行任何放大。
  3. 总的来说，如果你想使用任何非标准格式标签，请先询问，会有人指导你。基本上，你应尽量使用 markdown 格式，并尽可能只使用 code 和 nowiki 自定义格式标签。有趣的是，我在这个帖子里不得不同时使用这两者来展示 big 和 br 标签 :D

--[50keda](https://modding.scssoft.com/index.php?title=User:50keda&action=edit&redlink=1)（[讨论](https://modding.scssoft.com/index.php?title=User_talk:50keda&action=edit&redlink=1)）15:57，2024 年 4 月 19 日（UTC）

---

为什么不允许使用“big”？我喜欢更大的文字，不用这个标签的话，在很多平台上文字看起来太小了。另外，你还没有谈可视化编辑器扩展？能详细说明一下吗？使用这个扩展会让我创建这些教程更容易。

入门教程已准备好，另一个教程也已准备好，并移除了 BR 和 BIG。

[TeamDeer](../users/TeamDeer.md)

---

1. 我们尽量让所有主题使用相同的格式，即保持一致，big 格式也是如此。而 big 并不适合你上面提到的用法，它可以用来让个别单词更突出。
2. 至于扩展，情况类似，我们不想使用任何非必要的额外扩展，以便尽可能保持整洁和精简（从用户和维护的角度来看）。
3. 所有提交的页面都已批准，感谢你的修改。

--[50keda](https://modding.scssoft.com/index.php?title=User:50keda&action=edit&redlink=1)（[讨论](https://modding.scssoft.com/index.php?title=User_talk:50keda&action=edit&redlink=1)）14:43，2024 年 4 月 23 日（UTC）

[50keda](https://modding.scssoft.com/index.php?title=User:50keda&action=edit&redlink=1)

---

办公室搬迁进行得怎么样？我计划很快开始再写一些教程。你们搬迁期间我休息了一下——wiki 运行缓慢，我们也在忙 TMP 10 的事情。

- Deer

---

我已添加此页面以反映新文件：[https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_addon_painted_data](https://modding.scssoft.com/wiki/Documentation/Engine/Units/accessory_addon_painted_data)

[50keda](https://modding.scssoft.com/index.php?title=User:50keda&action=edit&redlink=1)

---

你好，我已为 1.54 版本更新了这个单元类；希望你能批准——我正在写自定义公司和新货物系统的教程。 :) [https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/cargo_model_match&oldid=5671](https://modding.scssoft.com/index.php?title=Documentation/Engine/Units/cargo_model_match&oldid=5671)

[TeamDeer](../users/TeamDeer.md)

---

是的，谢谢，我已经批准并修正了几处。

现在说说新货物系统主题的教程。不确定此刻我们是否真的应该做这件事，这只是第一版，我不确定所有内容是否都会保持不变，这意味着之后可能需要大量维护，而我不确定自己能提供这样的维护。

至于自定义公司，这需要由其他编辑来照看，希望我能找到人来审核。

[50keda](https://modding.scssoft.com/index.php?title=User:50keda&action=edit&redlink=1)

<!-- source: https://modding.scssoft.com/wiki/User_talk%3ATeamDeer | revision: 5674 | captured: 2026-10-21 23:56:14 -->
