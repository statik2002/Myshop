import io
import sys
import requests
from environs import Env
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from main.models import Product, ProductImage
from django.core.files import File
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from django.core.files.temp import NamedTemporaryFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from .utils import convert_image


env = Env()
env.read_env()
login = env.str('MOZAIKA_API_LOGIN')
password = env.str('MOZAIKA_API_PASSWORD')
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Command(BaseCommand):
    help = "update product images from neit.ru"

    def get_products(self, api_path: str) -> None:

        products = Product.objects.all()
        for product in products:

            data = {
                "code1c": product.code_1c
            }

            response = requests.get('https://neit.ru/api/v1/goods/get_good/', data=data, verify=False, timeout=6000)
            if response.status_code == 200:

                remote_product = response.json()
                print(f'Images = {remote_product.get("images")}')
                if len(remote_product.get('images')) < 1:
                    print(f'For product {product.name} have no images.')
                    continue

                try:
                    for image in remote_product.get('images'):
                        img = requests.get(f'https://neit.ru{image.get("image")}', verify=False)
                        if img.status_code == 200:
                            img_name = image.get('image').split('/')[-1]
                            resize_image = convert_image(Image.open(io.BytesIO(img.content)))
                            tmp_img = io.BytesIO()
                            resize_image.save(tmp_img, format='webp')
                            product_image = ProductImage.objects.create(
                                product=product, 
                                alt=img_name, 
                                image=InMemoryUploadedFile(tmp_img, None, img_name, 'image/webp', sys.getsizeof(tmp_img), None)
                                )
                            print(f'Image updated for {product.name}')

                except ObjectDoesNotExist:
                    print(f'Error get image for product: {product.name}')
                    continue
            else:
                print(f'Product {product.name} have no on site')

                

    def handle(self, *args, **options):
        products = Product.objects.all()

        self.get_products('https://neit.ru/api/v1/goods/get_good/')

        # for product in products:

