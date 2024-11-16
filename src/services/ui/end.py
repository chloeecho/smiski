from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from main import Game

Blit = tuple[pygame.Surface, tuple[float, float]]


class EndService:
    _game: "Game"
    _game_over: bool

    _menu: pygame.Surface

    def __init__(self, game: "Game"):
        self._game = game
        self._game_over = False

        self._menu = self._game.create_surface(
            "menu/end_screen_art.png", self._game.config["screen_size"]
        )

    def end_game(self):
        """End the game"""

        self._game_over = True

    def render(self):
        """Conditionally render the end screen if the game is over"""

        if not self._game_over:
            return

        self._game.window.blit(self._menu, (0, 0))
