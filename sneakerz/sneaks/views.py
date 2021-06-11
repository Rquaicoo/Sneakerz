from django.shortcuts import render
from django.http import JsonResponse, request
import json
import datetime
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

def signin_signup(request):
    return render(request, 'signin_signup.html')

def signin(request):
    return render(request, 'signin.html')




def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer  
        order, created = Order.objects.get_or_create(customer=customer, complete= False)     
        items = order.orderitem_set.all() # gets order items that have order as parent
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']
    
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems } #for passing in data
    return render(request, 'store.html', context)



def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer  
        order, created = Order.objects.get_or_create(customer=customer, complete= False)     
        items = order.orderitem_set.all() # gets order items that have order as parent
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_items_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)




def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer  
        order, created = Order.objects.get_or_create(customer=customer, complete= False)     
        items = order.orderitem_set.all() # gets order items that have order as parent
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)



def updateItem(request):
    data = json.loads(request.body) #passing in the data
    productId = data['productId'] #querying data from cart.js 
    action = data['action']

    print('Action: ', action)
    print('productId: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False) #get or create the order

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    #we use get or create because the item may already exist

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)#updates items in the cart

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) #get or create the order
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True  #prevents user from manipulating the data in the frontend
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                region = data['shipping']['region'],
                city = data['shipping']['city'],
                pickup = data['shipping']['pickup'],
                ) 
    else:
        print("User is not logged in..")
    return JsonResponse('Payment complete.', safe = False)

