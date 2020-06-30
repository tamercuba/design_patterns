from abc import ABC, abstractmethod
from typing import List
import random

class Observer(ABC):
    @abstractmethod
    def notify(self) -> None:
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
        print(f'Subject: Attached {observer}.')
        self._observers.append(observer)

    def dettach(self, observer: Observer) -> None:
        """
        unregisterObserver on UML
        """
        print(f'Subject: Dettached {observer}.')
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        """
        notifyObserver on UML
        """
        for observer in self._observers:
            observer.notify(event=self._state)

    def business_logic(self) -> None:
        self._state = random.randint(0, 10)
        self.notify_observers()

class ConcreteObserverA(Observer):
    _NAME = 'Concrete Observer A'
    def notify(self, event: int) -> None:
        if event < 4:
            print(f'{self._NAME}: Event trigged')

class ConcreteObserverB(Observer):
    _NAME = 'Concrete Observer B'
    def notify(self, event: int) -> None:
        if event % 2:
            print(f'{self._NAME}: Event trigged')


if __name__ == '__main__':
    subject = Subject()

    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.attach(observer_a)
    subject.attach(observer_b)

    subject.business_logic()
    subject.business_logic()
    subject.business_logic()

    subject.dettach(observer_a)

    subject.business_logic()
    subject.business_logic()
    subject.business_logic()