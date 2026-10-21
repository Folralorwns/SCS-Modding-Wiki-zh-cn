# Documentation/Tools/Map Editor/Sector lock API

The sector lock API allows one to give exclusive ownership of sectors to specific artists. This then minimizes conflicts when multiple people are working on one map.

The `{{url}}` is the configured url for the currently loaded map as specified in [editor_online_data.sii](Editor%20online%20data.md)

#### **GET** `{{url}}/get_locks.php`

Optional URL parameters:

- `submap`
- `minx`
- `miny`
- `maxx`
- `maxy`

Example response:

```
sec-0016-0015:-1|sec-0016-0014:1|sec-0016-0013:2
```

The response consists of a list of sectors and their corresponding owners specified by their artist id.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/Sector_lock_API | revision: 5706 | captured: 2026-10-21 23:56:14 -->
