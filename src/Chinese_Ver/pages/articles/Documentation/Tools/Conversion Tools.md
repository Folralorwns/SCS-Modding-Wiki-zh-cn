# Documentation/Tools/Conversion Tools

Conversion Tools 是一组二进制程序，用于将中间格式文件转换为游戏所使用的二进制格式文件。

通常，你应当使用这些工具转换整个模组文件系统结构以供游戏内使用，其中包括：使用 SCS Blender Tools 导出的任何 3D 资源、任何定义文件、声音文件、地图文件等。

## 下载与安装

#### 下载

- **[链接 (v2.21)](https://download.eurotrucksimulator2.com/conversion_tools_2_21.zip)** - ETS2（**1.58+**）与 ATS（**1.58+**） - 64 位二进制程序，转换修复（交叉口合并）、更新的效果
- **[链接 (v2.20)](https://download.eurotrucksimulator2.com/conversion_tools_2_20.zip)** - ETS2（**1.55+**）与 ATS（**1.55+**） - 64 位二进制程序
- **[链接 (v2.18)](https://download.eurotrucksimulator2.com/conversion_tools_2_18.zip)** - ETS2（**1.50+**）与 ATS（**1.50+**） - 含预制件 v24
- **[链接 (v2.17)](https://download.eurotrucksimulator2.com/conversion_tools_2_17.zip)** - **BETA** - ETS2（**1.50+**）与 ATS（**1.50+**）
- **[链接 (v2.15)](https://download.eurotrucksimulator2.com/conversion_tools_2_15.zip)** - ETS2（**1.49+**）与 ATS（**1.49+**）
- **[链接 (v2.14)](https://download.eurotrucksimulator2.com/conversion_tools_2_14.zip)** - ETS2（**1.47+**）与 ATS（**1.47+**）
- **[链接 (v2.13)](https://download.eurotrucksimulator2.com/conversion_tools_2_13.zip)** - ETS2（**1.44+**）与 ATS（**1.44+**）
- **[链接 (v2.12)](https://download.eurotrucksimulator2.com/conversion_tools_2_12.zip)** - ETS2（**1.37 - 1.43**）与 ATS（**1.37 - 1.43**）
- **[链接 (v2.10)](https://download.eurotrucksimulator2.com/conversion_tools_2_10.zip)** - ETS2（**1.36**）与 ATS（**1.36**）
- **[链接 (v2.9)](https://download.eurotrucksimulator2.com/conversion_tools_2_9.zip)** - ETS2（**1.36**）与 ATS（**1.36**）
- **[链接 (v2.8)](https://download.eurotrucksimulator2.com/conversion_tools_2_8.zip)** - ETS2（**1.35**）与 ATS（**1.35**）
- **[链接 (v2.7)](https://download.eurotrucksimulator2.com/conversion_tools_2_7.zip)** - ETS2（**1.32**）与 ATS（**1.32**）
- **[链接 (v2.6)](https://download.eurotrucksimulator2.com/conversion_tools_2_6.zip)** - ETS2（**1.31**）与 ATS（**1.31**）
- **[链接 (v2.5)](https://download.eurotrucksimulator2.com/conversion_tools_2_5.zip)** - ETS2（**1.30**）与 ATS（**1.29**）
- **[链接 (v2.4)](https://download.eurotrucksimulator2.com/conversion_tools_2_4.zip)** - ETS2（**1.27 - 1.28**）与 ATS（**1.6 - 1.28**）
- **[链接 (v1.8)](https://download.eurotrucksimulator2.com/conversion_tools_1_8.zip)** - ETS2（**1.27 及更低版本**）与 ATS（**1.5 及更低版本**）

> **注意：** 与 ETS2（最高 **v1.26**）、ATS（最高 **v1.5**）兼容的旧版 Conversion Tools 还需要最高 **v1.6** 的旧版 SCS Blender Tools。

#### 安装

要安装 Conversion Tools 二进制程序，只需将 ZIP 包解压到 PC 上某个可找到且**具有读写权限**的文件夹中。

## 用法

Conversion Tools 有两种使用方式：

1. ***在 Blender 中使用 Conversion Tools***
  - 首先请确保已安装 SCS Blender Tools。参见：[Documentation/Tools/SCS Blender Tools/Installation](SCS%20Blender%20Tools/Installation.md)
  - 在 *Output* 属性标签页中导航至 *Conversion Helper* 面板。
  - 将 *Conversion Tools Path* 设置为指向解压后的 Conversion Tools 文件夹。
  - 此后，当你使用 Conversion Helper 的操作符时，就会用到 Conversion Tools（更多信息参见：[Documentation/Tools/SCS Blender Tools/Conversion Helper](SCS%20Blender%20Tools/Conversion%20Helper.md)）。
2. ***直接使用二进制程序（适合高级用户）***：直接使用 Conversion Tools 需要通过命令行执行 “conversion_tools/convert.cmd” 脚本完成。运行该脚本会读取 “conversion_tools/base” 文件夹中的所有中间格式资源，将其正确转换为二进制格式文件，并放入 “conversion_tools/rsrc” 文件夹。转换完成后，所有内容都将位于 “conversion_tools/rsrc/base/@cache” 内。要创建模组，你可以将 “conversion_tools/rsrc/base/@cache” 文件夹打包为 ZIP，并照常放入游戏的 mod 文件夹。如果使用 “conversion_tools/extra_mount.txt”，则 extra mount 中的每个条目都会在 “conversion_tools/rsrc” 内拥有各自转换后的文件夹条目。因此，要打包模组，你必须从各自转换后的文件夹中取出结果，并将它们放入同一个 ZIP 文件中（例如，extra mount 条目 “my_mod” 的转换结果位于 “conversion_tools/rsrc/my_mod/@cache”）。

> > **注意：** 也可以使用 “conversion_tools/extra_mount.txt” 文件，在文件的每一行中指定 “base” 的同级附加文件夹路径。这会使 Conversion Tools 像挂载 “conversion_tools/base” 文件夹一样挂载所有这些路径。

> > **注意：** 如果转换过程中出现问题，你可以在 Conversion Tools 日志文件中找到更多信息（2.18 及更早版本为 “bin/win_x86/mass_convert.log”，2.19+ 为 “conversion_tools/mass_convert.log”）。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Conversion_Tools | revision: 5744 | captured: 2026-10-21 23:56:14 -->
