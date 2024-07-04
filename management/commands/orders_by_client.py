from django.core.management.base import BaseCommand
from homework_django_2.models import Client, Order


class Command(BaseCommand):
    help = "Get orders by clients id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        orders = Order.objects.filter(client__pk=pk)
        intro = f'All orders\n'
        text = '\n'.join(str(order) for order in orders)
        self.stdout.write(f'{intro}{text}')