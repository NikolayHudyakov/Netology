from stack import Stack


def find_pairs_bracket(brackets: str, pairs_brackets: list[str]) -> bool:
    for pairs_bracket in pairs_brackets:
        index = brackets.find(pairs_bracket)
        if index != -1:
            return find_pairs_bracket(brackets.replace(pairs_bracket, ''), pairs_brackets)
    return brackets == ''


def definition_of_balance(brackets: str) -> str:
    pairs_brackets = ['{}', '()', '[]']
    return 'Сбалансированно' if find_pairs_bracket(brackets, pairs_brackets) else 'Несбалансированно'


if __name__ == '__main__':
    print(definition_of_balance(input()))
