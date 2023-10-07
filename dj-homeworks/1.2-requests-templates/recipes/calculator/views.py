from django.http import HttpRequest
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def get_recipe(name: str, servings: int) -> dict[str, int]:
    ingredients = {}
    for ingredient, amount in DATA[name].items():
        ingredients[ingredient] = amount * servings
    return ingredients


def get_omlet(request: HttpRequest):
    servings = int(request.GET.get('servings', 1))
    context = {
      'recipe': get_recipe('omlet', servings)
    }
    return render(request, 'calculator/index.html', context)


def get_pasta(request: HttpRequest):
    servings = int(request.GET.get('servings', 1))
    context = {
      'recipe': get_recipe('pasta', servings)
    }
    return render(request, 'calculator/index.html', context)


def get_buter(request: HttpRequest):
    servings = int(request.GET.get('servings', 1))
    context = {
      'recipe': get_recipe('buter', servings)
    }
    return render(request, 'calculator/index.html', context)
