from django.db import models

# Create your models here.

class Mainpage(models.Model):
    pass

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='ingredient_images/', blank=True)


class Dish(models.Model):
    name = models.CharField(max_length = 20)
    price = models.FloatField()
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    image = models.ImageField(upload_to = 'menu_images/')
    def ingredient_list(self):
        value = models.IntegerField(choices=[(1, "Upvote"), (0, "Downvote")])
        return ", ".join([ingredient.name for ingredient in self.ingredients.all()])
       

class ImproveappendedDish(models.Model):
    name = models.CharField(max_length = 20)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'menu_images/')
    def ingredient_list(self):
        for ingredient in Dish.ingredients:
            value = models.IntegerField(choices=[(1, "Upvote"), (0, "Downvote")])
            if value == 0:
                pass
                 


    
class Order(models.Model):
    items = models.ManyToManyField(Dish)
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 20, default = 'Pending')
    created_by = models.CharField(max_length = 20, default = 'Guest')
    

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



