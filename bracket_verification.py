class Stack:
    some_str: str
    some_list: list
    round_bracket_counter: int
    curly_bracket_counter: int
    square_bracket_counter: int

    def __init__(self, some_str):
        self.some_str = some_str
        self.some_list = list(self.some_str)
        self.round_bracket_counter = 0
        self.curly_bracket_counter = 0
        self.square_bracket_counter = 0

    def is_empty(self) -> bool:
        return len(self.some_list) == 0

    def push(self, item) -> None:
        self.some_list.append(item)

    def pop(self) -> str:
        return self.some_list.pop()

    def peek(self) -> str:
        return self.some_list[-1]

    def size(self) -> int:
        return len(self.some_list)

    def is_correct_bracket(self) -> str:
        for _ in range(self.size()):
            match self.pop():
                case ")":
                    self.round_bracket_counter += 1
                case "]":
                    self.square_bracket_counter += 1
                case "}":
                    self.curly_bracket_counter += 1
                case "(":
                    self.round_bracket_counter -= 1
                    if self.round_bracket_counter < 0:
                        return f'«Несбалансированно»'
                case "[":
                    self.square_bracket_counter -= 1
                    if self.square_bracket_counter < 0:
                        return f'«Несбалансированно»'
                case "{":
                    self.curly_bracket_counter -= 1
                    if self.curly_bracket_counter < 0:
                        return f'«Несбалансированно»'
        return f'«Сбалансированно»' if self.round_bracket_counter == 0 and \
                                       self.curly_bracket_counter == 0 and \
                                       self.square_bracket_counter == 0 \
            else f'«Несбалансированно»'


if __name__ == '__main__':
    some_list_1 = Stack('(((([{}]))))')
    some_list_2 = Stack('[([])((([[[]]])))]{()}')
    some_list_3 = Stack('{{[()]}}')
    some_list_4 = Stack('}{}')
    some_list_5 = Stack("{{[(])]}}")
    some_list_6 = Stack("[[{())}]")

    print(some_list_1.is_correct_bracket())  # «Сбалансированно»
    print(some_list_2.is_correct_bracket())  # «Сбалансированно»
    print(some_list_3.is_correct_bracket())  # «Сбалансированно»
    print(some_list_4.is_correct_bracket())  # «Несбалансированно»
    print(some_list_5.is_correct_bracket())  # «Несбалансированно»
    print(some_list_6.is_correct_bracket())  # «Несбалансированно»
