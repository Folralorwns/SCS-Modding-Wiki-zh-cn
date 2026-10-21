# Documentation/Tools/Map Editor/New Editor Features 1.49

## Top Menu changes

The top menu **File - Edit - View - Map - Tools - Debug - Help** had changes in the content of each section and also the names of some sections.

The new setup is:

- **File** - stay the same
- **Edit** - represents the Edit functions and expanded with the various Edit modes, the isolation functions moved to next section
- **Selection** - represents the actions you can do with a selection in map

> **Note:** With the exception of Cut/Copy/Paste - those stay in Edit due to inter-software habits

- **View** - represents visualization options and dialogues that are supposed to show you some information

> **Note:** The View Distance Debug Tool was renamed to View Distance Display Range as it more precisely describes the function of this dialogue

- **Map** - represents the interactions you can do with the whole map file
- **Debug** - all debug views, validation and the traffic tool
- **Editor** - remaining software documentation and help, as well as the Editor/Map Settings

## Compound update

- **RMB click** on item in compound now opens the Properties of the Compound - you don't need to search for the Compound node
- **CTRL+RMB click** on item in compound now opens the Properties of that item - without need for you to break the Compound to access it

## Find Reference search in Find dialogue

You now can select option to search for Specific item by

- item index
- node index
- UID

If you do this instead of camera teleporting to the said item *(risking crash if there is a problem with the item)* the Found dialogue window opens and you can use it to remotely

- open the item's properties
- delete the item

> **Note:** *(previously you could only use "go to" function of the Find dialogue and/or console or delete such item using the console)*

## Changes in Errors&Warnings

- The small error popup informing you of too small item no longer appears!
- Instead ALL ERRORS now appear in the Found window where you can directly interact with the relevant items
- ADDITIONALLY you now can use **Debug -> Validate errors** button to display the error list whenever you need, not only on map save!

You can now delete items in Validate errors dialog using g_delete_by_uid via right-click menu on item.

- This only works if the selected items are both unlocked and invalid. :exclamation:
- This process is irreversible.

## Far Model Item & Visibility Area - interaction tools

A button for fmi&va **Find Parents** function added:

- **Selection -> Find Parents**

### Usage

- Select item (or items)
- Selection -> Find Parents

### Result

Found items dialogue containing list of Far Models Items / Visibility Areas the selected item(s) is assigned to.

*You can use this to check whether item you want to interact with (fe. add to compound) is a child of some FMI or VA or whether you can afford to break a compound (you should not if it is a part of FMI or VA)*

## Other changes and new features:

- When dropping items to the ground by F6 key you now can use the CTRL+F6 key combination to drop any item node to other item's geometry. *This should make placing lamps and other models on sidewalks much easier.*
- F8 map window now no longer switches to focus if you move your mouse cursor over it.
- Brush Tool material list now displays the "editor name" of the material

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/New_Editor_Features_1.49 | revision: 5339 | captured: 2026-10-21 23:56:14 -->
