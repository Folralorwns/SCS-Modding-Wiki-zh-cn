# Documentation/Engine/Units/journey events road event

The **journey_events_road_event** unit class is used to define [Random Road Events](../Random%20Road%20Events.md).

All cutscenes attributes (**start_cutscene**, **end_cutscene**, **layer_cutscenes**, **mirror_cutscenes**, **signs_cutscenes_inner** and **signs_cutscenes_outer** ) use link pointers of: [**journey_events_cutscene**](journey%20events%20cutscene.md) for linking cutscene data to each random event.

### Attributes

| Name | [Type](../Units.md#Attribute_types) | Default Value | Description |
| --- | --- | --- | --- |
| name | string |  | Name of the road event (description). |
| set_idx | unsigned |  | Index which determines used set of 'master' attributes, like 'minimal spawn distance' or 'probability' (see /def/world/journey_road_event_master.sii). |
| start_cutscene | link_ptr | NULL | Start cutscene of the road event. |
| end_cutscene | link_ptr | NULL | End cutscene of the road event. |
| layer_cutscenes | array<link_ptr> |  | Array of cutscenes placed between start and end cutscenes. This array has more than one element when stacking more types of cutscenes beside each other for example: roadwork should have first layer for signs and second for actual roadwork. Layer usage cabe be seen below: #Composition of the road event |
| mirror_cutscenes | array<link_ptr> |  | Similar as **layer_cutscenes** only that it's used for opposite road direction. Check **mirror_active** attributes for more info. |
| layer_min_curve | array&lt;float&gt; |  | Minimal allowed curvature of the road for layer cutscenes (in degress). It has to be defined for each item of **layer_cutscenes** array. |
| layer_max_curve | array&lt;float&gt; |  | Maximal allowed curvature of the road for layer cutscenes (in degress). It has to be defined for each item of **layer_cutscenes** array. |
| min_length | float | -1.0 | Minimal length of whole random event (in meters). |
| max_length | float | 10000.0 | Maximal length of whole random event (in meters). |
| min_shoulder_space | float | -1.0 | Minimal shoulder space of the road (in meters). Compared with road look shoulder_space_left/shoulder_space_right attributes. |
| max_shoulder_space | float | 100.0 | Maximal shoulder space of the road (in meters). Compared with road look shoulder_space_left/shoulder_space_right attributes. |
| traffic_block | bool | false | Is necessary to block the most outer lane? |
| weight | float | 1.0 | Weight of the generation probability of this road event. |
| countries | array&lt;token&gt; |  | Array of tokens of allowed countries for this road event, empty array for no limitation. Uses full name like eg. 'france'. |
| excluded_countries | array&lt;token&gt; |  | Array of tokens of excluded countries for this road event. |
| min_time_constraint | unsigned | 0 | Minimal allowed time for this road event generation (in game minutes in day). |
| max_time_constraint | unsigned | 24 * 60 | Maximal allowed time for this road event generation (in game minutes in day). |
| min_duration | unsigned | 0 | Minimal accident duration, accident will be active for this time at least, even if the road has been released (in game minutes). |
| area_tag | token | NULL | Limit the road event only to traffic area with certain tag (no tag for no limitation). |
| slow_down_passing | bool | false | Should AI vehicles passing the road event in adjacent lane slow down? |
| centerline_displacement | bool | false | Should AI vehicle drive near the centerline when passing the road event? |
| bridge_forbidden | bool | false | Prevent spawning of this road event on bridges? |
| tunnel_forbidden | bool | false | Prevent spawning of this road event in tunnels? |
| left_hand_traffic | bool | false | False for right-hand traffic, true for left-hand traffic. |
| allowed_lane_types | array&lt;token&gt; |  | Array of allowed lane types. Lane type is allowed if it's unit name contains some of the tokens from this array. Empty array means all lane are allowed (but still can be excluded with **excluded_lane_types** array). |
| excluded_lane_types | array&lt;token&gt; |  | Array of excluded lane types. Lane type is excluded if it's unit name contains some of the tokens from the array. |
| allowed_road_looks | array&lt;token&gt; |  | Array of allowed road looks. Expressed by suffix token of road look units. Empty array means that all road looks are allowed. |
| remove_map_sign | bool |  | If true then remove conflicting signs (speed limits) on the map overlapping with the road event. |
| inner_lane_allowed | bool | false | Is the road event allowed in the most inner lane? |
| center_lane_allowed | bool | false | Is the road event allowed in some of the center lanes? |
| outer_lane_allowed | bool | false | Is the road event allowed in the most outer lane? |
| allowed_lanes_count | array&lt;unsigned&gt; |  | Array of allowed road lanes counts. Empty array means no constraint. |
| mirror_active | bool | false | Should road event spawn in the opposite direction too? The opposite direction must fulfill all conditions of the road event. However **mirror_cutscenes** will be used in opposite direction instead of **layer_cutscenes**. |
| forward_allowed | bool | true | Is the road event allowed in the forward direction (nodes[0] -> nodes[1])? |
| backward_allowed | bool | true | Is the road event allowed in the backward direction (nodes[1] -> nodes[0])? |
| signs_cutscenes_outer | array<link_ptr> |  | Array of cutscenes for signs of the most outer lane. More info: [Documentation/Engine/Random Road Events#Signage](../Random%20Road%20Events.md#Signage). |
| signs_distances_outer | array&lt;float&gt; |  | Array of same size as **signs_cutscenes_outer** defining distances of signs for the most outer lane, where positive values will place signs before road event and negative will place it after. More info: [Documentation/Engine/Random Road Events#Signage](../Random%20Road%20Events.md#Signage). |
| signs_cutscenes_inner | array<link_ptr> |  | Array of cutscenes for signs of the most inner lane. More info: [Documentation/Engine/Random Road Events#Signage](../Random%20Road%20Events.md#Signage). |
| signs_distances_inner | array&lt;float&gt; |  | Array of same size as **signs_cutscenes_inner** defining distances of signs for the most inner lane, where positive values will place signs before road event and negative will place it after. More info: [Documentation/Engine/Random Road Events#Signage](../Random%20Road%20Events.md#Signage). |
| parent | link_ptr | NULL | Road event parent, all non explicitly defined values are inherited from the parent. |

## Composition of the road event

[![Layers in road event](../../../../../../images/articles/Documentation/Engine/Units/journey%20events%20road%20event/1024px-Engine_random_event_composition.jpg)](../../../../files/Engine%20random%20event%20composition.jpg.md)

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/journey_events_road_event | revision: 5045 | captured: 2026-10-21 23:56:14 -->
