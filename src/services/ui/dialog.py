from enum import Enum
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from main import Game


class DialogService:
    _game: "Game"

    class DialogItem(Enum):
        BELT_OBTAINED = "dialogs/belt_dialog.png"
        BLUE_KEY_OBTAINED = "dialogs/bluekey_dialog.png"
        GREEN_KEY_OBTAINED = "dialogs/greenkey_dialog.png"
        PURPLE_KEY_OBTAINED = "dialogs/purplekey_dialog.png"
        RED_KEY_OBTAINED = "dialogs/redkey_dialog.png"
        CHESRUS_JIST_OBTAINED = "dialogs/chresus_dialog.png"
        AMULET_HALF_OBTAINED = "dialogs/part_amulet_dialog.png"
        AMULET_FULL_OBTAINED = "dialogs/full_amulet_dialog.png"
        TORCH_OBTAINED = "dialogs/torch_dialog.png"
        BOULDER_ERROR = "dialogs/bouldererror_dialog.png"
        TOO_DARK_ERROR = "dialogs/dark_dialog.png"
        MISSING_KEY_ERROR = "dialogs/keyerror_dialog.png"
        WALLS_RETRACTED = "dialogs/wall_dialog.png"

    _show_dialog: bool
    _dialog_item: DialogItem

    def __init__(self, game: "Game"):
        self._game = game

        self._dialog_item = None
        self._show_dialog = False

    def show_dialog(self, dialog_item: DialogItem):
        """Opens the specified dialog

        Args:
            dialog_item (DialogItem): the dialog to open
        """

        self._dialog_item = dialog_item
        self._show_dialog = True

    def close_dialog(self):
        """Close the dialog"""

        self._dialog_item = None
        self._show_dialog = False

    def render(self):
        """Conditionally render the dialog if it is open"""

        if not self._show_dialog:
            return

        if(self._dialog_item != None):
            image_size = np.array((291, 113)) * 1.5
            surface = self._game.create_surface(self._dialog_item.value, image_size)

            rect = self._game.window.get_rect()

            self._game.window.blit(surface, (rect.width * 0.65, rect.height * 0.1))
            self._game.event_service.delay_event(5000, self.close_dialog)
