from django.core.management.base import BaseCommand
from homework_django_2.models import Product


class Command(BaseCommand):
    help = "Create new client."

    def handle(self, *args, **kwargs):
        client = Client(name='Bob', email='bob@example.com', phone='7654321', address='Saint-Petersburg, the best city')
        client.save()
        self.stdout.write(f'{client} has been registered successfully')