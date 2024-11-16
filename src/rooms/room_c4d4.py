from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Room_C4D4:
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
        wall = "blocks/32x32_brick_wall.png"
        water = "blocks/32x32_water-1.png"
        water_shrine = "blocks/32x32_shrine.png"
        pit = ""
        empty = ""

        self.dark_bool = False

        # Corner Blocks
        self.corners = {
            "top": wall
        }

        # fmt: off
        self.ground_plane =  [
            [ground, ground, ground, pit, pit, ground, ground, ground, ground, ground, pit, pit, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, pit, pit, ground, ground, ground, ground, ground, pit, pit, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, pit, pit, pit, pit, pit, pit, pit, pit, pit, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, pit, pit, pit, pit, pit, pit, pit, pit, pit, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, water, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, water, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, water, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, water, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, water, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground]
        ]

        self.objects_plane =  [
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, wall, wall, wall, empty, wall, empty, wall, wall, wall, wall, wall, wall, wall, wall, wall, empty, wall, wall],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, wall, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, water_shrine, empty, empty, empty, empty, wall, empty, wall, wall, empty, wall, wall, empty, wall, wall, wall, wall, wall, wall, empty, wall, empty, wall, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, wall, wall, empty, wall, wall, wall, wall, empty, wall, wall, empty, wall, empty, wall, wall, wall, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, wall, empty, empty, empty, wall, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, wall, empty, wall, wall, wall, wall, wall, wall, empty, wall, empty, wall, wall, wall, empty, wall, wall],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, wall, empty, empty, empty, empty, wall, empty, wall, empty, wall, wall, wall, empty, wall, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, wall, wall, empty, wall, empty, wall, wall, wall, wall, empty, wall, empty, empty, empty, wall, empty, wall, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, wall, wall, empty, wall, empty, wall, empty, empty, empty, empty, wall, wall, wall, empty, wall, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, wall, empty, wall, wall, empty, wall, empty, empty, empty, wall, empty, wall, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, wall, wall, empty, wall, empty, wall, empty, wall, wall, wall, wall, empty, wall, wall, wall, empty, wall, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, wall, wall, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            ]
        # fmt: on

        self.right_wall_plane = {"type": wall, "width": 15, "height": 10}

        self.left_wall_plane = {"type": wall, "width": 15, "height": 10}

        self.doors_plane = [
            {
                "type": "door",
                "position": "front",
                "direction": "right",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (30, 7),
                "spawn_coords": (30, 7),
                "id": "d4-e4",
                "target": "Room_E4",
            },
            {
                "type": "door",
                "position": "back",
                "direction": "left",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (7, -1),
                "spawn_coords": (7, 0),
                "id": "c4-c5",
                "target": "Room_C5C6",
            },
            {
                "type": "door",
                "position": "back",
                "direction": "right",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (-1, 6),
                "spawn_coords": (0, 6),
                "id": "b4-c4",
                "target": "Room_B3B4",
            },
        ]
