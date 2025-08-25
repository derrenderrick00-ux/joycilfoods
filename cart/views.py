import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import CartItem
from menu.models import Product   # make sure Product is imported from the right app

logger = logging.getLogger(__name__)

# 🛒 Add product to cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Create or update cart item
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity = F("quantity") + 1
        cart_item.save()
        cart_item.refresh_from_db()

    logger.debug(f"CartItem saved -> {cart_item.quantity} x {product.name} for {request.user.username}")

    return redirect("cart_detail")


# 🛒 Show cart details
@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.subtotal for item in cart_items)

    logger.debug(f"Cart detail fetched {cart_items.count()} items for {request.user.username}")
    for ci in cart_items:
        logger.debug(f" - {ci.product.name}: {ci.quantity} (Subtotal {ci.subtotal})")

    return render(request, "cart/cart_detail.html", {
        "cart_items": cart_items,
        "total_price": total_price
    })


# 🛒 Update quantity
@login_required
def update_quantity(request, item_id, action):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)

    if action == "increase":
        cart_item.quantity = F("quantity") + 1
        cart_item.save()
    elif action == "decrease" and cart_item.quantity > 1:
        cart_item.quantity = F("quantity") - 1
        cart_item.save()
    elif action == "decrease" and cart_item.quantity == 1:
        cart_item.delete()
        logger.debug(f"Removed {cart_item.product.name} for {request.user.username} (quantity was 1)")
        return redirect("cart_detail")

    cart_item.refresh_from_db()
    logger.debug(f"Updated quantity -> {cart_item.quantity} x {cart_item.product.name} for {request.user.username}")

    return redirect("cart_detail")


# 🛒 Remove item from cart
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    logger.debug(f"Removed {cart_item.product.name} for {request.user.username}")
    cart_item.delete()
    return redirect("cart_detail")
