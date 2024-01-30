from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('products/', views.products, name='products'),
    path('product/<int:product_id>', views.show_product, name='show_product'),
]
