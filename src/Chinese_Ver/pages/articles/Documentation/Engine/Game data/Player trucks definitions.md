# 文档/引擎/游戏数据/玩家卡车定义

玩家卡车定义可以分为两个组成部分：

- 车辆部件定义描述卡车及其众多配件的特性。

: -可以将其视为一组用于搭建卡车的积木；它们不会自行组装！

- 车辆配置将部件定义组装成一辆可驾驶或可购买的车辆。

: -可以将其视为给游戏的指令，让它在车辆首次加载时把这些积木（数据定义）组装成一辆车。

## 车辆部件定义

每辆卡车都在各自的文件夹中配置（例如下方树状视图中的 "**<brand.truck>**"），其中包含：

1. SII 文件：**data.sii** - *定义：卡车信息、摄像机、卡车各部件与必需配件的回退规则。共有 8 条强制回退规则：chassis、cabin、interior、engine、transmission、f_wheel（或 f_tire）、r_wheel（或 r_tire）、paint_job 以及 head_light*。
2. 子文件夹：（**chassis**、**cabin**、**interior**、**engine**、**transmission**、**paint_job**、**head_light**、**sound**）- *定义卡车的不同部件与配件。前 7 个文件夹因强制回退规则而必需，sound 文件夹则用于卡车必需的声音定义。*
3. 可选文件夹：**accessory** - *定义用户可在游戏内的升级商店中安装的卡车所有可能的配件。该文件夹下还有一级子文件夹，用于区分玩家可安装到卡车上的不同配件类型；玩家选择相应的配件类型后，这些类型就会在升级商店中列出。此外，子文件夹的名称直接对应卡车 3D 模型必须具有的模型定位器名称，只有具备这些定位器，才能在游戏中启用相应类型的配件。*

```
Root game folder
├def
  ├vehicle
    ├truck
      ├<brand.truck>               Truck main configuration folder.
        ├accessory                 Folder for defining all accessory types which can be installed on this truck.
          ├beacon                  Folder for defining accessories of the type "beacon".
            ├shape1.sii            File defining one beacon model which can be named freely (no restriction applies on SII file naming inside accessory type).
            └...                   More beacon models definition files.
          └...                     Folders defining more accessory types and its model definitions.
        ├cabin                     Folder with SII files defining cabin mandatory truck part; one cabin per one SII file.
        ├chassis                   Folder with SII files defining chassis mandatory truck part; one chassis per one SII file.
        ├engine                    Folder with SII files defining engine mandatory truck part; one engine per one SII file.
        ├head_light                Folder with SII files defining head light mandatory truck part; one head light type per one SII file.
        ├interior                  Folder with SII files defining interior mandatory truck part, its animations, dashboard colors and glass data; one interior per one SII file.
        ├paint_job                 Folder with SII files defining paint job mandatory truck part; one paint job per one SII file.
        ├transmission              Folder with SII files defining transmission mandatory truck part; one transmission per one SII file.
        └data.sii                  Defining truck global data: info, cameras and fallback rules.
      ├<2nd_brand.truck>           Folder defining second truck having the same inner folder structure as first truck above.
      ├...                         Folders for defining more trucks.
      └fallback.sii                Configuration of fallback truck in the case player loads save with truck that is not in game data any more (may happen when truck mod is removed).
```

## 车辆配置

根据在游戏中的用途，玩家卡车配置分为三种类型：

1. 经销商：位于文件夹 "**/def/vehicle/truck_dealer/**" 中（如果卡车有右舵版本，则也位于英国经销商文件夹 "**/def/vehicle/truck_dealer_uk/**" 中）。
2. 桌面预览：位于文件夹 "**/def/vehicle/truck_desktop/**" 中（如果卡车有右舵版本，则也位于英国经销商文件夹 "**/def/vehicle/truck_desktop_uk/**" 中）。
3. （可选）快速任务卡车：位于文件夹 "**/def/vehicle/truck_company/**" 中（如果卡车有右舵版本，则也位于英国经销商文件夹 "**/def/vehicle/truck_company_uk/**" 中）。

```
Root game folder
├def
  ├vehicle
    ├...
    ├truck_company                      Truck configurations for Quick Jobs.
      ├double                           Truck configurations for doubles Quick Jobs (ETS2 Only)
      ├heavy                            Truck configurations for heavy Quick Jobs
      ├oversize                         Truck configurations for Special Transport Quick Jobs
      ├<brand>_truck_a.sii              Quick Job truck configurations. The file name up to the first underscore is used for brand sorting.
      └...                              Additional Quick Job truck configurations
    ├truck_company_uk                   Quick Job truck configurations for RHD trucks (UK related). (ETS2 Only)
    ├truck_dealer                       Contains truck configurations in brand-specific subfolders..
      ├<brand>                          Contains truck configurations. The name of the folder should be tokenizable and will be detected as a brand.
        ├some_truck.sii                 Dealer truck configuration.
        └...                            More dealer truck configurations. Typically one per file.
    ├truck_dealer_uk                    Defines assortment of RHD trucks for dealers and has the same structure as truck_dealer. (ETS2 only)
    ├truck_desktop                      Truck configurations used in Truck Browser.
      ├some_truck.sii                   Desktop truck configuration. There are no naming restrictions, but be wary of naming collisions.
      └...                              Additional Desktop truck configurations
    ├truck_desktop_uk                   Truck configurations for RHD trucks used in Truck Browser if player started game in UK. (ETS2 only)
    ├truck_used                       Contains used truck configurations in brand-specific subfolders..
      ├<brand>                          Contains truck configurations. The name of the folder should be tokenizable and will be detected as a brand.
        ├some_truck.sii                 Used truck configuration.
        └...                            More used truck configurations. Typically one per file.
    ├truck_used_uk                    Defines assortment of used RHD trucks and has the same structure as truck_used. (ETS2 only)
    └...
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Game_data/Player_trucks_definitions | revision: 5748 | captured: 2026-10-21 23:56:14 -->
