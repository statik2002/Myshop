import requests
from environs import Env
from django.core.management.base import BaseCommand, CommandError

from main.models import Product


env = Env()
env.read_env()
login = env.str('MOZAIKA_API_LOGIN')
password = env.str('MOZAIKA_API_PASSWORD')


class Command(BaseCommand):
    help = "update product images from neit.ru"

    def handle(self, *args, **options):
        products = Product.objects.all()



        # for product in products:


    def get_token(self):
        url = 'https://neit.ru/api/'