from typing import TYPE_CHECKING

import numpy as np
import pygame

from rooms.room_a3a4 import Room_A3A4
from rooms.room_b3b4 import Room_B3B4
from rooms.room_c1c2 import Room_C1C2
from rooms.room_c3 import Room_C3
from rooms.room_c4d4 import Room_C4D4
from rooms.room_c5c6 import Room_C5C6
from rooms.room_d2e2 import Room_D2E2
from rooms.room_d3e3 import Room_D3E3
from rooms.room_e4 import Room_E4

if TYPE_CHECKING:
    from main import Game

Blit = tuple[pygame.Surface, tuple[float, float]]
Room = (
    Room_A3A4
    | Room_B3B4
    | Room_C1C2
    | Room_C3
    | Room_C4D4
    | Room_C5C6
    | Room_D2E2
    | Room_D3E3
    | Room_E4
)


class RoomService:
    _game: "Game"
    _background_color: tuple[int, int, int]
    _blits_background: list[Blit]
    _blits_above: list[Blit]
    _blits_below: list[Blit]
    _low_objects: list[str]

    dark: bool
    torch: bool
    torch_size: int
    current_room: Room
    cover: pygame.Surface
    rooms_dict: dict[str:Room]
    map_size: tuple[int, int, int]
    room: dict[str, pygame.Surface]

    def __init__(self, game: "Game"):
        self._game = game

        self.torch = (
            True
            if self._game.create_surface("items/32x32_torch.png")
            in self._game.inventory_service.items
            else False
        )
        self.torch_size = 5

        self._background_color = self._game.config["background_color"]

        self.rooms_dict = {
            "Room_A3A4": Room_A3A4(self._game),
            "Room_B3B4": Room_B3B4(self._game),
            "Room_C1C2": Room_C1C2(self._game),
            "Room_C3": Room_C3(self._game),
            "Room_C4D4": Room_C4D4(self._game),
            "Room_D2E2": Room_D2E2(self._game),
            "Room_D3E3": Room_D3E3(self._game),
            "Room_E4": Room_E4(self._game),
            "Room_C5C6": Room_C5C6(self._game),
        }

        self.cover = pygame.Surface(self._game.config["screen_size"], pygame.SRCALPHA)
        self.cover.fill((0, 0, 0, 150))
        self._load_room(self.rooms_dict["Room_C3"], (4, 4))

    def _load_room(self, room: Room, spawn: tuple[int, int]):
        """Loads a new room
            Args: Room, tuple[int, int]

        Sets instance variables
        """
        self.current_room = room

        self.dark = self.current_room.dark_bool

        self.map_size = (
            len(self.current_room.ground_plane[0]),
            len(self.current_room.ground_plane),
            self.current_room.left_wall_plane["height"],
        )
        self._game.coordinate_service.set_map_size(self.map_size)

        create_surface = self._game.create_surface

        self.room = {
            "floor": [
                [
                    create_surface(self.current_room.ground_plane[y][x])
                    for x in range(self.map_size[0])
                ]
                for y in range(self.map_size[1])
            ],
            "objects": [
                [
                    create_surface(self.current_room.objects_plane[y][x])
                    for x in range(self.map_size[0])
                ]
                for y in range(self.map_size[1])
            ],
            "left_wall": create_surface(self.current_room.left_wall_plane["type"]),
            "right_wall": create_surface(self.current_room.right_wall_plane["type"]),
            "coords": create_surface(self.current_room.corners["top"]),
            "doors": self._gen_doors(),
        }

        self._blits_above = self._load_blits()[0]
        self._blits_below = self._load_blits()[1]
        self._blits_background = self._load_bg()

        old_pos = self._game.movement_service.position

        self._game.movement_service.position = np.array((spawn[0], spawn[1]))
        self._game.movement_service._has_moved = True
        self._game.camera_service.update_camera(
            self._game.movement_service.position, old_pos
        )

        if self.dark and not self.torch:
            self._game.interaction_service.door(self.current_room.doors_plane[0])
            dialog_service = self._game.dialog_service
            too_dark = dialog_service.DialogItem.TOO_DARK_ERROR

            dialog_service.show_dialog(too_dark)

    def _gen_doors(self) -> list[pygame.Surface]:
        """Generates a list of Surfaces for the doors

        Returns:
            list[pygame.Surface]: list of surfaces for the doors
        """

        door_list = []

        for i in range(len(self.current_room.doors_plane)):
            door = self.current_room.doors_plane[i]

            door_surface = self._game.create_surface(
                door["sprites"],
                scale=(
                    self._game.config["scale_factor"] * 32,
                    self._game.config["scale_factor"] * 64,
                ),
            )

            if door["direction"] == "left":
                door_surface = pygame.transform.flip(
                    door_surface, flip_x=True, flip_y=False
                )

            door_list.append(door_surface)

        return door_list

    def _load_bg(self):
        """Generates the background blits for the current room

        Returns:
            list[Blit]: the blits for the background pieces
        """

        coord_func = self._game.coordinate_service.cartesian_to_isometric
        distance_from = self._game.movement_service.distance_from
        create_blit = self._game.create_blit

        # Create blit functions for both the floor and the wall
        wall_blit = create_blit(self.room["coords"], coord_func)

        # Fill in the top corner blit - contains the blits for all background pieces.
        coords_back = [
            wall_blit(-1, -1, self.map_size[2] - 1),
        ]

        # Generate the blits for the floor and walls
        # Iterates through the wall area and appends blits to coords list
        for z in range(0, self.map_size[2]):
            # Right wall
            for x in range(self.map_size[0]):
                if (
                    self.dark
                    and self.torch
                    and (distance_from((x, -1, z)) > self.torch_size)
                ):
                    continue

                coords_back.append(wall_blit(x, -1, z))

            # Left wall
            for y in range(self.map_size[1]):
                if (
                    self.dark
                    and self.torch
                    and (distance_from((-1, y, z)) > self.torch_size)
                ):
                    continue

                coords_back.append(wall_blit(-1, y, z))

        # Iterates through the floor tile list
        for y in range(self.map_size[1]):
            for x in range(self.map_size[0]):
                if (
                    self.dark
                    and self.torch
                    and (distance_from((x, y, 0)) > self.torch_size)
                ):
                    continue

                # Appends blits to coords list
                if self.room["floor"][y][x] is not None:
                    floor_blit = create_blit(self.room["floor"][y][x], coord_func)
                    coords_back.append(floor_blit(x, y, 0))

        # Generates door blits
        for i in range(len(self.room["doors"])):
            door = self.current_room.doors_plane[i]
            coords = door["coords"]

            if (
                self.dark
                and self.torch
                and (distance_from((*coords, 1)) > self.torch_size)
            ):
                continue

            if door["position"] == "back":
                door_surface = self.room["doors"][i]
                door_surface_blit = create_blit(door_surface, coord_func)
                coords_back.append(door_surface_blit(*door["coords"], 3))

        return coords_back

    def _load_blits(self) -> tuple[list[Blit], list[Blit]]:
        """Generates the object blits for the current room

        Returns:
            tuple[list[Blit], list[Blit]]: the blits for the current room in front of
            and behind the player
        """

        coord_func = self._game.coordinate_service.cartesian_to_isometric
        create_blit = self._game.create_blit

        movement_service = self._game.movement_service
        distance_from = movement_service.distance_from
        player_pos = movement_service.position

        # This contains all the blits for all the objects behind the player
        coords_below = []

        # This contains the blits for all the objects in front of the player
        coords_above = []

        # Iterates through room tile list
        for y in range(self.map_size[1]):
            for x in range(self.map_size[0]):
                if (
                    self.dark
                    and self.torch
                    and (distance_from((x, y, 1)) > self.torch_size)
                ):
                    continue

                # Appends blits to coords lists
                if self.room["objects"][y][x] is not None:
                    objects_blit = create_blit(self.room["objects"][y][x], coord_func)

                    # If the object is in front of the player, render it on top
                    if (x >= player_pos[0] and y >= player_pos[1]) and not (
                        x == player_pos[0] and y == player_pos[1]
                    ):
                        coords_above.append(objects_blit(x, y, 1))
                    else:
                        coords_below.append(objects_blit(x, y, 1))

        # Generates door blits
        for i in range(len(self.room["doors"])):
            door = self.current_room.doors_plane[i]
            coords = door["coords"]

            if (
                self.dark
                and self.torch
                and (distance_from((*coords, 1)) > self.torch_size)
            ):
                continue

            if door["position"] == "front":
                door_surface = self.room["doors"][i]
                door_surface_blit = create_blit(door_surface, coord_func)
                coords_above.append(door_surface_blit(*coords, 3))

        return (coords_above, coords_below)

    def render(self):
        """Generates the new blits and applies them to the window"""

        # If the room is dark and the player has no torch, don't render anything
        if self.dark and not self.torch:
            return self._game.window.fill((0, 0, 0))

        blits = self._load_blits()
        self._blits_above = blits[0]
        self._blits_below = blits[1]

        self._blits_background = self._load_bg()

        # Render the highlight on top of the room, and the player at the very top
        movement_blits = self._game.movement_service.update()
        blits = (
            self._blits_background
            + movement_blits[0]
            + self._blits_below
            + movement_blits[1]
            + self._blits_above
        )

        # Set the background color and apply the new blits
        self._game.window.fill(self._background_color)
        self._game.window.blits(blits)

        # Render the inventory if it is active
        if self._game.inventory_service.active:
            self._game.inventory_service.render_inventory()

        if self.dark:
            self._game.window.blit(self.cover, (0, 0))
