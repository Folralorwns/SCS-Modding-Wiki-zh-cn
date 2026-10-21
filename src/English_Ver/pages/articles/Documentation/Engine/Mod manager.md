# Documentation/Engine/Mod manager

With the new mod manager we introduce packages. Packages can be:

- zip archives - exactly the same which you used before with the .scs or .zip extension.
- normal directories - where each directory represents separate mod.

We recommend using normal directories for development of the mod and using zip archives for mod release, to make mod size smaller and more handy for end-user (one file vs. directory full of files). Inside the package you can define manifest file containing meta data about the mod. Metadata are used by mod manager to display your mod to the user. You can specify the description, the icon image and much more.

Since ETS2 & ATS version 1.48 you can use mods that contain subdirectories or files which are mounted only if DLC with the same name is owned. If mod root contains directory "base", zip archive "base.zip", directories or zip archives prefixed with "dlc_", game mounts only parts of the mod that correspond to owned DLCs. "base" part is mounted always (if it’s present). Mod manifest and other metadata are still contained in the mod root.

## Using the manifest

To set all metadata information you will need to create "manifest.sii" containing "mod_package" unit definition file in your mod package. Example "manifest.sii" file:

```
SiiNunit
{
# ".package_name" does not matter as the dot at the beginning of the file means
# that this unit is anonymous. Please keep this form to not make any conflicts
# with other mod packages (name collisions).
mod_package : .package_name
{
        # Package version can be any string with any length.
        package_version: "1.0 Release 3"

        # Display name can be any string with any length.
        display_name: "My mod"

        # Author can be any string with any length.
        author: "My Nick"

        # Categories is an array of strings.
        category[]: "ui"
        category[]: "truck"

        # Icon inside the root directory of the mod.
        icon: "mod_icon.jpg"

        # Description file inside the root directory of the mod.
        description_file: "mod_description.txt"

        # compatible_versions[]: "1.19.*" # Mod is compatible with 1.19.X..

        # dlc_dependencies[]: "dlc_north"
        # dlc_dependencies[]: "dlc_east"
}
}
```

**NOTE:** We do not limit attributes by length but some places where those meta data are displayed have limited space. To avoid problems we perform cutting of the values to fit the UI. Cutting will simply cut the string at some point and add ".." at the end of the string to mention that there is more content but it does not fit there.

- **package_version**
  - Type: string
  - The version of the mod package.
- **display_name**
  - Type: string
  - Display name of the mod. If none is specified name of the package without extension is used. **Note:** This string is not necessary when you want to create a steam workshop mod. You can specify the name of your mod at the uploading process in the SCS Workshop Uploader.
- **author**
  - Type: string
  - Author name.
- **category**
  - Type: array of strings
  - List of categories. Currently we limit categories up to 2 per mod. If you use more than two only first two will be used. If none is specified mod is assigned to "Others" category. You can use only categories from the set defined in Categories to use
- **icon**
  - Type: string
  - Name of file inside the root of the mod package directory which contains the icon image. Can be only .jpg file with exact size: 276x162px
- **description_file**
  - Type: string
  - Name of file inside the root of the mod package directory which contains the description text. Description file has to be a simple text file with .txt extension saved in UTF-8 encoding. Content of the description file is shown in mod details window and should include information about usage of your mod, additional credits of included mods etc. For possible text formatting see section Description of your mod > **TIP:** Since ETS 2 1.23 you can specify localized description files for more check: Localized description.
- **compatible_versions (Not applicable for Steam Workshop mods)**
  - Type: array of strings
  - List of compatible game versions. If the list is present and the game version does not match any version from that list, the user will be unable to use the mod and they will have to wait for the author to update it. Shall be used only for mods that are likely to get broken, like a map mod. <br>**Note:** If you want your mod to be compatible with all versions simply skip this parameter. Note also that formatting of the Steam version with "s" suffix (for example: 1.18.1s) does not exist in this versioning so please do not use it. <br>Each item from the list supports wildcards formatting shown below: <br><code>compatible_versions[]: "1.19.*"</code> This means that the mod is compatible with all "1.19.x" versions, e.g. all patches with number starting with 1.19 are compatible. Examples in the table show compatible game versions for the string "1.19.*": | **Version** | **Compatible?** | | --- | --- | | 1.18.1 | no | | 1.19.1 | yes | | 1.19.1.3 | yes | | 1.19.4 | yes | | 1.20.4 | no |You can also specify support for only one revision of the game which is not recommended as we do not change game a lot between minor patches.<br>For example: <br><code>compatible_versions[]: "1.19.1"</code>This usage is not a good idea as your mod will work only with the 1.19.1 version.<br>If we will release some hotfix, your mod will simply be incompatible with it.<br>You can also use more than one compatible version definition, like this: <br><code>compatible_versions[]: "1.19.*"<br>compatible_versions[]: "1.20.*"</code>This way you support both 1.19 and 1.20 patches.<br>**REMEMBER! If you specify a very restricted set of versions, users of your mod may wait for you to release a hot fix for the mod, even if your mod is 100% compatible with the latest release.**
  - Mod types and configurations for them:
    - Map mods <br><code>compatible_versions[]: "X.X.*"</code>Just check if major game version part matches. We might break map compatibility between major patches (1.17 > 1.18 for example) so you have to re-export your map mod from the map editor again. Between patches (like 1.18.1 > 1.18.2) there is a very small chance that we will introduce some critical change to map formats and thus break compatibility.
    - Tuning parts, trucks, model sets and any other <br>The best way is not to use this variable as there is a very small chance that your mod will be broken.
- **dlc_dependencies (Optional)**
  - Type: array of strings
  - From **ETS2 1.26** and **ATS 1.5** you are able to specify list of the DLCs which your mod requires to be installed in manifest file. This feature will block activation of the mod in mod manager when user has one of the required DLCs missing. To specify dependencies you need to edit your mod manifest.sii file and add the following:<br><code>dlc_dependencies[]: "package_name"</code>Where package_name is name of the DLC package - you can find package names in game directory for example if your mod requires DLC Scandinavia - package archive is called dlc_north.scs, the package name is the archive name without extension so in this case it will be dlc_north.
- **mp_mod_optional (Optional)**
  - Type: bool
  - Specifies whether players can join a multiplayer game with this mod installed, even if the server or other players do not have this mod. When set to true, the mod is considered optional for multiplayer compatibility. Such mod must not affect gameplay in a way that would require all participants to have it installed. Map mods will ignore this parameter.
  - The server must explicitly allow the use of optional mods. If not all mods are considered mandatory.
  - The client must explicitly allow servers with optional mods in session browser filter.

## Categories to use

There are 18 valid categories which may be used in the "category" array entries:

- truck
- trailer
- interior
- tuning_parts
- ai_traffic
- sound
- paint_job
- cargo_pack
- map
- ui
- weather_setup
- physics
- graphics
- models
- movers
- walkers
- prefabs
- other

## Description of your mod

Description text length is not limited. Moreover there is also additional ability to colorize your mod description with color tags.

List of available color tags:

| Tag | Result color |
| --- | --- |
| [red] | #FF2626 |
| [green] | #75FF00 |
| [blue] | #12ABE5 |
| [normal] | Default font color used in UI |
| [white] | #FFFFFF |
| [orange] | #FFAE00 |

**For example:**

```
[red]Hello [green]Wor[orange]ld
```

Will result in: **Hello World**

### Localized description

Also from **1.23** version you can localize your mod description. To use it you need to create description file separated for each language - the file name format is `description_file_name.[locale].txt` for example if description_file attribute is set to "description.txt":

- `description.en_gb.txt`
- `description.cz_cz.txt`
- `description.ru_ru.txt`
- `description.pl_pl.txt`

In case game is unable to find proper language file it will use description.txt file.

## Sample mod

You can download a sample mod with manifest [here](http://eurotrucksimulator2.com/modding/sample_mod.zip)

## Other problems not described here

If you have any problem with adjusting your mod to the new standards, feel free to write on our forum in the [mods forum section](http://forum.scssoft.com/viewforum.php?f=24).

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Mod_manager | revision: 5726 | captured: 2026-10-21 23:56:14 -->
