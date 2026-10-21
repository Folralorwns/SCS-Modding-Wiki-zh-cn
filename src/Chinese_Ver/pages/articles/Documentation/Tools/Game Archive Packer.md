# Documentation/Tools/Game Archive Packer

The ETS2/ATS update 1.50 introduces a v2 version of HashFS format. This format allows for more efficient loading of game data by storing resource metadata in memory. While all previous formats are still supported for mods, they might cause stalls for some resource types as the engine assumes that the metadata are available immediately. This tool provides support for creating and extracting .scs pack files. The creation supports v2 only, extraction supports both v1 and v2. The previous extraction-only variant with simplified interface is still [available](Game%20Archive%20Extractor.md).

The format handles textures as a single object. When tobj is encountered during packing step, it will read all referenced dds files and store result as a single combined object. Unreferenced dds files are ignored. This means that when modding a texture, you need to include both tobj and all referenced dds files.

## Archive extraction

To extract the content into the current directory use:

```
scs_packer extract archive.scs
```

To extract the content into a specific directory use:

```
scs_packer extract archive.scs -root <directory>
```

## Archive creation

To create archive from content of specified directory use:

```
scs_packer create archive.scs -root <directory>
```

The tool will automatically compress all compatible files. For development purposes it might be useful to disable the compression by specifying -nocompress parameter to speed up the entire process.

## Download

In general a newer version of tool can extract archives created for older version of the game. Game should be able to utilize archives created for older version however loading such files might be slower or it might cause stalls.

- **[LINK (1.50-1.54)](https://download.eurotrucksimulator2.com/scs_packer_1_50.zip)**
- **[LINK (1.55+)](https://download.eurotrucksimulator2.com/scs_packer_1_55.zip)** - 64bit binary. Updated 12.9.2025 to fix threading issue which could create malformed pack or crash.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Game_Archive_Packer | revision: 5720 | captured: 2026-10-21 23:56:14 -->
