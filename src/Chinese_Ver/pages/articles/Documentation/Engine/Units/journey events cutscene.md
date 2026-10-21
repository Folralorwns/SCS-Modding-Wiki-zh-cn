# Documentation/Engine/Units/journey events cutscene

The **journey events cutscene** unit class is used to define cutscenes for [Random Road Events](../Random%20Road%20Events.md).

This unit gathers multiple cutscenes and binds them with the attributes of this unit. So cutscenes with same auxiliary data can be defined in one journey event cutscene unit, which enables usage of more graphical variants wrapped under one journey event cutscene.

## Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| cutscene_tokens | array&lt;token&gt; |  | Array of token names of all cutscenes that this unit should gather (token name is matching cutscenes defined in "**/def/camera/cutscene.sii**" by last token of unit names). |
| left_width | float | -1.0 | The width of left side of the cutscenes gathered by given token names. More info: [Documentation/Engine/Random_Road_Events#Cutscene_width](../Random%20Road%20Events.md#Cutscene_width). |
| right_width | float | -1.0 | The width of right side of the cutscenes gathered by given token names. More info: [Documentation/Engine/Random_Road_Events#Cutscene_width](../Random%20Road%20Events.md#Cutscene_width). |
| sequence_mode | int | simple | How will game choose cutscene token if this cutscene data gathers more than one cutscene. **simple** - Each cutscene in sequence (when more layer_cutscenes are placed after one another) is selected randomly and independently. **pseudo** - Each cutscene in sequence (when more layer_cutscenes are placed after one another) is selected in the way, that each N-tuple (where N is the number of cutscenes gathered by token names) contains all cutscenes in random order. **fixed** - One random cutscene is used for the whole sequence. |
| lane_height | float | -1.0 | Height of the cutscenes gathered by token names. Value >= 0.0 means that we could apply random offset in the perpendicular direction to lane direction (if there is enough space) |
| align_buildings | bool | false | Should buildings be aligned to the drivable curve? When true all building nodes are placed in the same distance from the curve as is the X-axis distance from the cutscene origin. |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/journey_events_cutscene | revision: 3880 | captured: 2026-10-21 23:56:14 -->
