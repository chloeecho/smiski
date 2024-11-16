import os
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from main import Game


class InteractionService:
    _game: "Game"

    def __init__(self, game: "Game"):
        self._game = game
        self.smiski = False
        self.smiskis_placed = 0

    def handle_click(self, pos: tuple[int, int]):
        """Handle a click on the screen

        Args:
            pos (tuple[int, int]): the coordinates for the click
        """

        if self._game.movement_service.distance_from(pos) > 2:
            return

        objects = self._game.room_service.room["objects"]
        objects_floor_plan = self._game.room_service.current_room.objects_plane

        floor = self._game.room_service.room["floor"]

        create_surface = self._game.create_surface
        surface = objects[pos[1]][pos[0]]

        # check if the player is interacting with a door and handle it accordingly
        for x in self._game.room_service.current_room.doors_plane:
            if list(x["spawn_coords"]) == list(pos)[0:2]:
                if x["type"] != "door" and x["type"] != "one_way":
                    color = x["type"].split("_")[1]

                    if (
                        self._game.create_surface(f"items/32x32_key_{color}.png")
                        in self._game.inventory_service.items
                    ):
                        self.door(x)
                    else:
                        dialog_service = self._game.dialog_service
                        missing_key = dialog_service.DialogItem.MISSING_KEY_ERROR

                        dialog_service.show_dialog(missing_key)
                elif x["type"] == "door":
                    self.door(x)

        # map of all interactable items
        interactable_item = map(
            create_surface,
            [
                "items/32x32_amulet_left.png",
                "items/32x32_amulet_right.png",
                "items/32x32_key_blue.png",
                "items/32x32_key_green.png",
                "items/32x32_key_purple.png",
                "items/32x32_key_red.png",
                "items/32x32_power_belt.png",
                "items/32x32_torch.png",
                "items/32x32_smiski_statue.png",
            ],
        )

        # map of all interactable blocks
        interactable_block = map(
            create_surface,
            [
                "blocks/32x32_shrine.png",
                "blocks/32x32_empty.png",
            ],
        )

        amulet_left = create_surface("items/32x32_amulet_left.png")
        amulet_right = create_surface("items/32x32_amulet_right.png")
        full_amulet = create_surface("items/32x32_full_amulet.png")

        inventory_service = self._game.inventory_service
        has_right = amulet_right in inventory_service.items
        has_left = amulet_left in inventory_service.items

        # check which item was interacted with and handle it
        if surface in list(interactable_item):
            if surface == amulet_left and has_right:
                inventory_service.remove_item(amulet_right)
                inventory_service.add_item(full_amulet)
                objects[pos[1]][pos[0]] = None
            elif surface == amulet_right and has_left:
                inventory_service.remove_item(amulet_left)
                inventory_service.add_item(full_amulet)
                objects[pos[1]][pos[0]] = None

            elif surface == create_surface("items/32x32_smiski_statue.png") and (
                not self.smiski
                and not floor[pos[1]][pos[0]]
                == create_surface("blocks/32x32_water_ripple1.png")
            ):
                objects[pos[1]][pos[0]] = None

                self.smiski = True
            elif surface != create_surface("items/32x32_smiski_statue.png"):
                if surface == create_surface("items/32x32_torch.png"):
                    self._game.room_service.torch = True

                inventory_service.add_item(surface)
                sound_path = os.path.join("assets/audio", "add_item.wav")
                sound = pygame.mixer.Sound(sound_path)
                sound.set_volume(self._game.config["soundfx_vol"])

                # Play the sound on the separate channel
                pygame.mixer.Channel(4).play(sound)
                objects[pos[1]][pos[0]] = None
                objects_floor_plan[pos[1]][pos[0]] = ""

        elif surface in list(interactable_block):
            if surface == create_surface("blocks/32x32_shrine.png"):
                inventory_service.add_item(create_surface("items/32x32_blessing.png"))

                # Play sound
                sound_path = os.path.join("assets/audio", "blessing.wav")
                sound = pygame.mixer.Sound(sound_path)
                sound.set_volume(self._game.config["soundfx_vol"] / 4)

                # Play the sound on the separate channel
                pygame.mixer.Channel(5).play(sound)
            elif self.smiski:
                objects[pos[1]][pos[0]] = create_surface(
                    "items/32x32_smiski_statue.png"
                )

                self.smiskis_placed += 1
                self.smiski = False

                if self.smiskis_placed == 4:
                    self.retract_walls(True)

                # Play sound
                sound_path = os.path.join("assets/audio", "blessing.wav")
                sound = pygame.mixer.Sound(sound_path)
                sound.set_volume(self._game.config["soundfx_vol"] / 4)

                # Play the sound on the separate channel
                pygame.mixer.Channel(5).play(sound)

    def retract_walls(self, toggle: bool):
        """Switches retractable walls when pressed by boulder

        Args:
            toggle (bool): whether to switch the walls or not
        """

        create_surface = self._game.create_surface
        objects = self._game.room_service.room["objects"]

        retractable_indices = []
        retracted_indices = []

        for i in range(len(objects)):
            for j in range(len(objects[i])):
                if objects[i][j] == create_surface("blocks/32x32_retractable_wall.png"):
                    retractable_indices.append((i, j))

                if objects[i][j] == create_surface("blocks/32x32_retracted_wall.png"):
                    retracted_indices.append((i, j))

        if toggle:
            dialog_service = self._game.dialog_service
            retract_dialog = dialog_service.DialogItem.WALLS_RETRACTED

            dialog_service.show_dialog(retract_dialog)

            for n in range(len(retractable_indices)):
                objects[retractable_indices[n][0]][retractable_indices[n][1]] = (
                    create_surface("blocks/32x32_retracted_wall.png")
                )

            for n in range(len(retracted_indices)):
                objects[retracted_indices[n][0]][retracted_indices[n][1]] = (
                    create_surface("blocks/32x32_retractable_wall.png")
                )
        else:
            for n in range(len(retractable_indices)):
                objects[retractable_indices[n][0]][retractable_indices[n][1]] = (
                    create_surface("blocks/32x32_retractable_wall.png")
                )

            for n in range(len(retracted_indices)):
                objects[retracted_indices[n][0]][retracted_indices[n][1]] = (
                    create_surface("blocks/32x32_retracted_wall.png")
                )

        sound_path = os.path.join("assets/audio", "hydraulic.wav")
        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(self._game.config["soundfx_vol"])
        pygame.mixer.Channel(7).play(sound)

        self._game.room_service.render()

    def door(self, door: dict[str, str | tuple[int, int]]):
        """Loads the appropriate room for the interacted door

        Args:
            door (dict[str, str | tuple[int, int]]): the door that was interacted with
        """

        door_id = door["id"]
        target = door["target"]
        spawn = (0, 0)

        room_service = self._game.room_service
        room = self._game.room_service.rooms_dict[target]

        for i in range(len(room.doors_plane)):
            if room.doors_plane[i]["id"] == door_id:
                spawn = room.doors_plane[i]["spawn_coords"]
                break

        room_service._load_room(room, spawn)
