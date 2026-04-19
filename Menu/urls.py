from .views import *
from django.urls import path

urlpatterns = [
   path('', Mainpage.as_view(), name='menu'),
   path('menu', MenuView.as_view(), name='dishmenu')


]