from django.urls import path

from cart import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart, name='cart'),
]
