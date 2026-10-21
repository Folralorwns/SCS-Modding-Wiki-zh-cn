# 文档/工具/地图编辑器/Note API

Note API 允许多名用户共享地图内笔记，而无需在彼此之间手动共享文件。

`{{url}}` 是 [editor_online_data.sii](Editor%20online%20data.md) 中指定的 `note_server` 字段。

#### **GET** `{{url}}/version`

获取服务器协议版本。

示例响应：`2`

截至撰写本文时，唯一受支持的版本是 2。

#### **GET** `{{url}}/maps/:map_id`

获取地图信息。

示例响应：

```
{
    "name":"/map/europe.mbd"
}
```

#### **POST** `{{url}}/maps/:map_id`

URL 参数：

- `v` - 协议版本

更新地图信息。

示例请求体：

```
{
 "source": "base",
 "name": "/map/europe.mbd",
 "artist_id": 4
}
```

#### **GET** `{{url}}/maps/:map_id/notes`

获取笔记。

示例响应：

```
[
 {
  "id":"00000000000004a8",
  "artist_id":75,
  "creator_id":48,
  "private_id":48,
  "pos_x":1.23,
  "pos_y":-100,
  "pos_z":23,
  "type":2,
  "state":0,
  "name":"",
  "description":"",
  "data":"See comment",
  "version":2,
  "create_time":"1565945862 2019-08-16 08:57:42 UTC",
  "update_time":"1709125289 2024-02-28 13:01:29 UTC"
 }
]
```

`data` 是 base64 编码的二进制数据：

```
u32 data_version; // Can be 1 or 2
u32 name_color;
s32 shape_type;
float line_width;
u32 shape_color;
u32 point_count;
if (is_qa_bug) {
    // point_count needs to be 0
}
else {
    // Load each point as a float3
}

if (data_version >= 2) {
    u32 item_uids_count;
    // Load each uid as a u64
}
```

#### **GET** `{{url}}/maps/:map_id/changes/:note_id`

获取最后对此笔记做出更改的艺术家。

示例响应：

```
{
    "artist_id": "1"
}
```

#### **POST** `{{url}}/maps/:map_id/session/:session_id/notes/batch`

尝试创建新笔记。

URL 参数：

- `v` - 协议版本

示例请求体：

```
[
 [
  "",
  {
   "id": 1234,
   "creator_id": 4,
   "pos_x": 1.2,
   "pos_y": 3,
   "pos_z": 42.0,
   "type": 4,
   "state": 1,
   "name": "issue",
   "description": "it dont work",
   "private_id": 2,
   "data": ""
  }
 ]
]
```

另一个示例请求体：

```
[
 [
  "/:note_id/update/:note_revision",
  {
   "description": "it still dont work"
  }
 ]
]
```

另一个示例请求体：

```
[
 [
  "/:note_id/delete/:note_revision"
 ]
]
```

示例响应：

```
[
 [
  201,
  {
   "id": "2f1",
   "artist_id": "4",
   "update_time": "1755247764",
   "version": 2
  }
 ]
]
```

数组中的条目数量应与提交的笔记数量一致。第一个条目是该笔记的 HTTP 响应码，第二个条目是该笔记的相关信息。

#### **POST** `{{url}}/maps/:map_id/session/:session_id/commit`

尝试提交当前会话。任何更新或新笔记都必须提交后，其他人才能看到。

#### **POST** `{{url}}/maps/:map_id/session/:session_id/abort`

尝试中止当前会话，不提交任何更新或新笔记。

#### **GET** `{{url}}/maps/:map_id/notes/:note_id`

按 id 获取特定笔记。

示例响应请参阅 `{{url}}/maps/:map_id/notes`。唯一区别在于此处期望的是单个对象，而非数组。

#### **GET** `{{url}}/maps/:map_id/updates/:timestamp`

示例响应：

```
{
 "time":"1755248256 2025-08-15 08:57:36 UTC",
 "update": [
  Refer to {{url}}/maps/:map_id/notes for example response.
 ],
 "delete": [
  {
   "id":"000000000007ea54",
   "version":2
  }
 ]
}
```

#### **POST** `{{url}}/maps`

URL 参数：

- `v` - 协议版本

示例请求体：

```
{
 "id": "742eb98d",
 "source": "base",
 "name": "/map/europe.mbd",
 "artist_id": 2
}
```

#### **POST** `{{url}}/maps/:map_id/session`

创建新会话。

示例请求体：

```
{
 "artist_id": 3
}
```

示例响应：

```
{
 "id":"12345"
}
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/Note_API | revision: 5707 | captured: 2026-10-21 23:56:14 -->
