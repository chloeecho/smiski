from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class Room_A3A4:
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
        grass = "blocks/32x32_grass.png"
        wall = "blocks/32x32_brick_wall.png"
        smiski = "items/32x32_smiski_statue.png"
        water = "blocks/32x32_water-1.png"
        ripple = "blocks/32x32_water_ripple1.png"
        ripple_object = "blocks/32x32_empty.png"
        wall_high = "blocks/32x32_retractable_wall.png"
        wall_low = "blocks/32x32_retracted_wall.png"
        amulet_half = "items/32x32_amulet_right.png"
        door = ""
        empty = ""

        self.dark_bool = True

        # Corner Blocks
        self.corners = {"top": wall}

        # fmt: off
        self.ground_plane =  [
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground],
            [ground, grass, ground, ground, ground, water, water, water, water, water, ground, ground, ground, grass, ground],
            [ground, ground, water, water, water, water, water, water, water, water, water, water, water, ground, ground],
            [ground, ground, water, water, water, water, water, water, water, water, water, water, water, ground, ground],
            [ground, ground, water, water, water, water, water, water, water, water, ripple, water, water, ground, ground],
            [ground, ground, water, water, water, water, water, water, water, water, water, water, water, ground, ground],
            [ground, water, ripple, water, water, water, water, water, water, water, water, water, water, water, ground],
            [ground, water, water, water, water, water, water, water, water, water, water, water, water, water, ground],
            [ground, water, water, water, water, water, water, water, water, water, water, water, water, water, ground],
            [ground, water, water, water, water, water, water, water, water, water, water, water, water, water, ground],
            [ground, water, water, water, water, water, water, water, water, water, water, water, water, water, ground],
            [ground, water, water, water, water, water, water, water, water, water, water, water, water, water, ground],
            [ground, water, water, water, water, ground, ground, ground, ground, ground, water, water, water, water, ground],
            [ground, water, water, water, water, ground, grass, grass, grass, ground, water, water, water, water, ground],
            [ground, water, water, water, water, ground, grass, grass, grass, ground, water, water, water, water, ground],
            [ground, water, water, water, water, ground, grass, grass, grass, ground, water, water, water, water, ground],
            [ground, water, water, water, water, ground, grass, grass, grass, ground, water, water, water, water, ground],
            [ground, water, water, water, water, ground, grass, grass, grass, ground, water, water, water, water, ground],
            [ground, water, water, water, water, ground, ground, ground, ground, ground, water, water, water, water, ground],
            [ground, water, water, water, water, water, water, water, water, water, water, water, water, water, ground],
            [ground, water, water, water, water, water, water, water, water, water, water, water, water, water, ground],
            [ground, water, water, water, water, water, water, water, water, water, water, water, water, water, ground],
            [ground, water, water, water, water, water, water, water, water, water, water, water, water, water, ground],
            [ground, water, water, water, water, water, water, water, water, water, water, water, water, water, ground],
            [ground, water, water, water, water, ripple, water, water, water, water, water, water, water, water, ground],
            [ground, ground, water, water, water, water, water, water, water, water, water, water, water, ground, ground],
            [ground, ground, water, water, water, water, water, water, water, water, water, water, water, ground, ground],
            [ground, ground, water, water, water, water, water, water, water, water, water, water, water, ground, ground],
            [ground, ground, water, water, water, water, water, water, ripple, water, water, water, water, ground, ground],
            [ground, grass, ground, ground, ground, water, water, water, water, water, ground, ground, ground, grass, ground],
            [ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground]
        ]

        self.objects_plane =  [
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, smiski, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, smiski, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, ripple_object, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, ripple_object, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, wall_high, wall_high, wall_high, wall_high, wall_high, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, wall_high, empty, empty, empty, wall_high, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, wall_high, empty, empty, empty, wall_high, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, wall_high, empty, amulet_half if self._game.create_surface(amulet_half) not in self._game.inventory_service.items else empty, empty, wall_high, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, wall_high, empty, empty, empty, wall_high, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, wall_high, empty, empty, empty, wall_high, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, wall_high, wall_high, wall_high, wall_high, wall_high, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, ripple_object, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty],
            [empty, empty, empty, empty, empty, empty, empty, empty, ripple_object, empty, empty, empty, empty, empty, empty],
            [empty, smiski, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, smiski, empty],
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
                "coords": (14, 6),
                "spawn_coords": (14, 6),
                "id": "a4-b4",
                "target": "Room_B3B4",
            },
        ]
