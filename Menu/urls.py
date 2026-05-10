from .views import *
from django.urls import path

urlpatterns = [
   path('', Mainpage.as_view(), name='menu'),
   path('menu', MenuView.as_view(), name='dishmenu'),
   path('ingredients/<int:pk>', IngredientView.as_view(), name = 'ingredients'),
   path('ordering/<int:dish_pk>', OrderHere.as_view(), name = 'order'),

]





# "," 