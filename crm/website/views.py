from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'website/home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass