# Documentation/Tools/SCS Blender Tools/Animation system

Animations used in SCS games are driven by skeletons and keyframe animations (which are manipulating bones in the skeleton). There are two types of these animations:

1. **Program driven animations** which mostly expects animation range from 0 to 1 if not stated differently in animation definition files. This means that first frame will be used as 0 state and last frame will be used as state 1, any state between this range is interpolated across whole keyframe range of animation. Example of these animations are truck interior animations in Euro Truck Simulator 2 which are defined inside each truck definition folder (example path: *"def/vehicle/truck/man.tgx/interior/animations.sui"*).
2. **Static loop animations** used by so called "mover" objects. Movers can be placed all around the game world with the help of map editor. Examples for mover objects are: windmills, pedestrians, animals etc. To create your own mover you should create new *"def/world/mover.\<id_of_your_mod>.sii"* file and define mover in that file by the template from original *"def/world/mover.sii"* file. > > **Note:** Special type of movers named "walkers" can also use forward movement in their animation which can be animated as movement of skeleton object on Y axis.

Regardless of the SCS Animation type, creation pipeline within Blender Tools is the same for both above types. To create SCS Animation you will have to use standard Blender procedure of [armature creation](https://docs.blender.org/manual/animation/armatures/introduction.html), [vertices skinning](https://docs.blender.org/manual/animation/armatures/skinning/parenting.html#with-empty-groups), [bones posing](https://docs.blender.org/manual/en/latest/animation/armatures/posing/introduction.html) and [setting keyframes](https://docs.blender.org/manual/en/latest/animation/keyframes/introduction.html).

> > **Note:** Only location, rotation and scale manipulation of bones will be exported during SCS Animation export, anything else will be ignored even if it will be animated and played inside Blender.

After you successfully animate bones with Blender action you will have to set up SCS Animation in #SCS Animations panel. Once setup is done you can export your SCS Game Object as you did before and animations will be exported with it.

> > **Note:** Remember that for export of animated model you have to enable ***Animated Model*** in SCS Root Object properties, switch can be found in the locators panel [Root objects](Root%20objects.md).

## SCS Animations panel

To export created Blender action into the game you will have to define SCS Animations with usage of SCS Animations sub-panel which you can find inside Blender properties window in *Object* tab under *SCS Object* panel. The panel will appear only if the currently selected object is armature.

[![SCS_Tools_Object_Specials_-_Animations.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Animation%20system/SCS_Tools_Object_Specials_-_Animations.280.png)](../../../../files/SCS%20Tools%20Object%20Specials%20-%20Animations.280.png.md)

> > **Note:** When seeing "No 'SCS Root Object'!" message instead of animations list make sure to parent armature object to SCS Root Object.

#### Custom Export Path

Custom export path should be used to store your animation files somewhere else than the rest of the files when exporting SCS Game Object.

This path may be useful when you are creating sequence of animations for walkers, as all of your walkers can use the same skeleton and animations and thus you may export them in different directory.

If custom path remains disabled, all of the SCS Animations will be exported beside the rest of the files.

#### SCS Animations list

SCS Animations list contains all animations used on current SCS Game Object. For creation or deletion of SCS Animations use **+** and **−** buttons on the side of the animations list. Furthermore, animations can be imported with import button ( **⤓** ), which will place you into the file browser to select SCS Animation for importing.

Each SCS Animation entry features:

- export inclusion property will exclude animation used in that line from exporting, if it's unchecked and you are exporting whole SCS Game Object,
- name of SCS Animation which will be also used as the name of exported animation file (PIA),
- export operator button for direct export of animation used in that line via file browser.

#### Active Animation Settings

This panel area is place where you link Blender action (animation) and set various properties to currently selected SCS Animation in list.

Properties of SCS Animation:

- **Start** - frame in action which will be used as a start of SCS Animation,
- **End** - frame in action which will be used as an end of SCS Animation,
- **Length** - SCS Animation duration in seconds,
- **Increase Animation Step ( + )** - stretches action by factor 2 and increases ***Export Step*** by 1 to compensate scaling. This gives you better control on sub keyframes and distribution of transformations over time,
- **Decrease Animation Step ( − )** - shrinks action by factor 2 and decreases ***Export Step*** by 1 to compensate scaling. This removes each second keyframe, which decreases control over the animation,
- **Export Step** - number of frames to step in Blender action for each iteration during export.

#### Animation Player

To preview currently selected SCS Animation you can use Animation Player, which is nothing more than wrapped interface from multiple Blender editors for already existing settings.

First row consist from **Start**, **End** and **Current** frame of animation playback. While second row gives you possibility to use playback controls and set FPS for animation playback.

> > **Note:** Changing FPS manually will invalidate preview of currently selected SCS Animation as FPS is calculated by set ***Start***, ***End*** and ***Length*** of SCS Animation.

## SCS Skeleton panel

There is also additional panel for setting custom skeleton file path inside SCS Project Base Path and name of skeleton file (PIS) which will be created in the case of exporting animated SCS Game Object.

[![SCS_Tools_Object_Specials_-_Skeleton.280.png](../../../../../../images/articles/Documentation/Tools/SCS%20Blender%20Tools/Animation%20system/SCS_Tools_Object_Specials_-_Skeleton.280.png)](../../../../files/SCS%20Tools%20Object%20Specials%20-%20Skeleton.280.png.md)

This custom path and name come handy again in the case of creating sequence of animations for walkers, as all of your walkers can use the same skeleton and thus you may export skeleton in different directory.

If both paths remain empty, skeleton file (PIS) will be saved beside other exported files and will use SCS Root Object name as the name of the file.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/SCS_Blender_Tools/Animation_system | revision: 4305 | captured: 2026-10-21 23:56:14 -->
