from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Room_C3:
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
        water = "blocks/32x32_water-1.png"
        key_blue = "items/32x32_key_blue.png"
        boxes_smiski = "npcs/boxes_frame1.png"
        flute_smiski = "npcs/flute_frame1.png"
        hulahoop_smiski = "npcs/hulahoop_frame1.png"
        empty = ""

        self.dark_bool = False

        # Corner Blocks
        self.corners = {
            "top": wall
        }

        # fmt: off
        self.ground_plane =  [
            [ground, water, ground, ground, ground, ground, ground, ground, water, water, water, ground, water, ground, ground],
            [ground, water, ground, ground, ground, water, ground, ground, ground, ground, ground, ground, water, ground, water],
            [ground, water, water, ground, ground, water, ground, ground, ground, water, ground, ground, water, ground, water],
            [ground, ground, ground, ground, ground, water, ground, ground, ground, water, ground, ground, ground, ground, water],
            [ground, ground, water, ground, ground, water, water, water, water, water, water, water, water, ground, water],
            [ground, ground, water, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [water, water, water, ground, ground, ground, water, ground, ground, water, water, water, water, water, water],
            [ground, ground, water, ground, ground, water, water, water, ground, ground, ground, ground, ground, ground, ground],
            [ground, ground, water, ground, ground, ground, water, ground, ground, ground, ground, ground, water, water, water],
            [ground, ground, water, water, water, ground, ground, ground, water, water, water, water, water, water, water],
            [ground, ground, ground, ground, water, ground, ground, ground, ground, ground, ground, ground, water, water, ground],
            [water, water, ground, ground, water, water, ground, ground, water, water, water, ground, water, water, ground],
            [water, water, water, ground, ground, water, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [water, water, water, ground, ground, water, water, ground, ground, water, water, water, water, water, ground],
            [ground, water, water, ground, ground, ground, ground, ground, ground, water, ground, ground, ground, ground, ground]
        ]

        self.objects_plane =  [
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, hulahoop_smiski, empty, empty, empty],
            [empty, empty, empty, empty, flute_smiski, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, boxes_smiski, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [key_blue if self._game.create_surface(key_blue) not in self._game.inventory_service.items else empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty]
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
                "id": "b3-c3",
                "target": "Room_B3B4",
            },
            {
                "type": "locked_blue",
                "position": "front",
                "direction": "left",
                "sprites": "blocks/32x64_locked_brick_door_blue.png",
                "coords": (11, 14),
                "spawn_coords": (11, 14),
                "id": "c2-c3",
                "target": "Room_C1C2",
            },
            {
                "type": "door",
                "position": "front",
                "direction": "right",
                "sprites": "blocks/32x64_brick_door.png",
                "coords": (14, 7),
                "spawn_coords": (14, 7),
                "id": "c3-d3",
                "target": "Room_D3E3",
            },
        ]
