from django.contrib import admin
from .models import Ingredient, Recipe, ShoppingList

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(ShoppingList)

class ShoppingListAdmin(admin.ModelAdmin):
    pass