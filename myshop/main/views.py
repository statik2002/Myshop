from django.forms import modelform_factory, modelformset_factory, inlineformset_factory
from django.shortcuts import render, get_object_or_404

from main.forms import ProductForm
from main.models import Product, Metrics, Color


def products(request):

    products = Product.objects.all().prefetch_related('metrics').prefetch_related('colors')

    context = {
        'products': products,
    }

    return render(request, 'main/products.html', context)


def edit_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    productformset = inlineformset_factory(Product, Metrics, exclude=('product', 'id'), extra=0)
    productcolorformset = inlineformset_factory(Product, Color, fields=('value',), extra=1)
    product_form = modelform_factory(Product, ProductForm, exclude=('rating', 'create_date', 'show_count'))

    metrics_formset = productformset(instance=product)
    colorformset = productcolorformset(instance=product)
    product_form = product_form(instance=product)

    context = {
        'metricsformset': metrics_formset,
        'colorformset': colorformset,
        'product_form': product_form
    }

    return render(request, 'main/edit_product.html', context)


def add_property(request):

    context = {

    }

    return render(request, 'main/add_property.html', context)
