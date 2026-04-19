from django.shortcuts import render
from .models import *
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import View
# Create your views here.


class Mainpage(View):
    template_name = 'mainpage.html'
    model = Mainpage
    context_object_name = 'mainpage'
    success_url = reverse_lazy('menu')
    def get(self, request):
        context = {'slogan': settings.STATIC_URL + 'media/slogan.png'}
        return render(request, self.template_name, context)
    


class MenuView(View):
    template_name = 'menu.html'
    model = Dish
    success_url = reverse_lazy('dishmenu')
    def get(self, request):
        dishes = Dish.objects.all()
        return render(request, self.template_name, {'dishes': dishes})

class DishDetailView(View):
    template_name = 'detail.html'
    model = Dish
    def get(self, request, dish_id):
        dish = Dish.objects.get(id=dish_id)
        return render(request, self.template_name, {'dish': dish})

class OrderView(View):
    template_name = 'order.html'
    model = Order
    def post(self, request):
        # Logic to create an order based on the posted data
        pass

class IngredientView(View):
    template_name = 'Dish_ingredients.html'
    model = Ingredient
    def get(self, request, dish_id):
        dish = Dish.objects.get(id=dish_id)
        ingredients = dish.ingredients.all()
        return render(request, self.template_name, {'ingredients': ingredients})




















