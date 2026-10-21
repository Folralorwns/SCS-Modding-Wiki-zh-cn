# Documentation/Engine/Random Road Events

![Engine_random_event.jpg](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/400px-Engine_random_event.jpg)

*Random event preview*

![Engine_random_event_composition.jpg](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/400px-Engine_random_event_composition.jpg)

*Composition of the road event*

Road events (RE) are dynamically generated situations on roads present in ETS2 and ATS.

RE are defined from several cutscenes placed along the road. RE distinguishes 3 types of cutscenes:

- **Start cutscene** - The first cutscene of the RE, only one per the RE.
- **End cutscene** - The last cutscene of the RE, only one per the RE.
- **Layer cutscenes** - Cutscenes between Start and End cutscenes.

According to the length of the RE and the lengths of cutscenes, the space between start and end cutscenes is filled with layer cutscenes.

## Road events creation pipeline

For working road event we need:

1. Exported one or more cutscenes from map editor - #Cutscene export.
2. Defined cutscenes exported in step 1 - #Cutscene definition.
3. Defined journey cutscenes with last token of cutscene unit names defined in step 2 - #Defining journey cutscenes.
4. Finally defined road events inside with linked journey cutscenes from step 3 - #Defining random events.

### Cutscenes for random events

Basic element that is used on the RE is cutscene. Cutscene is exported map that can be dynamically inserted into the game.

#### Cutscene export

Cutscenes are exported from the editor as standard map SBD files. However for RE, each exported cutscene has to have **camera_point_item** with tag ***cutscene***. This point serves as cutscene origin (position and rotation) when placing cutscene on the RE.

Example RE cutscene with camera point item:

[![Cutscene for road event with camera point item](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/800px-Engine_random_event_cutscene_origin.jpg)](../../../files/Engine%20random%20event%20cutscene%20origin.jpg.md)

> **Note:** From example it is seen, that camera point is put on navigation line, which is on purpose, as RE cutscenes are placed along navigation lines. This way one can nicely setup cutscene on the road without guessing how it will be placed later on.

#### Cutscene definition

All of the cutscenes are defined in "**/def/camera/cutscene.sii**" and are used for different purposes.

For RE one has to define cutscene like this:

```
//                            ----- Cutscene token
//                           |
//                           v
cutscene_data: cutscene.acc_stop_lii
{
    objects_path: "/map/scenes/accident_stop_lights_in.sbd"
}
```

Where **objects_path** attribute points to exported cutscene and last token in unit name donates "cutscene token". Cutscene token (in example: "***acc_stop_lii***") is the name that is later used for gathering of cutscenes in journey event cutscenes trough **cutscene_tokens** attribute: [Documentation/Engine/Units/journey_events_cutscene](Units/journey%20events%20cutscene.md).

### Defining journey cutscenes

All cutscene attributes of RE: **start_cutscene**, **end_cutscene**, **layer_cutscenes**, **mirror_cutscenes**, **signs_cutscenes_inner** and **signs_cutscenes_outer** are using same unit type: [**journey_events_cutscene**](Units/journey%20events%20cutscene.md), which are listed/defined in "**/def/world/journey_cutscene.sii**".

These cutscenes are then linked to RE via their unit names.

Example **journey_cutscene.sii** file definition:

```
SiiNunit
{
# For modders: Please do not modify this file if you want to add a new entry. Create in
# this directory a new file "<base_name>.<idofyourmod>.sii" where <base_name> is name of
# base file without the extension (e.g. "city" for "/def/city.sii") and <idofyourmod> is
# some string which is unlikely to conflict with other mod.
#
# Warning: Even if the units are specified in more than one source file, they share the
# same namespace so suffixes or prefixes should be used to avoid conflicts.

journey_events_cutscene : j_cut.acc_stop_li
{
    cutscene_tokens[]:     acc_stop_li1   // Last token from unit names defined in "/def/camera/cutscene.sii"
    cutscene_tokens[]:     acc_stop_li2

    left_width:             80.0       // [m]
    right_width:            5.0        // [m]
    sequence_mode:          pseudo
}
journey_events_cutscene : j_cut.acc_mid
{
    cutscene_tokens[]:     acc_mid_1
    cutscene_tokens[]:     acc_mid_2
    cutscene_tokens[]:     acc_mid_3

    left_width:             15.0       // [m]
    right_width:            15.0       // [m]
    sequence_mode:          pseudo
}
journey_events_cutscene : j_cut.acc_plane
{
    cutscene_tokens[]:     acc_rare_1

    left_width:             35.0       // [m]
    right_width:            25.0       // [m]
    sequence_mode:          pseudo
}
}
```

#### Cutscene width

In case of RE, cutscene definition of type [journey_events_cutscene](Units/journey%20events%20cutscene.md) also uses **left_width** and **right_width** attributes, which defines the length of the cutscene. This two attributes are very important as they determinate how much space is between different cutscenes, how many layer cutscenes can be places in whole RE and where traffic blocks will be placed.

To determinate left and right width one has to:

1. Add cutscene on the part of the road.
2. Rotate the cutscene in map editor so that driving direction is from right to left:<br> ![Random event cutscene left and right width](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/Engine_random_event_cutscene_widths.jpg) *Random event cutscene left and right width*
3. Once seeing cutscene as on picture, use the ruler tool in map editor to measure distance from cutscene origin point on each side.
4. Use measured widths in journey event cutscene definition.

### Defining random events

All RE are stored in "**/def/world/journey_road_event.sii**" as list of [**journey_events_road_event**](Units/journey%20events%20road%20event.md) units.

Example **journey_road_event.sii** file definition:

```
SiiNunit
{
# For modders: Please do not modify this file if you want to add a new entry. Create in
# this directory a new file "<base_name>.<idofyourmod>.sii" where <base_name> is name of
# base file without the extension (e.g. "city" for "/def/city.sii") and <idofyourmod> is
# some string which is unlikely to conflict with other mod.
#
# Warning: Even if the units are specified in more than one source file, they share the
# same namespace so suffixes or prefixes should be used to avoid conflicts.

journey_events_road_event : j_re.acc_uni_p
{
    signs_distances_outer[]: 50

    layer_min_curve[]: 0.0
    layer_max_curve[]: 15.0

    max_length: 55.0
    min_length: 55.0
}
journey_events_road_event : j_re.acc_plane
{
    start_cutscene: j_cut.acc_stop_li    // From example above cutscene "j_cut.acc_stop_li" is featured as start cutscene here.
    layer_cutscenes[]: j_cut.acc_mid
    end_cutscene: j_cut.acc_plane

    min_shoulder_space: 3.0
    outer_lane_allowed: true
    centerline_displacement: true

    layer_max_curve[]: 2.0

    weight: 10.0

    parent: j_re.acc_spec_p

    name: "Accident country specific plane (1)"
}
}
```

#### Total length

The total length of RE is defined as:

```
total_length = (distance between start cutscene placement and end cutscene placement) + (start cutscene right width) + (end cutscene left width)
```

Depending on defined **max/min_length** there can be three situations by spawning of the RE:

- **max_length** not defined - Start and end cutscenes are placed in the way that **total_length** is the same as road length and the RE occupies.
- **max_length** < **total_length** - Start and end cutscenes placements are translated closer to each other so that computed **total_length** is equal to **max_length**.
- **min_length** is defined and **min_length** > **total_length** - RE will not be spawned.

> **Note:** In case of very short road segment it is possible that no layer cutscene will fit into the middle, so one can use **min_length** to prevent this.

> **Note:** In case that **traffic_block** is set to true then there must be **35m of uninterrupted** roads in front and the back of RE, otherwise event will not spawn.

#### Curvature

As roads are usually not straight it's essential that RE can be spawned on curved roads also. This is driven by **layer_min_curve** and **layer_max_curve** attributes which have to be defined for all layer cutscenes (number of elements in this arrays has to be the same). These numbers determine the minimal and maximal allowed curvature between each adjacent cutscene within one layer.

[![Engine_random_event_curvature.jpg](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/600px-Engine_random_event_curvature.jpg)](../../../files/Engine%20random%20event%20curvature.jpg.md)

Example above shows layer consisting of two barrier cutscenes and direction vector of their placements (blue arrows). Curvature is then computed as angle between these vectors, from which we can get minimal and maximal curve angle.

#### Signage

As RE can change flow of the traffic and even block lanes, we have to have support for warning signage which is placed before and after event. Warning signs are defined with:

- **signs_cutscenes_inner** and **signs_distances_inner** - defines signs and it's distances on most inner road lane.
- **signs_cutscenes_outer** and **signs_distances_outer** - defines signs and it's distances on most outer road lane.

In both cases sign cutscenes donates array of cutscenes for warning signage and distances provide their placement (this also means that array size of cutscenes and distances has to be the same).

Positive distances place sign cutscene before road event and negative distances place sign cutscene after road event (example below shows inner signs placed before event). Thus for RE to be spawned there has to be enough uninterrupted road before and after event (at least as much as provided maximal distance).

[![Engine_random_event_cutscene_signs.jpg](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/800px-Engine_random_event_cutscene_signs.jpg)](../../../files/Engine%20random%20event%20cutscene%20signs.jpg.md)

#### Synchronization

Choices which cutscene will be generated from the **start_cutscene**, **end_cutscene** and **layer_cutscene** are independent. But sometimes it could be useful to have some degree of dependency between them. Because of that the game can synchronize their selection. We can have 2 cases when the synchronization will happen:

1. RE has both **start_cutscene** and **end_cutscene**. If these cutscenes have the same number of **cutscene tokens** then the game will randomly choose index for both of them.
  - Moreover if the RE has **layer_cutscene** with the **fixed** sequence mode and the number of **cutscene tokens** is the same as the **start_cutscene** and **end_cutscene** tokens then, their chosen index will be used for the **layer_cutscene** as well.
2. RE has either **start_cutscene** or **end_cutscene**. If the RE has **layer_cutscene** with the **fixed** sequence mode and the number of **cutscene tokens** is the same as the **start_cutscene** resp. **end_cutscene** tokens then the index selected for the **start_cutscene** resp. **end_cutscene** will be used for the **layer_cutscene** as well.

[![Engine_random_event_sync1.png](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/1000px-Engine_random_event_sync1.png)](../../../files/Engine%20random%20event%20sync1.png.md)

[![Engine_random_event_sync2.png](../../../../../images/articles/Documentation/Engine/Random%20Road%20Events/1000px-Engine_random_event_sync2.png)](../../../files/Engine%20random%20event%20sync2.png.md)

Example of two RE variants with synchronized **start_cutscene**, **end_cutscene** and the first **layer_cutscene**.

## See also

- [Documentation/Engine/Units/journey_events_cutscene](Units/journey%20events%20cutscene.md)
- [Documentation/Engine/Units/journey_events_road_event](Units/journey%20events%20road%20event.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Random_Road_Events | revision: 3655 | captured: 2026-10-21 23:56:14 -->
