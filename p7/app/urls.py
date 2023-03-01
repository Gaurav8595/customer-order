from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('order/', views.order, name="order"),
    path('customer/', views.customer, name="customer"),
    path('create_customer/', views.createCustomer, name='create_customer'),
    path('update_customer/<str:pk>', views.updateCustomer, name='update_customer'),
    path('delete_customer/<str:pk>', views.deleteCustomer, name='delete_customer'),

    path('product/', views.product, name="product"),
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<str:vidur>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete_order'),

    path('register_user/', views.registerUser, name="register_user"),
    path('login_user/', views.loginUser, name="login_user"),
    path('logout_user/', views.logoutUser, name="logout_user")


    

]
