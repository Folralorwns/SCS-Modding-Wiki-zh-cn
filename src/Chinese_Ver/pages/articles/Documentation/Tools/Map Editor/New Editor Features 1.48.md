# Documentation/Tools/Map Editor/New Editor Features 1.48

## Rotate the New Item before placing

When placing a new item you can now hold down the left mouse button and pre-rotate the item (in the Y axis) before placing it.

- the pre-rotation is started with LMB down and item is placed with LMB up
- works on new Model Items, Signs and Prefabs
- the rotation is kept - it does not reset with each new item
- there is a 200ms safety window where you can rotate the item but when placed it will be in the original rotation *(to prevent items from slightly rotating on LMB click)*
- if you hold SHIFT during this process the item will not be placed but the rotation will be kept

While NOT USING this function you can hover over a node of an item in the map and press:

- CTRL+ALT to assign that item's rotation (all axes) to the new item you are placing
- CTRL to assign that item's Y rotation to the new item you are placing *(this function was also added to the move function for already placed item!)*

Additionally these shortcuts can be used before placing the new item:

- CTRL+SHIFT+mouse_move to reset the new item's rotation to the default
- useful when the X and Z axes of the prerotated item are not 0 at the given moment
- HOME button can also be used to pre-rotate the new item in 90° steps from the current rotation the same way it is used on existing objects in the map

## Far Model Item and Visibility Area

**Visualisation Tweaks** <br> Far Model Item:

- the Far Model Area rectangle now has a distinctive pink color to be better visible in the map
- the lines leading from the Far Model Item to it's child items are now slightly different color from the area rectangle and are now visible only when the Far Area is selected

Visibility Area:

- the rectangle color has been changed to orange
- the central cross had been removed to reduce the visual clutter

*(the VA Properties can be accessed from the rectangle corner control nodes now so it is no longer necessary to search exclusively for the main node)*

- the lines leading from the VA to it's child items now have a color signifying the VA function
- for "show objects" and "show hidden objects" function the lines that appear when you select the area are GREEN
- for "hide objects" function the lines that appear when you select the area are RED

**Systems**

- VA and FMI child item lists now contain a [View Distance], [Distance to Center] and [Distance to Area] columns
- Both VA and FMI now contain the Child Item counter in the top panel of the Properties

## Hookup Item updates

**Compounding**

- Hookup Items now can be compounded using CTRL+G
- you can only compound hookup items with other hookup items
- you can compound max 16 hookup items in one group
- while in compound the number of unique vehicles spawned is limited depending on the model quality of the hookup items inside the group (default quality 6 unique models, average 4, low 2 and very low 1)

**Parked Car pools**

- Instead of 3 categories (common, vintage, luxury) there are now 5 categories you can use depending on the location context - common, cheap, expensive, cheap uncommon and expensive uncommon

## Gate Item

- as the name implies this item is for placing functional gates into the map
- when you place the Gate Item model into the map it contains only one node
- if you open the Gate Item Properties you can select

1. the gate model
2. option to display it as always open or always closed *(only available when the item does not have a selected trigger!)*
3. up to two triggers that make the Gate Item functional

- when a trigger is selected in the list, an additional node with a trigger area appears in the map and you can move/rotate them into the position you need
- trigger areas for this item are rectangular and the size of an average road lane so they can be more easily placed

Trigger Types:

- AI only = works only for AI, the players cannot operate those gates and they don't open for them

1. Automatic = the gate opens automatically on the AI car approach and every following AI vehicle can drive through as long as the gate is open
2. Manual = each AI vehicle has to stop at the trigger location and open the gate, it closes behind them

- Player & AI = both for the AI vehicles and the players can operate these gates

1. Automatic
2. Manual (Border) = for border gates use, displays a visible trigger with border specific symbol
3. Manual (Generic) = for depot use, uses a visible trigger with a generic gate symbol

- Player Only = only the players can operate this gate (for situations where the trigger is not placed on the AI line)

*Beware - AI completely ignores such a gate and drives through it. It should not be placed on places with active AI traffic.*

1. Automatic
2. Manual (Border)
3. Manual (Generic)

## Item Visibility - performance counter icon

Instead of displaying all the Performance counters at the some time you can now pick and select to display each of them separately

- Triangle counter
- Draw Calls counter
- Draw Calls (*no shadows) counter
- Clusters counter

## Report Bug dialogue update

When you use ALT+F11 to report bug or copy coordinates you can

- press button to copy the whole preview line
- press button to copy just the coordinates
- check With Screenshot to attach a screenshot of the current view to the bug
- check Add goto to automatically add text "goto" at the beginning of the copied coordinates text

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/New_Editor_Features_1.48 | revision: 5307 | captured: 2026-10-21 23:56:14 -->
