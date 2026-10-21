# Documentation/Tools/Map Editor/Batch Renaming

The editor now supports a batch renaming of some types of objects based on config file. First you need to prepare configuration file describing the changes which should be applied (see below). Afterwards you need to load the map in the editor, press **F3** to open the replacement dialog, press the **Batch replace** button and confirm the change. Afterwards you should save and reload the map.

The operation requires that units for both the old and the new names exist during the operation so you will need to do the operation in separate steps by first adding units under the new names to the definitions, then doing the rename and afterwards removing the units with the old names from the definitions.

The configuration file must be stored as **Documents\Euro Truck Simulator 2\replace.sii** or **Documents\American Truck Simulator\replace.sii**. The file must contain a single unit of type **editor_search_replace**. The unit contains string array attribute **sectors** which must contain names of all sectors in which to apply the changes. The sector name corresponds to base name of the files used to store that sector (e.g. sec+0001-0001). The unit also contains additional string array attributes which define the replacements. The format of the replacement string is "old_name|new_name". Following arrays are supported:

> **Note:** Please add any new arrays before approval, for instance I've seen *road_template* and *prefab_model* in replace files for ATS.

- **ter_material** - terrain materials
- **road_material** - road materials
- **sidewalk_material** - sidewalk materials
- **bld_scheme** - building schemes
- **model** - models
- **mover** - movers
- **walker** - walkers/pedestrians
- **vegetation** - vegetations
- **road_look** - road looks
- **ter_profile** - terrain profiles
- **railing** - railings on roads
- **sign** - lamps/bollards along the road

Example of replacement file:

```
SiiNunit
{
editor_search_replace : .edit_replace
{
# List of sectors where the search replace should be performed
# If you want to search everywhere in the map use the wildcard character "*"

sectors[]: "sec-0002-0007"
sectors[]: "sec-0002-0008"

# Terrain material replacement old terrain material unit suffix | new terrain material unit suffix

ter_material[]: "24|121"
ter_material[]: "103|129"

# Building scheme replacement old scheme unit suffix | new scheme unit suffix

bld_scheme[]: "22|2sc"

# Model replacement old model unit suffix | new model unit suffix

model[]: "122|1sc"
model[]: "757|2sc"
model[]: "56a|3sc"
}
}
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/Batch_Renaming | revision: 3380 | captured: 2026-10-21 23:56:14 -->
