from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listes/', views.ShoppingListListView.as_view(), name='shoppinglists'),
    path('liste/<int:pk>', views.ShoppingListDetailView.as_view(), name='shoppinglist-detail')
]

