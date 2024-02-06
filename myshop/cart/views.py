from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddProductForm
from main.models import Product, ProductImage


def cart_detail(request):
    cart = Cart(request)

    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart.html', context)


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        form_cleaned_data = form.cleaned_data
        cart.add(product=product, quantity=form_cleaned_data['quantity'], override_quantity=form_cleaned_data['override'])

    return redirect('cart:cart_detail')


@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

