import sys
from typing import TYPE_CHECKING

import numpy as np
import pygame

if TYPE_CHECKING:
    from main import Game

Blit = tuple[pygame.Surface, tuple[float, float]]


class StartService:
    _game: "Game"
    _menu: pygame.Surface

    running: bool
    has_loaded: bool
    blit: tuple[pygame.Surface, tuple[int, int]]
    clock: pygame.time.Clock

    def __init__(self, game: "Game"):
        self._game = game
        self.has_loaded = False

        self._menu = self._game.create_surface(
            "menu/start_menu_art.png", self._game.config["screen_size"]
        )

        self.running = False
        self.clock = pygame.time.Clock()

        self.register_events()

    def _start(self, event_type: int):
        """Start the game and exit the start menu"""

        self.has_loaded = True

        # Register the movement keybinds
        self._game.movement_service.register_events()

    def register_events(self):
        """Create the start game events"""

        register = self._game.event_service.register
        register(pygame.K_RETURN, self._start)
        register(pygame.K_SPACE, self._start)

    def unregister_events(self):
        """Remove the start game events"""

        unregister = self._game.event_service.unregister
        unregister(pygame.K_RETURN)
        unregister(pygame.K_SPACE)

    def _render(self):
        """Render the game contents"""

        try:
            if self.has_loaded:
                # Update the window blits and rerender the screen
                self._game.room_service.render()

                # Show the current dialog, if any
                self._game.dialog_service.render()
            else:
                # Display the default start screen
                self._game.window.blit(self._menu, (0, 0))

                # Render the start and menu buttons
                button_service = self._game.button_service
                button_size = np.array((64, 32)) * self._game.config["scale_factor"]

                rect = self._menu.get_rect()

                button_service.render(
                    "menu/start_button.png",
                    lambda: self._start(0),
                    button_size,
                    (rect.width * 0.65, rect.height * 0.65),
                    self._menu,
                )

                button_service.render(
                    "menu/menu_button.png",
                    lambda: self._game.menu_service.toggle_menu(pygame.KEYDOWN),
                    button_size,
                    (rect.width * 0.25, rect.height * 0.65),
                    self._menu,
                )

            # Rerender the end screen if the game is over
            self._game.end_service.render()

            # Render the menu if open
            self._game.menu_service.render()

            pygame.display.flip()
        except pygame.error:
            sys.exit(0)

    def start_loop(self):
        """Starts the pygame event loop"""

        self.running = True

        while self.running:
            # Hook onto the event handler and run the callbacks
            for event in pygame.event.get():
                self._game.event_service.hook(event)

            # Render the game contents
            self._render()

            # Set the framerate to 60 FPS
            self.clock.tick(60)
