# Documentation/Engine/Mover model group

Mover model group 是一种新的 mover 定义单元。这个新单元的设计思路是提供一个能够轻松组合兼容模型与动画的系统。其主要用途是为角色省去为每种模型与动画组合单独定义的需要。此外，这些 mover 组可以使用独立模型中的道具，并且你可以轻松地将它们“蒙皮”到特定骨骼。

整个系统由四个单元组成：

## Mover desc

单元 `mover_desc` 表示模型及其数据。它定义在 `/base/def/world/mover_desc.sii` 中。

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

**属性：**

- `model_desc` 模型描述符。
- `model_coll` 模型碰撞。
- `lods` 模型 LOD 描述符。
- `lod_distances` LOD 距离。
- `group_tags` 组标签。更多信息见 **mover_model_group** 一节。

## Mover anim

单元 `mover_anim` 表示动画及其数据。它定义在 `/base/def/world/mover_anim.sii` 中。

```
mover_anim : mover_anim.sweeper {
    model_anim: "/model/mover/characters/new_generation/animations/universal/sweeping_anim.pma"

    group_tags[]: human
    group_tags[]: man
    group_tags[]: sweeper

    props[]: mover_props.sweeper.broom
}
```

**属性：**

- `model_anim` 动画描述符。
- `group_tags` 组标签。更多信息见 **mover_model_group** 一节。
- `props` 指向动画道具的链接指针数组。

## Mover anim props

单元 `mover_anim_props` 表示动画道具及其设置。它定义在 `/base/def/world/mover_anim_props.sii` 中。

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

**属性：**

- `bone_a` 用于“蒙皮”前缀的第一根骨骼。
- `bone_b` 用于“蒙皮”前缀的第二根骨骼。
- `bone_offset_a` 第一根骨骼的蒙皮偏移。
- `bone_offset_b` 第二根骨骼的蒙皮偏移。
- `model` 道具模型描述符。
- `model_animation` 道具模型动画。
- `sync_animation` 强制道具动画与 mover 动画之间的时间同步。
- `model_offset` 道具放置偏移。
- `model_rotation` 道具放置旋转。

**工作原理**

道具作为独立模型渲染和放置。通过骨骼 A 和骨骼 B，我们可以将道具附着到 mover 骨架。共有三种可能的设置方式。

: **1) 未设置骨骼。** 道具放置在 mover 原点加上 `model_offset` 的位置，旋转为零加上 `model_rotation`。例如放在地面上的水桶。
: **2) 仅设置骨骼 A。** 道具放置在骨骼 A 的位置加上 `bone_offset_a` 再加上 `model_offset` 处，旋转为骨骼 A 的旋转加上 `model_rotation`。例如握在一只手中的海绵。
: **3) 设置了骨骼 A 和骨骼 B。** 道具放置在骨骼 A 的位置加上 `bone_offset_a` 再加上 `model_offset` 处，旋转由方向向量（**从**骨骼 B 的位置加上 `bone_offset_b` **到**骨骼 A 的位置加上 `bone_offset_a`）加上 `model_rotation` 给出。例如双手握持的扫帚。

## Mover model group

单元 `mover_model_group` 表示指定的 mover desc 与 mover anim 之间所有有效的组合。它定义在 `/base/def/world/mover.group.sii` 中。但它可以放置在任意 mover 定义文件中。

```
mover_model_group: mover.work_sw_all {
    mover_name: "worker sweeper all"

    desc_tags[]: man
    desc_tags[]: worker
    anim_tags[]: man
    anim_tags[]: sweeper
}
```

**属性：**

- `desc_tags` Mover desc 标签。
- `anim_tags` Mover anim 标签。
- `country_specific` 若为 true，则只生成包含由 mover 放置位置所指定国家标签的 mover desc。

**工作原理**

该单元加载时，会收集包含 `desc_tags` 属性中全部标签的所有 mover desc，以及包含 `anim_tags` 属性中全部标签的所有 mover anim。生成 mover 时，它会随机选择一个已收集的 mover desc，然后尝试选择一个已收集的、使用与所选 mover desc 模型**相同骨架**的 mover anim。

这一点很重要，因为有时你希望组中包含骨架不同的模型和骨架不同的动画。但你只想要有效的模型-动画组合。**例如**由行走的男性和女性组成的组，其中男性使用与女性不同的骨架。

**优化**

由于引擎保证只会创建有效的模型-动画组合，因此看起来动画标签只需要包含描述动画活动的标签。但由于模型-动画组合是在生成 mover 的那一刻选择的，我们希望尽可能限制组合池。因此，mover anim 标签应当包含（除活动本身之外）描述兼容 mover desc 的标签。在上面的 `mover_anim` 示例中，这些标签是 `human` 和 `man`。而在相关的 mover 组中，应在 `anim_tags` 里使用这些标签。在示例中即为标签 `man`。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Mover_model_group | revision: 5135 | captured: 2026-10-21 23:56:14 -->
