from django.shortcuts import render, get_object_or_404
from django.db.models import Min

from cart.forms import CartAddProductForm
from main.models import ProductImage, ProductProperty, Product


def product_serializer(products):

    serialized_products = []
    for product in products:
        serialized_products.append(
            {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'available': product.available,
                'catalog': product.catalog,
                'slug': product.slug,
                'rating': product.rating,
                'tags': [tag for tag in product.tags.all()],
                'image': product.product_images.first(),
                'price': product.price,
            }
        )

    return serialized_products


def products(request):

    products = Product.objects.all().prefetch_related('properties').prefetch_related('product_images')
    serialized_products = product_serializer([product for product in products])

    context = {
        'products': products,
        'serialized_products': serialized_products,
    }

    return render(request, 'main/products.html', context)


def show_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    images = ProductImage.objects.filter(product=product)
    properies = ProductProperty.objects.filter(product=product)
    serialized_product = {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'images': images,
    }

    add_to_cart_form = CartAddProductForm()

    context = {
        'product': serialized_product,
        'images': images,
        'properties': properies,
        'add_to_cart_form': add_to_cart_form,
    }

    return render(request, 'main/show_product.html', context)
