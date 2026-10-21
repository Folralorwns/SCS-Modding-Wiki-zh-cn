# User talk:Aveneger

你好，Avenger，

本页面将作为你讨论自身贡献的交流渠道。

2024-04-16 - **建议/想法**：我一直在考虑编写一个脚本，用来生成某种“API 参考”，其完整程度要涵盖两款游戏（ATS/ETS2）在 def.scs 文件中所用内容的合并总和。也就是说，比如：

```
def/vehicle/ai/bus_opalin.sii

traffic_spawn_condition: .traffic.bus_s.condition.time
{
 # spawn only in following game time intervals
 type: time

 # 06:00 - 9:00
 num_param[]: 360
 num_param[]: 540

 # 16:00 - 18:00
 num_param[]: 960
 num_param[]: 1080
}

traffic_spawn_condition: .traffic.bus_s.condition.city
{
 # spawn only inside cities
 type: city
 str_param[]: "?*"
}
```

根据上面的用法，我可以推断 `traffic_spawn_condition` 类型（我该称它为“类型”吗？）可以接受 `type` 作为 `enum`、`num_param[]` 作为 `integer`、`str_param[]` 作为 `string`。

然后通过解析所有文件，脚本应该能够发现其他用法，例如 `type: area` 和 `type: weather`，并为该情形“补全”枚举。它还能判断出 `type` 是必填项，而 `*_param` 是可选项。

接下来是描述的问题。要么让描述与脚本保持同步，以便每次发布都重新生成 **API 参考**。也可以直接从 wiki 获取新增或更新的描述，并传给脚本。

然后为便于维护，我们可以把它全部发布在单个页面中，并例如用 `details` 和 `summary` HTML 启用可展开区块，[details 展开元素 - MDN 文档](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)，让所有内容都能在单个页面中搜索，而不是（至少最初）无休止地滚动（但愿如此）。

```
<details>
 <summary>traffic_spawn_condition</summary>
 type => enum (area, city', time, weather)
</details>
```

嗯，这可能是个有点大的工程，但那会是我乐意去做的事！

---

*> 嗯，当任何单元发生更新或删除时，这套东西该如何运作？*

**A：确实需要完整重跑，以重新生成整个“超大页面”。而且我想，wiki 应该能像任何 CVS 大概能做到的那样，以漂亮的差异对比说明究竟改了什么。**

*> 谁来维护单元的数据库？*

**A：恐怕得靠志愿者。起初是我自己。**

*> 你会为每次更新重新生成所有用到的单元并上传吗？*

**A：这正是我提出的一个点。如果页面只有一个，事情会容易得多，对吧？然后各主题通过某种 `<details>` HTML 实体“收缩”，用类似的东西让单元可以折叠和展开。至少对文档的初版迭代而言如此。如果效果不错，之后可以做一些自动化，把它分发到各个独立页面，我不确定 wiki 在多大程度上可“自动化”，但表单提交之类的，我觉得相当可行，只是在生成器的初版迭代中并不真正现实。**

*> 关键在于，我们数据中用到的并非一切都仍然有效，某些属性可能已经废弃，或者只是留在那里、从未被游戏加载。简单来说，如果要让这样的东西出现在官方 Modding Wiki 上，它就应该从代码本身生成，因为单元在哪里声明、哪些有效、哪些应当存在，只有代码才知道。*

**A：我完全同意这个观点。但我能接触到的是数据；我在构思这个想法时觉得，近似而简洁的东西总比没有好。正确的做法确实是，对，从源码中提取。但我觉得 SCS 里至今还没有人有机会去做类似的事情，对吧？**

所以，这个提案确实充满了限制条件，会有大量假设和猜测，比如可接受的输入（float/int/str）、可接受的范围，主要来自对数据中所用值的“有根据的猜测”，或人工录入的文档（描述，即社区逐渐弄清各属性作用的部分）。因此，`spawn_ratio` 可能会把可接受值报告为 0.0 到 1.0 的区间，而看起来它们在游戏中至少能达到 6.0，并带有某种含义。至少它能成为模组作者乃至开发团队针对该游戏的一个集中参考，也可以用来发现数据中的错误（单次使用冒出来、范围高得离谱、与上一版本相比出现意外变化等）。

（请原谅我不太会使用这个讨论频道 :}）

--[50keda](https://modding.scssoft.com/index.php?title=User:50keda&action=edit&redlink=1) ([讨论](https://modding.scssoft.com/index.php?title=User_talk:50keda&action=edit&redlink=1)) 16:24, 19 April 2024 (UTC)

<!-- source: https://modding.scssoft.com/wiki/User_talk%3AAveneger | revision: 5500 | captured: 2026-10-21 23:56:14 -->
