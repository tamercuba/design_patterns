import pytest

from builder.implementation import Builder, Director


@pytest.fixture
def director():
    director_instance = Director()
    director_instance.builder = Builder()

    return director_instance


def test_build_simple(director):
    director.build_simple()
    expected_response = 'Product parts: [1, 2]'
    assert str(director.get_result()) == expected_response


def test_build_repeated(director):
    director.build_repeated()
    expected_response = 'Product parts: [1, 2, 1, 2]'
    assert str(director.get_result()) == expected_response


@pytest.mark.parametrize(
    'produce_one_times, produce_two_times, result',
    [
        (0, 0, []),
        (1, 9, [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]),
        (5, 0, [1, 1, 1, 1, 1]),
        (3, 3, [1, 1, 1, 2, 2, 2]),
    ],
)
def test_custom_build(director, produce_one_times, produce_two_times, result):
    for _ in range(0, produce_one_times):
        director.builder.produce_one()

    for _ in range(0, produce_two_times):
        director.builder.produce_two()

    expected_response = f'Product parts: {result}'
    assert str(director.get_result()) == expected_response
