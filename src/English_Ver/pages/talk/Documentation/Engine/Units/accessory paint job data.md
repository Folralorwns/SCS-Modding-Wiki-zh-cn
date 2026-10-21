# Talk:Documentation/Engine/Units/accessory paint job data

## Required Attributes

Status: open

Attributes that are *required* need to have their names **bolded** in the name column. [Smarty](../../../../users/Smarty.md) ([talk](../../../../user_talk/Smarty.md)) 21:15, 22 September 2016 (CEST)

## Flipflake Mode/Attributes Description

Status: open

Someone more knowledgeable is going to have to help me out with the flipflake stuff. My impression is that it does two specular effects:

- Clearcoat: dominant pass based on the calculated world space normal using vertex normals (or tangents and texture_nmap for tsnmap flavour)
  - flake_clearcoat_rolloff: I'm *really* unsure on this. Does it affect the relative strength of flake specular vs clearcoat specular?
- Flake: weaker pass based on world space normal, manipulated somehow by the flake_noise texture

Plus an effect that colours areas beyond some angular threshold (set by flip_strength?) with the flip_color

Am I close? [Smarty](../../../../users/Smarty.md) ([talk](../../../../user_talk/Smarty.md)) 21:15, 22 September 2016 (CEST)

<!-- source: https://modding.scssoft.com/wiki/Talk%3ADocumentation/Engine/Units/accessory_paint_job_data | revision: 2830 | captured: 2026-10-21 23:56:14 -->
