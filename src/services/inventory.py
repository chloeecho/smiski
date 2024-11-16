from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from main import Game


class InventoryService:
    _game: "Game"
    items: list[pygame.Surface]

    # sets variables for inventory service class
    def __init__(self, game: "Game"):
        self._game = game
        create_surface = self._game.create_surface

        self.active = False
        self.items = [
            # Items for testing
            # create_surface("items/32x32_torch.png"),
            # create_surface("items/32x32_full_amulet.png"),
            # create_surface("items/32x32_blessing.png"),
            # create_surface("items/32x32_power_belt.png")
        ]

    def add_item(self, item: pygame.Surface):
        """Add an item to the inventory.

        Args:
            item (str): the item to add to the inventory
        """

        DialogItem = self._game.dialog_service.DialogItem

        item_names = list(self._game.surface_cache.keys())
        surfaces = list(self._game.surface_cache.values())

        item_name = item_names[surfaces.index(item)]
        dialog_option = None

        match item_name:
            case "items/32x32_amulet_left.png":
                dialog_option = DialogItem.AMULET_HALF_OBTAINED
            case "items/32x32_amulet_right.png":
                dialog_option = DialogItem.AMULET_HALF_OBTAINED
            case "items/32x32_full_amulet.png":
                dialog_option = DialogItem.AMULET_FULL_OBTAINED
            case "items/32x32_key_blue.png":
                dialog_option = DialogItem.BLUE_KEY_OBTAINED
            case "items/32x32_key_green.png":
                dialog_option = DialogItem.GREEN_KEY_OBTAINED
            case "items/32x32_key_purple.png":
                dialog_option = DialogItem.PURPLE_KEY_OBTAINED
            case "items/32x32_key_red.png":
                dialog_option = DialogItem.RED_KEY_OBTAINED
            case "items/32x32_power_belt.png":
                dialog_option = DialogItem.BELT_OBTAINED
            case "items/32x32_torch.png":
                dialog_option = DialogItem.TORCH_OBTAINED
            case "items/32x32_blessing.png":
                dialog_option = DialogItem.CHESRUS_JIST_OBTAINED

        self._game.dialog_service.show_dialog(dialog_option)

        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item: pygame.Surface):
        """Remove an item from the inventory.

        Args:
            item (pygame.Surface): the item to remove from the inventory
        """

        if item in self.items:
            self.items.remove(item)

    def has_items(self, items: list[str]) -> bool:
        """Check if items are in the inventory.

        Args:
            items (list[str]): the items to check

        Returns:
            bool: whether or not all the items are in the inventory
        """

        return all([self._game.create_surface(item) in self.items for item in items])

    def clear_inventory(self):
        """Clear the inventory."""
        self.items = []

    def toggle_inventory(self, yuh: int):
        """Toggle active inventory."""

        self.active = not self.active

    def render_inventory(self):
        """Render the inventory."""

        inventory = self._game.create_surface("menu/inventory.png", (192 * 5, 128 * 5))
        center = self._game.window.get_rect().center

        self._game.window.blit(
            inventory,
            (
                center[0] - 192 * 2.5,
                center[1] - 128 * 2.5,
            ),
        )

        for i, item in enumerate(self.items):
            item_image = pygame.transform.scale(item, (200, 200))

            self._game.window.blit(
                item_image,
                (
                    center[0] - 192 * 2.5 + 30 + 235 * (i % 4),
                    center[1] - 128 * 2.5 + 110 + 230 * (i // 4),
                ),
            )
