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
    model = Order
    pass

class OrderForWorker(View):
    def get(self):
        pass



class IngredientView(View):
    template_name = 'ingredients.html'
    reverse_lazy = 'ingredients'
    model = Ingredient
    def get(self, request, pk):
        dish = Dish.objects.get(id = pk)
        #ingredients = dish.ingredients.all()
        return render(request, self.template_name, {'dish': dish })



class Delivery(View):
    model = Deliver
    template_name = 'Ordermenu.html'
    reverse_lazy = 'ordermenu'
    def get(request, self, orderview_price):
        costs = orderview_price + 10
        return render(request, self.template.name, costs)


















