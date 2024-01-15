from django.shortcuts import render
from main.models import Product


def products(request):

    products = Product.objects.all().prefetch_related('properties').prefetch_related('product_images')

    context = {
        'products': products,
    }

    return render(request, 'main/products.html', context)

