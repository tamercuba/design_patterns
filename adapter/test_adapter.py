import pytest

from adapter.implementation import Adaptee, Adapter, Target, client


def test_adapter():
    target = Target()
    adaptee = Adaptee()
    adapter = Adapter()

    assert client(target) == '- Target operation -'
    assert client(adapter) == '- Adapter operation: 1, 2, 3, 4, 5 -'
    with pytest.raises(AttributeError):
        assert client(adaptee)
