from django.db import models

from main.models import Customer, Product


class Cart(models.Model):

    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return f'{self.user.phone_number} -> {self.products.count()}'
