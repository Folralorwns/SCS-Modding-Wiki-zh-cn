# Documentation/Engine/Mover model group

Mover model group is a new mover definition unit. The idea of this new unit is to have a system which can easily combine compatible models and animations. The main use is for characters to remove the need of definition for every combination of models and animations. Moreover these mover groups can use props in separate models and you can easily "skin" them to specific bones.

The whole system consists of four units:

## Mover desc

Unit `mover_desc` represents model and its data. It is located in `/base/def/world/mover_desc.sii`.

```
mover_desc : mover_desc.worker_3 {
    model_desc: "/model/mover/characters/new_generation/new/models/man/worker_vest/worker_vest_nemiro_lod0.pmd"

    lods[0]: "/model/mover/characters/new_generation/new/models/man/worker_vest/worker_vest_nemiro_lod1.pmd"
    lods[1]: "/model/mover/characters/new_generation/new/models/man/worker_vest/worker_vest_nemiro_lod2.pmd"
    lods[2]: "/model/mover/characters/new_generation/new/models/man/worker_vest/worker_vest_lod3.pmd"

    lod_distances[0]: 10
    lod_distances[1]: 30
    lod_distances[2]: 90

    group_tags[]: human
    group_tags[]: man
    group_tags[]: cauca
    group_tags[]: worker
}
```

**Properties:**

- `model_desc` Model descriptor.
- `model_coll` Model collision.
- `lods` Model lod descriptors.
- `lod_distances` Lod distances.
- `group_tags` Group tags. More about it in **mover_model_group** section.

## Mover anim

Unit `mover_anim` represents animation and its data. It is located in `/base/def/world/mover_anim.sii`.

```
mover_anim : mover_anim.sweeper {
    model_anim: "/model/mover/characters/new_generation/animations/universal/sweeping_anim.pma"

    group_tags[]: human
    group_tags[]: man
    group_tags[]: sweeper

    props[]: mover_props.sweeper.broom
}
```

**Properties:**

- `model_anim` Animation descriptor.
- `group_tags` Group tags. More about it in **mover_model_group** section.
- `props` Array of link pointers to animation props.

## Mover anim props

Unit `mover_anim_props` represents animation props and its settings. It is located in `/base/def/world/mover_anim_props.sii`.

```
mover_anim_props : mover_props.sweeper.broom {
    model: "/model/mover/characters/new_generation/models/props/independent/broom.pmd"
    bone_a: lefthand
    bone_b:	righthand
    bone_offset_a: (0.03, 0.08, 0)
    bone_offset_b: (-0.2, 0.16, -0.15)
    model_offset: (0.0, 0.0, -0.67)
    model_rotation: (0.0, 0.0, 0.0)
}
```

**Properties:**

- `bone_a` First bone to "skin" prefix.
- `bone_b` Second bone to "skin" prefix.
- `bone_offset_a` Skin offset for the first bone.
- `bone_offset_b` Skin offset for the second bone.
- `model` Props model descriptor.
- `model_animation` Props model animation.
- `sync_animation` Force time synchronization between props animation and mover animation.
- `model_offset` Props placement offset.
- `model_rotation` Props placement rotation.

**How does it work?**

Props is rendered and placed as separate model. Using bone A and bone B we can attach the props to the mover skeleton. There are three possible setups.

: **1) No bones are set.** Props is placed to the mover origin plus `model_offset` and with zero rotation plus `model_rotation`. For example a bucket on the ground.
: **2) Bone A is set only.** Props is placed to the bone A placement plus `bone_offset_a` plus `model_offset` with bone A rotation plus `model_rotation`. For example a sponge in one hand.
: **3) Bone A and bone B are set.** Props is placed to the bone A placement plus `bone_offset_a` plus `model_offset` with rotation given by direction vector (**from** bone B placement plus `bone_offset_b` **to** bone A placement plus `bone_offset_a`) plus `model_rotation` For example a broom in both hands.

## Mover model group

Unit `mover_model_group` represents all valid combinations between specified mover desc and mover anim. It is located in `/base/def/world/mover.group.sii`. But it can placed in any mover def file.

```
mover_model_group: mover.work_sw_all {
    mover_name: "worker sweeper all"

    desc_tags[]: man
    desc_tags[]: worker
    anim_tags[]: man
    anim_tags[]: sweeper
}
```

**Properties:**

- `desc_tags` Mover desc tags.
- `anim_tags` Mover anim tags.
- `country_specific` If true then only mover desc containing country tag given by mover placement will be generated.

**How does it work?**

When the unit is loaded, it collects all mover desc containing all tags from the `desc_tags` property and all mover anim containing all tags from the `anim_tags` property. When the mover is generated, it randomly chooses one of the collected mover desc and then it tries to choose one of the collected mover anim which use the **same skeleton** as the choosen mover desc model.

This is important because sometimes you want to have group containing models with different skeletons and animations with different skeletons. But you want only valid model-anim combinations. **For example** group of walking men and women where men use different skeleton than women.

**Optimization**

Because engine ensures that only valid model-anim combinations will be created, it may seem that animation tags should contain only tags describing the animation activity. But because the model-anim combinations are choosen in the moment of mover generation, we want to limit the combination pool as much as possible. Because of that mover anim tags should contain (apart from the activity itself) tags describing compatible mover desc. In `mover_anim` the example above these tags are `human` and `man`. And in the related mover group use these tags in `anim_tags`. In the example it is the tag `man`.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Mover_model_group | revision: 5135 | captured: 2026-10-21 23:56:14 -->
