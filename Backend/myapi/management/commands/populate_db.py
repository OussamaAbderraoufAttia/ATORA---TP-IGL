import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from users.models import Utilisateur

class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        # get or create superuser
        user = Utilisateur.objects.filter(username='admin').first()
        if not user:
            user = Utilisateur.objects.create_superuser(username='admin', password='test')




