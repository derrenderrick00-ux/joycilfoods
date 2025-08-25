from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem

def menu_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'menu/menu_list.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        item.quantity += 1
        item.save()
    
    print("DEBUG: Added to cart:", item, "Qty:", item.quantity, "User:", item.user)

    return redirect('cart_detail')  # <-- show the cart after adding

#@login_required
#def cart_detail(request):
    items = CartItem.objects.filter(user=request.user).select_related('product')
    total = sum(i.product.price * i.quantity for i in items)
    return render(request, 'cart/cart_detail.html', {
        'cart_items': items,
        'total_price': total,
    })

#@login_required
#def update_quantity(request, item_id, action):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if action == 'increase':
        item.quantity += 1
        item.save()
    elif action == 'decrease':
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
    return redirect('cart_detail')

#@login_required
#def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart_detail')
