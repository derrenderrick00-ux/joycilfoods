# menu/admin.py
from django.contrib import admin
from .models import Product, CartItem

# Product admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')  # columns in the list view
    list_filter = ('available',)                  # filter by availability
    search_fields = ('name', 'description')       # search by name or description
    ordering = ('name',)                          # default ordering

# CartItem admin
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_at')  # columns to show
    search_fields = ('user__username', 'product__name')          # search by user or product
    list_filter = ('added_at',)                                  # filter by date added
    ordering = ('-added_at',)                                    # latest first
