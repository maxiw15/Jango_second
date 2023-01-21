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


def recipes(request, cook):
    count = int(request.GET.get("servings", 1))
    recipes = DATA.get(cook)
    new_recipe = {}
    for key, value in recipes.items():
        new_recipe[key] = value * count
    context = {"recipe": new_recipe}
    return render(request, 'calculator/index.html', context)
