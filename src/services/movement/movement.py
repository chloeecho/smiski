import os
from typing import TYPE_CHECKING, Callable

import numpy as np
import numpy.typing as npt
import pygame

if TYPE_CHECKING:
    from settings import MovementMode

    from main import Game

Blit = tuple[pygame.Surface, tuple[int, int]]

images = {
    "east": ["f_se_1.png", "f_se_2.png"],
    "west": ["f_nw_1.png", "f_nw_2.png"],
    "north": ["f_ne_1.png", "f_ne_2.png"],
    "south": ["f_sw_1.png", "f_sw_2.png"],
}

sounds = {
    "boot1": "boot1.wav",
    "boot2": "boot2.wav",
    "boot3": "boot3.wav",
}


class MovementService:
    _game: "Game"
    _create_blit: Callable
    _directions: "MovementMode"

    _cursor_moved: bool
    _previous_pos: tuple[int, int]
    _selection_blit: Blit
    _highlight_blit: Blit
    _selection_surface: pygame.Surface
    _highlight_surface: pygame.Surface
    _selection_pos: tuple[int, int, int]
    _highlight_pos: tuple[int, int, int]

    _has_moved: bool
    _first_render: bool
    position: npt.NDArray
    blit: list[Blit]
    direction: str
    current_frame: int
    sound_index: int
    teleporting: bool

    def __init__(self, game: "Game"):
        self._game = game
        create_surface = self._game.create_surface

        self.surface = create_surface("player/f.png")
        self.teleporting = False

        # Create the blit function for the player character
        self._create_blit = self._game.create_blit(
            self.surface,
            self._game.coordinate_service.cartesian_to_isometric,
        )

        # Initialize the hover effect and attach it to mouse movement
        self._selection_surface = create_surface("game/32x32_selection.png")
        self._highlight_surface = create_surface("game/32x32_highlight.png")

        self._selection_pos = (-100, -100, 0)
        self._highlight_pos = (-100, -100, 0)
        self._previous_pos = (0, 0)
        self._cursor_moved = True

        self.update_highlight()

        # Initialize the player's direction, position, and animation variables
        self._has_moved = True
        self._first_render = True
        self.position = np.array((4, 4))
        self.direction = "east"
        self.current_frame = 0

        self.blit = self.update()
        self.sound_index = 0

        # Create a separate channel for the player's sound
        self.sound_channel = pygame.mixer.Channel(1)

    def walk_animation(self) -> pygame.Surface:
        """Get the current frame for the walking animation

        Returns:
            pygame.Surface: the current frame of the walking animation
        """

        frame_list = images[self.direction]
        frame_index = self.current_frame % len(frame_list)
        frame_image = frame_list[frame_index]

        return self._game.create_surface(f"player/{frame_image}")

    def play_sound(self):
        """Play the sound based on the current sound index"""

        sound_name = "boot" + str(self.sound_index % 3 + 1)
        sound_file = sounds[sound_name]
        sound_path = os.path.join("assets/audio", sound_file)

        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(self._game.config["soundfx_vol"])

        # Play the sound on the separate channel
        self.sound_channel.play(sound)
        self.sound_index += 1

    def register_events(self):
        """Add every movement keybind to the event handler"""

        register = self._game.event_service.register
        directions = self._game.setting_service.movement_mode

        # Set keybinds for WASD
        register(pygame.K_w, self.move(directions.FRONT))
        register(pygame.K_a, self.move(directions.LEFT))
        register(pygame.K_s, self.move(directions.BACK))
        register(pygame.K_d, self.move(directions.RIGHT))

        # Set keybinds for the arrow keys
        register(pygame.K_UP, self.move(directions.FRONT))
        register(pygame.K_LEFT, self.move(directions.LEFT))
        register(pygame.K_DOWN, self.move(directions.BACK))
        register(pygame.K_RIGHT, self.move(directions.RIGHT))

        # Set keybind for mouse click (click-to-move)
        register(pygame.MOUSEBUTTONDOWN, self.move_to_cursor)

        # Set teleport keybind
        register(pygame.K_LSHIFT, self.shift_key)

        # Set keybind for mouse hover (hover tile effect)
        register(pygame.MOUSEMOTION, self.update_highlight)

        register(pygame.K_TAB, self._game.inventory_service.toggle_inventory)

    def unregister_events(self):
        """Remove every movement keybind from the event handler"""

        unregister = self._game.event_service.unregister

        # Unset keybinds for WASD
        unregister(pygame.K_w)
        unregister(pygame.K_a)
        unregister(pygame.K_s)
        unregister(pygame.K_d)

        # Unset keybinds for the arrow keys
        unregister(pygame.K_UP)
        unregister(pygame.K_LEFT)
        unregister(pygame.K_DOWN)
        unregister(pygame.K_RIGHT)

        # Unset keybind for mouse click (click-to-move)
        unregister(pygame.MOUSEBUTTONDOWN)

        # Unset keybind for mouse hover (hover tile effect)
        unregister(pygame.MOUSEMOTION)

    def update_highlight(self):
        """Update the location of the highlight effect"""

        previous_pos = self._previous_pos

        self._previous_pos = pygame.mouse.get_pos()
        self._highlight_pos = self._hover_tile()

        if previous_pos != self._previous_pos:
            self._cursor_moved = True

    def update_selection(self):
        """Update the location of the selection effect"""

        self._selection_pos = self._hover_tile()
        self._game.interaction_service.handle_click(self._selection_pos)

    def _hover_tile(self) -> tuple[int, int, int]:
        """Generates a cursor hover effect from the mouse position

        Returns:
            tuple[int, int, int]: the position for the blit
        """

        coordinates = self._game.coordinate_service
        iso_to_cart = coordinates.isometric_to_cartesian

        # Convert the screen position to a cartesian position
        max_pos = coordinates.map_size[:-1] - np.array((2, 2))
        pos = np.clip(iso_to_cart(pygame.mouse.get_pos()), -1, max_pos)

        # Offset to later convert back to isometric pixel coordinates
        return (pos[0] + 1, pos[1] + 1, 0)

    def distance_from(self, position: tuple[int, int, int]) -> float:
        """Get the distance from the player to a given position

        Args:
            position (tuple[int, int]): the position to check

        Returns:
            float: the distance from the player to the position
        """

        # Use the L2 norm, or euclidian (squared) distance
        return np.linalg.norm(np.append(self.position, 1) - list(position))

    def _move_in_direction(self, direction: npt.NDArray):
        """Performs additional checks before moving to the position

        Args:
            direction (npt.NDArray): the direction to move in
        """

        # Make sure the new position is within the room bounds
        coordinates = self._game.coordinate_service
        max_pos = coordinates.map_size[:-1] - np.array((1, 1))

        pos = self.position + direction
        new_pos = np.clip(pos, 0, max_pos)

        create_surface = self._game.create_surface
        room_service = self._game.room_service
        room = room_service.room

        # If player is near a boulder, push it in the direction they are moving
        objects = room["objects"]
        boulder = self._game.create_surface("blocks/32x32_boulder.png")

        # If you have the power belt, you can push boulders
        has_power_belt = self._game.inventory_service.has_items(
            ["items/32x32_power_belt.png"]
        )

        # If you have the blessing, you can walk on water
        has_blessing = self._game.inventory_service.has_items(
            ["items/32x32_blessing.png"]
        )

        object = objects[new_pos[1]][new_pos[0]]

        if object == boulder and has_power_belt:
            self.play_sound()

            boulder_pos = new_pos + direction

            # If boulders new posiiton is within bounds of map
            if (
                boulder_pos[0] >= 0
                and boulder_pos[0] < max_pos[0]
                and boulder_pos[1] >= 0
                and boulder_pos[1] < max_pos[1]
            ):
                # If the boulder is going to end up in a pit or in water, do not move
                ground_plane = room["floor"]

                if (
                    ground_plane[boulder_pos[1]][boulder_pos[0]] == create_surface("")
                    or ground_plane[boulder_pos[1]][boulder_pos[0]]
                    == create_surface("blocks/32x32_water-1.png")
                    or ground_plane[boulder_pos[1]][boulder_pos[0]]
                    == create_surface("blocks/32x32_water_ripple1.png")
                ):
                    return

                # If the boulder is going to end up on a wall, do not move
                if (
                    objects[boulder_pos[1]][boulder_pos[0]] is None
                    or objects[boulder_pos[1]][boulder_pos[0]]
                    is create_surface("blocks/32x32_retracted_wall.png")
                    or objects[boulder_pos[1]][boulder_pos[0]]
                    is create_surface("blocks/32x32_pressed_plate.png")
                ):
                    objects[boulder_pos[1]][boulder_pos[0]] = create_surface(
                        "blocks/32x32_boulder.png"
                    )

                    # Remove the boulder from its old position
                    objects[new_pos[1]][new_pos[0]] = None

                    # If plate is pressed
                    if (
                        room_service.current_room.objects_plane[boulder_pos[1]][
                            boulder_pos[0]
                        ]
                        == "blocks/32x32_pressed_plate.png"
                    ):
                        self._game.interaction_service.retract_walls(True)

                    objects[boulder_pos[1]][boulder_pos[0]] = create_surface(
                        "blocks/32x32_boulder.png"
                    )

                    past_tile = room_service.current_room.objects_plane[new_pos[1]][new_pos[0]]

                    # Reform earlier object blocks after boulder passes over them
                    if(past_tile == "blocks/32x32_retracted_wall.png" or past_tile == "blocks/32x32_retractable_wall.png"):
                        objects[new_pos[1]][new_pos[0]] = create_surface("blocks/32x32_retracted_wall.png")
                    elif(past_tile == "blocks/32x32_pressed_plate.png"):
                        objects[new_pos[1]][new_pos[0]] = create_surface("blocks/32x32_pressed_plate.png")
                    else:
                        objects[new_pos[1]][new_pos[0]] = create_surface("")

                    # If plate is pressed
                    if objects[new_pos[1]][new_pos[0]] == create_surface("blocks/32x32_pressed_plate.png"):
                        self._game.interaction_service.retract_walls(True)

                    self.position = new_pos
                    self._has_moved = True

                    # Update camera
                    self._game.camera_service.update_boulder_camera(direction)

                    # Play boulder sound
                    sound_path = os.path.join("assets/audio", "boulder_slide.wav")
                    sound = pygame.mixer.Sound(sound_path)
                    sound.set_volume(self._game.config["soundfx_vol"])

                    # Play the sound on the separate channel
                    pygame.mixer.Channel(2).play(sound)

                    return self.play_sound()
        elif object == boulder and not has_power_belt:
            dialog_service = self._game.dialog_service
            too_heavy = dialog_service.DialogItem.BOULDER_ERROR

            dialog_service.show_dialog(too_heavy)
        elif object == create_surface("items/32x32_idol.png"):
            return self._game.end_service.end_game()

        # Only move if the new position isn't where the player already is
        if np.array_equal(pos, new_pos):
            # Don't move if there is a block in that spot
            if (
                room["objects"][new_pos[1]][new_pos[0]] is not None
                and room["objects"][new_pos[1]][new_pos[0]]
                is not create_surface("blocks/32x32_retracted_wall.png")
                and room["objects"][new_pos[1]][new_pos[0]]
                is not create_surface("blocks/32x32_pressed_plate.png")
            ):
                return

            # Don't move if you can't travel on that block
            forbidden_surfaces = map(
                create_surface,
                ["", "blocks/32x32_water-1.png", "blocks/32x32_water_ripple1.png"],
            )

            floor_tile = room["floor"][new_pos[1]][new_pos[0]]

            if floor_tile == create_surface(""):
                return

            if floor_tile in list(forbidden_surfaces) and not has_blessing:
                return

            # self._game.camera_service.update_camera(direction)
            self._game.camera_service.update_camera(new_pos, self.position)
            self.play_sound()

            self.position = new_pos
            self._has_moved = True

            # Update the player's direction based on the movement
            mappings = {
                (0, -1): "north",
                (0, 1): "south",
                (-1, 0): "west",
                (1, 0): "east",
                # Placeholders for cartesian movement
                (-1, -1): "north",
                (1, 1): "south",
                (-1, 1): "south",
                (1, -1): "north",
            }

            self.direction = mappings.get((*direction,))

    def move(self, direction: "MovementMode"):
        """Move in the direction of the pressed key (regular movement)

        Args:
            direction (MovementMode): the direction being moved in
        """

        dir = np.array(direction.value)

        def handler(event_type: int):
            """Handle the event for regular movement

            Args:
                event_type (int): whether or not the key is being pressed
            """

            # Only move if the mouse is being released
            if event_type == pygame.KEYDOWN:
                return

            # Add the direction to the player's current position
            self._move_in_direction(dir)

        return handler

    def shift_key(self, event_type: int):
        """Switches teleportation based on shift key

        Args:
            event_type (int): whether or not the key is being pressed
        """

        self.teleporting = (
            event_type == pygame.KEYDOWN
            and self._game.inventory_service.has_items(["items/32x32_full_amulet.png"])
        )

    def move_to_cursor(self):
        """Move in the direction of the cursor (click-to-move)"""

        # Update the selection if the cursor has moved
        if self._cursor_moved:
            self._cursor_moved = False
            return self.update_selection()

        # Move towards the current selection
        coordinates = self._game.coordinate_service
        world = coordinates.isometric_to_cartesian(self._selection_blit[1])
        world = (world[0] + 2, world[1] + 1)

        # Do not move if the cursor is already near the player's position
        # Use the L2 norm, or euclidian (squared) distance, to compare
        offset = world - self.position

        if np.linalg.norm(offset) < 1:
            return

        # Calculate the direction to move in
        dir_list = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
        ]

        # Use dot products to find the closest movement direction
        dir = max(dir_list, key=lambda dir: np.dot(dir, offset))

        if self.teleporting:
            self.teleport()
        else:
            self._move_in_direction(dir)

    def teleport(self):
        """Teleports player to selected spot after collecting amulet"""

        old_pos = self.position
        new_pos = (self._selection_pos[0], self._selection_pos[1])

        # Don't move if there is a block in that spot
        room = self._game.room_service.room
        create_surface = self._game.create_surface

        # collision detection
        if (
            room["objects"][new_pos[1]][new_pos[0]] is not None
            and room["objects"][new_pos[1]][new_pos[0]]
            is not create_surface("blocks/32x32_retracted_wall.png")
            and room["objects"][new_pos[1]][new_pos[0]]
            is not create_surface("blocks/32x32_pressed_plate.png")
        ):
            return

        forbidden_surfaces = map(
            create_surface,
            [
                "",
                "blocks/32x32_water-1.png"
                if self._game.create_surface("items/32x32_blessing.png")
                not in self._game.inventory_service.items
                else None,
                "blocks/32x32_water_ripple1.png",
            ],
        )

        if room["floor"][new_pos[1]][new_pos[0]] in list(forbidden_surfaces):
            return

        # self.play_sound()

        self.position = np.array(new_pos)
        self._has_moved = True

        self._game.camera_service.update_camera(new_pos, old_pos)

        # play teleport sound
        sound_path = os.path.join("assets/audio", "teleport.wav")
        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(self._game.config["soundfx_vol"])

        # Play the sound on the separate channel
        pygame.mixer.Channel(3).play(sound)

    def update(self) -> list[Blit]:
        """Update the blit for the player"""

        # Only update the blit if the player has moved
        if self._has_moved:
            self._has_moved = False
            self.surface = self.walk_animation()

            # Instead of making a new surface, replace current surface
            self._create_blit = self._game.create_blit(
                self.surface,
                self._game.coordinate_service.cartesian_to_isometric,
            )
            self.blit = [self._create_blit(*self.position, 1)]

            # Update the frame index for the next animation frame
            self.current_frame += 1

        # Only enable the hover effect after the first render
        if not self._first_render:
            # Convert the grid coordinates to pixel coordinates
            cart_to_iso = self._game.coordinate_service.cartesian_to_isometric

            highlight_pos = cart_to_iso(self._highlight_pos)
            selection_pos = cart_to_iso(self._selection_pos)

            # Recreate the blit objects using the positions
            self._highlight_blit = (self._highlight_surface, highlight_pos)
            self._selection_blit = (self._selection_surface, selection_pos)

            # Render the player above the hover effect
            return ([self._highlight_blit, self._selection_blit], self.blit)

        self._first_render = False
        return (None, self.blit)
