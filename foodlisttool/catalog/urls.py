from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listes/', views.ShoppingListListView.as_view(), name='shoppinglists'),
    path('liste/<int:pk>', views.ShoppingListDetailView.as_view(), name='shoppinglist-detail'),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredients'),
    path('ingredient/<int:pk>', views.IngredientDetailView.as_view(), name='ingredient-detail'),
    path('recettes/', views.RecipeListView.as_view(), name='recipes'),
    path('recette/<int:pk>', views.RecipeDetailView.as_view(), name='recipe-detail'),
]

