from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Game


class IsometricDirection(Enum):
    FRONT = (0, -1)
    LEFT = (-1, 0)
    BACK = (0, 1)
    RIGHT = (1, 0)


class CartesianDirection(Enum):
    FRONT = (-1, -1)
    LEFT = (-1, 1)
    BACK = (1, 1)
    RIGHT = (1, -1)


MovementMode = IsometricDirection | CartesianDirection


class SettingService:
    _game: "Game"

    movement_mode: MovementMode

    def __init__(self, game: "Game"):
        self._game = game

        # Set the default settings
        self.movement_mode = IsometricDirection

    def set_movement_mode(self, new_mode: MovementMode):
        """Update the movement mode

        Args:
            new_mode (MovementMode): the new mode
        """
        self.movement_mode = new_mode
