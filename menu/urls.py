from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    #path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]