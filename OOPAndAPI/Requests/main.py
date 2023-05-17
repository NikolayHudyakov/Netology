from super_heroes import SuperHeroes
from ya_uploader import YaUploader


if __name__ == '__main__':
    # Задача 1
    # super_heroes = SuperHeroes()
    # print(super_heroes.get_smartest_hero(['Hulk', 'Captain America', 'Thanos']))


    # Задача 2
    path_to_file = 'file.txt'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
