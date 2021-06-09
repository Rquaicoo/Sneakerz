from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def signin(request):
    return render(request, 'signin.html')

def store(request):
    products = Product.objects.all()
    context = {'products': products} #for passing in data
    return render(request, 'store.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def checkout(request):
    context = {} 
    return render(request, 'checkout.html', context)