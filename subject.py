from typing import List
from observer import Observer

class RaceEvent:
    def __init__(self):
        self._observers: List[Observer] = []
        self._race_state = {}

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def update_positions(self, race_state: dict):
        self._race_state = race_state
        self._notify_observers()

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._race_state)
