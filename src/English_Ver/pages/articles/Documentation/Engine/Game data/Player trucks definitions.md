# Documentation/Engine/Game data/Player trucks definitions

Player truck definitions can be thought of in two components:

- Vehicle parts definitions describe the characteristics of the truck and its many accessories.

: -Think of these as a set of building blocks from which the truck can be built; They don't assemble themselves!

- Vehicle configurations assemble the parts definitions into a vehicle that may be driven or purchased.

: -Think of them as the instructions for the game to assemble the building blocks (data definitions) into a vehicle when it is first loaded.

## Vehicle Parts Definitions

Each truck is configured in its own folder (e.g. "**<brand.truck>**" in tree view below) containing:

1. SII file: **data.sii** - *defining: truck info, cameras, fallback rules for parts of the truck and required accessories. There are 8 mandatory fallback rules: chassis, cabin, interior, engine, transmission, f_wheel (or f_tire), r_wheel (or r_tire), paint_job and head_light*.
2. Subfolders: (**chassis**, **cabin**, **interior**, **engine**, **transmission**, **paint_job**, **head_light**, **sound**) - *defining different parts and accessories of the truck. First 7 folders are needed because of mandatory fallback rules and sound folder is needed for truck mandatory sounds definitions.*
3. Optional folder: **accessory** - *defining all possible accessories for the truck that the user can install in the game Upgrade Shop. This folder holds another level of sub folders for separating different accessory types that the player can install on the truck and will be listed in the Upgrade Shop once the player selects the proper accessory type. Moreover names of subfolders directly correspond to the names of model locators that the truck 3D model has to have for the ability of having those types of accessories enabled in the game.*

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

## Vehicle Configurations

There are three types of player truck configurations, depending on their use in the game:

1. Dealers inside folder: "**/def/vehicle/truck_dealer/**" (if truck has RHD variant also in UK dealers folder: "**/def/vehicle/truck_dealer_uk/**").
2. Desktop preview inside folder: "**/def/vehicle/truck_desktop/**" (if truck has RHD variant also in UK dealers folder: "**/def/vehicle/truck_desktop_uk/**").
3. (Optional) Quick Jobs trucks inside folder: "**/def/vehicle/truck_company/**" (if truck has RHD variant also in UK dealers folder: "**/def/vehicle/truck_company_uk/**").

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
