# 文档/引擎/游戏电台

## 文件结构

游戏电台的基本结构。

此处未展示电台图形文件，因为它们是可选的。

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

支持的音频格式：`ogg`、`mp3`

出于组织管理的考虑，建议使用单独的子文件夹 `offline_radio/stationid/music`；但请注意，对于曲目，你指定的是完整的游戏文件系统路径，因此这种组织结构是可选的；原则上音频文件可以位于任意位置，甚至可以在多个电台之间共享。

## 单元说明

### 电台的定义

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

#### 曲目选择与播放历史

由于我们不希望同一首曲目播放得过于频繁，电台的曲目选择会受到播放历史的影响。

该过程由电台定义中的 2 个值控制：

- `recently_played_history_size_fraction` 决定“历史窗口”的大小，在该窗口内已经播放过的曲目不能作为下一首曲目播放。因此，如果该值为 `0.5` 且电台有 20 首曲目，那么当前歌曲再次播放之前，至少要播放 10 首其他歌曲。
- `min_num_tracks_between_same_artist` 在此基础上进一步防止同一艺人播放得过于频繁。请注意，这仅是对曲目之间 `artist` 值的简单比较，因此 `"Artist"` 与 `"Artist feat. Someone else"` 是不同的，`"Artist"` 与 `"ARTIST"` 也是不同的。

选择这些值时请保持合理：限制过于严格会导致曲目选择过程无法正常工作。

### 各电台的定义

`offline_radio/<my_station_id>/tracks.sii` - 提供电台各个曲目的数据。

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

## 已知限制

目前压缩音频资源存在问题，因此不支持使用 `.zip` 模组格式。请使用 `.scs` 包或普通文件夹。

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Game_Radio | revision: 5769 | captured: 2026-10-21 23:56:14 -->
