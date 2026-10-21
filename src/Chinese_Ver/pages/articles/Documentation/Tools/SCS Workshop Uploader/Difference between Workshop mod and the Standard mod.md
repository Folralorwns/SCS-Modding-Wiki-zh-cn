# Documentation/Tools/SCS Workshop Uploader/Difference between Workshop mod and the Standard mod

### Differences between standalone and workshop mods

- Workshop mods have a specific layout. See details in the [Workshop mod Structure](Workshop%20mod%20structure.md) page.
  - A root directory containing the [versions.sii](versions.sii.md) file.
  - Subdirectories containing each version of the mod pointed by the [versions.sii](versions.sii.md) file, where the actual mod files reside.
  - New version subdirectories should be created when the mod becomes incompatible with changes introduced by new versions of the game, to keep backwards compatibility for people using old versions.

- The following configuration directives should be removed from the version subdirectories' [manifest.sii](../../Engine/Mod%20manager.md#Using_the_manifest) files:
  - **compatible_versions**: inherited from the [versions.sii](versions.sii.md) file
  - **display_name**: uses the name configured in the [SCS Workshop Uploader](../../Tools.md#SCS_Workshop_Uploader) tool

- Standard mods require taking care of their distribution, and users need to manually update them upon new releases.
- Steam Workshop mods are automatically updated to the subscriber when a new version is uploaded.
- Steam Workshop mods also are capable of selecting specific mod versions known to work in specific game versions, when available, allowing for automatic backwards compatibility.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Workshop_Uploader/Difference_between_Workshop_mod_and_the_Standard_mod | revision: 5750 | captured: 2026-10-21 23:56:14 -->
