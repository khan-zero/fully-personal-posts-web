from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .context import get_context
from .forms import Nimadur

def index(request):
    context = get_context()
    return render(request, 'index.html', context)


def register(request):
    if request.method == "POST":
        User.objects.create_user(
            username = reuest.POST['username'],
            password = request.POST['password']
        )
    return render(request, "register.html")

def login_user(request):
    if render.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authanticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, "login.html")
    
def log_out(request):
    logout(request)
    return redirect('index')
    
def archive(request):
    context = get_context()
    return render(request, "archive.html", {'user_info': user_info})
    
def contact(request):
    context = get_context()
    return render(request, "contact.html", context)
    
def profile_card(request, id):
    user = User.objects.get(id = id)
    context = {
        'user_info': user
    }
    return render(request, 'profile_card.html', context)

