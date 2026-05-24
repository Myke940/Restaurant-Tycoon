from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import View


class Mainpage(View):
    template_name = 'mainpage.html'

    def get(self, request):
        context = {'slogan': settings.STATIC_URL + 'media/slogan.png'}
        return render(request, self.template_name, context)


class MenuView(View):
    template_name = 'menu.html'

    def get(self, request):
        dishes = Dish.objects.all()
        return render(request, self.template_name, {'dishes': dishes})


class IngredientView(View):
    template_name = 'ingredients.html'

    def get(self, request, pk):
        dish = get_object_or_404(Dish, id=pk)
        return render(request, self.template_name, {'dish': dish})


def recalc_order(order):
    total = 0
    for item in order.OrderItems.all():
        total += item.dish.price * item.quantity
        for adj in item.ingredient_adjustments.all():
            total += adj.quantity * adj.ingredient.price * item.quantity
    order.total_price = total
    order.save()


class AddToOrder(View):
    def get(self, request, dish_id):
        dish = get_object_or_404(Dish, id=dish_id)
        order, _ = Order.objects.get_or_create(user=request.user, status='pending')
        orderitem, created = OrderItem.objects.get_or_create(order=order, dish=dish)
        if not created:
            orderitem.quantity += 1
            orderitem.save()
        recalc_order(order)
        return redirect('dishmenu')


class CartView(View):
    template_name = 'orderMenu.html'

    def get(self, request):
        order = Order.objects.filter(user=request.user, status='pending').first()
        if not order:
            return render(request, self.template_name, {'order': None})

        items_data = []
        for item in order.OrderItems.all():
            dish_ingredients = item.dish.ingredients.all()
            adjustments = {a.ingredient_id: a.quantity for a in item.ingredient_adjustments.all()}
            ingredients = [
                {
                    'obj': ing,
                    'qty': adjustments.get(ing.id, 0),
                    'price': ing.price,
                }
                for ing in dish_ingredients
            ]
            items_data.append({'item': item, 'ingredients': ingredients})

        return render(request, self.template_name, {'order': order, 'items_data': items_data})

    def post(self, request):
        order = get_object_or_404(Order, user=request.user, status='pending')
        action = request.POST.get('action')

        if action == 'confirm':
            order.status = 'confirmed'
            order.save()
            return redirect('dishmenu')

        if action == 'adjust_ingredient':
            item_id = request.POST.get('item_id')
            ingredient_id = request.POST.get('ingredient_id')
            direction = request.POST.get('direction')

            order_item = get_object_or_404(OrderItem, id=item_id, order=order)
            ingredient = get_object_or_404(Ingredient, id=ingredient_id)

            adj, _ = OrderItemIngredient.objects.get_or_create(order_item=order_item, ingredient=ingredient)
            if direction == 'plus' and adj.quantity < 10:
                adj.quantity += 1
            elif direction == 'minus' and adj.quantity > -1:
                adj.quantity -= 1
            adj.save()
            recalc_order(order)

        if action == 'remove_item':
            item_id = request.POST.get('item_id')
            OrderItem.objects.filter(id=item_id, order=order).delete()
            recalc_order(order)

        return redirect('cart')


class OrderForWorker(View):
    template_name = 'worker_orders.html'

    def get(self, request):
        if not request.user.is_staff:
            return redirect('dishmenu')
        orders = Order.objects.filter(status='confirmed').order_by('-created_at')
        orders_data = []
        for order in orders:
            items_data = []
            for item in order.OrderItems.all():
                adjustments = {a.ingredient_id: a.quantity for a in item.ingredient_adjustments.all()}
                ingredients = [
                    {'obj': ing, 'qty': adjustments.get(ing.id, 0)}
                    for ing in item.dish.ingredients.all()
                ]
                items_data.append({'item': item, 'ingredients': ingredients})
            orders_data.append({'order': order, 'items_data': items_data})
        return render(request, self.template_name, {'orders_data': orders_data})

    def post(self, request):
        if not request.user.is_staff:
            return redirect('dishmenu')
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        order.status = 'done'
        order.save()
        return redirect('worker_orders')