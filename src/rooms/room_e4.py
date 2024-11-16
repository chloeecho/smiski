from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Room_E4:
    _game: "Game"
    ground_plane: list[list[str]]
    objects_plane: list[list[str]]
    left_wall_plane: dict[str, str | int]
    right_wall_plane: dict[str, str | int]
    corners: dict[str, str]
    dark_bool: bool
    # doors_plane:

    def __init__(self, game: "Game"):
        self._game = game

        ground = "blocks/32x32_brick_ground.png"
        wall = "blocks/32x32_brick_wall.png"
        water = "blocks/32x32_water-1.png"
        pit = ""
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
            [pit, pit, pit, pit, pit, ground, water, water, water, water, water, water, water, water, water],
            [pit, pit, pit, pit, pit, ground, water, water, water, water, water, water, water, water, water],
            [pit, pit, pit, pit, pit, ground, ground, ground, ground, ground, ground, ground, ground, water, water],
            [ground, ground, ground, ground, ground, pit, pit, pit, pit, pit, pit, pit, ground, water, water],
            [water, water, water, water, ground, pit, pit, pit, pit, pit, pit, pit, ground, water, water],
            [water, water, water, water, ground, ground, ground, ground, ground, ground, pit, pit, ground, water, water],
            [ground, ground, water, water, water, water, water, water, water, ground, pit, pit, ground, water, water],
            [ground, ground, water, water, water, water, water, water, water, ground, pit, pit, ground, water, water],
            [ground, ground, water, water, water, water, water, water, water, ground, pit, pit, ground, water, water],
            [water, water, water, water, ground, ground, water, water, water, ground, pit, pit, ground, ground, ground],
            [water, water, water, water, ground, ground, water, water, water, ground, ground, ground, pit, pit, pit],
            [ground, ground, ground, ground, water, water, water, water, water, water, water, ground, pit, pit, pit],
            [pit, pit, pit, ground, water, water, water, water, water, water, water, ground, pit, pit, pit],
            [pit, pit, pit, ground, water, water, ground, ground, ground, water, water, ground, pit, pit, pit],
            [pit, pit, pit, ground, water, water, ground, ground, ground, water, water, ground, pit, pit, pit]
        ]

        self.objects_plane =  [
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty]
        ]
        # fmt: on

        self.right_wall_plane = {"type": wall, "width": 15, "height": 10}

        self.left_wall_plane = {"type": wall, "width": 15, "height": 10}

        self.doors_plane = [
            {
                "type": "door",
                "position": "back",
                "direction": "right",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (-1, 7),
                "spawn_coords": (0, 7),
                "id": "d4-e4",
                "target": "Room_C4D4",
            },
            {
                "type": "door",
                "position": "front",
                "direction": "left",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (7, 14),
                "spawn_coords": (7, 14),
                "id": "e3-e4",
                "target": "Room_D3E3",
            },
        ]
