from django.urls import path
from .views import *

urlpatterns = [
    path('authentication/Sign_in', Sign_in.as_view(), name = 'signing')
]