from typing import TYPE_CHECKING, Callable, Optional

import pygame

if TYPE_CHECKING:
    from main import Game


class ButtonService:
    _game: "Game"
    _button_index: int

    _buttons: dict[int, pygame.Rect]
    _callbacks: dict[int, Callable]

    def __init__(self, game: "Game"):
        self._game = game
        self._button_index = 0

        self._buttons = {}
        self._callbacks = {}

        self._game.event_service.register(pygame.MOUSEBUTTONUP, self._handle_click)

    def _handle_click(self):
        """Handle the global click event and call the appropriate callback"""

        pos = pygame.mouse.get_pos()

        for id, rect in self._buttons.items():
            if rect.collidepoint(pos):
                self._callbacks[id]()

    def render(
        self,
        button_name: str,
        callback: Callable,
        button_size: tuple[int, int],
        button_pos: tuple[int, int],
        parent: Optional[pygame.Surface],
    ):
        """Generate a button using the provided arguments

        Args:
            button_name (str): the name of the button image
            callback (Callable): the callback to run on click
            button_size (tuple[int, int]): the size of the button
            button_pos (tuple[int, int]): the position of the button
            parent (Optional[pygame.Surface]): the surface to render the button on
        """

        button = self._game.create_surface(button_name, button_size)

        surface = parent or self._game.window
        rect = surface.blit(button, button_pos)

        self._button_index += 1
        self._buttons[self._button_index] = rect
        self._callbacks[self._button_index] = callback
