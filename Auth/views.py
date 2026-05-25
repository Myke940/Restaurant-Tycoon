from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib import messages
from django.views.generic import View
from django.urls import reverse_lazy

# Create your views here.


class Sign_in(View):
    template_name = "Authentications/signin.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords not similar to each other")
            return render(request, self.template_name)

        if User.objects.filter(username = username).exists():
            messages.error(request, "Username already exists")
            return render(request, self.template_name)

        user = User.objects.create_user(username = username, password = password1)
        login(request, user)
        return redirect("mainpage.html")

class Log_in(View):
    template_name = "Authentications/login.html"
    succes_url = reverse_lazy('login')
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        if username or password != None:
            try:
                u = authenticate(username = username, password = password)

                login(request, u)
                return redirect('mainpage')
            except Exception:
                return messages.error(request, "Error ---- check your password or username. If everything is okay with the data but u cant log in write an email to PizzaSaliItaliano423@gmail.com")


class Log_out(View):
    def get(self, request):
        logout(request)
        return redirect('mainpage')
"""      
class Log_in(View):
    def get(self, request, user, pw):
        if user in UserII.username:
            if pw == UserII.password:
                return login(request, user), redirect(template_name = "mainpage.html")
                
                
            
class Logout():
    def get(self, request):
        return logout(request), redirect(templat_name = "mainpage.html")
        
"""
    
            













