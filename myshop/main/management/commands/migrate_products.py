from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "upload products from server"

    def handle(self, *args, **options):
        pass