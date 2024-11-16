from typing import TYPE_CHECKING, Callable

import pygame
from pygame.event import Event

if TYPE_CHECKING:
    from main import Game


class EventService:
    _game: "Game"
    _callbacks: dict[int, Callable]

    _event_id: int
    _event_map: dict[int, Event]

    def __init__(self, game: "Game"):
        self._game = game
        self._callbacks = {}

        self._event_id = pygame.USEREVENT
        self._event_map = {}

    def create_event(self) -> int:
        """Create a custom event

        Returns:
            int: the event id
        """

        # Assign an id to the event and create an event object
        self._event_id += 1
        index = self._event_id
        event = Event(index)

        # Associate the event id to the event object
        self._event_map[index] = event
        self.hook(event)

        return index

    def fire_event(self, id: int):
        """Execute an event given its id

        Args:
            id (int): the event id
        """

        event = self._event_map.get(id)

        if event:
            pygame.event.post(event)

    def register(self, id: int, callback: Callable):
        """Attach a callback to an existing event

        Args:
            id (int): the event id
            callback (Callable): the callback function
        """

        self._callbacks[id] = callback

    def unregister(self, id: int):
        """Remove a callback from an existing event

        Args:
            id (int): the event id
        """

        del self._callbacks[id]

    def delay_event(self, interval: int, callback: Callable):
        """Create a delayed event

        Args:
            interval (int): the interval in milliseconds
            callback (Callable): the callback function
        """

        event = self.create_event()

        def handler():
            self.unregister(event)
            callback()

        self.register(event, handler)

        pygame.time.set_timer(event, interval, loops=1)

    def hook(self, event: Event):
        """Hook onto the event handler and run the correct callback

        Args:
            event (Event): the event object that was posted
        """

        if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            # If the event is a key, provide the actual event key
            self._callbacks.get(event.key, lambda _: None)(event.type)
        else:
            # Otherwise, just call it using the event type
            self._callbacks.get(event.type, lambda: None)()
