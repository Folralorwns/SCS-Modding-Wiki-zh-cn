# Tutorials/SCS Workshop Uploader/How to upload new mod?

## Introduction

In this tutorial, we will show you how to prepare your mod for uploading it to the workshop step by step.

### Workshop mod files and directories layout

First of all - the layout of your mod will change a little bit. To check the Steam Workshop mods structure click [here](../../Documentation/Tools/SCS%20Workshop%20Uploader/Workshop%20mod%20structure.md).

### Preparing mod for uploading step by step

|  |  |  |
| --- | --- | --- |
| **1** | [![0002_create_folder.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0002_create_folder.jpg)](../../../files/0002%20create%20folder.jpg.md) | First step of preparing your mod is creating of the folder. You will put there all the files and folders needed for your mod to be compatible with Steam Workshop. |
| **2** | [![0003_create_latest_folder.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0003_create_latest_folder.jpg)](../../../files/0003%20create%20latest%20folder.jpg.md) | After creating of the folder open it and create another folder inside called **universal**. (Instead of folder you can also create ZIP archives with game data) |
| **3** | [![Universal_directory_content.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-Universal_directory_content.jpg)](../../../files/Universal%20directory%20content.jpg.md) | The universal directory (or archive) should contain all the standard mod package content so: manifest.sii file, description file, icon file and the mod content. **Note:** Remember! In Workshop mods manifest.sii, description and icon files are required! [Find more info here](../../Documentation/Engine/Mod%20manager.md) |
| **4** | [![0004_open_text_editor_and_create_versions_sii.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0004_open_text_editor_and_create_versions_sii.jpg)](../../../files/0004%20open%20text%20editor%20and%20create%20versions%20sii.jpg.md) | Open your favorite text editor and create file called versions.sii - save it in the same folder where you created **universal** folder |
| **5** | [![0005_fill_versions_sii_with_magic_and_global_sii_scope.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0005_fill_versions_sii_with_magic_and_global_sii_scope.jpg)](../../../files/0005%20fill%20versions%20sii%20with%20magic%20and%20global%20sii%20scope.jpg.md) | Add sii file frame to your versions.sii file. SiiNunit { } |
| **6** | [![0006_add_package_version_info_for_latest_version.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0006_add_package_version_info_for_latest_version.jpg)](../../../files/0006%20add%20package%20version%20info%20for%20latest%20version.jpg.md) | Add definition of universal version unit. SiiNunit { package_version_info : .universal { } } |
| **7** | [![0007_add_folder_attribute_to_latest_info.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0007_add_folder_attribute_to_latest_info.jpg)](../../../files/0007%20add%20folder%20attribute%20to%20latest%20info.jpg.md) | Set **package_name** to name of the folder or ZIP archive with the mod data. SiiNunit { package_version_info : .universal { package_name: "universal" } } |

When you do those points and put your game content to package you and you don't want to support exact game updates you can skip next points and go to Uploading part.

### Supporting specify version of the game

|  |  |  |
| --- | --- | --- |
| **1** | [![0008_create_folder_for_122_content.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0008_create_folder_for_122_content.jpg)](../../../files/0008%20create%20folder%20for%20122%20content.jpg.md) | In case you have data that supports one exact game version you need to create folder or archive where you will store the content. <br> **TIP:** For better organization of the directories. We recommend to call this folder *122_content* - 122 stands for 1.22. For example - for 1.23 update it will be 123, for 1.6 it will be 16, etc. |
| **2** | [![0009_add_new_unit_to_versions_sii_with_122_content_step_1.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0009_add_new_unit_to_versions_sii_with_122_content_step_1.jpg)](../../../files/0009%20add%20new%20unit%20to%20versions%20sii%20with%20122%20content%20step%201.jpg.md) | Open your text editor and do exactly the same steps as you did while adding a definition for the universal version of your mod (besides using a different folder and unit name this time). SiiNunit { package_version_info : .universal { package_name: "universal" } package_version_info : .122_content { package_name: "122_content" } } |
| **3** | [![0010_add_new_unit_to_versions_sii_with_122_content_step_2.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0010_add_new_unit_to_versions_sii_with_122_content_step_2.jpg)](../../../files/0010%20add%20new%20unit%20to%20versions%20sii%20with%20122%20content%20step%202.jpg.md) | Now there are some more steps you will need to go through: Set the value of the compatible_versions attribute. As we want to have data for 1.22 update write "1.22.*". Values are similar to compatible_versions array in manifest.sii. If you want to use this package for version 1.23 only you need to write: compatible_versions: "1.23.*" If you want to support only one version (not recommended) you will write: compatible_versions[]: "1.22.1" The value of this attribute can contain numbers, dots "." (between numbers) and asterisk "*" (at the end). If you only write "1.35.1" your mod will only be compatible with this specific version. The use of "1.35.*" will make your mod compatible with all small updates for version 1.35 (recommended). SiiNunit { package_version_info : .universal { package_name: "universal" } package_version_info : .122_content { package_name: "122_content" compatible_versions[]: "1.22.*" } } |
| **4** | [![0011_create_multiversion_folder.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0011_create_multiversion_folder.jpg)](../../../files/0011%20create%20multiversion%20folder.jpg.md) | In case you want to support more than one exact version you need to setup folder for it. <br> **TIP:** We recommend using similar syntax as for single version specify content, but for separating the versions use underscore "_". For example, if the content will be used by both 1.23 and 1.24 content package will be called: "123_124_content" in case you want the content package to be used for 1.24, 1.25.0 and 1.25.2 updates the content package will be called "124_1250_1252_content". |
| **5** | [![0012_add_another_unit_to_versions_sii.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0012_add_another_unit_to_versions_sii.jpg)](../../../files/0012%20add%20another%20unit%20to%20versions%20sii.jpg.md) | Add again the same definition for the unit. SiiNunit { package_version_info : .universal { package_name: "universal" } package_version_info : .122_content { package_name: "122_content" compatible_versions[]: "1.22.*" } package_version_info : .120_121_content { package_name: "120_121_content" } } |
| **6** | [![0013_add_first_version_attribute.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0013_add_first_version_attribute.jpg)](../../../files/0013%20add%20first%20version%20attribute.jpg.md) | Add compatible_version value for one update you support. SiiNunit { package_version_info : .universal { package_name: "universal" } package_version_info : .122_content { package_name: "122_content" compatible_versions[]: "1.22.*" } package_version_info : .120_121_content { package_name: "120_121_content" compatible_versions[]: "1.20.*" } } |
| **7** | [![0014_add_second_version_attribute.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0014_add_second_version_attribute.jpg)](../../../files/0014%20add%20second%20version%20attribute.jpg.md) | And add again compatible_version value for second update you want to support. SiiNunit { package_version_info : .universal { package_name: "universal" } package_version_info : .122_content { package_name: "122_content" compatible_versions[]: "1.22.*" } package_version_info : .120_121_content { package_name: "120_121_content" compatible_versions[]: "1.20.*" compatible_versions[]: "1.21.*" } } |

## Uploading

> **Useful link:** If you don't have SCS Workshop Uploader installed - check this tutorial - [How to download and install SCS Workshop Uploader?](How%20to%20download%20the%20tool_.md)

[![Scs_workshop_uploader_tutorial_preview.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/Scs_workshop_uploader_tutorial_preview.jpg)](../../../files/Scs%20workshop%20uploader%20tutorial%20preview.jpg.md)

- Run **SCS Workshop Uploader** tool from your steam client.

1. Select the **game** that is compatible with your mod.
2. Select **New** from the dropdown. It should be selected by default when you launch the tool.
3. In the **Mod data** section - browse for your **mod data folder**. This folder should include your packages and version.sii file.
4. If you select folder, browse for **mod preview image**.
5. In next step fill **mod name**.
6. Select **mod visibility** in steam workshop. If it's **Private**, **Friends only** or **Public**.
7. Fill your **mod description** which will be shown in your item workshop page. **(Minimum 50 characters)**
8. If you want to know formatting possibilities click on the question mark button.
9. Now, you have to select **type tag** for your mod.
10. You can select **truck parts** and **brand** tag if appropriate.
11. You can now fill **change note** of your mod. If you need to have the edit box bigger simply resize the tool window. As it's initial upload step you will more likely write nothing here - or write something like *"Initial upload."*.
12. If you did all the points simply click **Upload** button. Before the actual upload operation, the tool will check if your mod contains the correct data.

> **Note:** You may notice that when you are using non [ASCII characters](https://en.wikipedia.org/wiki/ASCII) the counters are decreasing by more than one. It is because those characters have a bigger size than one byte. The counters are counting bytes space used by description and title - not the character count

### Validation

- In case of any validation error you will notice this dialog.

[![0025_in_case_of_error_you_will_get_this_dialog.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/500px-0025_in_case_of_error_you_will_get_this_dialog.jpg)](../../../files/0025%20in%20case%20of%20error%20you%20will%20get%20this%20dialog.jpg.md)

When you click **OK** you will see log dialog with all errors and warnings that occurred during validation. In case if you have only warnings you can both continue or abort the operation. In case of errors, you will **need to** fix them before uploading.

> **Useful link:** If you need help with solving your validation errors click **[here](../../Documentation/Tools/SCS%20Workshop%20Uploader/Validation%20errors%20and%20solutions%20for%20them.md)**

[![Validation_result_window.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/Validation_result_window.jpg)](../../../files/Validation%20result%20window.jpg.md)

1. In this line you have the summary of the validation - the number of errors and warnings.
2. In this area you have log of the validation. All the log entires have the following form: ***[TYPE] [CODE] (file): Message***
3. Bellow you have two checkboxes, you can hide warnings or errors here.
4. In case there are is at least one error you are able to only click Abort. This button simply aborts the upload.
5. In case validation did not report any error you can click this button and continue uploading your mod. If there are errors you are unable to continue - you have to fix the problems.

### Success

If there are no errors the upload will continue and if everything goes right you will see this dialog.

[![0026_upload_success.jpg](../../../../../images/articles/Tutorials/SCS%20Workshop%20Uploader/How%20to%20upload%20new%20mod_/0026_upload_success.jpg)](../../../files/0026%20upload%20success.jpg.md)

However it is possible that there was some failure while uploading - you will then notice dialog with the error message. If you have some problem with resolving the problem write on **[our forum](http://forum.scssoft.com/viewforum.php?f=24)**

## Steam Workshop Terms Of Service

If it’s your first mod and you were not doing any mods for other game you will likely get an error about not accepted Steam Workshop Terms Of Service - if so happens the tool will show you appropriate message and the steam workshop terms of service will be opened in your default web browser - you have to login to your Steam account read and accept the terms of service and if you do so simply go back to the tool and try again with uploading your mod. It is **mandatory** to agree to these terms.

<!-- source: https://modding.scssoft.com/wiki/Tutorials/SCS_Workshop_Uploader/How_to_upload_new_mod%3F | revision: 4564 | captured: 2026-10-21 23:56:14 -->
