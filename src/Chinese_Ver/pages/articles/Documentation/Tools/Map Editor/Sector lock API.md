# 文档/工具/地图编辑器/扇区锁定 API

扇区锁定 API 允许将扇区的独占所有权分配给特定的艺术家。这样可最大限度减少多人同时处理同一地图时的冲突。

`{{url}}` 是当前已加载地图所配置的 URL，在 [editor_online_data.sii](Editor%20online%20data.md) 中指定。

#### **GET** `{{url}}/get_locks.php`

可选的 URL 参数：

- `submap`
- `minx`
- `miny`
- `maxx`
- `maxy`

示例响应：

```
sec-0016-0015:-1|sec-0016-0014:1|sec-0016-0013:2
```

响应由扇区列表及其对应所有者组成，所有者通过其艺术家 id 指定。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/Sector_lock_API | revision: 5706 | captured: 2026-10-21 23:56:14 -->
