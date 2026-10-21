# Documentation/Tools/SCS Workshop Uploader/Changelog

Changelog of the **SCS Workshop Uploader** tool.

## Intro

This page contains detailed changelogs of SCS Workshop Uploader tool. There are multiple possible versions:

- **Current Version** - uploader version that is compatible with the currently released version of the games. Available when you have no beta selected in steam.
- **Public Beta Version** - uploader version that is compatible with the game's version that is available in open or experimental beta. To access this version, you can find it in the public_beta branch on Steam. The way to access it is as follows: Steam client → LIBRARY → Tools section → right-click on SCS Workshop Uploader → Properties → Betas tab → public_beta. No password is required. The branch may not be available if no public beta is in progress.
- **Historical Versions** - uploader versions for various historical versions of the game. Version compatible with game version XY is available in 1xy_compatibility_branch beta.
- **Very old historical versions** - because of the limit on number of beta branches, versions targeting very old versions of the games were moved into legacy_compatibility_branch. In this case the branch contains multiple versions of the tool and the desired version must be selected in the launch options.

## 1.62

### Public Beta Version 1.62.0 (e3f33c1d8ed3) - 20.10.2026

- Initial support for 1.62

## 1.61

### Current Version 1.61.2 (c1a541806cc4) - 13.10.2026

- Support for car related tags for ATS.

### 1.61.0 (83a4ab1b9bd4) - 01.09.2026

- Initial support for 1.61

## 1.60

### 1.60.1 (8586ce5dcc67) - 04.06.2026

- Initialization fixes

### 1.60.0 (abb38d64ec99) - 02.06.2026

- Initial support for 1.60

## 1.59

### 1.59.0 (d391e4dd1bea) - 14.04.2026

- Initial support for 1.59

## 1.58

### 1.58.0 (20139f0733b8) - 27.01.2026

- Initial support for 1.58

## 1.57

### 1.57.1 (090c5fd1e04c) - 06.11.2025

- Initial support for 1.57

## 1.56

### 1.56.2 (ac508c163790) - 01.9.2025

- Support for cargo grab definitions

### 1.56.1 (419f7150602e) - 28.8.2025

- Support for 1.56

## 1.55

### 1.55.0 (9f8edb4308e8) - 17.6.2025

- Support for 1.55
- Switched to 64bit version.

## 1.54

### 1.54.3 (c86c11e01ffc) - 27.3.2025

- Updated to changes in 1.54 release

### 1.54.2 (d4608397e651) - 10.3.2025

- Updated to changes in open beta
- Support for **sliding_axle** and **sliding_axle_end** sounds for chassis accessory.

### 1.54.0 (cd8517773620) - 3.3.2025

- Initial support for 1.54 open beta.
- Changed the tool versioning to better align with the targeted version of the game. The first two components of the version should match the version of the game.

## 1.53

### 1.0.62 (cd53409d429f) - 25.11.2024

- Support for additional attributes

### 1.0.61 (10157d3b3da1) - 25.10.2024

- Initial support for 1.53

## 1.52

### 1.0.60 (5831e632ae08) - 16.10.2024

- Initial support for 1.52 (no academy support yet)

## 1.51

### 1.0.54 (e7b0ddda7785) - 20.9.2024

- Support for the **type** parameter of **dynamic_cargo_data** units.
- Support for the **procedural_animation_params** parameter in **mover_action** unit

### 1.0.52 (534f1153508e) - 29.8.2024

- Initial support for 1.51

## 1.0.51

### 1.0.51 (c9c43f89682f) - 25.5.2024

- Fixed checking of mod icon inside Hashfs v2 archives.

## 1.50

### 1.0.50 (9ce3a01a100a) - 22.5.2024

- Fixed compatibility with old material formats. Note that gaps in the texture indices are still not allowed.

### 1.0.49 (af61694b8c38) - 21.5.2024

- Re-enabled texture related checks

### 1.0.47 (aabb848ab8da) - 10.5.2024

- Updated to changes in 1.50. Some texture related checks are currently still inactive.

### 1.0.46 (f9653d7801b3) - 6.5.2024

- Initial support for 1.50. Some texture related checks are currently inactive.
- Support for using HashFS v2 archives using .scs extension.

## 1.49

### 1.0.42 (fa585abcd511) - 22.11.2023

- Supports new unit attributes for used vehicles and env profiles.

### 1.0.41 (66f9ea406b70) - 6.11.2023

- Initial support for 1.49 during open beta

## 1.48

### 1.0.40 (6faa1b89354e) - 23.6.2023

- Fixed crash when validating new format of material files.

### 1.0.39 (5435398fdad2) - 23.6.2023

- Fixed validation of addon hookups when using the DLC aware format.

### 1.0.38 (8a4828d3bdc0) - 23.6.2023

- DLCs listed as part of **dlc_dependencies** inside the version manifest are now considered as part of the base data when using the DLC aware format.

### 1.0.37 (11c8411444a2) - 23.6.2023

- Support for 1.48 open beta

## 1.47

### 1.0.36 (c90d9316d4dc) - 29.5.2023

- Support for **system_warning1**, **system_warning2** and **system_warning3** sound events

### 1.0.35 (0bf78930b473) - 15.3.2023

- 1.47 support

## 1.46

### 1.0.34 (5b43437971ad) - 8.11.2022

- Updated for compatibility with final 1.46

### 1.0.33 (38441c2862e0) - 12.10.2022

- Fixed crash if versions.sii started with informational version

### 1.0.32 (5b4fcc0b2516) - 27.6.2022

- 1.46 support

## 1.45

### 1.0.31 (bd13cf127747) - 27.6.2022

- 1.45 support

## 1.44

### 1.0.30 (ccbb66864ea3) - 10.5.2022

- Do not fail if condition_data.sii is not present in the game (ATS 1.44)

### 1.0.29 (836e413aac4e) - 25.4.2022

- 1.44 support

## 1.43

### 1.0.28 (b45779eeb809) - 9.12.2021

- Support for newly added unit attributes (e.g. city_icon_size, no_geometry_stretch, first_direction_focus_id)

### 1.0.27 (3ba2b42b5df4) - 12.11.2021

- 1.43 support

## 1.42

### 1.0.26 (2a736d7f7ec1) - 1.10.2021

- 1.42 support

## 1.41

### 1.0.25 (2fb534cc2738) - 2.09.2021

- Support for **accessory_addon_tank_data** accessory

### 1.0.24 (8a410f02f1f4) - 1.07.2021

- Support for "retarder_remote" sound in transmission accessory

### 1.0.23 (c2699032a20d) - 21.06.2021

- 1.41 support

## 1.40

### 1.0.22 (f6563bb6628c) - 12.04.2021

- Support for headlight lamp setup override

### 1.0.21 (f08dd65c9116) - 15.03.2021

- 1.40 support

## 1.39

### 1.0.20 (7871b0a1f072) - 8.12.2020

- added brand tag for Freightliner brand

### 1.0.20 (917bd8f7b2de) - 2.12.2020

- compatible_versions check relaxed to allow for specifying explicit non-zero third and fourth components

### 1.0.20 (91e0c6211ebf) - 20.10.2020

- Support for position_offset parameter in soundref files

### 1.0.19 (cc61be1d06b1) - 19.10.2020

- Fixed air_horn sound support

### 1.0.18 (50b6d3bf0478) - 19.10.2020

- Updated for 1.39 Open Beta

## 1.38

### 1.0.17 (a56d7d045cc8) - 1.10.2020

- Added Western Star to the Brand list

### 1.0.16 (15e1b3589de8) - 29.06.2020

- Fixed verification of traffic vehicles
- Fixed incorrect report of duplicate unit name for some unit types (e.g. cargoes)

### 1.0.15 (02685c693f52) - 19.06.2020

- Updated for ATS Open Beta 1.38

## 1.37

### 1.0.14 (8b094d6f3693) - 26.05.2020

- Allowed direct "bank#event" reference from units in addition to soundref file
- Improved validation of soundref files
- Removed warning for missing sound references for accessory attributes where default is provided (e.g. sound_horn)

### 1.0.13 (d9e3c1783307) - 28.04.2020

- Support for Mack brand tag for ATS

### 1.0.12 (0c9147422e49) - 27.04.2020

- Support for sound_retarder attribute of transmission accessory

### 1.0.11 (34d490f577a6) - 08.04.2020

- Updated for ETS2 Open Beta 1.37

### 1.0.10 (0c443be8cb93) - 12.03.2020

- Support for .soundref format validation

### 1.0.10 (22898975fb90) - 02.03.2020

- Support for ATS Open Beta 1.37
- Support for validating .mask format
- Support for validating FMOD sound banks format
- Small UI tweaks

## 1.0.9

### 1.0.9 (2aaea92d9825) - 12.12.2019

- Update to all changes introduced during open beta
- Added International brand tag to ATS

### 1.0.9 (5c58b47e85f9) - 21.10.2019

- Update to wander camera unit changes introduced during open beta

### 1.0.9 (cbd5aa3c8fef) - 17.10.2019

- 1.36 game version support

## 1.0.8

### 1.0.8 (ef80e2961800) - 11.06.2019

- Fixed validation of multiple packages. Previously if X file was in the first package, it was used for validation in all packages.

### 1.0.8 (3f3f9b51c140) - 06.06.2019

- Added "Changelog" button opening this page.
- Fixed language mod descriptions and titles are fetched in to set it to English. Previously steam client language was used. (If user had client set to Polish, Polish descriptions were fetched however upload override English descriptions)

### 1.0.8 (ad5d573c2a51) - 03.06.2019

- Fixed game selection droplist not being activated if user has only one game installed
- Added "Voice Navigation" mods category

### 1.0.8 (a54215a157e0) - 06.05.2019

- 1.35 game version support
- Unit files validation has been re-implemented, all parsing errors will now be properly reported as validation errors so you no longer have to look at tool.log.txt to understand what is wrong.
- Euro Truck Simulator 2 is no longer preselected when the tool is launched so when the user wants to upload ATS mod he no longer has to wait for ETS2 data to be loaded.
- Validation of packages was changed - from now on only universal and/or packages that are compatible with tool version are validated. Packages that are prepared for a newer version of the game than the version supported by the tool will cause a validation error.
- Correctly detect missing effect referenced by material.
- In case the installed game version is different than the tool version it is now properly shown to the user.
- Validation progress dialog has been slightly redesigned.
- Tool will now ask user for confirmation when closing tool, changing game or an item with unsaved changed to currently edited mod.
- Disable delete button during update.
- Fixed memory wasting caused by new item being created multiple times without a reason.
- Fixed UI bug causing wrong item to be selected after creating a new one.
- Fixed UI glitches when resizing window.
- Fixed missing icons on message boxes.
- Fixed bug that caused previously selected mod icon to be still displayed when selecting new or mod without icon.

## 1.32

### 1.0.7 (51ad53473468) - 05.09.2018

- Fixed validation of trailer configurations.
- Added missing message box icons.

### 1.0.7 (121b71f23ccd) - 04.09.2018

Experimental release for 1.32 compatibility. (public_beta branch)

- Added support for 1.32 version of the game.
- Game data is now being loaded after the main dialog of the tool is open with a proper progress bar displayed. Previously it was possible when the user had many DLCs it would take a significant amount of time to start a tool.
- The file discovering phase is now also updating UI so validation progress dialog is no longer stuck showing nothing.
- Fixed various crashes when validating units and data files.

## 1.31

### 1.0.6 (c1006f4d79a0) - 15.05.2018

Release for 1.31 compatibility.

### 1.0.6 (5aeec64b6ae6) - 19.12.2017

- Fixed crash when validating mod that contains multiple definitions of economy unit.
- Fixed crash when validating player unit. (initial save mods)
- Fixed validation of .sii files that are using UTF-8 with BOM encoding.

### 1.0.6 (4928518be2a5) - 19.12.2017

- Added validation of automat materials folder structure.
- Added support for legacy material hash names.
- Print full path to the resource relative to the mod root instead of package root for better understanding which file causes the problem in multi-package mods.

### 1.0.6 (850da2b2cfee) - 13.12.2017

- Added validation if automat material file content hash matches its name.
- Materials are now validated before any texture.
- Added name of the material referencing tobj to missing tobj error message if available.

### 1.0.6 (3b47a0690a7b) - 12.12.2017

- Fixed crash when validating UI windows.

### 1.0.6 (a1fcdaeeb768) - 04.12.2017

- Temporary workaround for traffic_trailer_type.sii related error in ATS vanilla data.

### 1.0.6 (8a923435d922) - 28.11.2017

- Support for .font files.
- More restrictive check of the data presence.
- New validation error code (10) which indicates I/O errors.
- Do not prepend path to the package in case there was some problem with the validation of the file that does not belong to the mod.
- Fixed loading of the game effects database. Previously the tool was not able to load any effect and as a result, there was a spam in the tool log file.

## 1.29

### 1.0.5 (070a99774791) - 10.11.2017

Compatibility update for ATS 1.29 release - available only in **123ats_compatibility** beta.

The access this build open Steam client then go to LIBRARY → Next to search bar select TOOLS → right-click on SCS Workshop Uploader → Properties → Betas tab → 129ats_compatibility. No password is required.

## 1.28

### 1.0.5 (2835351ba167) - 26.07.2017

Stable security release.

### 1.0.5 (79a99c4668c7) - 26.07.2017

public_beta branch release for open beta 1.28 compatibility.

## Very old versions

### 1.0.5 (b04d44242646) - 15.05.2017

The compatibility patch to ETS2 1.27.2.1 and ATS 1.6.1.9.

### 1.0.5 (859ab7102bb0) - 04.03.2017

The compatibility patch to ETS2 1.27 and ATS 1.6.

### 1.0.5 (c8931052fa92) - 13.01.2017

- Allow using materials from base without copying them to mod content.

### 1.0.5 (6a889ac42143) - 05.12.2016

The compatibility patch to ETS2 1.26 and ATS 1.5 available in **default** branch on steam.

### 1.0.5 (37800fdabf36) - 15.11.2016

The compatibility patch to ETS2 1.26 and ATS 1.5 - you can test it by selecting **public_beta** beta on the steam.

### 1.0.5 (ba8913a1daee) - 15.09.2016

- Fixed returning of the mods list. (If the creator has more than 50 mods all of them will be shown now)
- Fixed validation of traffic definitions.
- Slightly optimized validation of many SII files.

### 1.0.4 (9f8292f559f8) - 08.09.2016

- Updated tool to work with new units that appeared in ATS 1.4 and ETS2 1.25 updates.
- Fixed crash when validating mods that override cutscene data.

### 1.0.4 - 13.06.2016

- Fixed crash when validating any resource that depends on substances.
- Fixed validation of mods that override UI templates.
- Fixed abnormal CPU usage (+/- 13%) when the tool is idle.
- Fixed problem with unresponsive background window when closing foreground window.
- Added support for informational packages.
- Support for damage_data unit.

### 1.0.3 - 17.03.2016

- Fixed crash when validating mod that changes road look.
- Fixed crash when validating mod that changes initial profiles. (economy unit)

### 1.0.2 - 16.03.2016

- Fixed crash when validating mod that changes photo camera definition.
- Allow using glass.dat file, however, throw a warning about that it's not the best practice to use it.

### 1.0.1 - 15.03.2016

- Added version to the main window of the tool.
- Fixed modding of the files which reference prefabs, models, country and other data.
- Fixed validation of the mod when using ZIP packages.

### 1.0 - 14.03.2016

Initial release.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Workshop_Uploader/Changelog | revision: 5813 | captured: 2026-10-21 23:56:14 -->
