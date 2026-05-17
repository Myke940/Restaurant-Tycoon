from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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
    name = models.CharField(max_length = 20)
    price = models.FloatField()
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    image = models.ImageField(upload_to = 'menu_images/')
    def ingredient_list(self):
        return ", ".join([ingredient.name for ingredient in self.ingredients.all()])
       

class ImproveappendedDish(models.Model):
    name = models.CharField(max_length = 20)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'menu_images/')
    '''def post(self):
        for ingredient in Dish.ingredients:
            if Ingredient.name is ingredient:
                value = 
            value = models.IntegerField(choices=[(1, "Upvote"), (0, "Downvote")])'''
            

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, related_name = 'UserOrders')
    total_price = models.DecimalField(max_digits=8, decimal_places=2, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    orderis = models.BooleanField(default = True) #if order is active or not (TRUE False)
    
            

                 
        
# for workers

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='OrderItems')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    extra_ingredients = models.ManyToManyField(
        Ingredient,
        blank=True,
        related_name='extra_in_order_items'
    )
    removed_ingredients = models.ManyToManyField(
        Ingredient,
        blank=True,
        related_name='removed_in_order_items'
    )


class Deliver(models.Model):
    location = models.TextField()
    def get(self, reuqest, total_price):
        extrasdeliver = total_price + 10
        


