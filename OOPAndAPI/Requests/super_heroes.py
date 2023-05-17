import requests


class SuperHeroes:
    def __init__(self):
        self.url = "https://akabab.github.io/superhero-api/api/all.json"

    def get_smartest_hero(self, heroes: list) -> str:
        response = requests.get(self.url)
        all_heroes = response.json()
        selected_heroes = []
        for hero in all_heroes:
            if hero['name'] in heroes:
                selected_heroes.append(hero)
        smartest_hero = max(selected_heroes, key=lambda h: h['powerstats']['intelligence'])
        return smartest_hero['name']

