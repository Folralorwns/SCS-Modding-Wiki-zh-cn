# Documentation/Engine/Units/dynamic cargo data

The **dynamic cargo data** unit class includes all needed data related to dynamic cargo loading feature. Units of this type are found in **/def/vehicle/cargo/<cargo_name>/**, typically in the same file as [accessory cargo data](accessory%20cargo%20data.md). Such accessory cargo data then contains a pointer to its dynamic cargo data.

For debugging purposes, it is better to not leave this unit nameless. But choose the name carefully to avoid conflicts! The naming convention for SCS cargoes is *dyn.cargo.data.<cargo_name>*, where you substitute <cargo_name> for the cargo that you're adding. For example *dyn.cargo.data.potatoes_b*.

## Attributes

Many attributes can be omitted. From 1.56 there are now three types of dynamic cargo (un)loading:

- **Particles** - the dynamic cargo (un)loading of grainhoppers added in 1.51. For this type the other required attributes are **trailer_particle**, **world_particle**, and **material_path**. For dynamic cargo data to be considered correct, you must be able to load it (world_particle), unload it (trailer_particle), and display a material on the cargo pile mesh inside the trailer (material_path).
- **Mover** - the dynamic cargo (un)loading of logger trailers added in 1.52. This type ignores all the particle attributes and as of 1.54 it uses the cargo model from [accessory cargo data](accessory%20cargo%20data.md) if the loading_method: cylinder is supported.
- **Mover_bulk** - the dynamic cargo (un)loading of scrap metal added in 1.56. This type uses a mover to load the cargo, but inside the trailer there is a mesh that grows as in the particle-based loading, albeit in increments.

Entries marking legend:

- p - required for particles-based bulk (un)loading.
- m - required for mover-based cylinder (un)loading.
- b - required for mover-based bulk loading.

If no letter is marked, this signifies that the attribute is optional.

| Name | [Type](../Units.md#Attribute_types) | Required | Description |
| --- | --- | --- | --- |
| type | enum | pmb | The type of the dynamic cargo data, currently three exist (see above). particles mover mover_bulk |
| trailer_particle | string | p | [Unit name](../Units.md) of the particle effect (particle_set) that is emitted from the trailer during dynamic cargo UNLOADING. |
| trailer_particle_night | string |  | Unit name of the particle effect that is emitted from the trailer during dynamic cargo UNLOADING. (Night variant) |
| impact_particle | string |  | Unit name of the particle effect that is emitted at the place where the loading particle effect (world_particle) touches the trailer. |
| impact_particle_night | string |  | Unit name of the particle effect that is emitted at the place where the loading particle effect (world_particle) touches the trailer. (Night variant) |
| world_particle | string | p | Unit name of the particle effect that is emitted from a cargo particle hookup in the map during dynamic cargo LOADING. |
| world_particle_night | string |  | Unit name of the particle effect that is emitted from a cargo particle hookup in the map during dynamic cargo LOADING. (Night variant) |
| material_path | string | pb | Path to the material used for the mesh representing the pile of cargo inside the trailer. |
| cargo_slope_angle | float |  | The [angle of repose](https://en.wikipedia.org/wiki/Angle_of_repose) of the cargo when it is loaded into the trailer. In other words how steep the pile of cargo will be when loading. *Default value:* 25.0. |
| loading_sound | string |  | Path to the sound emitted from the trailer at the spot where the stream of cargo touches the pile of cargo during loading phase/when the loader mover places a pile of cargo inside the trailer. |
| unloading_sound_default | string |  | Path to the sound emitted from the trailer at the spot where the stream of cargo exits the trailer during unloading phase/when the loader mover takes out a pile of cargo from the trailer. |
| pile_model | string | b | Path to the static model serving as the pile inside the grab handle. |
| grab_types | array&lt;token&gt; | mb | Array of tokens of the names of grab handles that can (un)load this cargo. Can repeat, which is used for defining the *variants* attribute. |
| variants | array&lt;token&gt; | b | Array of tokens of the names of the variants of the *pile_model*. You must define the same number of variants as *grab_types*, effectively matching them to the grab handles. |
| variant_radius | array&lt;float&gt; | b | Array of "fake radii" of the variants of the *pile_model*. You must define the same number of variants as *grab_types*, effectively matching them to the grab handles. This radius serves to control how much the grab handle will close around the cargo and must be fiddled with before a perfect fit is created. |

##### Note on optional attributes

If night variants of particles are not defined, the normal (day) variant is used.

Sounds can be defined for any loading type, but they behave slightly differently. For particles-based loading, the sound is played continuously during the trailer (un)loading. For mover-based loading, the sound is played once when the cargo 'pops' from the grab handle into the trailer or vice versa.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Units/dynamic_cargo_data | revision: 5732 | captured: 2026-10-21 23:56:14 -->
