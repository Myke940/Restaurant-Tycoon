from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from .models import UserII
from django.contrib import messages
from django.views.generic import View
from django.urls import reverse_lazy

# Create your views here.

class Sign_in(View):
    model = UserII
    template_name = 'authenticate/signin.html'
    success_url = reverse_lazy('signing')
    def get(self, request, password1, password2, user, adress, pn):
        if password1 == password2:
            UserII.password = password1
            UserII.username = user
            UserII.save()
            if adress:
                UserII.adress = adress
            if pn:
                UserII.phonenumber = pn
                return login(request, user), redirect(template_name = "mainpage.html")
        else:             #return self.unique_error_message('Passwords are not similar to each other. Please check and rewrite th passwords correct')
            messages.error(request, "Passwords are not similar to each other. Please check and rewrite th passwords correct")
            return render(request, template_name="")
            
        
class Log_in(UserII):
    def get(self, request, user, pw):
        if user in UserII.username:
            if pw == UserII.password:
                return login(request, user), redirect(template_name = "mainpage.html")
                
                
            
class Logout():
    def get(self, request):
        return logout(request), redirect(templat_name = "mainpage.html")
        

    
            













