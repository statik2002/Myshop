from decimal import Decimal
from django.core.management.base import BaseCommand, CommandError

from main.models import Product
from main.tg_bot import main


class Command(BaseCommand):
    help = "Telegram bot"

    def handle(self, *args, **options):
        
        main()