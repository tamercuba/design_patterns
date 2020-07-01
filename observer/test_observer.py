from observer.implementation import (
    ConcreteObserverA,
    ConcreteObserverB,
    Subject,
)


def test_business_logic():
    subject = Subject()

    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()

    subject.attach(observer_a)
    subject.attach(observer_b)

    assert subject.business_logic(3) == ['Event A']
    assert subject.business_logic(5) == []
    assert subject.business_logic(2) == ['Event A', 'Event B']

    subject.dettach(observer_b)

    assert subject.business_logic(3) == ['Event A']
    assert subject.business_logic(5) == []
    assert subject.business_logic(2) == ['Event A']
