from pprint import pprint


def get_dict(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf8') as file:
        while recipe := file.readline().strip():
            cook_book[recipe] = []
            for _ in range(int(file.readline())):
                ingredient = file.readline().strip().split(sep='|')
                cook_book[recipe].append({'ingredient_name': ingredient[0].strip(),
                                          'quantity': ingredient[1].strip(),
                                          'measure': ingredient[2].strip()})
            file.readline()
    return cook_book


pprint(get_dict('file.txt'))