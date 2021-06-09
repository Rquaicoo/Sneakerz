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
    if request.user.is_authenticated:
        customer = request.user.customer  
        order, created = Order.objects.get_or_create(customer=customer, complete= False)     
        items = order.orderitem_set.all() # gets order items that have order as parent
    else:
        items = []
        order = {'get_cart_total':0, 'get_items_total':0}
    context = {'items': items, 'order': order}
    return render(request, 'cart.html', context)



def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer  
        order, created = Order.objects.get_or_create(customer=customer, complete= False)     
        items = order.orderitem_set.all() # gets order items that have order as parent
    else:
        items = []
        order = {'get_cart_total':0, 'get_items_total':0}
    context = {'items': items, 'order': order}
    return render(request, 'checkout.html', context)