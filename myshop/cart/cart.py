from decimal import Decimal

from main.models import Product, ProductImage
from myshop import settings


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, product: Product, quantity=1, override_quantity: bool = False):
        product_id = str(product.pk)
        product_images = ProductImage.objects.filter(product=product)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'cart_quantity': 0,
                'price': str(product.price),
                'images': product_images.first().image.url,
            }

        if override_quantity:
            self.cart[product_id]['cart_quantity'] = quantity
        else:
            self.cart[product_id]['cart_quantity'] += quantity

        self.save()

    def remove(self, product: Product):
        product_id = str(product.pk)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.pk)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['cart_quantity']
            yield item

    def __len__(self):
        return sum(item['cart_quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price'] * item['cart_quantity']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
