# Documentation/Tools/SCS Workshop Uploader/Validation errors and solutions for them

## 00001 - Generic

#### Description file has to be put inside the same directory as manifest.sii file.

The mod description file should be placed next to the manifest.sii file in the version package. You need to move it or create in case you have not done it yet.

#### Description file must be TXT file (?)

The mod description must be a .txt file. The solution for this problem is to change the extension of the file to .txt.

#### Icon file has to be put inside the same directory as manifest.sii file.

The mod icon file should be placed next to the manifest.sii file in the version package. You need to move it or create in case you have not done it yet.

#### Icon file must be JPG file (?)

Icon file must be a valid .jpg file. The solution is to resave your icon file to .jpg format.

#### Incorrect icon file dimmensions. Allowed dimmensions are ?x?px (the icon size: ?x?px)

Mod icon file has incorrect dimensions. To fix it you need to have image with proper size.

For now the limit is: **276px x 162px**

#### No animation frames found.

The .pma file has no animation frames. You should try to run your mod data resource conversion again.

#### No defined bones found.

.pma file without any bone defined is incorrect. You should try to run your mod data resource conversion again.

#### No description file specified!

All workshop mods data must have description files specified. Please add it.

#### No icon specified.

All workshop mods must have icon specified. Please add it.

#### No package versions defined.

In **versions.sii** there are no valid version info entries. Please add at least one.

Example versions.sii file:

```
SiiNunit
{
package_version_info : .universal
{
    package_name: "universal"
}
}
```

#### No vertices defined for piece ?.

One of the pieces in .pmg file has no vertices defined. Please run resource conversion of your mod data again.

#### Referenced look (?) does not exists in the model.

look referenced by definition file does not exists in the model. You should make sure that the model has the look - in case it has run again your mod data conversion.

#### Referenced variant (?) does not exists in the model.

variant referenced by definition file does not exists in the model. You should make sure that the model has the look - in case it has run again your mod data conversion.

#### Unable to load model animation file.

The load of the animation file failed. Try to run resource converstion for your mod again - in case it won't help check [tool.log.txt](tool.log.txt.md) file for more informations.

#### Unable to load model collision file.

The load of the collision file failed. Try to run resource converstion for your mod again - in case it won't help check [tool.log.txt](tool.log.txt.md) file for more informations.

#### Unable to load model descriptor file.

The load of the descriptor file failed. Try to run resource converstion for your mod again - in case it won't help check [tool.log.txt](tool.log.txt.md) file for more informations.

#### Unable to load model geometry file.

The load of the geometry file failed. Try to run resource converstion for your mod again - in case it won't help check [tool.log.txt](tool.log.txt.md) file for more informations.

#### Unable to load tobj file.

Failed to load .tobj file. Try running again mod data conversion - in case it did not check [tool.log.txt](tool.log.txt.md) if there are no informations about the tobj problem.

#### Unable to read units from file.

Unable to deserialize units from sii file. All the parsing errors are printed out to the [tool.log.txt](tool.log.txt.md) file. Check it for more info.

#### Unable to mount version.

Unable to mount mod data package. Try compresing mod data again as it may be broken.

#### Unable to open description file.

Failed to open mod description file. The reason may be invalid path it must be only the file name, also the problem may be not enough memory or some file system problem.

#### Unable to open file.

Failed to open a file. The reason may be invalid path, not enough memory or some problem with file system.

#### Unable to open icon file.

Failed to open mod icon file. The reason may be invalid path it must be only the file name, also the problem may be not enough memory or some file system problem.

#### Unable to read content of description file.

The reading of the file data failed. The reason may be not enough memory to load the data file.

#### Unable to retreive informations about material.

Unable to get informations about material resource. Try to run again mod data conversion.

## 00002 - File not found

#### Description file (?) does not exists.

Description file for your mod does not exists. Make sure if description file name in **manifest.sii** is correct and the description file exists in the same directory as **manifest.sii**.

#### File is not present

```
ERROR [00002] (file_name): File is not present
```

Make sure that the **file_name** exists.

#### Icon file (?) does not exists

Icon file for your mod does not exists. Make sure if icon file name in **manifest.sii** is correct and the icon file exists in the same directory as **manifest.sii**.

#### The version package does not exists!

Package specified in version info inside **versions.sii** file does not exists. Make sure you did not make any typo and the package really exists.

#### Unable to find descriptor file for model geometry! (geometry: ?)

There is .pmg file but no .pmd file. If you are using some model from base you have to move both pmg and pmd files into your mod for better compatibility. In case the model is yours you have to run again mod data conversion. Remember .pmd and .pmg files must be in the same directory!

#### Unable to find geometry file for model descriptor ?.

There is .pmd file but no .pmg file. If you are using some model from base you have to move both pmg and pmd files into your mod for better compatibility. In case the model is yours you have to run again mod data conversion. Remember .pmd and .pmg files must be in the same directory!

#### Unable to find manifest file.

Unable to find **manifest.sii** in one of the mod data packages.

#### Unable to find material file referenced by model descriptor ?. The material must be placed in mod folder.

Unable to find the material file which is referenced by model descriptor. In case you have a model and you are using some materials from the base.scs archive you **have to** copy them to your mod folder to keep compatibility in case we change the material.

#### Unable to find model descriptor file referenced in addon hookup data definition (?).

There is no .pmd file with this name in both base.scs or your mod data package - make sure the name is correct and the file exists.

#### Unable to find model geometry file for model descriptor (?) referenced by addon hookup data definition (?).

There is no .pmg file with this name in both base.scs or your mod data package - make sure the name is correct and the file exists.

#### Unable to find preview icon for ? defined in ?

Unable to find preview icon for the accessory. Make sure it exists.

#### Unable to get material

Unable to get material data. The material file is probably malformed. Try converting your mod data again.

## 00003 - Not allowed

#### Package name (?..) name is too long. Maximum length is ?.

Package name is too long. Maximum length of the name is: **256**.

#### Package name is not a valid string

The package name is not valid string. Make sure that you are using of correct characters.

#### File with the unsupported extension found in the mod. Please remove it before uploading the mod.

Steam Workshop Mods supports only specified set of file types. Having file of the type that is not supported is forbidden and you have to remove it.

For instance, map files (extensions **.aux**, **.base**, **.data**, **.desc** and **.layer**) are not supported, thus Steam Workshop mods cannot contain map modifications. Although the files are valid mod files, they are intentionally not accepted by the SCS Workshop Uploader.

#### Found second universal version entry. Please use only one.

Universal version entry is an version definition inside **versions.sii** file without any compatible versions defined.

For example:

```
package_version_info : .universal
{
    package_name: "universal"
    // No compatible_versions[]: X here!
}
```

In case there are more than one versions like that inside **versions.sii** file you will get this error. To fix this simply remove one of the definitions.

#### In the mod root folder there can be only versions.sii file and version packages. Found ? not allowed entries:

There must be only **versions.sii** file and version packages. Example workshop mod should be - for example:

```
my_mod\
    my_mod\versions.sii     <-- Definition file containing informations about versions and mod packages.
    my_mod\universal        <-- Universal mod package (can be zip or archive)
    my_mod\122_content.zip  <-- Mod package for the 1.22 update. (can be zip archive)
```

#### Mod package unit has to be placed inside the manifest.sii files put in version specific mod package. For example: "/latest/manifest.sii". (path: ?, manifest: ?)

The **mod_package** definition must be placed inside manifest.sii file.

Example mod layout:

```
my_mod/
    my_mod/versions.sii
    my_mod/universal
        my_mod/universal/manifest.sii        <-- mod_package can be defined here.
    my_mod/122_content.zip
        my_mod/122_content.zip/manifest.sii  <-- mod_package can be defined here.
```

#### Path cannot contain '..'. (position: ?)

Paths used in the mods cannot use two dots ("..").

**Invalid:** `../other_folder/file.txt`

**Correct:** `/other_folder/file.txt`

#### Path cannot contain Windows-style path separator (\\) only Unix-style separators are allowed (/). (position: ?)

All the paths used by mods must use unix-style separators.

**Invalid:** `\folder\folder2\file.txt`

**Correct:** `/folder/folder2/file.txt`

#### txt/.jpg files that are not referenced by any sii file are not allowed!

Any .txt or .jpg file that is not referenced by any definition file is not allowed. You have to remove it.

Also it is possible that you are referencing this file but you made a typo either in file name or in the definition that references it. Please check it.

#### Unable to find universal version defined.

There is no universal version defined inside **versions.sii** file. You have to add one.

Universal version is:

```
package_version_info : .universal  <-- .universal can be any text starting with . (up to 12 characters)
{
    package_name: "name"           <-- package_name is the folder or archive name where you store mod data.
}
```

#### Units of type ? are not allowed.

This unit is not allowed to be placed inside the file. Please remove it.

#### Units of type ? can be stored only inside the '?' file.

This unit definition can be only stored only inside the file written in the error message. Please remove it or move it.

#### Using SCS files is not allowed for Steam Workshop mods - please use normal .zip files or folders.

With Steam Workshop mods you are not able to use ZIP files renamed to .scs. Please use normal ZIP files with .zip extension or folders.

You can however use .scs files if they are in the HashFS v2 format.

#### Package name contains disallowed characters. Allowed [a-z0-9_].

Package name can only contains characters from range a to z, 0 to 9 and underscore characters _.

Example:

| Correct? | Folder/archive name |
| --- | --- |
| yes | universal |
| yes | 122_content |
| yes | 122_123_content |
| no | Universal |
| no | $FOLDERNAME$$ |

#### package_name attribute in version definition file must be set.

The package_name value must be set in all version definitions.

## 00004 - Malformed file

#### Unable to load data from model ? file. (file is probably malformed - please run resource conversion again)

Model file is malformed and the validator was unable to load data from it please run resource conversion again to fix this problem.

#### 1D, 2D, 3D and Rect tobj can have only one map set! (map index: ?)

The .tobj file is likely malformed. Run the conversion of your mod data again.

#### Count of the parts does not match descriptor file ?. (desc: ?, geom: ?)

There is some problem with the model you are using. Please try running conversion of mod data again.

#### Count of the parts does not match geometry file ?. (desc: ?, geom: ?)

There is some problem with the model you are using. Please try running conversion of mod data again.

#### Incorrect map at index ?

Incorrect map in .tobj file has been detected. Please try running conversion of mod data again

#### Incorrect map type. (?)

The .tobj file is likely malformed. Run the conversion of your mod data again.

#### Incorrect texture sampler_name: "?".

Material is corrupted. Please try running conversion of mod data again. In case it did not help please check all the paths in the material file.

#### Malformed DDS file!

The DDS file is malformed. Save it again using your graphic editor in case it's created by you - in case it's result of mod data conversion run it again.

#### Malformed description file. The description file should be encoded in UTF-8!

The description file is not encoded in UTF-8 and contain invalid characters. Please resave it using your text editor using UTF-8 encoding. (In case your text editor is not supporting UTF-8 we recommend using [Notepad++](https://notepad-plus-plus.org/))

#### Malformed OGG file. Please correct it before uploading the mod.

The audio OGG file is malformed. Please re-save it.

#### Malformed tobj file.

The .tobj file is malformed. Please run mod data conversion again.

#### Unable to load icon likely malformed file.

Unable to load data from the mod package icon. The file is likely broken please save it again using your image editor.

#### Unable to read magic SII mark from file.

The .sii file does not contain magic SII mark ("SiiNunit"). The correct .sii file is:

```
SiiNunit
{
// Content
}
```

## 00005 - Missing required attribute

#### At least interior_model or exterior_model must be set to valid model descriptor file.

Make sure all the at least exterior_model or interior_model is set in your accessory definition file.

## 00006 - Access denied

#### Unable to create validation log file.

The tool is unable to create validation.log.txt file. The file is probably opened by some application. Make sure you close all applications using the file and restart the tool.

## 00007 - Not supported

#### Cube texture maps must be pot textures. (texture_name: ?)

All the maps inside cube texture must have size that is power of two. Correct maps size.

#### Mipmapping is not supported for npot texture.

Mip maps are not supported in case you have non power of two textures. To use mip maps you must change size of your texture to be power of two (e.g. 64, 128, 256, 512, 1024 etc).

#### Unsupported tobj version. (version: ?)

This .tobj file version is not supported. Run conversion of your mod data again.

## 00008 - Unable to load

#### Unable to load file.

Unable to load the file. To solve this you should run mod data conversion again.

#### Unable to load model descriptor referenced by accessory addon data definition (?)

Make sure that the .pmd file exists. In case it exists run again mod data conversion.

## 00009 - File is too big

#### Maximum size of description file is ? MB

Mod description file is too big. Maximum size is: **1 MB**.

#### Maximum size of icon file is ? MB

The mod icon is too big. Maximum allowed size for is: **1 MB**

## 00010 - IO Error

This kind of error mostly happens when the application is not able to read/write information to the hard disk. Make sure you have enough space on your hard disk. If it happens during reading, it is possible that an anti-virus was blocking the file and application failed to read it - try disabling it for the time of application use.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Workshop_Uploader/Validation_errors_and_solutions_for_them | revision: 5757 | captured: 2026-10-21 23:56:14 -->
