# Documentation/Tools/Dedicated Server

## How to download a dedicated server

##### Game owner, using Steam client

Dedicated server can be downloaded via the Steam client. You can either search directly for application ID in your library tab

```
Euro Truck Simulator 2 Dedicated Server ID = 1948160
American Truck Simulator Dedicated Server ID = 2239530
```

or you can find it among listed tools. To show tools in the Steam library, you have to adjust steam filters (combo box above search field in library tab).

##### Anonymous, without game ownership, or without Steam Client

If you are not game owner or you don't have the Steam client installed, you have to use [SteamCMD](https://developer.valvesoftware.com/wiki/SteamCMD) to download server. **Remember that SteamCMD does not auto-update your server.**

## How to launch a dedicated server

You can launch the dedicated server either from the Steam client's library tab, or directly by starting its executable. Game ownership is not required. If you want to launch a server with different configuration, you can use the following startup parameters:

```
-server "server packages file name" (loads non default server game setup)
-server_cfg "server config file name" (loads non default server configuration)
-homedir "path" (redirects game/server home directory on Windows, use XDG_DATA_HOME environment for the same thing on Linux)
-nosingle (enables multiple instances of server, will be default in next patch)
```

If you have redirected home directory for the game (location where server_config, server.log, game.log, server_packages are stored), you have to redirect server home directory as well (this is done with -homedir parameter).

### How to launch a dedicated server on Linux without Steam client installed

You may get the following error when starting a server with Linux: `[S_API FAIL] SteamAPI_Init() failed; unable to locate a running instance of Steam, or a local steamclient.dll.` To launch server on Linux `steamclient.so` library is required. You can either use provided server_launch.sh script (located in folder next to the server executable) or create a link to this library using `ln -s steamcmd/linux64/steamclient.so ~/.steam/sdk64/steamclient.so`

## First launch

First launch will create server home folder and default server_config.sii.

By default server home directory is configured to point at the [Game User Path](../Engine/Game%20user%20path.md).

This location can be changed with -homedir start up parameter, however it must be changed for both game and server.

Next you will receive following error: "&lt;ERROR&gt; [MP] Error: Server packages file not found. This is required to load proper map, DLCs and mods". This means, you have to provide additional server configuration according to following steps.

## Required files to run dedicated server

In the server/game home folder the following files are used to set up a dedicated server session:

**server_config.sii**

- contains session description and configuration, connections ports info, logon token and list of moderators
- ports and logon token must be different for each session instance running at the same time
- default configuration, which is generated automatically on first launch

**server_packages.sii**

- contains map details, dlc and mods configuration

**server_packages.dat**

- contains internal map data

server_packages.sii and server_packages.dat must be generated manually via calling the `export_server_packages` command while normal game is running. Generated configuration will mirror your game configuration. These files are necessary for a dedicated server to start. If you are running a server without the base game installed on it, you have to manually copy these files to the server home directory.

These files are NOT linked to your account in any way.

## How to export server_packages

In config.cfg (found in game home directory) enable game console - uset g_console "1". When game is running press `~` to open game console and run `export_server_packages` or `export_server_packages destination file` command. server_packages.sii will be generated in the game home folder. It is necessary for map to be loaded when this command is called. This will generate server_packages.sii and server_packages.dat. These files carry dlc and mod configuration based on your current game setup.

## Running server without game installed

After first launch server home directory will be created. It will contain server.log.txt and server_config.sii. You have to provide generated server_packages.sii and server_packages.dat to this location.

## Data requirements

Dedicated server does not require any additional DLC or mod data. Everything needed is handled via server_packages.sii and server_packages.dat files. It is not required to copy any additional files. As the dedicated server does not use the Steam Client, it cannot access the workshop.

## Network address translation (NAT)

Dedicated server does not handle NAT punching and public IP or port forwarding is required to show server in session browser. However, session direct search works even for server that is behind NAT and it is possible to connect to such server.

Search id is listed when dedicated server starts or in convoy info screen for hosted sessions. To search for a server use search field in game server browser.

## Ports setup

**connection_virtual_port** and **query_virtual_port** are virtual ports used for connection to server. Allowed range is <100,200>.

**connection_dedicated_portand** and **query_dedicated_port** are physical ports used by the Steam game server api to fill sessions browser. For LAN games query_dedicated_port has be in range of <27015,27020>.

For port forwarding both TPP/IP and UPD rules are required. Virtual ports do not need forwarding.

## Server logon token

By default, whenever a dedicated server is launched it is using an anonymous account. For such an account non-persistent server id is generated (used for direct search). To avoid this you can acquire a logon token on [https://steamcommunity.com/dev/managegameservers](https://steamcommunity.com/dev/managegameservers) (game ownership is required). This token has to be placed into server_config.

Use the game appID to generate token, not the server appID!

Example:

```
server_logon_token: 6544F7E034119F113526E96474F
```

## Session moderators

As the dedicated server does not have any form or user interface, it is not possible to promote any player to a moderator while the session is running. You can register moderators in server_config using their steam_id to automatically promote them once they join the session.

Example for two moderators:

```
moderator_list: 2
moderator_list[0]: 123456789
moderator_list[1]: 234567891
```

where 123456789 is the moderator's Steam id

## Quality of life

Any player who is a moderator can now change the game time or disable rain. This can be done via chat message box by sending a message containing an admin command. Available admin commands are

```
/set_time <HH:MM>
/set_rain_factor <value from 0 to 1>
/help
```

## How to close server

Press Ctrl + C.

## Troubleshooting

In server home folder server.log.txt and server.crash.txt (when server crashes) files can be found to help solve any issue with a dedicated server.

## Known issues

When server is closed with message:

```
[MP] Steam disconnected
[MP] Session closure requested (reason - 33).
[MP] Session closing
```

It is caused by Steam losing connection. This can happen when internet connection is lost, or when the computer switches to sleep mode. Will be fixed in next patch.

## Server config paramaters

```
 lobby_name: "Euro Truck Simulator 2 server"            // Session name, limited to 63 characters.
 description: ""                                        // Session description, limited to 63 characters.
 welcome_message: ""                                    // Session welcome message, limited to 127 characters.
 password: ""                                           // Session password, limited to 63 characters.
 max_players: 8                                         // Maximum players in session, limit is 8 players.
 max_vehicles_total: 100
 max_ai_vehicles_player: 50
 max_ai_vehicles_player_spawn: 50
 connection_virtual_port: 100
 query_virtual_port: 101
 connection_dedicated_port: 27015
 query_dedicated_port: 27016
 server_logon_token: 6544F7E034119F113526E96474F        // Token for game server login (persistent account).
 player_damage: true                                    // Flag if player can receive damage from other players.
 traffic: true                                          // Flag if traffic is enabled.
 hide_in_company: false                                 // Flag if remote player are hidden in company area.
 hide_colliding: true                                   // Flag to hide colliding vehicle after teleport.
 force_speed_limiter: false                             // Flag to force speed limiter.
 mods_optioning: false                                  // Flag to enable mods marked as optional, to be really optional.
 timezones: 2                                           // Values 0 - 2.
 service_no_collision: false                            // Disable collisions on service area.
 in_menu_ghosting: false                                // Disable collisions when game paused.
 name_tags: true                                        // Show player name tags above vehicles.
 friends_only: false                                    // Not used for dedicated server.
 show_server: true                                      // Not used for dedicated server.
 moderator_list: 2                                      // Default moderators.
 moderator_list[0]: 123456789                           // User steam id.
 moderator_list[1]: 234567891                           // User steam id.
```

<!-- source: https://modding.scssoft.com/wiki/Documentation/Tools/Dedicated_Server | revision: 5329 | captured: 2026-10-21 23:56:14 -->
