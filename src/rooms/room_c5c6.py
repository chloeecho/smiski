from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Room_C5C6:
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
        smiski = "items/32x32_smiski_statue.png"
        water = "blocks/32x32_water-1.png"
        idol = "items/32x32_idol.png"
        pit = ""
        door = ""
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
            [ground, ground, ground, ground, water, grass, grass, grass, water, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, grass, water, grass, water, grass, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, water, water, water, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, water, water, water, ground, ground, ground, ground, ground, ground, ground],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, water, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, water, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, water, water, water, pit, pit],
            [pit, water, water, pit, pit, pit, pit, pit, pit, pit, pit, pit, water, pit, pit],
            [pit, water, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, water, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, water, water, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, water, water, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, water, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, water, water, water],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, water, water, water],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, water, water, water],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, ground, ground, ground, ground, ground, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, ground, ground, ground, ground, ground, pit, pit, pit, pit, pit],
        ]

        self.objects_plane =  [
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, smiski, empty, idol, empty, smiski, empty, empty, empty, empty, empty, empty],
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

        self.left_wall_plane = {"type": wall, "width": 31, "height": 10}

        self.doors_plane = [
            {
                "type": "door",
                "position": "front",
                "direction": "left",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (7, 30),
                "spawn_coords": (7, 30),
                "id": "c4-c5",
                "target": "Room_C4D4",
            },
        ]
