from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('signin/', views.signin, name="signin"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout" )
]