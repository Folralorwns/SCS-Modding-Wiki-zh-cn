# Documentation/Tools/Map Editor/Editor online data

The **editor_online_data** class is used to define the API urls and extra data for editor online services. When loading it, the editor first tries to load it from your home directory at `/home/editor_online_data.sii`. When it can't load from your home directory it tries to load it from `/def/editor_online_data.sii`.

An example definition of `editor_online_data.sii` with comments explaining the purpose of each field:

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

The structure of the json at `note_username_url` looks like this:

```
{
    "1":"NoteUser1",
    "2":"NoteUser2",
    "3":"NoteUser3",
}
```

The id corresponds to `g_map_note_user_id`

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Map_Editor/Editor_online_data | revision: 5705 | captured: 2026-10-21 23:56:14 -->
