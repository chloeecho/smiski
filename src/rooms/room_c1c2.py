from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Room_C1C2:
    _game: "Game"
    ground_plane: list[list[str]]
    objects_plane: list[list[str]]
    left_wall_plane: dict[str, str | int]
    right_wall_plane: dict[str, str | int]
    corners: dict[str, str]
    dark_bool: bool

    def __init__(self, game: "Game"):
        self._game = game

        ground = "blocks/32x32_brick_ground.png"
        wall = "blocks/32x32_brick_wall.png"
        plate = "blocks/32x32_pressed_plate.png"
        boulder = "blocks/32x32_boulder.png"
        wall_high = "blocks/32x32_retractable_wall.png"
        wall_low = "blocks/32x32_retracted_wall.png"
        amulet_half = "items/32x32_amulet_left.png"
        torch = "items/32x32_torch.png"
        pit = ""
        empty = ""

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
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit, pit],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, pit, pit, pit, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground]
        ]

        self.objects_plane =  [
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, torch, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, amulet_half, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, wall, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty],
            [empty, empty, empty, empty, wall, empty, empty, empty, empty, empty, plate, empty, wall, boulder, empty],
            [wall, wall, wall, wall, wall, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, wall, wall],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [wall_high, wall_high, wall_high, wall_high, wall_high, wall_high, empty, empty, empty, wall_high, wall_high, wall_high, wall_high, wall_high, wall_high],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty],
            [empty, empty, empty, plate, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, wall],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, wall],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, wall],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, wall, wall, boulder, wall],
            [wall_low, wall_low, wall_low, wall_low, wall_low, wall_low, empty, empty, empty, empty, wall, empty, empty, empty, wall],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, wall, empty, empty, wall, wall],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, wall, wall, empty, empty, empty, empty, empty],
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
                "direction": "right",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (14, 7),
                "spawn_coords": (14, 7),
                "id": "c2-d2",
                "target": "Room_D2E2",
            },
            {
                "type": "door",
                "position": "back",
                "direction": "left",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (11, -1),
                "spawn_coords": (11, 0),
                "id": "c2-c3",
                "target": "Room_C3",
            },
        ]
