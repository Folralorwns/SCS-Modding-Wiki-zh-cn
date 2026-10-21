# Documentation/Tools/Map Editor/Note API

The note API allows multiple users to share in-map notes without having to manually share files between each other.

The `{{url}}` is the `note_server` field as specified in [editor_online_data.sii](Editor%20online%20data.md)

#### **GET** `{{url}}/version`

Get server protocol version.

Example response: `2`

As of writing this the only supported version is 2.

#### **GET** `{{url}}/maps/:map_id`

Fetches map information

Example response:

```
{
    "name":"/map/europe.mbd"
}
```

#### **POST** `{{url}}/maps/:map_id`

URL parameters:

- `v` - protocol version

Updates map info.

Example body:

```
{
 "source": "base",
 "name": "/map/europe.mbd",
 "artist_id": 4
}
```

#### **GET** `{{url}}/maps/:map_id/notes`

Fetches notes.

Example response:

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

`data` is base64 encoded binary data:

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

Get the last artist that made a change to this note

Example response:

```
{
    "artist_id": "1"
}
```

#### **POST** `{{url}}/maps/:map_id/session/:session_id/notes/batch`

Attempts to create new notes.

URL parameters:

- `v` - protocol version

Example body:

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

Another example body:

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

Another example body:

```
[
 [
  "/:note_id/delete/:note_revision"
 ]
]
```

Example response:

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

The number of array entries should match the number of notes submitted. The first entry is the http response code for that note, the second entry is information about the note.

#### **POST** `{{url}}/maps/:map_id/session/:session_id/commit`

Attempts to commit current session. Any updates or new notes need to be commited for others to see them.

#### **POST** `{{url}}/maps/:map_id/session/:session_id/abort`

Attempts to abort current session without commiting any updates or new notes.

#### **GET** `{{url}}/maps/:map_id/notes/:note_id`

Fetches a specific note by id.

Refer to `{{url}}/maps/:map_id/notes` for example response. The only difference being that here we expect just the one object, not an array.

#### **GET** `{{url}}/maps/:map_id/updates/:timestamp`

Example response:

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

URL parameters:

- `v` - protocol version

Example body:

```
{
 "id": "742eb98d",
 "source": "base",
 "name": "/map/europe.mbd",
 "artist_id": 2
}
```

#### **POST** `{{url}}/maps/:map_id/session`

Creates a new session.

Example body:

```
{
 "artist_id": 3
}
```

Example response:

```
{
 "id":"12345"
}
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/Note_API | revision: 5707 | captured: 2026-10-21 23:56:14 -->
