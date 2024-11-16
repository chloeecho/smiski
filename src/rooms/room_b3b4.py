from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Room_B3B4:
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
        empty = ""
        plate = "blocks/32x32_pressed_plate.png"
        boulder = "blocks/32x32_boulder.png"
        wall_high = "blocks/32x32_retractable_wall.png"

        self.dark_bool = False

        # Corner Blocks
        self.corners = {
            "top": wall
        }

        # fmt: off
        self.ground_plane =  [
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
        ]

        self.objects_plane =  [
            [empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, wall, wall, wall, empty, empty, wall, empty, empty, empty, wall, wall, wall, empty, empty],
            [empty, empty, empty, wall, empty, empty, wall, empty, empty, empty, wall, empty, empty, empty, empty],
            [empty, empty, empty, wall, empty, empty, wall, empty, empty, empty, wall, empty, empty, empty, empty],
            [empty, empty, empty, wall, empty, empty, wall, empty, empty, empty, wall, empty, empty, empty, empty],
            [empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty],
            [empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty],
            [empty, empty, empty, wall, empty, empty, empty, empty, wall, wall, wall, wall, wall, wall, wall],
            [empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, empty, wall, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, wall, wall, wall, wall, empty, empty, empty],
            [wall_high, wall_high, wall_high, wall_high, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall, wall],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [wall, wall, wall, wall, wall, wall, wall, empty, empty, empty, wall, wall, wall, wall, wall],
            [empty, empty, empty, empty, empty, wall, wall, boulder, wall, wall, wall, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [boulder, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, wall, wall, wall, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [wall, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [plate, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
        ]
        # fmt: on

        self.right_wall_plane = {"type": wall, "width": 15, "height": 10}

        self.left_wall_plane = {"type": wall, "width": 31, "height": 10}

        self.doors_plane = [
            {
                "type": "door",
                "position": "back",
                "direction": "right",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (-1, 6),
                "spawn_coords": (0, 6),
                "id": "a4-b4",
                "target": "Room_A3A4",
            },
            {
                "type": "door",
                "position": "front",
                "direction": "right",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (14, 6),
                "spawn_coords": (14, 6),
                "id": "b4-c4",
                "target": "Room_C4D4",
            },
            {
                "type": "door",
                "position": "front",
                "direction": "right",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (14, 23),
                "spawn_coords": (14, 23),
                "id": "b3-c3",
                "target": "Room_C3",
            },
        ]
