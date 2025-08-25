from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self): 
        return self.name

# CartItem model
class CartItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='menu_cartitems'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='menu_cartitems'
    )
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.user.username}"
