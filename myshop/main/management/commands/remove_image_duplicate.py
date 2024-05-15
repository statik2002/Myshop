from django.core.management.base import BaseCommand
from django.db.models import Count

from main.models import Product, ProductImage


class Command(BaseCommand):
    help = "Удаляет дубликаты картинок"

    def handle(self, *args, **options):
        products = Product.objects.prefetch_related('product_images').annotate(image_count=Count('product_images__image')).filter(image_count__gt=0)

        img_for_delete = []

        for product in products:
            prev_image = None
            for product_image in product.product_images:
                if product_image.image == prev_image:
                    img_for_delete.append(product_image)
                    
                prev_image = product_image.image

        
        for img in img_for_delete:
            img.delete()