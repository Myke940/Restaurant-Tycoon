from django.contrib import admin
from .models import Dish, Ingredient, ImproveappendedDish
# Register your models here.

admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(ImproveappendedDish)