from abc import ABC, abstractmethod
from typing import Any


class Product:
    def __init__(self) -> None:
        self.parts = list()

    def add(self, value: int) -> None:
        self.parts.append(value)

    def __str__(self) -> str:
        return f'Product parts: {str(self.parts)}'


class AbstractBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError

    @property
    def product(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def produce_one(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def produce_two(self) -> None:
        raise NotImplementedError


class Builder(AbstractBuilder):
    def __init__(self) -> None:
        self.reset()

    @property
    def product(self) -> Any:
        """
        This property is similar to "getResult" method, which the most
        commonly used method name to this operation
        """
        product = self._product
        self.reset()

        return product

    @product.setter
    def product(self, product) -> None:
        self._product = product

    def reset(self) -> None:
        self.product = Product()

    def produce_one(self) -> None:
        self._product.add(1)

    def produce_two(self) -> None:
        self._product.add(2)


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_simple(self) -> None:
        self.builder.produce_one()
        self.builder.produce_two()

    def build_repeated(self) -> None:
        self.builder.produce_one()
        self.builder.produce_two()
        self.builder.produce_one()
        self.builder.produce_two()

    def get_result(self) -> Product:
        return self._builder.product
