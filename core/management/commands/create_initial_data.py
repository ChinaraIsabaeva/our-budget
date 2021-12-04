from django.core.management.base import BaseCommand

from core.models import Income
from expenses.models import Expense
from spaces.models import Space


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Management command to update spaces
        """
        Income.objects.create(name='Salary', amount=2400)

        Expense.objects.create(name='Rent', amount=950)
        Expense.objects.create(name='Utility bills', amount=150)
        Expense.objects.create(name='Internet', amount=33)
        Expense.objects.create(name='Grocery', amount=400)
        Expense.objects.create(name='Car insurance', amount=50)

        Space.objects.create(name='Holidays', monthly_replenishment=100)
        Space.objects.create(name='Gifts for family', monthly_replenishment=100)

