# Documentation/Engine/Game Radio

## File structure

Basic structure of game radio.

This doesn't show station graphics files as they are optional.

```
├─ manifest.sii                 <typical mod metadata file>
├─ icon.jpg                     <typical mod metadata file>
├─ mod_description.txt          <typical mod metadata file>
│
└─ offline_radio                <game radio folder, same level as you would normally place def, material, etc. folders>
   │
   ├─ offline_radio.mymod.sii   <required: contains definitions for the new radio station(s)>
   │
   ├─ mymod_stn0                <required: must match the id specified in offline_radio.mymod.sii>
   │  ├─ tracks.sii             <required>
   │  └─ music
   │     ├─ song_a.ogg
   │     └─ song_b.mp3
   │
   └─ mymod_stn1
      └─ ...
```

Supported audio formats: `ogg`, `mp3`

For organizational purposes a separate subfolder `offline_radio/stationid/music` is recommended; note, however, that for the tracks you're specifying the full game file system path, so this organizational structure is optional; in principle the audio files could be anywhere and even be shared among stations.

## Unit descriptions

### Definition of station(s)

`offline_radio/offline_radio.<my_mod_id>.sii`

```
SiiNunit
{

offline_radio_station : _nameless.0
{
    # ID of the station. Can be anything but must be globally unique, so use reason.
    # [token, required]
    id: mymod_stn0

    # User-friendly name of the station.
    # [string, required]
    name: "Hard FM"

    # Info displayed in the radio table.
    # [string, required]
    genre: "Techno/Schranz"

    # Info displayed in the radio table.
    # [string, required]
    language: "EN"

    # Are the tracks supposed to not generate copyright claims (on services such as YouTube and Twitch)?
    # (Not enforced in any way, please don't specify unless you know for sure.)
    # [bool, optional, default = false]
    stream_safe: false

    # "History size" for previously played tracks as a fraction of total number of songs.
    # (See discussion below.)
    # [float from 0.0 to 1.0, optional, default = 0.5]
    recently_played_history_size_fraction: 0.5

    # Minimum number of tracks that must play before another track from the same artist can play.
    # (See discussion below.)
    # [non-negative integer, optional, default = 0 (no restriction)]
    min_num_tracks_between_same_artist: 0

    # Path to image to be used in the radio table. If not given, name will be displayed as text.
    # [string, optional]
    cover_img: "/material/ui/radio/offline_station/mymod_stn0.mat"

    # Path to cover station image shown in the miniplayer. If not given, default icon will be used.
    # [string, optional]
    miniplayer_img: "/material/ui/radio/offline_station/mymod_stn0_small.mat"

    # Custom PML, acting as title text. Usually includes an <img> element.
    # If not given, regular text with station name will be used.
    # [string, optional]
    miniplayer_title_pml: "<align vstyle=center><color value=FFFFFFFF><img src=/material/ui/radio/offline_station/mymod_stn0_title.mat height=18 width=144></align>"

    # Crossfade duration between tracks.
    # [non-negative integer, optional, default = 2000, if 0 crossfade is disabled]
    music_crossfade_duration_ms: 2000
}

offline_radio_station : _nameless.1
{
    # Station data...
}

# More stations...

}
```

#### Track selection & playback history

Because we don't want the same track to play too often, radio track selection is influenced by the playback history.

This process is governed by 2 values in station definition:

- `recently_played_history_size_fraction` determines the size of a "history window", any tracks that have been played within it are not eligible for being played as the next track. So if the value is `0.5` and the station has 20 tracks, at least 10 other songs must play before the current song can be played again.
- `min_num_tracks_between_same_artist` acts on top of this by preventing the same artist being played too often. Note that this is just a simple comparison of `artist` values between tracks so `"Artist"` and `"Artist feat. Someone else"` are different, as are `"Artist"` and `"ARTIST"`.

Please use reason when selecting these values: them being too restrictive will cause the track selection process to not function properly.

### Per-station definitions

`offline_radio/<my_station_id>/tracks.sii` - provides data about individual tracks for the radio.

```
SiiNunit
{

offline_radio_track : _nameless.0
{
    artist: "NIKOLINA, Teletech"
    name: "No More Lies"
    ufs_path: "/offline_radio/mymod_stn0/music/nikolina_no_more_lies.ogg"
}

offline_radio_track : _nameless.1
{
    # Track data...
}

# More tracks...

}
```

## Known limitations

Currently there are issues with compressed audio assets, so using the `.zip` mod format is not supported. Please use `.scs` packs or regular folders.

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Game_Radio | revision: 5769 | captured: 2026-10-21 23:56:14 -->
