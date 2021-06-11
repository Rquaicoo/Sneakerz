from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('signin_signup/', views.signin_signup, name="signin_signup"),
    path('signin/', views.signin, name="signin"),
    
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout" ),
    
    
    path('update_item/', views.updateItem, name="update_item"),#path for update items
    path('process_order/', views.processOrder, name="process_order")
]