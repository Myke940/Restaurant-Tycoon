from django.contrib import admin
from .models import Dish, Ingredient, Order, OrderItem, OrderItemIngredient, Deliver
# Register your models here.

admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderItemIngredient)
admin.site.register(Deliver)