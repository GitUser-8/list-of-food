from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import json
from datetime import date
from django.contrib.auth.decorators import login_required
from .models import Ingredient, Recipe, ShoppingList, UserInfo
from django.core import serializers

# Create your views here.

def index(request):
    """View function for home page of site."""

    ingredient_list = Ingredient.objects.all()

    context = {
        'ing_list': ingredient_list,
    }

    
    if request.user.is_authenticated:
        shoppinglist_list = serializers.serialize("json", ShoppingList.objects.filter(user=request.user))

        if shoppinglist_list:
            context['shoplists'] = shoppinglist_list
    
        favorite_shoppinglist = UserInfo.objects.filter(user=request.user.id).get().favorite
        context['favorite'] = favorite_shoppinglist


    response = render(request, 'index.html', context=context)

    # Get the clicked element id, add to the current list
    if request.method == "POST":
        post_data = json.loads(request.body.decode("utf-8"))
        if post_data["clicked_id"]:
            response.headers["clicked_id"] = post_data["clicked_id"]

    return response

@login_required
def save_shopping_list_name(request):
    if request.method == 'POST':
        list_to_update = ShoppingList.objects.get(user=request.user)
        list_to_update.name = request.POST["name"]
        list_to_update.save()
    return HttpResponse("Object has probably been saved.")

# def add_item_to_list_view(request):
#     response = HttpResponse("trying")
#     response.headers["my_header"] = 48000
#     if request.method == "POST":
#         post_data = json.loads(request.body.decode("utf-8"))
#         if post_data["id"] == 142:
#             response.headers["my_header"] = 49000
#     return response

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

