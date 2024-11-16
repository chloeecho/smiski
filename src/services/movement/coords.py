from typing import TYPE_CHECKING

import pygame
import numpy.typing as npt

if TYPE_CHECKING:
    from main import Game


class CoordinateService:
    _game: "Game"

    map_size: tuple[int, int, int]
    tile_size: int
    screen_size: tuple[int, int]

    tile_offset_x: int
    tile_offset_y: int

    def __init__(self, game: "Game"):
        self._game = game

        config = self._game.config

        self.map_size = (0, 0, 0)
        self.tile_size = config["scale_factor"] * 32
        self.screen_size = config["screen_size"]

        self.width, self.height = self.screen_size
        pygame.display.set_mode(self.screen_size)

        # The offset between the tiles and the top left corner of the screen
        self.tile_offset_x = self.width // 2 - self.tile_size // 2
        self.tile_offset_y = self.height // 4 - self.tile_size // 4

    def set_map_size(self, map_size):
        self.map_size = map_size

    def cartesian_to_isometric(
        self, obj_coords: tuple[int, int, int]
    ) -> tuple[int, int]:
        """Convert cartesian grid coordinates to a pixel value

        Args:
            obj_coords (tuple[int, int, int]): cartesian grid coordinates representing the tile

        Returns:
            tuple[int, int]: isometric world coordinates in pixels
        """  # noqa: E501

        # Cartesian object space to cartesian world space
        world_x = obj_coords[0] * self.tile_size
        world_y = obj_coords[1] * self.tile_size

        # Cartesian world space to isometric world space
        iso_x = (world_x - world_y) / 2 + self.tile_offset_x
        iso_y = (world_x + world_y) / 4 + self.tile_offset_y

        z_offset = obj_coords[2] * self.tile_size // 2

        return (int(iso_x), int(iso_y - z_offset))

    def isometric_to_cartesian(self, iso_coords: tuple[int, int]) -> tuple[int, int]:
        """Convert isometric pixel coordinates to a tile coordinate

        Args:
            iso_coords (tuple[int, int, int]): isometric world coordinates in pixels

        Returns:
            tuple[int, int]: cartesian grid coordinates representing the tile
        """

        # Undo offsets from the world coordinates
        world_x = iso_coords[0] - self.tile_offset_x - self.tile_size / 2
        world_y = iso_coords[1] - self.tile_offset_y - self.tile_size / 2

        # Isometric world space to cartesian world space
        cart_x = world_y * 2 + world_x
        cart_y = world_y * 2 - world_x

        # Cartesian world space to cartesian object space
        obj_x = cart_x // self.tile_size  # + 1
        obj_y = cart_y // self.tile_size  # + 1

        return (int(obj_x), int(obj_y))

    def iso_to_cart_direction(self, iso_direction: npt.NDArray) -> tuple[int, int]:
        """Convert isometric directions to cartesian directions

        Args:
            iso_direction (npt.NDArray): isometric direction

        Returns:
            tuple[float, float]: cartesian direction
        """

        mappings = {
            (0, -1): (1, -1),
            (0, 1): (-1, 1),
            (-1, 0): (-1, -1),
            (1, 0): (1, 1),
            (-1, -1): (0, -1),
            (1, 1): (0, 1),
            (-1, 1): (-1, 0),
            (1, -1): (1, 0),
        }

        return mappings.get((*iso_direction,), (0, 0))  # type: ignore
