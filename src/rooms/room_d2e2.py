from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game



class Room_D2E2:
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
        key_red = "items/32x32_key_red.png"
        water = "blocks/32x32_water-1.png"
        boulder = "blocks/32x32_boulder.png"
        plate = "blocks/32x32_pressed_plate.png"
        wall_high = "blocks/32x32_retractable_wall.png"
        wall_low = "blocks/32x32_retracted_wall.png"
        empty = ""

        self.dark_bool = True

        # Corner Blocks
        self.corners = {
            # "bottom_left": "32x32_brick_wall.png",
            # "bottom_right": "32x32_brick_wall.png",
            "top": wall
        }

        # fmt: off
        self.ground_plane =  [
            [water, water, water, water, water, water, water, water, water, ground, ground, ground, water, water, water, ground, ground, ground, ground, water, water, water, ground, ground, ground, water, water, water, water, water, water],
            [water, ground, ground, ground, ground, water, water, water, water, water, water, ground, water, water, water, ground, water, water, ground, water, water, water, ground, ground, ground, water, ground, ground, ground, ground, water],
            [water, ground, water, water, ground, ground, ground, ground, ground, ground, water, ground, ground, ground, ground, ground, water, water, ground, water, water, water, water, ground, water, water, ground, water, water, ground, water],
            [water, ground, water, water, ground, water, water, water, water, ground, water, ground, water, water, water, ground, water, water, ground, ground, ground, ground, water, ground, water, water, ground, water, water, ground, water],
            [water, ground, water, ground, ground, water, water, water, water, ground, water, ground, ground, ground, water, ground, water, water, water, water, water, ground, water, ground, water, water, ground, water, water, ground, water],
            [water, ground, water, ground, water, water, water, water, water, ground, water, water, water, ground, water, ground, water, water, water, water, water, ground, water, ground, water, water, ground, ground, water, ground, water],
            [ground, ground, water, ground, water, ground, ground, ground, ground, ground, water, ground, ground, ground, water, ground, water, ground, ground, ground, water, ground, water, ground, water, water, water, ground, water, ground, water],
            [ground, ground, water, water, water, ground, water, water, water, ground, water, water, water, water, water, ground, water, ground, water, ground, water, ground, water, ground, water, water, water, ground, water, ground, water],
            [ground, ground, water, water, water, ground, water, water, water, ground, water, water, ground, ground, ground, ground, water, ground, water, ground, water, ground, water, ground, water, water, water, ground, water, ground, water],
            [water, water, water, ground, ground, ground, water, ground, water, ground, water, water, ground, water, water, ground, water, ground, water, ground, water, ground, water, ground, ground, ground, ground, ground, water, ground, water],
            [water, water, water, ground, water, ground, water, ground, water, ground, water, water, ground, water, water, ground, water, water, water, ground, water, ground, water, water, water, water, water, ground, water, ground, water],
            [water, ground, ground, ground, water, ground, water, ground, water, ground, water, water, ground, water, water, ground, water, water, water, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, ground, water],
            [water, water, ground, water, water, ground, water, ground, water, ground, water, water, ground, water, water, ground, water, water, water, water, water, water, water, water, water, water, water, water, water, ground, water],
            [ground, ground, ground, water, water, ground, ground, ground, water, ground, ground, ground, ground, water, water, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water],
            [ground, ground, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water, water]
        ]

        self.objects_plane =  [
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, boulder, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, plate, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [wall_high, wall_high, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [key_red, wall_high, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty]
        ]
        # fmt: on

        self.right_wall_plane = {"type": wall, "width": 15, "height": 10}

        self.left_wall_plane = {"type": wall, "width": 15, "height": 10}

        self.doors_plane = [
            {
                "type": "door",
                "position": "back",
                "direction": "left",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (23, -1),
                "spawn_coords": (23, 0),
                "id": "e2-e3",
                "target": "Room_D3E3"
            },
            {
                "type": "locked_red",
                "position": "back",
                "direction": "right",
                "sprites": "blocks/32x64_locked_brick_door_red.png",
                "coords": (-1, 7),
                "spawn_coords": (0, 7),
                "id": "c2-d2",
                "target": "Room_C1C2"
            },
        ]
