from django.forms import forms, ModelForm

from main.models import Product


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
