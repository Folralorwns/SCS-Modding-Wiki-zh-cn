# Documentation/Tools/Dedicated Server

## 如何下载专用服务器

##### 游戏所有者，使用 Steam 客户端

专用服务器可以通过 Steam 客户端下载。你既可以在库标签页中直接搜索应用程序 ID

```
Euro Truck Simulator 2 Dedicated Server ID = 1948160
American Truck Simulator Dedicated Server ID = 2239530
```

也可以在列出的工具中找到它。要在 Steam 库中显示工具，你必须调整 Steam 筛选器（库标签页搜索框上方的组合框）。

##### 匿名，无游戏所有权，或未安装 Steam 客户端

如果你不是游戏所有者，或未安装 Steam 客户端，则必须使用 [SteamCMD](https://developer.valvesoftware.com/wiki/SteamCMD) 下载服务器。**请记住，SteamCMD 不会自动更新你的服务器。**

## 如何启动专用服务器

你可以从 Steam 客户端的库标签页启动专用服务器，也可以直接启动其可执行文件。无需游戏所有权。如果你想以不同的配置启动服务器，可以使用以下启动参数：

```
-server "server packages file name" (loads non default server game setup)
-server_cfg "server config file name" (loads non default server configuration)
-homedir "path" (redirects game/server home directory on Windows, use XDG_DATA_HOME environment for the same thing on Linux)
-nosingle (enables multiple instances of server, will be default in next patch)
```

如果你已重定向游戏的主目录（即存储 server_config、server.log、game.log、server_packages 的位置），那么你也必须重定向服务器的主目录（通过 -homedir 参数完成）。

### 如何在未安装 Steam 客户端的情况下在 Linux 上启动专用服务器

在 Linux 上启动服务器时，你可能会遇到以下错误：`[S_API FAIL] SteamAPI_Init() failed; unable to locate a running instance of Steam, or a local steamclient.dll.` 在 Linux 上启动服务器需要 `steamclient.so` 库。你可以使用提供的 server_launch.sh 脚本（位于服务器可执行文件旁边的文件夹中），或使用 `ln -s steamcmd/linux64/steamclient.so ~/.steam/sdk64/steamclient.so` 创建指向该库的链接。

## 首次启动

首次启动会创建服务器主文件夹与默认的 server_config.sii。

默认情况下，服务器主目录被配置为指向[游戏用户路径](../Engine/Game%20user%20path.md)。

此位置可以通过 -homedir 启动参数更改，但必须为游戏和服务器同时更改。

接下来你会收到以下错误：“&lt;ERROR&gt; [MP] Error: Server packages file not found. This is required to load proper map, DLCs and mods”。这意味着你必须按照以下步骤提供额外的服务器配置。

## 运行专用服务器所需的文件

在服务器/游戏主文件夹中，以下文件用于设置专用服务器会话：

**server_config.sii**

- 包含会话描述与配置、连接端口信息、登录令牌以及管理员列表
- 端口与登录令牌对于同时运行的每个会话实例必须不同
- 默认配置，在首次启动时自动生成

**server_packages.sii**

- 包含地图详情、DLC 与模组配置

**server_packages.dat**

- 包含内部地图数据

server_packages.sii 与 server_packages.dat 必须在正常游戏运行时通过调用 `export_server_packages` 命令手动生成。生成的配置会与你的游戏配置保持一致。这些文件是专用服务器启动所必需的。如果你在未安装基础游戏的机器上运行服务器，则必须手动将这些文件复制到服务器主目录。

这些文件与你的账户没有任何关联。

## 如何导出 server_packages

在 config.cfg（位于游戏主目录）中启用游戏控制台：uset g_console "1"。游戏运行时按 `~` 打开游戏控制台，并运行 `export_server_packages` 或 `export_server_packages destination file` 命令。server_packages.sii 会生成在游戏主文件夹中。调用此命令时必须已加载地图。这将生成 server_packages.sii 与 server_packages.dat。这些文件会根据你当前的游戏设置携带 DLC 与模组配置。

## 在未安装游戏的情况下运行服务器

首次启动后会创建服务器主目录。其中会包含 server.log.txt 与 server_config.sii。你必须将生成的 server_packages.sii 与 server_packages.dat 放到此位置。

## 数据要求

专用服务器不需要任何额外的 DLC 或模组数据。所有需要的内容都通过 server_packages.sii 与 server_packages.dat 文件处理。无需复制任何额外文件。由于专用服务器不使用 Steam 客户端，因此无法访问创意工坊。

## 网络地址转换（NAT）

专用服务器不处理 NAT 穿透，要在会话浏览器中显示服务器，需要公网 IP 或端口转发。不过，即使服务器位于 NAT 之后，会话直接搜索也能工作，并且可以连接到这样的服务器。

搜索 ID 会在专用服务器启动时列出，托管会话时也会显示在车队信息界面中。要搜索服务器，请使用游戏服务器浏览器中的搜索字段。

## 端口设置

**connection_virtual_port** 与 **query_virtual_port** 是用于连接服务器的虚拟端口。允许范围为 <100,200>。

**connection_dedicated_portand** 与 **query_dedicated_port** 是 Steam 游戏服务器 API 用于填充会话浏览器的物理端口。对于局域网游戏，query_dedicated_port 必须在 <27015,27020> 范围内。

端口转发需要同时具备 TPP/IP 与 UPD 规则。虚拟端口无需转发。

## 服务器登录令牌

默认情况下，专用服务器每次启动时都使用匿名账户。对此类账户会生成非持久化的服务器 ID（用于直接搜索）。要避免这种情况，你可以在 [https://steamcommunity.com/dev/managegameservers](https://steamcommunity.com/dev/managegameservers) 获取登录令牌（需要游戏所有权）。该令牌必须放入 server_config。

请使用游戏 appID 生成令牌，而不是服务器 appID！

示例：

```
server_logon_token: 6544F7E034119F113526E96474F
```

## 会话管理员

由于专用服务器没有任何形式的用户界面，因此无法在会话运行期间将任何玩家提升为管理员。你可以在 server_config 中使用玩家的 steam_id 注册管理员，以便他们在加入会话时自动提升为管理员。

两个管理员的示例：

```
moderator_list: 2
moderator_list[0]: 123456789
moderator_list[1]: 234567891
```

其中 123456789 是管理员的 Steam id

## 便利功能

任何作为管理员的玩家现在都可以更改游戏时间或禁用降雨。这可以通过聊天消息框发送包含管理命令的消息来完成。可用的管理命令如下：

```
/set_time <HH:MM>
/set_rain_factor <value from 0 to 1>
/help
```

## 如何关闭服务器

按 Ctrl + C。

## 故障排查

在服务器主文件夹中可以找到 server.log.txt 与 server.crash.txt（在服务器崩溃时生成）文件，有助于解决专用服务器的任何问题。

## 已知问题

当服务器关闭并显示以下消息时：

```
[MP] Steam disconnected
[MP] Session closure requested (reason - 33).
[MP] Session closing
```

这是由 Steam 断开连接导致的。当互联网连接丢失，或计算机进入睡眠模式时可能发生。将在下一个补丁中修复。

## 服务器配置参数

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
