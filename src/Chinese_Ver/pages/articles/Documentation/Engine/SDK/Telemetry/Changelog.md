# Documentation/Engine/SDK/Telemetry/Changelog

## SDK 1.10

- Added gameplay events support.
- Both trucks and trailers now have also license plate information provided by configs.
- Trailers
  - Added support for multiple trailers (up to 10) (See channels and configs: trailer.[index], 'trailer' has the same data as 'trailer.0' for backward compatibility)
  - New config attributes
    - brand
    - name
    - chain.type
    - body.type
  - New channels
    - trailer.wear.wheels - (float) Average wear across all wheel accessories.
    - trailer.cargo.damage - (float) Damage of the cargo inside this trailer.
  - Trailers now also report liftable axles informations.
- Job changes
  - New config attributes
    - cargo.unit.mass - (float) What is the mass of single cargo unit in kg.
    - cargo.unit.count - (u32) How many units of cargo does the job consist of.
    - cargo.loaded - (bool) Is cargo loaded?
    - job.market - (string) The market the job is for (see comment for possible values)
    - special.job - (bool) Is that special transport job?
  - New channels
    - job.cargo.damage - (float) The total damage of the cargo.
  - Special transport jobs will now report correctly source and destination cities.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/SDK/Telemetry/Changelog | revision: 3928 | captured: 2026-10-21 23:56:14 -->
