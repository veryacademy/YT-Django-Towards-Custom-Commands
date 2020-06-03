from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'DB random user generator'

    def add_arguments(self, parser):
        parser.add_argument('qty', type=int, help='The amount of users to create')
        parser.add_argument('-a', '--admin', action='store_true', help='Define an admin account')

    def handle(self, *args, **kwargs):
        qty = kwargs['qty']
        admin = kwargs['admin']

        for i in range(qty):
            username = get_random_string(10)
            password = get_random_string(10)

            if admin:
                User.objects.create_superuser(username=username, email='', password=password)
            else:
                User.objects.create_user(username=username, email='', password=password)

            self.stdout.write('User "%s (%s)" account created!' % (username, password))