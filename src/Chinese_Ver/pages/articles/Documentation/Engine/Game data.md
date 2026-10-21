# Documentation/Engine/Game data

> **TIP:** Be aware that this page is obsolete, due to big changes in game structure with each update! For more information on structure changes check [modding updates](../../Games/ETS2/Modding%20guides.md) pages.

All of SCS games are using partially prescribed folder structure. This means that some resources must have the proper name and be placed into the proper folder otherwise game may malfunction or even crash. That's why this topic is giving insight to game base folder structure, its crucial resources and their place in folders.

In general, this topic is showing and describing the structure of the folders and files as you get them by using the [Game Archive Extractor](../Tools/Game%20Archive%20Extractor.md) for two basic files with .scs extension found in game installation directory: "**base.scs**" and "**def.scs**".

## Root game folder

Root game folder consists of:

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

### Definitions

Definitions for most of configurable game content like: vehicles, economy, map assets etc.

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

#### Camera definitions

Camera definitions folder ("**/def/camera**") is using "**camera_storage(.infix).sii**" files as storage files defining cameras that can be used by player while in game (UI interface is not handled by cameras, as UI is drawn directly on screen 2D plane). Note that this defines only storage for available in game cameras, but which camera is used in the game depends on currently user selected view and current used player vehicle.

Beside storage files camera definitions folder also includes "**cutscene.sii**" file which defines camera and its movement in different cut-scenes.

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

#### Cargo definitions

This folder contains all cargoes definitions that player can transport in the game.

Unique cargo is defined by SII file and folder having one or more SII files defining trailers which can carry this cargo. So for each cargo you have one SII file inside "**/def/cargo/**" and one or multiple SII files inside folder "**/def/cargo/<cargo_name>/**". Example definition for cargo: "**<cargo_name>**" is shown in the tree below.

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

#### Climate definitions

Each climate is defined in its own folder "**/def/climate/<climate_name>/**" and usually have profile SII files: one for nice weather "**nice.sii**" and second for bad weather "**bad.sii**". Climates definitions are used in Map Editor (Editor Settings -> Weather tab).

By default there should be at least two climates:

```
Root game folder
├def
  ├climate
    ├reference    Reference climate.
      ├bad.sii    Climate definition for bad weather.
      └nice.sii   Climate definition for nice weather.
    └...          The rest of climates.
```

#### Company definitions

Companies are entry and exit places on map for player missions (e.g. trailer delivery). So when defining new company make sure to include it in company storage file "**/def/company(.infix).sii**" otherwise company won't appear in the Map Editor and later in game.

Company definition folder with included company "**<company_name_1>**" would look like:

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

#### Country definitions

Defines available countries that can be used in the Map Editor and later in game. While defining new country make sure to include it in country storage file "**/def/country(.infix).sii**".

Each country has its own folder defining all possible country specific data. Worth mentioning is modification of AI traffic appearing frequencies, which is done by adding SII files inside "**/def/country/<country_name>/ai/**" folder. Each SII file defines modified frequency for one AI vehicle, where its name tells which car it is. Possible file names are AI vehicles unit name suffixes used inside AI vehicle definitions (AI vehicles definitions can be found in: "**/def/vehicle/ai/**").

Tree overview of country definitions:

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

#### Ferry definitions

Defines names of the ferries and their connections. For proper working in game this ferries has to be used in Map Editor while adding Ferry points. All ferries also have to be included in ferry storage file "**/def/ferry(.infix).sii**".

Connections on the other hand are defined in "**/def/ferry/connection/**" folder. Each file in that folder defines one direction connection from one ferry to second ferry. How connection is directed is defined by SiiUnit name, so for example SiiUnit name: "**conn.&lt;ferry1&gt;.&lt;ferry2&gt;**" is presenting ferry connection from &lt;ferry1&gt; to &lt;ferry2&gt;.

Tree overview of ferry definitions:

```
Root game folder
├def
  ├ferry
    ├connection   Folder with SII files defining connections between ferries. Each file defines one way direction between two ferries.
    └...          SII files defining ferries. Each file defines one unique ferry.
```

#### Sign definitions

Sign definitions are meant for new on-the-fly sign generation system which uses:

- Image atlases which are used to combine several related image into one and use atlas entries to address only part of the image.
- Frame templates which replaces sign background images for generated ones, where quality is not compromised with scaling.

Moreover sign definitions includes projects and template folder where game saves projects and end sign templates created within Map Editor.

Whole sign definitions tree structure:

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

#### Vehicle definitions

Vehicle definitions are responsible for configuration of any type of vehicles and its parts in SCS games that are not map assets. Biggest part of this configurations belongs to configuration of possible player vehicles and its parts.

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

##### AI vehicle definitions

AI vehicle definition consists of AI traffic vehicles definition files and folders for them containing "**chassis.sii**" file defining chassis data of each vehicle. All of the vehicles definition files have to be included in one of traffic storage files: "**traffic_storage_bus(.infix).sii**", "**traffic_storage_bus(.infix).sii**", "**traffic_storage_bus(.infix).sii**" or any other custom defined traffic vehicle type storage file.

> **Note:** Euro Truck Simulator 2 has extra: "**/def/vehicle/ai/truck/**" subfolder for grouping folders of traffic truck chassis definitions.

> **Note:** This folder doesn't include trailers definitions for traffic as it's a common practice that trailers for AI traffic are defined inside Trailer definitions.

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

##### Trailer definitions

Trailer definitions defines trailers for usage with players truck or for usage by AI traffic. For defining a trailer, one SII file and folder with "**chassis.sii**" and/or additional cargo definitions has to be created. All of the trailers definition files also have to be included in one of the storage files to be used in game. In case trailer should be used by player it has to be included in one of the "**trailer_storage(.infix).sii**" files and if trailer should be used by AI trucks it has to be included in one of "**traffic_storage_semi_trailer(.infix).sii**" files or custom type of AI trailers storage file.

> **Note:** AI trailers and player trailers are handled somewhat differently. Player trailers use the "**trailer**" SiiUnit class with a naming convention of `trailer.<name>`, while AI trailers use the "**traffic_trailer**" SiiUnit class and a naming convention of `traffic.trailer.<name>`.

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

##### Player trucks definitions

Player truck definitions are containing all definitions that defines trucks that player can use in game and accessories for them.

For more information see the dedicated page: [Player trucks definitions](Game%20data/Player%20trucks%20definitions.md).

#### World definitions

Defines all world items that can be placed on the map with Map Editor and their behaviour. All of the different item types have their own definition file where items of the same type are defined.

While defining new world items alternative infixed naming of SII file shall be used e.g. for defining new static models infixed file example would be: "**model.mymod.sii**".

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

### Fonts

Folder for storing game fonts. Mostly used in UI and inside vehicle dashboard displays.

```
Root Game Folder
├font
  ├license_plate             Fonts used by licence plates.
  └sign                      Fonts used by road signs.
```

### Predefined materials

Library of predefined materials and textures.

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

### Sounds

Library of sounds used by game.

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

### UI definitions

Library of all UI layouts and control definitions including vehicle dashboards.

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

### Vehicle model resources

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
