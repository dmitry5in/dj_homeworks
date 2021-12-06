from django.shortcuts import render, reverse


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

}


def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Рецепт омлета': reverse('omlet'),
        'Рецепт пасты': reverse('pasta'),
        'Рецепт бутерброда': reverse('buter')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def recipes(request):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    for keys in DATA.keys():
        if keys in request.path:
            recipe = DATA.get(keys).copy()
    template_name = 'calculator/index.html'
    for key in recipe.keys():
        recipe[key] = recipe.get(key) * servings
    context = {
        'recipe': recipe,
        }
    return render(request, template_name, context)
