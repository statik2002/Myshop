from decimal import Decimal
from django.core.management.base import BaseCommand, CommandError

from main.models import Product


class Command(BaseCommand):
    help = "Наценить товары по онлайн цене"

    def add_arguments(self, parser):
        parser.add_argument('margin', type=float)

    def handle(self, *args, **options):
        
        products = Product.objects.all()
        if options['margin']:
            add_price = options['margin']
        else:
            add_price = 1.3

        print(add_price)

        for product in products:
            if product.first_price == 0:
                continue

            if product.price == product.first_price:
                continue

            calc_price = product.first_price * Decimal(add_price)

            product.online_price = Decimal(calc_price).quantize(1) + 1
            product.save()
        
        print('margin is set')