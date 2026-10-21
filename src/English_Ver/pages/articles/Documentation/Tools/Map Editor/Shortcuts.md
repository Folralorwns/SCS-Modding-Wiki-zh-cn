# Documentation/Tools/Map Editor/Shortcuts

## Editor Shortcuts

Legend:

- **LMB** = Left Mouse Button
- **RMB** = Right Mouse Button
- **MMB** = Middle Mouse Button
- **MW** = Mouse Wheel

### Modes

There can be only one mode selected. A different mode can be selected by clicking a toolbar button or by pressing a key:

- **Esc** – *None* mode.
- **E** – *Create new item* mode.
- **P** – *Item properties* mode. Clicking on a node opens properties of the selected items.
- **N** – *Node properties* mode. Clicking on a node opens properties of the selected nodes.
- **D** – *Delete item* mode. Clicking on a node deletes the item.
- **M** – *Move item* mode.
- **H** – *Height* mode. Dragging with a node moves the selected items along the Y axis.
- **R** – *Rotation* mode.
- **S** – S*cale item* mode.
- **B** – *Brush* mode. Allows manipulation with stamps on items. Opens Stamp dialog and shows current stamps on hovered items.
- **I** – *Import map* mode. **LMB** click imports to the same place as clicked. **MMB** click imports to the same coordinates as exported.
- **Q** – *Quick Edit Mode* **TOGGLE**.
- **O**– *Traffic preview* mode.
- **V**– *Vertex tool* mode.
- **U** – *Scene preview* mode.

### Item Types

There can be only one item type selected. A different type can be selected in the toolbar combo or by pressing a key:

- **1** – Road
- **2** – Prefab
- **3** – Building
- **4** – Model
- **5** – Sign
- **6** – Bezier Patch
- **7** – Cut Plane
- **8** – Mover
- **9** – Terrain

### Selection

- **LMB** – Standard selection on click including deselection when click into void. Box selection when mouse dragged.
- **RMB** - Open the item properties.
- **Ctrl+RMB** - Open the node properties.
- **Ctrl+LMB** – Adds items into the selection.
- **Alt+LMB** – Removes items from selection.
- **.** – Grows selection by one step in both directions from the currently selected nodes. That means selecting nodes nearest to the ones already selected (direct neighbours).
- **Shift+. / Ctrl+A** – Grows selection as much as possible in both direction from the currently selected nodes. This is supported only for buildings and terrains.
- **Shift+LMB** – In None mode selects by geometry.
- **ALT + S** - set selected item's scale to default 1:1:1
- **ALT + O** - reset curve offsets *(atm only for curve items, but will work also for building items)*
- **CTRL+SHIFT+P** - search compatible prefabs - based on the selected nodes of roads and prefabs the Content Browser searches for Prefabs that are compatible with all of them

### Manipulation

- **Ctrl+C** – Copies the selected item to clipboard.
- **Ctrl+V** – Pastes the clipboard content at position of cursor click.
- **Ctrl+Z** – Undos last world map change, that means movement, rotation, adding, deleting etc. Changing values in properties dialog is not undoable!
- **Ctrl+Y** – Redos change.
- **Up, Down, Left, Right** – Moves the selected items in X, Z axis.
- **Delete** – Deletes the selected items.
- **Ctrl+G** – Groups the selected items into a coumpound item for optimization purposes. Works for up to 16 models/buildings.
- **MMB** – Inserts a new node in the middle of the segment when performed over a road, building or mover node.
- **Ctrl+MMB** – Decimates a node when performed over a building or mover node. That means the following two buildings are automatically merged into one piece.
- **F6** – Drops the selected items to the ground. With **Alt** it also aligns rotation.
- **Alt+R** – Opens Random rotation/scale dialog.
- **Insert** – In free camera rotates the selected items in Z-axis (with **Shift** in opposite direction).
- **Delete** – In free camera rotates the selected items in Y-axis rotation.
- **End** – In free camera rotates the selected items in X-axis rotation.
- **Page Up/Down** – In free camera moves the selected items up or down in Y axis.
- **Alt+X** – Toggles *Free rotation* flag.
- **Home** – Rotates the selected items 90 degrees clockwise.

### Camera

- **C** – Toggles between the top down and free move cameras.
- **F** – Focus camera on selection.

###### Top camera

- **RMB** – Moves the camera in X, Z axis.
- **Page Up/Down, MW** – In top camera moves the camera up/down.

###### Free camera

- **RMB** – Rotates the camera.
- **MMB** – Moves the camera on view plane.
- **Space** – Cycles between editation and non-editation modes.
- **W,S,A,D** – Moves the camera forward, backward, left or right. The speed can be doubled by holding **Shift** .
- **Q,E** – Moves the camera in top or down.
- **Space** – Toggles editation mode. In editation mode the nodes are visible.
- **MW** – In editation mode moves the camera forward or backward. In non-editation mode changes the speed of camera movement.
- **Ctrl+NumPlus** – Decreases the camera's FOV (field of view).
- **Ctrl+NumMinus** – Increases the camera's FOV.
- **Ctrl+NumAsterisk** – Resets the camera's FOV.

### Isolated Selection

- **Ctrl+I**- Isolate selection
- **Alt+I** - Hide selection
- **Ctrl+Shift+I** - Exit isolation

### Locked Selection

- **Cltr+L** – Lock Vertex/Node Selection
- **Ctrl+Alt+L** – Reset Vertex/Node Lock

### Move Mode

LMB dragging with a node moves with the selected items. Whole multiselection is moved when dragged with one node (must be from the multiselection).

- **Tab** – Changes gizmo orientation.
- **Shift+Tab** – Changes gizmo orientation (backward direction).
- **X** – During move locks to X axis.
- **Y** – During move locks to Y axis.
- **Z** – During move locks to Z axis.
- **Shift+X** – During move locks to YZ plane.
- **Shift+Y** – During move locks to XZ plane.
- **Shift+Z** – During move locks to XY plane.
- **Shift+LMB** – During move disconnects the dragged node from the chain. Useful for roads, buildings and prefabs.
- **Alt** – During move snaps also Y axis (height). The standard snap leaves Y be.
- **Ctrl+Shift** – Before pressing LMB duplicates and moves current selection.
- **X** – Toggle between circle/curve mode.

If you are locked to single axis, you can use numpad to control movement or rotation.

- **Numpad number keys** - Enter value.
- **Numpad plus/minus** - Make value positive/negative.
- **Backspace** - Delete last digit.
- **Delete** - Throw away the value and get back to control move or rotation with mouse.

Vertex move:

- **Ctrl+Q** – Average selection.
- **Shift+Q** – Explode selection.
- **Ctrl+W** – Bridge selection.
- **Shift+W** – Weld selection.

### Rotation Mode

LMB dragging rotates the selected node in the selected axis. This does not work for multiselection.

###### Single selection

- **R** – Cycles between the axes X, Y, Z and LMB dragging with .

###### Multiselection

- **R** – Rotates the selected items clockwise by 90 degrees around their center in Y axis. With **Shift** it rotates only by 1 degree. With **Ctrl** it rotates counter-clockwise.

###### Free Node Rotation

Works for buildings, walkers and roads. In their node properties there is Free Rotation checkbox. With this turned on the node direction is not updated during internal computations but stays as it was set up by user. It could be useful when you want to set a specific rotation for road or building nodes to tweak the geometry shape.

### Brush Mode

- **Ctrl+LMB** – Removes a stamp.
- **Shift+LMB** – Picks a stamp settings (shows it in the stamp dialog).
- **Alt+LMB** – Draw color only.

### Vertex Move Mode

- **V** = vertex move tool
- **Ctrl+H** = sculptor LMB = up
- **Ctrl+LMB** = down
- **Shift+LMB** = revert to previous position
- **Alt+LMB** = smooth

*Just a warning - sculpting with CTRL + H can't be undone via CTRL + Z!*

### New item Mode

- **LMB** – Creates a new item of the selected type. Some items like roads or buildings need several clicks to define their shape.
- **Num+/-** – Selects previous or next preview (during the prefab of model item creation).

### Place Start Mode

- **LMB** – Put placement of the start truck position on the world map.
- **Num+/-** – Rotate start placement orientation.

### Terrain Picker Mode

This mode allows picking "terrain patterns" from roads, terrains and prefabs and reapplying them to other items (it is similar to Format Painter known in office software). The tool does live preview of terrain properties change when hovering over an item.

- **LMB** – Apply last picked terrain pattern to a hovered item.
- **Ctrl+LMB** – Pick terrain pattern of a hovered item.

### Traffic Mode

This mode provides debug information related to the in game traffic.

- **Num-** – Change mode of the tool.
- **Num*/** – Change vehicle type in the accessibility tool mode.
- **Ctrl+MW** – Change speed in the speed limits tool mode.
- **Home** – Remove all vehicles.

### Trajectory Item

Trajectory item shortcuts.

- **MMB** – Add a new node before of the clicked node.
- **MMB + Ctrl** – Remove the node before the clicked node.
- **MMB + Shift** – Split the item into the two by the clicked node.
- **MMB + Shift + Alt** – Split the item into the separate nodes.

Useful shortcuts when working with trajectory items.

- **F6** – Drop to ground.
- **Alt + F6** – Drop to ground with rotation.
- **Ctrl + Alt** – Node snap with rotation.

### Bug reporting

- **F11** – Goes to the next bug.
- **Shift+F11** – Go to the previous bug.
- **Alt+F11** – Reports a bug (shows Report bug dialog).
- **Shift+Alt+F11** – Reports a bug with a screenshot (shows Report bug dialog).

### ﻿View

- **Alt+W** – Toggle visibility of wireframe.
- **Alt+C** – Toggle visibility of collision boxes.

### Find References

- **Ctrl+C** – Copy selected rows into clipboard in CSV format.
- **F5** – Refresh the results.

### Misc

- **A** – Toggles backgound map. The background texture is located here: /material/editor/bcgmap.png. The size of the background map is hardcoded in the editor code.
- **G** – Toggles snap to ground mode.
- **Ctrl+F** – Opens find dialog. Finds item and node by their index and City and Road by their names.
- **F1** – Opens Help dialog with the list of shortcuts.
- **F2** – Opens Content browser.
- **F3** – Opens attribute replacement dialog.
- **F5** – Toggles minimap.
- **F7** – Toggles mirrors.
- **F8** – Opens UI map.
- **F9** – Opens weather dialog.
- **Ctrl+MW** – Changes grid step (1 cm, 10 cm etc).
- **Ctrl+E** – Exports the selected items to a file. Supports internal .sbd format, that can be imported by Import tool and .obj format, that can be imported in Maya or Blender.
- **Ctrl+S** – Saves the current map.
- **Ctrl+Shift+S** – Opens Saves As dialog that allows saving map to a different location.
- **Ctrl+O** – Opens dialog where another map can be selected and loaded.
- **Ctrl+N** – Opens a new empty map.
- **Ctrl+Tab** – Toggle drop free camera modes.
- **Ctrl+Tab (in Prefab Item Properties)** - skip between same property fields of each node
- **Ctrl+T** - Open traffic tool
- **Alt+V** - toggle instanced geometry on and off---

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/Shortcuts | revision: 5709 | captured: 2026-10-21 23:56:14 -->
