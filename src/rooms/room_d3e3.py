from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Room_D3E3:
    _game: "Game"
    ground_plane: list[list[str]]
    objects_plane: list[list[str]]
    left_wall_plane: dict[str, str | int]
    right_wall_plane: dict[str, str | int]
    corners: dict[str, str]
    # doors_plane:
    dark_bool: bool
    # doors_plane:

    def __init__(self, game: "Game"):
        self._game = game

        ground = "blocks/32x32_brick_ground.png"
        grass = "blocks/32x32_grass.png"
        wall = "blocks/32x32_brick_wall.png"
        water = "blocks/32x32_water-1.png"
        boulder = "blocks/32x32_boulder.png"
        punch_belt = "items/32x32_power_belt.png"
        key_green = "items/32x32_key_green.png"
        key_purple = "items/32x32_key_purple.png"
        empty = ""

        self.dark_bool = False

        # Corner Blocks
        self.corners = {
            # "bottom_left": "32x32_brick_wall.png",
            # "bottom_right": "32x32_brick_wall.png",
            "top": wall
        }

        # fmt: off
        self.ground_plane =  [
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, water, water],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, water, water, water],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, ground, ground, water, ground, ground, ground, ground, ground, water, water, water, grass, grass],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, ground, ground, water, ground, ground, ground, ground, ground, water, water, grass, grass, grass],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, ground, ground, water, ground, ground, ground, ground, ground, water, water, grass, grass, grass],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, ground, ground, water, ground, ground, ground, ground, ground, water, water, grass, grass, grass],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, ground, ground, water, ground, ground, ground, ground, ground, water, water, water, grass, grass],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, water, water, water],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, water, water],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground]
        ]

        self.objects_plane =  [
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, punch_belt, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, wall, empty, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, key_purple if self._game.create_surface(key_purple) not in self._game.inventory_service.items else empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, boulder, empty, empty, empty, empty, wall, wall, wall, wall, wall, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, wall, empty, empty, empty, wall, key_green, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, wall, empty, empty, empty, wall, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty]
        ]
        # fmt: on

        self.right_wall_plane = {"type": wall, "width": 15, "height": 10}

        self.left_wall_plane = {"type": wall, "width": 15, "height": 10}

        self.doors_plane = [
            {
                "type": "locked_green",
                "position": "back",
                "direction": "right",
                "sprites": "blocks/32x64_locked_brick_door_green.png",
                "coords": (-1, 6),
                "spawn_coords": (0, 6),
                "id": "c3-d3",
                "target": "Room_C3",
            },
            {
                "type": "locked_purple",
                "position": "front",
                "direction": "left",
                "sprites": "blocks/32x64_locked_brick_door_purple.png",
                "coords": (23, 14),
                "spawn_coords": (23, 14),
                "id": "e2-e3",
                "target": "Room_D2E2",
            },
            {
                "type": "one_way",
                "position": "back",
                "direction": "left",
                "sprites": "blocks/32x64_oneway_door.png",
                "coords": (23, -1),
                "spawn_coords": (23, 0),
                "id": "e3-e4",
                "target": "Room_E4",
            },
        ]
