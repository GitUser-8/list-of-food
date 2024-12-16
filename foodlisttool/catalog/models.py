from django.db import models
from django.urls import reverse
import datetime
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered_recipes = models.ManyToManyField("Recipe")
    favorite = models.ForeignKey("ShoppingList", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class Ingredient(models.Model):
    """Model reprenting an ingredient."""
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/ingredients/', null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a particular ingredient instance."""
        return reverse('ingredient-detail', args=[str(self.id)])

class Recipe(models.Model):
    """Model representing a recipe."""
    name = models.CharField(max_length=100, null=True)
    ing_list = models.ManyToManyField(Ingredient)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular recipe instance."""
        return reverse('recipe-detail', args=[str(self.id)])
    
class ShoppingList(models.Model):
    """Model representing a store list."""
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True)
    name = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    ing_list = models.ManyToManyField(Ingredient, blank=True)
    recipe_list = models.ManyToManyField(Recipe, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.user.username+" - "+self.date.strftime('%d/%m/%Y')

    def get_absolute_url(self):
        """Returns the url to access a particular shopping list instance."""
        return reverse('shoppinglist-detail', args=[str(self.id)])
