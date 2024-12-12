from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Ingredient, Recipe, ShoppingList

def index(request):
    """View function for home page of site."""

    num_ing = Ingredient.objects.count()
    num_recipe = Recipe.objects.count()
    num_shoplist = ShoppingList.objects.count()

    context = {
        'num_ing': num_ing,
        'num_recipe': num_recipe,
        'num_shoplist': num_shoplist,
    }

    return render(request, 'index.html', context=context)

class ShoppingListListView(generic.ListView):
    model = ShoppingList

class ShoppingListDetailView(generic.DetailView):
    model = ShoppingList

class IngredientListView(generic.ListView):
    model = Ingredient

class IngredientDetailView(generic.DetailView):
    model = Ingredient

class RecipeListView(generic.ListView):
    model = Recipe

class RecipeDetailView(generic.DetailView):
    model = Recipe