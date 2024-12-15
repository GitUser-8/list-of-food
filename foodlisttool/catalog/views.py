from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
import json

# Create your views here.

from .models import Ingredient, Recipe, ShoppingList

def index(request):
    """View function for home page of site."""

    all_ing_list = Ingredient.objects.all()

    context = {
        'ing_list': all_ing_list
    }

    if request.method == "POST":
        post_data = json.loads(request.body.decode("utf-8"))
        context['id_posted'] = post_data['id']

    

    return render(request, 'index.html', context=context)

def add_item_to_list_view(request):
    if request.method == "POST":
        post_data = json.loads(request.body.decode("utf-8"))
        return post_data['id']

class ShoppingListDetailView(LoginRequiredMixin, generic.DetailView):
    model = ShoppingList

class ShoppingListByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing shopping lists to current user."""
    model = ShoppingList
    template_name = 'catalog/shoppinglist_list_user.html'
    
    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user).order_by('date')

class IngredientListView(generic.ListView):
    model = Ingredient

class IngredientDetailView(generic.DetailView):
    model = Ingredient

class RecipeListView(generic.ListView):
    model = Recipe

class RecipeDetailView(generic.DetailView):
    model = Recipe

