from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('', views.home, name="home"),

    path('signup/', views.signup, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name ="resetpassword.html" ), 
    name="reset_password"),
    
    path('reset_password_sent/',
     auth_views.PasswordResetDoneView.as_view(template_name ="resetsent.html"),
      name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name ="resetform.html"), 
    name="password_reset_confirm"),
    
    path('reset_password_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name ="resetcomplete.html"), 
    name="password_reset_complete"),

    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout" ),
    
    
    path('update_item/', views.updateItem, name="update_item"),#path for update items
    path('process_order/', views.processOrder, name="process_order")
]