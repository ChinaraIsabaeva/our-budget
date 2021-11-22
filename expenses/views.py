# -*- coding: utf-8 -*-

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse

from expenses.forms import RegularExpensesForm
from expenses.models import RegularMonthlyExpenses


class ExpenseUpdateView(UpdateView):
    model = RegularMonthlyExpenses
    template_name = 'expenses/expense_update.html'
    form_class = RegularExpensesForm


class ExpenseCreateView(CreateView):
    model = RegularMonthlyExpenses
    form_class = RegularExpensesForm

    def get_success_url(self):
        return reverse('expenses:all')


class RegularExpenseListView(ListView):
    template_name = 'expenses/regular_expenses.html'
    model = RegularMonthlyExpenses
    context_object_name = 'expenses'

