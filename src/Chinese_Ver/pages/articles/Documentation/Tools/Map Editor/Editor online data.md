# 文档/工具/地图编辑器/编辑器在线数据

**editor_online_data** 类用于定义编辑器在线服务的 API URL 和额外数据。加载时，编辑器首先尝试从主目录的 `/home/editor_online_data.sii` 加载。无法从主目录加载时，会尝试从 `/def/editor_online_data.sii` 加载。

`editor_online_data.sii` 的定义示例，其中注释说明了各字段的用途：

```
SiiNunit
{
editor_online_data : .edit_online
{
	# Parallel arrays of map filename and url for fetching sector locks.
	map_server[]: "http://example.com"
	map_name[]: "/map/europe.mbd"

	# The url for fetching notes.
	note_server: "http://example.com"

	# URL address of mapping of map note user IDs to usernames.
	note_username_url: "http://example.com/list.json"

	# URL address of mantis bug resolve page.
	qa_bug_resolve_url: "https://example.com/bug_actiongroup_page.php"

	# Map note autosave interval from start of session (in seconds).
	note_autosave_interval_session_start: 300

	# Map note autosave interval from last session modification (in seconds).
	note_autosave_interval_session_modified: 30

	# How often should the editor try to refresh map notes (in seconds).
	note_autorefresh_interval: 60

	# The index of each name corresponds to the artist id
	# which is determined by the value of g_artist_id
	artists[0]: "None"
	artists[1]: "ArtistName1"
	artists[2]: "ArtistName2"
}
}
```

`note_username_url` 中 json 的结构如下：

```
{
    "1":"NoteUser1",
    "2":"NoteUser2",
    "3":"NoteUser3",
}
```

该 id 对应 `g_map_note_user_id`

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/Editor_online_data | revision: 5705 | captured: 2026-10-21 23:56:14 -->
