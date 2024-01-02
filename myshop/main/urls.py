from django.urls import path

from main import views

app_name = 'main'
urlpatterns = [
    path('products/', views.products, name='products'),
    path('edit_product/<slug:product_slug>', views.edit_product, name='edit_product')
]
