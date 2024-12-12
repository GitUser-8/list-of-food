from django.shortcuts import render

# Create your views here.

from .models import Ingredient, Recipe, ShoppingList

def index(request):
    """View function for home page of site."""

    num_ing = Ingredient.count()
    num_recipe = Recipe.count()
    num_shoplist = ShoppingList.count()

    context = {
        'num_ing': num_ing,
        'num_recipe': num_recipe,
        'num_shoplist': num_shoplist,
    }

    return render(request, 'index.html', context=context)
