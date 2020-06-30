import random
from typing import List, Any


class Target:
    def operation(self) -> str:
        return "- Target operation -"


class Adaptee:
    def incompatible_operation(self) -> List:
        return [str(random.randint(1, 100)) for x in range(0, 10)]


class Adapter(Adaptee):
    def operation(self) -> str:
        result = self.incompatible_operation()

        return f'- Adapter operation: {",".join(result)} -'

def client(target: Any) -> None:
    result = target.operation()
    print_result = result if type(result) == str else 'INVALID'

    print(print_result)

if __name__ == '__main__':
    print('Deafault target works fine: ')
    target = Target()
    client(target)
    print('\n')

    print('Adaptee doesnt work well')
    try:
        adaptee = Adaptee()
        client(adaptee)
    except AttributeError as e:
        print(e)
        print('\n')

    print('Client can work with Adaptee via Adapter class: ')
    adapter = Adapter()
    client(adapter)
    print('\n')