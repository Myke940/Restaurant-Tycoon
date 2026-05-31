from django.db import models
from django.contrib.auth.models import User


class Mainpage(models.Model):
    pass


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='ingredient_images/', blank=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    image = models.ImageField(upload_to='menu_images/')

    def ingredient_list(self):
        return ", ".join([i.name for i in self.ingredients.all()])
    
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='UserOrders')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order by {self.user.username}, status: {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='OrderItems')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Ordered {self.dish.name} ({self.quantity} items) in {self.order}"


class OrderItemIngredient(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='ingredient_adjustments')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)  # negative = removed, positive = extra


class Deliver(models.Model):
    location = models.TextField()