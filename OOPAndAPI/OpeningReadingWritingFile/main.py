from pprint import pprint
import os


# Задача 1
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


cook_book = get_dict('file.txt')
pprint(cook_book)


# Задача 2
def get_shop_list_by_dishes(dishes, person_count, cook_book):
    ingredients = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredients.get(ingredient['ingredient_name']) is None:
                    ingredients[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                  'quantity': int(ingredient['quantity']) * person_count}
                else:
                    ingredients[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
    return ingredients


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2, cook_book))


# Задача 3
def merge_files(path_directory):
    files = []
    for file_path in os.listdir(path_directory):
        if file_path != 'NewFile.txt':
            with open(os.path.join(path_directory, file_path), encoding='utf8') as file:
                quantity_lines = 0
                text = ''
                for line in file:
                    quantity_lines += 1
                    text += line
                files.append({'name': os.path.basename(file.name),
                              'quantity_lines': quantity_lines,
                              'text': text})
    with open(os.path.join(path_directory, 'NewFile.txt'), 'w+', encoding='utf8') as new_file:
        for file in sorted(files, key=lambda file_dict: file_dict['quantity_lines']):
            new_file.write(f'{file["name"]}\n{file["quantity_lines"]}\n{file["text"]}\n')


merge_files('Task2')
