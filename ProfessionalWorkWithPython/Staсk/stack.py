class Stack:
    def __init__(self):
        self.list = []

    def is_empty(self) -> bool:
        return self.size() == 0

    def push(self, item: object) -> None:
        self.list.append(item)

    def pop(self) -> object:
        return self.list.pop()

    def peek(self) -> object:
        return self.list[-1]

    def size(self) -> int:
        return len(self.list)

    def __str__(self) -> str:
        return f'{self.list}'

