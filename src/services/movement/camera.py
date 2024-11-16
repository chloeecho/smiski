from typing import TYPE_CHECKING

import numpy.typing as npt

if TYPE_CHECKING:
    from main import Game


class CameraService:
    _game: "Game"
    screen_size: tuple[int, int]

    def __init__(self, game: "Game"):
        self._game = game

        self.screen_size = self._game.config["screen_size"]

    def update_boulder_camera(self, direction: npt.NDArray):
        """Update the camera's position based on the player's movement

        Args:
            direction (npt.NDArray): the direction to move in
        """

        coordinate_service = self._game.coordinate_service

        tile_size = coordinate_service.tile_size
        direction = coordinate_service.iso_to_cart_direction(direction)

        if direction[0] == 0 or direction[1] == 0:
            # Diagonal movement is twice as fast as linear movement
            coordinate_service.tile_offset_x -= 2 * direction[0] * tile_size / 2
            coordinate_service.tile_offset_y -= 2 * direction[1] * tile_size / 4
        else:
            coordinate_service.tile_offset_x -= direction[0] * tile_size / 2
            coordinate_service.tile_offset_y -= direction[1] * tile_size / 4

        self._game.movement_service.update_highlight()

    def update_camera(self, new_position: npt.NDArray, old_position: npt.NDArray):
        """Update the camera's position based on the player's position

        Args:
            new_position (npt.NDArray): the position of the player
            old_position (npt.NDArray): the previous position of the player
        """

        coordinate_service = self._game.coordinate_service

        tile_size = coordinate_service.tile_size

        iso_x_difference = new_position[0] - old_position[0]
        iso_y_difference = new_position[1] - old_position[1]

        coordinate_service.tile_offset_x += (
            iso_y_difference * tile_size / 2 - iso_x_difference * tile_size / 2
        )
        coordinate_service.tile_offset_y -= (
            iso_y_difference * tile_size / 4 + iso_x_difference * tile_size / 4
        )
