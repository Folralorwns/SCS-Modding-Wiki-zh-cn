# Documentation/Tools/SCS Workshop Uploader/Workshop mod structure

The standard mod is a single **package** with manifest.sii file inside, description and icon files and the mod data files. The Workshop mod can and should consist of many **packages** - this option allows you to provide multiple versions of your mod for users on different game versions using one Workshop mod. In the **[versions.sii](versions.sii.md)** file you specify which **package** should be used when using the specified game update. But remember - this layout is only correct for Workshop mods. Standard mods are still using the one package approach.

[![Mod_layout_explanation.jpg](../../../../../../images/articles/Documentation/Tools/SCS%20Workshop%20Uploader/Workshop%20mod%20structure/Mod_layout_explanation.jpg)](../../../../files/Mod%20layout%20explanation.jpg.md)

Each of these packages contains directly mod metadata (manifest.sii, description, icon) and mod data files.

[![Package_with_mod_metadata_and_mod_data_files.jpg](../../../../../../images/articles/Documentation/Tools/SCS%20Workshop%20Uploader/Workshop%20mod%20structure/Package_with_mod_metadata_and_mod_data_files.jpg)](../../../../files/Package%20with%20mod%20metadata%20and%20mod%20data%20files.jpg.md)

Since SCS Workshop Uploader version 1.0.38, package might contain subdirectories or files which are mounted only if DLC with the same name is owned. If mod root contains directory "base", zip archive "base.zip", directories or zip archives prefixed with "dlc_", game mounts only parts of the mod that correspond to owned DLCs. "base" part is mounted always (if it’s present). Mod manifest and other metadata are still contained in the package.

[![Package_with_zip_files.jpg](../../../../../../images/articles/Documentation/Tools/SCS%20Workshop%20Uploader/Workshop%20mod%20structure/Package_with_zip_files.jpg)](../../../../files/Package%20with%20zip%20files.jpg.md)

[![Package_with_subdirectories.jpg](../../../../../../images/articles/Documentation/Tools/SCS%20Workshop%20Uploader/Workshop%20mod%20structure/Package_with_subdirectories.jpg)](../../../../files/Package%20with%20subdirectories.jpg.md)

When using new style packages, each directory or zip archive is validated separately and only game base data and DLC with the same name is mounted to perform the validation. If you need to mount other DLCs, list them in manifest's **dlc_dependencies** array.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Workshop_Uploader/Workshop_mod_structure | revision: 5288 | captured: 2026-10-21 23:56:14 -->
