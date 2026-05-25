from django.urls import path
from .views import *

urlpatterns = [
    path('Sign_in', Sign_in.as_view(), name = 'signin'),
    path('Log_in', Log_in.as_view(), name = 'login'),
    path('Log_outs', Log_out.as_view(), name = 'logout'),
]