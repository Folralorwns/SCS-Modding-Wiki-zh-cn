# Documentation/Engine/Sound/Modding

### Modding Sound

FMOD requires each sound bank to have its own globally unique identifier (GUID). It also requires that the main mix buses of the master bank of each sound have the same GUIDs.<br> FMOD Studio does not provide a user interface to edit GUIDs, so to make it easier to create a correctly authored third party sounds, we are providing our Master Bank as a template for the new sound projects.<br> <br> All modded sounds must be a part of new FMOD bank to be usable for the game.<br> You need install FMOD Studio software to authoring new sound for the game.<br> Always use template (for the specific game version) of the sound bank to create your sound project.<br> Visit the [Downloads](Downloads.md) section to get template project or sound examples.

## Create own bank - Step by step

1. Download template.bank project.
2. Unzip project to the 'your new sound project' folder.
3. Rename "template.fspro" file (in project root folder) to "[my project name].fspro".<br>(*Not necessary but recommended.*)
4. Open your project (simply open [my project name].fspro file) in FMOD Studio software.
5. There are three browsers that can appear in an event editor window: the events browser, the banks browser, and the assets browser.<br>To create a new bank, right click in an empty space in the banks browser and select "New Bank".
6. Set the **name** of the new bank.<br>*The bank name determines the name of the bank file so it is strongly recommended to use system independent names (lowercase chars, no spaces,...).*
7. That is it!<br>New GUID is automatically created by FMOD for the new bank, so you have your own independent bank which can be used in the game for modded sounds.

*Notes:*<br> - *Always create new bank because creating new GUID for the bank is necessary!*<br> - *If you create new project from other templates (for ex. from your older project) also always create new bank. The GUIDs have to be unique!*<br> - *Never rename 'master' bank to other bank!*<br> - *Never delete the standard buses that come with the template project! If you delete them and create your own, they will not work even if the names are the same!*

## Create own sound - Step by step

It is very easy if you are familiar with FMOD Studio.

1. Open your project in FMOD Studio to edit it.<br>The events browser displays your project's events and event folders.
2. To create an event in this browser, right click on an empty space and select "New Event" from the context menu.<br>This opens a sub-menu, in which you have the option to make a 3D Event or a 2D Event (or a custom default event).
3. Select 2D or 3D option in dependency which sound you want to modding.
4. Set name for the new event. (*System independent names are strongly recommended.*)
5. Assign the event to your bank.<br>Right click on the "new event", select "Assign to Bank" menu and select target bank in submenu.
6. Assign the event to the audio bus.<br>Open window "Mixer Routing" and drag the "new event" to the target audio bus.
7. Edit your sound...

*Notes:*<br> - *Always create new events!*<br> - *If you create new project from other templates (for ex. from your older project) also always create new event with unique GUID!*<br> - *The 'copy-paste' process create new GUID for the event so it is recomended way to duplicate or move sound events.*<br> - *Take a care for abilities of sound - 2D/3D, loop, controlling parameters. Sound features are dependent on sound type you modding. Some abilities of the sound are necessary for the correct sound playing.*

## Prepare bank to the game - Step by step

When you finished work on new sounds you should prepare the sound bank to the game.

1. Build the bank.<br>Simply select menu File / Build... in the FMOD Studio.<br>The file "[bank name].bank" should be created in the "build" subfolder of your project.<br>*The "master.bank" and "master.strings.bank" files will probably also be created, but ignore them.*
2. Export GUIDs.<br>Select menu File / Export GUIDs... in the FMOD Studio.<br>The file "GUIDs.txt" should be created in the same subfolder.<br>(*You should see your new events in the object list in the GUIDs.txt file content.*)
3. Rename file "GUIDs.txt" to "[bank name].bank.guids".
4. You can optimize the contents of the guids file by leaving only those objects you created yourself and remain part of the new bank. But it is not absolutely necessary.
5. The both files ("[bank name].bank" and "[bank name].bank.guids") is the only one content you should use in your sound mod.
6. Edit the game's configuration files to include a link to your audio events.
7. Enjoy new sounds.

*Notes:*<br> - *Please, take a care what do you want to change in game and minimize overwriting files. You should provide space for the other modders.*<br> - *If you want to change all sound in the bank create new bank with the same name on overwrite it.*<br> - *If you want to change global or default sound create new bank with new event. Then overwrite only the .soundref file to redirect sound event to your new bank and event.*<br> - *If you want to change specific sound create new bank with new event. Then overwrite configuration file of the specified component or accessory to redirect sound to your event.*

## Fan-created video tutorials and info

Here you can see various approaches or variants of basic process as stored in first post of FMOD thread on our forum (rest of thread are learning and discussions from open beta period). It might be easier to understand for someone as it was created by people that did not knew the system at first - [https://forum.scssoft.com/viewtopic.php?f=178&t=281124](https://forum.scssoft.com/viewtopic.php?f=178&t=281124)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/Modding | revision: 5311 | captured: 2026-10-21 23:56:14 -->
