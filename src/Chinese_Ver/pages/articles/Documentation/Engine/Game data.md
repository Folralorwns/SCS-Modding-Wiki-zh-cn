# 文档/引擎/游戏数据

> **提示：** 请注意，本页面已过时，因为每次更新都会带来游戏结构的重大变化！有关结构变化的更多信息，请查看[模组更新](../../Games/ETS2/Modding%20guides.md)页面。

所有 SCS 游戏都使用部分规定的文件夹结构。这意味着某些资源必须具有正确的名称并放置在正确的文件夹中，否则游戏可能出错甚至崩溃。因此，本主题将深入介绍游戏基础文件夹结构、其中的关键资源及其在文件夹中的位置。

总体而言，本主题展示并描述通过 [Game Archive Extractor](../Tools/Game%20Archive%20Extractor.md) 从游戏安装目录中两个基本 .scs 扩展名文件（"**base.scs**" 和 "**def.scs**"）提取得到的文件夹和文件结构。

## 游戏根文件夹

游戏根文件夹包括：

```
Root game folder
 ├automat         Material storage with generated material files produced during conversion of 3D model assets with conversion tools.
 ├contentbrowser  Folder used by Map Editor content browser.
 ├custom          Legacy folder for storing custom/modded definitions (NOTE: This folder is obsolete and might be removed in the future).
 ├def             See: Definitions.
 ├dlc             Shared models used by dlc such like "dead end" sign.
 ├effect          Set of compiled shader effects used by game for rendering of any visual element.
 ├font            See: Fonts.
 ├map             Storage for maps and its additional data.
 ├material        See: Predefined materials.
 ├model           Storage for 1st generation of map assets.
 ├model2          Storage for 2nd generation of map assets.
 ├prefab          Storage for 1st generation of prefab assets.
 ├prefab2         Storage for 2nd generation of prefab map assets.
 ├road_template   Road template models for new system of road generation.
 ├sound           See: Sounds.
 ├system          Low level engine resources needed for console and fall-back cases of missing resources.
 ├ui              See: UI definitions.
 ├unit            Definitions for predefined hookups spawned in game trough locators, for example: light flare, light sources, no weather areas.
 ├vehicle         See: Vehicle model resources.
 ├video           Video based animated textures for UI.
 ├autoexec.cfg    Configuration file which is automatically executed on game start-up.
 └version.txt     File containing game version string.
```

### 定义

用于大多数可配置游戏内容的定义，例如：车辆、经济、地图资产等。

```
Root game folder
├def
  ├animated_model                Directory with definitions for animated models triggered when distance to player is small enough.
  ├camera                        See: Camera definitions.
  ├cargo                         See: Cargo definitions.
  ├city                          Defines cities for game. Each city is defined in its own SII file.
  ├climate                       See: Climate definitions.
  ├company                       See: Company definitions.
  ├country                       See: Country definitions.
  ├desktop                       Desktop (main menu) scene configurations. By default "/def/desktop/config.sii" is used.
  ├ferry                         See: Ferry definitions.
  ├initial_save                  Stores zero day save files where folder: normal is used by creating new user profile and preview while running game in preview mode.
  ├regional_settings             Regional settings profiles data. By default there should be 3 profiles: Europe, USA and UK.
  ├sign                          See: Sign definitions.
  ├stamp                         Defines brush stamping layouts which are defined as stamps in "/def/world/stamp.sii" and used in Map Editor while using Stamp Tool.
  ├vehicle                       See: Vehicle definitions.
  ├world                         See: World definitions.
  ├aux_lamp_colors.sii           Defines players vehicle auxiliary light mask colors.
  ├bank_data.sii                 Bank loans configuration.
  ├car_colors.sii                Defines colors for AI traffic cars.
  ├cargo.sii                     Storage of cargoes for trailer generation. When defining your own cargoes use infixed version of this SII file for example: "cargo.my_mod.sii".
  ├city.sii                      Storage of cities in game. When defining your own cities use infixed version of this SII file for example: "city.my_mod.sii".
  ├climate.sii                   Storage of climate profiles. When defining your own climate use infixed version of this SII file for example: "climate.my_mod.sii".
  ├company.sii                   Storage of companies that can be used in game. When defining your own companies use infixed version of this SII file for example: "company.my_mod.sii".
  ├...
  ├country.sii                   Storage of countries used in game. When defining your own countries use infixed version of this SII file for example: "country.my_mod.sii".
  ├...
  ├economy_data.sii              Game economy definition.
  ├...
  ├env_data.sii                  Environment global configuration such as day in the year.
  ├...
  ├ferry.sii                     Storage of ferry ports. When defining your own cargoes use infixed version of this SII file for example: "ferry.my_mod.sii".
  ├...
  ├game_data.sii                 Various global game definitions.
  ├hdr.sii                       High dynamic range effect definitions.
  ├...
  ├job_trailer_preview.sii       Scene setup for generating preview images of trailers in freight market.
  ├job_truck_preview.sii         Scene setup for generating preview images of trucks in quick jobs.
  ├job_wotr_trailer_preview.sii  Scene setup for generating preview images of trailers in WOTR contracts.
  ├...
  ├mail_data.sii                 Defines players mails.
  ├photo_camera_data.sii         Configuration of Photo Mode camera.
  ├...
  ├police_data.sii               Defines player offences: fine amounts, offence check delay.
  ├...
  ├sound_player.sii              Defines sounds for UI actions and global game sounds.
  ├...
  ├traffic_data.sii              Defines different AI traffic data: total AI max count, yield attributes, safety distances etc.
  ├traffic_light_lamp_colors.sii Defines mask colors for traffic lights.
  ├trailer_preview_scene.sii     Defines scene configuration parameters for Trailer Browser.
  ├...
  ├truck_colors.sii              Defines colors for AI traffic trucks.
  ├truck_config_scene.sii        Defines scene configuration parameters for Upgrade Shop & Truck Browser.
  ├truck_dealer_scene.sii        Defines scene configuration parameters for Truck Dealers.
  ├...
  └vehicle_lamp_colors.sii       Defines players vehicle light mask colors.
```

#### 摄像机定义

摄像机定义文件夹（"**/def/camera**"）使用 "**camera_storage(.infix).sii**" 文件作为存储文件，定义玩家在游戏中可以使用的摄像机（UI 界面不由摄像机处理，因为 UI 直接绘制在屏幕的 2D 平面上）。请注意，这里只定义游戏内可用摄像机的存储，而游戏中实际使用哪个摄像机取决于用户当前选择的视图和当前使用的玩家车辆。

除了存储文件之外，摄像机定义文件夹还包含 "**cutscene.sii**" 文件，用于定义不同过场动画中的摄像机及其运动。

```
Root game folder
├def
  ├camera
    ├...                        Folders for cut scenes camera definitions.
    ├ui                         Folder for storing camera movement definitions related to game desktop (main menu).
    ├units                      Folder for storing players camera included in "camera_storage" SII files.
    ├camera_storage.sii         Defining cameras storage that can be used in game by player. When creating your own cameras use infixed storage file name like: "camera_storage.mymod.sii".
    ├camera_storage.oculus.sii  Same as camera_storage.sii with purpose of defined cameras for Oculus Rift head set.
    └cutscene.sii               Defines cut scene data for each type.
```

#### 货物定义

此文件夹包含玩家在游戏中可以运输的所有货物定义。

每种货物由一个 SII 文件以及一个包含一个或多个 SII 文件的文件夹定义，这些 SII 文件定义可以运载该货物的挂车。因此，对于每种货物，你在 "**/def/cargo/**" 中有一个 SII 文件，并在 "**/def/cargo/<cargo_name>/**" 文件夹中有一个或多个 SII 文件。下方树状图展示了货物 "**<cargo_name>**" 的示例定义。

```
Root game folder
├def
  ├cargo
    ├<cargo_name_1>             Folder defining trailers that can carry cargo defined in "<cargo_name>.sii" file.
      ├trailer.unit.name.sii    Defines trailer that can carry this cargo. SII file is named by trailer SiiUnit name.
      └...                      More definitions for different trailers carrying this cargo.
    ├<cargo_name_2>
      └...
    ├...                        The rest of cargo trailer definition folders.
    ├<cargo_name_1>.sii         Defining one cargo data.
    ├<cargo_name_2>.sii
    └...                        The rest of unique cargoes definition.
```

#### 气候定义

每种气候定义在各自的文件夹 "**/def/climate/<climate_name>/**" 中，通常包含配置文件 SII：一个用于好天气 "**nice.sii**"，另一个用于恶劣天气 "**bad.sii**"。气候定义在地图编辑器中使用（Editor Settings -> Weather 选项卡）。

默认情况下应至少有两种气候：

```
Root game folder
├def
  ├climate
    ├reference    Reference climate.
      ├bad.sii    Climate definition for bad weather.
      └nice.sii   Climate definition for nice weather.
    └...          The rest of climates.
```

#### 公司定义

公司是地图上玩家任务（例如挂车交付）的进入和离开地点。因此，在定义新公司时，请务必将其包含在公司存储文件 "**/def/company(.infix).sii**" 中，否则该公司不会出现在地图编辑器中，之后也不会出现在游戏中。

包含公司 "**<company_name_1>**" 的公司定义文件夹如下所示：

```
Root game folder
├def
  ├company
    ├<company_name_1>        Folder defining company data, named same as its corresponding company data file.
      ├editor                Folder containing definitions for cities in which this company exists and which prefab will be used for it.
      ├in                    Folder containing SII files for cargoes this company accepts.
      └out                   Folder containing SII files for cargoes this company is shipping out.
    ├<company_name_2>
      └...
    ├...                     The rest of the folders defining other companies data.
    ├<company_name_1>.sii    File defining company: name, trailer look and sounds.
    ├<company_name_2>.sii
    └...                     The rest of companies definitions.
```

#### 国家定义

定义可在地图编辑器中使用、并随后在游戏中使用的国家。在定义新国家时，请务必将其包含在国家存储文件 "**/def/country(.infix).sii**" 中。

每个国家都有自己的文件夹，用于定义所有可能的国家特定数据。值得一提的是 AI 交通出现频率的修改，其做法是在 "**/def/country/<country_name>/ai/**" 文件夹中添加 SII 文件。每个 SII 文件定义一种 AI 车辆修改后的频率，其名称表明对应哪种车辆。可用的文件名是 AI 车辆定义中使用的 AI 车辆单元名称后缀（AI 车辆定义可在 "**/def/vehicle/ai/**" 中找到）。

国家定义的树状概览：

```
Root game folder
├def
  ├country
    ├<country_name_1>      Folder defining other country specific data: license plates, speed limits, AI cars frequency.
      ├ai                  Folder containing SII files for AI traffic vehicles, that should have modified frequency in that country.
      ├license_plates.sii  Defines license plate data for that country.
      └speed_limits.sii    Defines speed limits for AI traffic for that country.
    ├<country_name_2>
      ├...
      └...
    ├...                   Folders for the rest of the countries data.
    ├<country_name_1>.sii  File defining country general data: id, name, country code, position, fuel price etc.
    ├<country_name_2>.sii
    └...                   The rest of the countries definition.
```

#### 渡轮定义

定义渡轮的名称及其连接。为使游戏正常运行，在地图编辑器中添加渡轮点时必须使用这些渡轮。所有渡轮还必须包含在渡轮存储文件 "**/def/ferry(.infix).sii**" 中。

而连接则定义在 "**/def/ferry/connection/**" 文件夹中。该文件夹中的每个文件定义一个从一个渡轮到另一个渡轮的单向连接。连接的方向由 SiiUnit 名称定义，例如 SiiUnit 名称 "**conn.&lt;ferry1&gt;.&lt;ferry2&gt;**" 表示从 &lt;ferry1&gt; 到 &lt;ferry2&gt; 的渡轮连接。

渡轮定义的树状概览：

```
Root game folder
├def
  ├ferry
    ├connection   Folder with SII files defining connections between ferries. Each file defines one way direction between two ferries.
    └...          SII files defining ferries. Each file defines one unique ferry.
```

#### 标志牌定义

标志牌定义用于新的即时标志牌生成系统，该系统使用：

- 图像图集，用于将多个相关图像合并为一个，并使用图集条目仅引用图像的一部分。
- 边框模板，用于将标志牌背景图像替换为生成的图像，且缩放时不会损失质量。

此外，标志牌定义还包括项目和模板文件夹，游戏在此保存在地图编辑器中创建的项目和最终标志牌模板。

标志牌定义的完整树状结构：

```
Root game folder
├def
  ├sign
    ├atlas            Defines image atlases for signs. SII files are created by hand.
    ├frame            Defines frames templates for signs. SII files are created by hand
    ├project          Defines sign projects which links associated data for example: creation of signs for one country. SII files are created by Map Editor.
    ├template         Defines signs template featuring all sign components, their positions and other properties. SII files are created by Map Editor.
    └templates.sii    Templates storage file including templates from "/def/sign/template/ folder. Also managed by Map Editor
```

#### 车辆定义

车辆定义负责配置 SCS 游戏中非地图资产的各种车辆类型及其部件。这些配置的绝大部分属于玩家可用车辆及其部件的配置。

```
Root game folder
├def
  ├vehicle
    ├addon_hookups                      Folder for defining available libraries of players truck accessory hookups e.g. horns, interior toys or grill lights.
    ├ai                                 See: AI vehicle definitions
    ├ai_wheel                           AI vehicle wheel definitions containing separate definitions for front and rear wheels.
    ├f_cover                            Players vehicle front wheel cover definitions.
    ├f_disc                             Players vehicle front wheel rim definitions.
    ├f_hub                              Players vehicle front wheel hub definitions.
    ├f_nuts                             Players vehicle front wheel nuts definitions.
    ├f_rim                              Obsolete. Used only for backward compatibility with 2nd gen. of players truck wheel system.
    ├f_tire                             Players vehicle front tire definitions.
    ├f_wheel                            Partially obsolete. Used for backward compatibility with 1st gen. of players truck wheel system and defining AI trucks front wheel.
    ├r_cover                            Players vehicle rear wheel cover definitions.
    ├r_disc                             Players vehicle rear wheel rim definitions.
    ├r_hub                              Players vehicle rear wheel hub definitions.
    ├r_nuts                             Players vehicle rear wheel nuts definitions.
    ├r_rim                              Obsolete. Used only for backward compatibility with 2nd gen. of players truck wheel system.
    ├r_tire                             Players vehicle front tire definitions.
    ├r_wheel                            Partially obsolete. Used for backward compatibility with 1st gen. of players truck wheel system and defining AI trucks rear wheel.
    ├trailer                            See: Trailer definitions.
    ├truck                              See: Player trucks definitions.
    ├truck_company                      Trucks configurations for Quick Jobs.
    ├truck_company_uk                   Trucks configurations for RHD trucks (UK related) Quick Jobs. This folder exists only in: ETS2 game data.
    ├truck_dealer                       See: Truck dealer definitions.
    ├truck_dealer_uk                    Defines assortment of RHD trucks for dealers; has same structure as: Truck dealer definitions and exists only in ETS2 game data.
    ├truck_desktop                      Trucks configurations used in Truck Browser.
    ├truck_desktop_uk                   Trucks configurations for RHD trucks used in Truck Browser, if player started game in UK.
    ├t_wheel                            Trailer wheels definitions.
    ├addon_hookup_storage.sii           Storage file for including truck accessory hookup libraries in the game. For new libraries use e.g. "addon_hookup_storage.mymod.sii".
    ├physics.sii                        Defines players vehicle common physics parameters.
    ├physics_interior_camera.sii        Defines interior camera movement physics parameters.
    ├rim_data.sii                       Defines players vehicle wheels assembling rules and backward compatibility for old game profiles using old wheels assembling system.
    ├traffic_storage_bus.sii            Storage file for AI traffic bus vehicles inclusion in game. For new AI buses use e.g. "traffic_storage_bus.mymod.sii".
    ├traffic_storage_car.sii            Storage file for AI traffic car vehicles inclusion in game. For new AI cars use e.g. "traffic_storage_car.mymod.sii".
    ├traffic_storage_semi_trailer.sii   Storage file for AI traffic semi trailers inclusion in game. For new AI semi trailers use e.g. "traffic_storage_semi_trailer.mymod.sii".
    ├traffic_storage_truck.sii          Storage file for AI traffic trucks inclusion in game. For new AI truck use e.g. "traffic_storage_truck.mymod.sii".
    ├traffic_trailer_type.sii           Defines types of AI traffic trailers for which storage files will be searched and included in game. For new trailer types use e.g. "traffic_storage_truck.mymod.sii".
    ├traffic_vehicle_type.sii           Defines types of AI traffic vehicles for which storage files will be searched and included in game.
    └trailer_storage.sii                Storage file for inclusion of trailers for player. For new trailers use e.g. "traffic_storage.mymod.sii".
```

##### AI 车辆定义

AI 车辆定义由 AI 交通车辆定义文件以及相应的文件夹组成，文件夹中包含定义各车辆底盘数据的 "**chassis.sii**" 文件。所有车辆定义文件都必须包含在以下某个交通存储文件中："**traffic_storage_bus(.infix).sii**"、"**traffic_storage_bus(.infix).sii**"、"**traffic_storage_bus(.infix).sii**"，或任何其他自定义的交通车辆类型存储文件。

> **注意：** Euro Truck Simulator 2 额外有 "**/def/vehicle/ai/truck/**" 子文件夹，用于对交通卡车底盘定义的文件夹进行分组。

> **注意：** 此文件夹不包含交通挂车的定义，因为通常的做法是在挂车定义中定义 AI 交通挂车。

```
Root game folder
├def
  ├vehicle
    ├ai
      ├<ai_vehicle_1>       Folder for defining AI traffic vehicle chassis file.
        └chassis.sii        Defines AI traffic vehicle 3D model paths and variants/looks configuration for it.
      ├<ai_vehicle_2>
        └chassis.sii
      ├...                  The rest of AI traffic vehicles chassis configuration folders.
      ├<ai_vehicle_1>.sii   Defines AI traffic vehicle. Has to be included in some traffic vehicle storage file inside parent folder: "/def/vehicle/".
      ├<ai_vehicle_2>.sii
      └...                  The rest of AI traffic vehicles definition files.
```

##### 挂车定义

挂车定义用于定义供玩家卡车使用的挂车或供 AI 交通使用的挂车。定义挂车时，必须创建一个 SII 文件以及一个包含 "**chassis.sii**" 和/或额外货物定义的文件夹。所有挂车定义文件还必须包含在某个存储文件中才能在游戏中使用。如果挂车应由玩家使用，则必须将其包含在某个 "**trailer_storage(.infix).sii**" 文件中；如果挂车应由 AI 卡车使用，则必须将其包含在某个 "**traffic_storage_semi_trailer(.infix).sii**" 文件中，或包含在自定义类型的 AI 挂车存储文件中。

> **注意：** AI 挂车和玩家挂车的处理方式有所不同。玩家挂车使用 "**trailer**" SiiUnit 类，命名约定为 `trailer.<name>`；而 AI 挂车使用 "**traffic_trailer**" SiiUnit 类，命名约定为 `traffic.trailer.<name>`。

```
Root game folder
├def
  ├vehicle
    ├trailer
      ├<trailer_1>               Folder for cargo hookup and chassis definition of first trailer.
        ├company_paint_job       Folder for company-specific paint job definitions of first trailer.
          └<trailer_look>.sii    Defines paint job for companies with corresponding trailer_look attribute. (eg plain, trameri, etc), this cannot exceed 12 characters in length
        ├custom_paint_job        Folder for custom paint job definitions, selectable in the trailer selection dialog.
        ├<cargo_accessory>.sii   SII file defining cargo model hookup for this trailer.
        ├...                     More SII files defining cargo models available for second trailer.
        └chassis.sii             Defines chassis model of the trailer.
      ├<trailer_2>               Folder for cargo hookup and chassis definition of second trailer.
        └chassis.sii
      ├...                       The rest of the trailers folders for defining their cargo hookups and chassis.
      ├<trailer_1>.sii           Trailer definition for player usage referencing just chassis file from "<trailer_1>" folder.
      ├<trailer_1_cargo>.sii     Trailer definition for player usage referencing chassis and cargo hookup file from "<trailer_1>" folder.
      ├<trailer_2>.sii           Second trailer definition for player usage referencing chassis from "<trailer_1>" folder.
      ├<trailer_2_traffic>.sii   Second trailer definition for AI traffic referencing chassis from "<trailer_2>" folder.
      └...                       The rest of definition files defining other trailers.
```

##### 玩家卡车定义

玩家卡车定义中包含用于定义玩家可在游戏中使用的卡车及其配件的所有定义。

更多信息请参见专门页面：[玩家卡车定义](Game%20data/Player%20trucks%20definitions.md)。

#### 世界定义

定义所有可使用地图编辑器放置到地图上的世界物品及其行为。所有不同的物品类型都有自己的定义文件，同类型的物品在该文件中定义。

定义新世界物品时，应改用带中缀的 SII 文件命名方式，例如定义新静态模型时，带中缀的文件示例为："**model.mymod.sii**"。

```
Root game folder
├def
  ├world
    ├building_model.sii          Defines continuous models that can be used as curve path profile models.
    ├building_scheme.sii         Defines schemas for curve path building items  (hedges, fences, electro wirings, tree avenues ...). In Map Editor used as Buildings item type.
    ├detail_vegetation.sii       Defines global detail vegetation data.
    ├detail_vegetation_def.sii   Defines detail vegetation models to texture assignments.
    ├hinge.sii                   Currently unused. It defined object that could be placed on map and be swung by player truck e.g. swing doors.
    ├model.sii                   Defines static map models which can be in Map Editor used as Models item type.
    ├model.custom.sii            Obsolete. Used only for backward compatibility.
    ├mover.sii                   Defines map models with animations which can be in Map Editor used as Movers or Walkers item type.
    ├overlay.sii                 Defines overlay names for cities and roads.
    ├overlay.custom.sii          Obsolete. Used only for backward compatibility.
    ├prefab.sii                  Defines prefab map models like companies, gas stations, dealers, crossings. In Map Editor used as Prefabs item type.
    ├prefab.custom.sii           Obsolete. Used only for backward compatibility.
    ├railing.sii                 Defines side roads elements like: crash barriers, anti noise barriers etc.
    ├road.sii                    Basic road data definition like different road lines lengths.
    ├road_edge.sii               New template road system edge definitions.
    ├road_look.sii               Old road system definitions. In Map Editor used as Road item type.
    ├road_look.template.sii      New template road system definitions. In Map Editor used as Road item type.
    ├road_material.sii           Old road system materials definitions.
    ├road_sidewalk.sii           Old road system side walk definitions.
    ├semaphore_model.sii         Defines semaphore models that can be used in semaphore profiles.
    ├semaphore_profile.sii       Defines semaphore profiles which can be assigned to prefabs models. Used in Blender Tools or Maya.
    ├sign.sii                    Defines road signs. In Map Editor used as 'Sign item type.
    ├sign.custom.sii             Obsolete. Used only for backward compatibility.
    ├sound_item_data.sii         Defines sound items that can be placed on map and will be triggered once player comes near. In Map Editor used as Sound item type.
    ├stamp.sii                   Defines stamp brushes for brushing in Map Editor. They are used with Brush tool.
    ├terrain_material.sii        Defines terrain materials paths. Used indirectly on more map items through their properties.
    ├terrain_profile.sii         Defines terrain profiles that can be used on the sides of the road. Used indirectly on road items through properties.
    ├traffic_lane.sii            Defines general traffic lanes data like: allowed vehicles types, spawn count limits and frequencies.
    ├traffic_rules.sii           Defines traffic rules that can be used on Traffic area' items in Map Editor. Additionally they can be used while creating prefab model using Blender Tools or Maya.
    ├traffic_rules.compat.sii    Obsolete. Used only for backward compatibility.
    ├trigger_action.sii          Defines action triggers that can be used to trigger different commands in game. Used in Blender Tools or Maya while creating prefab model.
    ├vegetation.sii              Defines vegetation profiles that can be used on road sides. In Map Editor they are used indirectly from properties of Road item type.
    ├vegetation_model.sii        Defines tree and bush vegetation models for usage in vegetation.sii file.
    └vegetation_old.sii          Obsolete. Used only for backward compatibility.
```

### 字体

用于存储游戏字体的文件夹。主要用于 UI 以及车辆仪表盘显示屏内部。

```
Root Game Folder
├font
  ├license_plate             Fonts used by licence plates.
  └sign                      Fonts used by road signs.
```

### 预定义材质

预定义材质和纹理库。

```
Root Game Folder
├material
  ├...
  ├editor          Map Editor background textures.
  ├environment     Environmental cube maps used for reflections.
  ├...
  ├logo            Textures for in game company logos & SCS Software logos.
  ├...
  ├road            Textures & materials for roads. Folder supports material aliasing.
  ├...
  ├sign            Texture atlases & frames for new sign system.
  ├special         Special purposes texture atlases.
  ├terrain         Terrain textures & materials e.g. for grass, sand, water. Folder supports material aliasing.
  ├tiled           Collection of tillable textures.
  ├ui              Textures and materials used by UI such like buttons, windows, icons etc.
  └material.db     Physical materials (substances) database. Names of this substances may be used on materials attribute called "Substance".
```

### 声音

游戏使用的声音库。

```
Root Game Folder
├sound
  ├ai                      Sounds used by AI Traffic vehicles such like engine sounds, horns and sirens.
  ├environment             Environment ambient loops.
  ├mover                   Sounds produced by mover objects in game.
  ├music                   Music used in many places for example during cutscenes.
  ├truck                   Truck related sounds such like engine sounds, crash sounds, trailer attach sounds etc.
  └ui                      Sound effects used when user is interacting with the UI. For example click on the UI element.
```

### UI 定义

所有 UI 布局和控件定义的库，包括车辆仪表盘。

```
Root Game Folder
├ui
  ├company_manager         Company manager UI layouts.
  ├dashboard               Truck dashboard UI layouts.
  ├desc                    UI descriptors.
  ├editor                  Editor UI layouts.
  ├license_plate           Licence plate UI layouts.
  ├options                 Options screens UI layouts.
  ├template                UI templates (definitions of the controls look).
  └...                     UI window layouts for all in game windows.
```

### 车辆模型资源

```
Root Game Folder
├vehicle
  ├ai         AI traffic vehicles models and resources of all types: cars, trucks, buses, trains.
  ├driver     Driver models for usage in AI traffic vehicles.
  ├share      Shared texture resources for vehicles.
  ├trailer*   Models and resources for player and AI traffic trailers. (*)- for ETS2 there will be "trailer_eu" instead.
  ├truck      Player trucks vehicles models and resources.
  └wheel      Models and resources for all vehicle wheels except wheels for player trucks.
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Game_data | revision: 5754 | captured: 2026-10-21 23:56:14 -->
