# Documentation/Engine/Sound/Mixer

### Audio buses, routing and mixer

The definition of the sound buses and their routing is a very important part of the Master Bank.

- Master Bus<br>The master bus creates the final submix of all buses routed to it before outputting audio to the speaker channels.<br>All buses, return buses, and events not assigned to a group are routed into the master bus.
- Bus<br>The bus is an object which helps to collect specific sounds to groups and centrally control their volume or mute state.<br>Any sound event in the game should be assigned to the corresponding prepared audio bus.
- Routing<br>Routing the events and buses by the mixer helps to control specific sounds in groups and applying effects (as a reverb) for the whole group of the sounds together.

Current table describes mixer principles in our Master Bank:

| Bus | Routing to... | Using for sounds... | Remark |
| --- | --- | --- | --- |
| master |  | *- none -* | Target for the central mixing of all other audio buses.<br>"Master" volume and mute state (from application settings) is applied to the bus. |
| <--- cabin | *master* | *- none -* |  |
| .....<--- interior | *cabin* | Individual truck interior sounds as for example:<br>air warning, blinkers, sticks, park brake, wipers, windows, seat noise... |  |
| .....<--- window_left | *cabin* | *- none -* |  |
| .....<--- window_right | *cabin* | *- none -* |  |
| .....<--- window_out | *cabin* | *- none -* |  |
| <--- outside | *master* | *- none -* | The bus should not contents any sounds. It is only technically group to collect all sounds from the outer world. |
| ...<--- exterior | *outside* | *- none -* | The bus should not contents any sounds. It is only technically group to collect all exterior sounds. |
| .....<--- traffic | *exterior* | Sounds of the traffic system. |  |
| .....<--- trailer | *exterior* | Player's trailer sounds. |  |
| .....<--- truck_effects | *exterior* | Player's truck effects<br>(air cutoff, air gear, hook, horns, reverse, ...). |  |
| .....<--- truck_engine | *exterior* | Player's truck engine.<br>([see: Sounds - Truck Engine](TruckEngine.md)) |  |
| .....<--- truck_exhaust | *exterior* | Player's truck exhaust.<br>([see: Sounds - Truck Engine](TruckEngine.md)) |  |
| .....<--- truck_turbo | *exterior* | Player's truck turbo.<br>([see: Sounds - Truck Engine](TruckEngine.md)) |  |
| .....<--- truck_noise | *exterior* | Player's truck noise<br>(aero noise, suspension noise, ...). |  |
| .....<--- world | *exterior* | Prefab sounds, sounds of animations... |  |
| ...<--- unprocessed | *outside* | *- none -* | The bus should not contents any sounds. It is only technically group to collect all exterior sounds which are not affected by sound processing (like reverb). |
| .....<--- ambient | *unprocessed* | Ambient and environmental sounds and effects. |  |
| <--- game | *master* | *- none -* |  |
| .....<--- music | *game* | In-game music (as a 'hurry up' melody). |  |
| .....<--- navigation | *game* | Voice navigation output. |  |
| .....<--- ui | *game* | Sounds of the user interface<br>(click, mail, reward, camera, ...). |  |
| .....<--- ui_music | *game* | Music for UI (menu, garage, service, ...). |  |
| .....<--- voiceover | *game* | Reserved for the future use. |  |
| <--- radio | *master* | Output for the in-game radio (user music) player. |  |

<!-- source: https://modding.scssoft.com/wiki/Documentation/Engine/Sound/Mixer | revision: 5167 | captured: 2026-10-21 23:56:14 -->
