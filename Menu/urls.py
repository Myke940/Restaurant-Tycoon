from .views import *
from django.urls import path

urlpatterns = [
   path('', Mainpage.as_view(), name='menu'),
   path('menu', MenuView.as_view(), name='dishmenu'),
   path('ingredients/<int:pk>', IngredientView.as_view(), name='ingredients'),
   path('ordering/<int:dish_id>', AddToOrder.as_view(), name='order'),
   path('cart', CartView.as_view(), name='cart'),
   path('worker/orders', OrderForWorker.as_view(), name='worker_orders'),   
   path('Homepage', Mainpage.as_view(), name = 'mainpage')

]





# "," 