from django.core.management.base import BaseCommand
from homework_django_2.models import Client


class Command(BaseCommand):
    help = 'Get all clients.'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        text = '\n'.join(str(client) for client in clients)
        self.stdout.write(f'{text}')
