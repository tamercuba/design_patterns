from abc import ABC, abstractmethod
from typing import Any, List


class Observer(ABC):
    @abstractmethod
    def notify(self, event: Any) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        return self._NAME


class Subject:
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """
        registerObserver on UML
        """
        self._observers.append(observer)

    def dettach(self, observer: Observer) -> None:
        """
        unregisterObserver on UML
        """
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        """
        notifyObserver on UML
        """
        result = []
        for observer in self._observers:
            notification = observer.notify(event=self._state)
            if notification:
                result.append(notification)

        return result

    def business_logic(self, state) -> None:
        self._state = state
        return self.notify_observers()


class ConcreteObserverA(Observer):
    _NAME = 'Event A'

    def notify(self, event: int) -> str:
        if event < 4:
            return self._NAME
        return None


class ConcreteObserverB(Observer):
    _NAME = 'Event B'

    def notify(self, event: int) -> str:
        if not event % 2:
            return self._NAME
        return None
