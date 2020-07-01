from typing import Any, List


class Target:
    def operation(self) -> str:
        return '- Target operation -'


class Adaptee:
    def incompatible_operation(self) -> List:
        return ['1', '2', '3', '4', '5']


class Adapter(Adaptee):
    def operation(self) -> str:
        result = self.incompatible_operation()

        return f'- Adapter operation: {", ".join(result)} -'


def client(target: Any) -> None:
    result = target.operation()
    return result if isinstance(result, str) else 'INVALID'
