from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout" ),
    
    
    path('update_item/', views.updateItem, name="update_item"),#path for update items
    path('process_order/', views.processOrder, name="process_order")
]