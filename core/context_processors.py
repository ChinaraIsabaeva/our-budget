from django.db.models import Sum
from core.models import Income
from spaces.models import Space
from expenses.models import Expense
from core.utils import available_amount


def get_aggregated_data(request):
    income = Income.objects.all().aggregate(total=Sum('amount'))
    free_money = available_amount()
    if income['total'] is None:
        income_total = 0
    else:
        income_total = income['total']

    total_spaces = Space.objects.filter(
        closed=False).aggregate(total=Sum('current_amount'))
    if total_spaces['total'] is None:
        total_spaces = 0
    else:
        total_spaces = total_spaces['total']

    total_spaces_monthly = Space.objects.filter(
        closed=False).aggregate(total=Sum('monthly_replenishment'))
    if total_spaces_monthly['total'] is None:
        total_spaces_monthly = 0
    else:
        total_spaces_monthly = total_spaces_monthly['total']

    sum_regular_expenses = Expense.objects.all().aggregate(
        total=Sum('amount')
    )
    if sum_regular_expenses['total'] is None:
        sum_regular_expenses = 0
    else:
        sum_regular_expenses = sum_regular_expenses['total']

    context = {
        'available_amount': free_money,
        'income': income_total,
        'total_spaces': total_spaces,
        'total_spaces_monthly': total_spaces_monthly,
        'total_regular': sum_regular_expenses
    }
    return context
