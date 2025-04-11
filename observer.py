from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, race_state: dict):
        pass
