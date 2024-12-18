from django.contrib import admin
from .models import Ingredient, Recipe, ShoppingList, UserInfo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Recipe)

class ShoppingListAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShoppingList, ShoppingListAdmin)

class UserInfoInLine(admin.StackedInline):
    model = UserInfo
    can_delete = False
    verbose_name_plural = "userinfo"

class UserAdmin(BaseUserAdmin):
    inlines = [UserInfoInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)