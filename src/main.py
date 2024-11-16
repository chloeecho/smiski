import os
from typing import Callable, Optional, TypedDict

import pygame
import screeninfo

from services.events import EventService
from services.interactions import InteractionService
from services.inventory import InventoryService
from services.movement.camera import CameraService
from services.movement.coords import CoordinateService
from services.movement.movement import MovementService
from services.rooms import RoomService
from services.settings import SettingService
from services.ui.buttons import ButtonService
from services.ui.dialog import DialogService
from services.ui.end import EndService
from services.ui.menu import MenuService
from services.ui.start import StartService

Config = TypedDict(
    "Config",
    {
        "title": str,
        "scale_factor": int,
        "screen_size": tuple[int, int],
        "background_color": tuple[int, int, int],
        "soundfx_vol": float,
        "music_vol": float,
    },
)

Blit = tuple[pygame.Surface, tuple[int, int]]


class Game:
    config: Config
    surface_cache: dict[str, pygame.Surface]
    window: pygame.Surface

    event_service: EventService
    setting_service: SettingService
    button_service: ButtonService
    inventory_service: InventoryService
    coordinate_service: CoordinateService
    movement_service: MovementService
    camera_service: CameraService
    interaction_service: InteractionService
    room_service: RoomService
    menu_service: MenuService
    start_service: StartService
    end_service: EndService
    dialog_service: DialogService

    def __init__(self, config: Config):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(config["title"])

        self.config = config
        self.surface_cache = {}
        self.window = pygame.display.set_mode(config["screen_size"])
        self._load_icon_image()

        # Initialize the game services
        self.event_service = EventService(self)
        self.setting_service = SettingService(self)
        self.button_service = ButtonService(self)
        self.inventory_service = InventoryService(self)
        self.coordinate_service = CoordinateService(self)
        self.movement_service = MovementService(self)
        self.camera_service = CameraService(self)
        self.interaction_service = InteractionService(self)
        self.room_service = RoomService(self)
        self.menu_service = MenuService(self)
        self.start_service = StartService(self)
        self.end_service = EndService(self)
        self.dialog_service = DialogService(self)

        # Register events for the game
        self.event_service.register(pygame.QUIT, self.quit)
        self.event_service.register(pygame.K_ESCAPE, self.menu_service.toggle_menu)
        # self.event_service.register("dialog", self.dialog_service.toggle_menu)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def create_surface(
        self, image_name: str, scale: Optional[tuple[int, int]] = None
    ) -> pygame.Surface:
        """Load a texture and prepare it for usage in blits

        Args:
            image_name (str): name of the file to load
            scale: Optional[tuple[int, int]]1: what to resize the texture to. Defaults
            to coordinate_service.tile_size.

        Returns:
            pygame.Surface: scaled and alpha-converted texture
        """

        if not image_name:
            return

        cached = self.surface_cache.get(image_name)

        if cached:
            return cached

        tile_size = self.config["scale_factor"] * 32
        scale = scale if scale is not None else (tile_size, tile_size)

        image = pygame.image.load(os.path.join("assets", image_name))
        surface = pygame.transform.scale(image.convert_alpha(), scale)

        self.surface_cache[image_name] = surface

        return surface

    def create_blit(self, image: pygame.Surface, coordinate_func: Callable) -> Callable:
        """Utility function to create a blit

        Args:
            image (pygame.Surface): texture to use for the blit
            coordinate_func (Callable): function to transform the coordinates using

        Returns:
            Callable: blit function for the given image and coordinate function
        """

        def blit(x: int, y: int, z: int) -> Blit:
            return (image, coordinate_func((x, y, z)))

        return blit

    def _load_icon_image(self):
        """Loads the custom image for the cursor and icon"""

        image = self.create_surface("game/32x32_cursor.png", (48, 48))

        pygame.display.set_icon(image)
        pygame.mouse.set_cursor(pygame.Cursor((0, 0), image))

    def quit(self):
        """Properly quits the game client"""

        self.start_service.running = False
        pygame.quit()

        return 0


def main():
    """Starts the game client"""

    # Dynamically select the size based on the monitor size
    monitor = screeninfo.get_monitors()[0].height * 0.75
    screen_size = (monitor * 16 / 9, monitor)

    config: Config = {
        "title": "Curse of the Smiski",
        "scale_factor": screen_size[1] / 320,
        "screen_size": screen_size,
        "background_color": (0, 0, 0),
        "soundfx_vol": 1.0,
        "music_vol": 0.35,
    }

    # Properly quit the game client when the process exits
    with Game(config) as client:
        pygame.mixer.init()
        pygame.mixer.music.load("assets/audio/music.wav")
        pygame.mixer.music.set_volume(config["music_vol"])
        pygame.mixer.music.play(-1)

        client.start_service.start_loop()


if __name__ == "__main__":
    main()
