# 教程/SCS Workshop Uploader/如何使用模组版本控制

> **提示：** 游戏和工具目前处于公开测试阶段。要使用信息包，请切换到 Steam 上的 public_beta 分支

通过 Steam Workshop 模组，你可以更灵活地让模组兼容指定的游戏版本。自 ETS2 1.24 更新、ATS 1.3 更新和 SCS Workshop Uploader 1.0.4 起，你可以使用新的包选项——信息包。

信息包是仅用于信息告知的包——这意味着它不会以任何方式影响玩法，它存在的目的只是让模组用户知道要使用你的模组需要做什么——例如升级到最新补丁，或降级到当前受支持的补丁（对需要一些时间才能更新模组以适配最新补丁的地图作者很有用）。

假设你的 **versions.sii** 文件如下所示：

```
SiiNunit
{

package_version_info : .content
{
    package_name: "content"
    compatible_versions[]: "1.25.*"
}

}
```

这意味着你的模组仅兼容 **1.25** 更新。

不兼容包应包含 **manifest.sii**、模组图标和模组描述文件。manifest 可以与普通包的 manifest 相同——图标可以表明这只是一个不含任何功能的信息版本，但模组用户会在模组管理器中看到模组旁红色的“Incompatible”标签，因此图标也可以与用于不同版本时相同。描述*应当*让模组用户知道如何调整游戏以使你的模组正常工作，例如：

```
To make super mod 1000 work you must downgrade your game to patch 1.25. To do that go to your steam game library, select Euro Truck Simulator 2 click right mouse button on it select Preferences go to Beta tab and select temporary_1_25 - 1.25 for incompatible mods beta and close the dialog. Steam will downgrade your game version and on next launch of the game super mod 1000 will be useable again!
```

在 **versions.sii** 中，该版本将如下所示：

```
package_version_info : .info.any
{
    package_name: "informational"
    informational: true
}
```

该版本甚至会被用于比 **1.25** 更旧和更新的版本。目前无法为更旧的游戏版本指定不同的信息包，因此，举例来说，如果你的模组面向 **1.25** 游戏补丁，你可以为 1.24 及更旧补丁指定不同的信息版本，并为 1.26 及更新版本指定另一个。不过，你可以指定信息包的版本，使其仅用于指定的版本。假设你有两个信息版本——一个提示降级（文件夹名为 **downgrade_info_package**），另一个提示游戏更新（文件夹名为 **upgrade_info_package**）。

两个包中都有清晰的描述，并附有如何进行升级和降级的建议，你现在只需将这些包添加到 **versions.sii** 中。

更旧游戏版本所用的版本将如下所示：*（我们仅使用 1.24 及更旧版本演示该功能——该功能将从 ETS2 的 1.24 补丁和 ATS 的 1.3 开始生效）*

```
package_version_info : .info.upgrade.older.game.versions
{
    package_name: "upgrade_info_package"
    informational: true
    compatible_versions[]: "1.24.*"
    compatible_versions[]: "1.23.*"
    compatible_versions[]: "1.22.*"
}
```

更新游戏版本所用的版本将如下所示。

```
package_version_info : .info.downgrade.newer.game.versions
{
    package_name: "downgrade_info_package"
    informational: true
}
```

你可能注意到，较新的包中没有指定兼容版本。因为你的内容包如下所示：

```
package_version_info : .content
{
    package_name: "content"
    compatible_versions[]: "1.25.*"
}
```

所有更旧的游戏版本都列在升级包中——只有高于 1.25 的补丁才会选中降级包。

<!-- source: https://modding.scssoft.com/wiki/Tutorials/SCS_Workshop_Uploader/How_to_use_mod_versioning | revision: 2702 | captured: 2026-10-21 23:56:14 -->
