from typing import TYPE_CHECKING

import numpy as np
import pygame

if TYPE_CHECKING:
    from main import Game


class MenuService:
    _game: "Game"
    _menu_open: bool
    _cover: pygame.Surface

    def __init__(self, game: "Game"):
        self._game = game
        self._menu_open = False

        self.cover = pygame.Surface(self._game.config["screen_size"], pygame.SRCALPHA)
        self.cover.fill((0, 0, 0, 192))

    def toggle_menu(self, event_type: int):
        """Toggles the open/close state of the menu"""

        if event_type != pygame.KEYDOWN:
            return

        self._menu_open = not self._menu_open

        if self._menu_open:
            self._game.start_service.unregister_events()

            if self._game.start_service.has_loaded:
                self._game.movement_service.unregister_events()
        else:
            self._game.start_service.register_events()
            self._game.movement_service.register_events()

    def render(self):
        """Conditionally renders the menu only if open"""

        if self._menu_open:
            self._game.window.blit(self.cover, (0, 0))

            rect = self.cover.get_rect()

            self._game.button_service.render(
                "menu/quit_button.png",
                self._game.quit,
                np.array((64, 32)) * self._game.config["scale_factor"],
                (rect.width * 0.85, rect.height * 0.05),
                self.cover,
            )

            # Render controls png (not a button just a static image)
            controls = self._game.create_surface("menu/controls.png", (640, 480))
            self._game.window.blit(controls, (64, 32))
