from django.db.models import Sum
from spaces.models import Space

from core.models import Income
from expenses.models import Expense


def available_amount():
    incomes = Income.objects.all().aggregate(total=Sum('amount'))
    expenses = Expense.objects.all().aggregate(
        total=Sum('amount')
    )
    spaces = Space.objects.all().filter(
        closed=False).aggregate(total=Sum('monthly_replenishment')
                                )
    if incomes['total'] is None:
        incomes_total = 0
    else:
        incomes_total = incomes['total']
    if expenses['total'] is None:
        expenses_total = 0
    else:
        expenses_total = expenses['total']
    if spaces['total'] is None:
        spaces_total = 0
    else:
        spaces_total = spaces['total']
    free_money = incomes_total - expenses_total - spaces_total
    return free_money
