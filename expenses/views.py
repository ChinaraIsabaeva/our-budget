# -*- coding: utf-8 -*-


from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse

from core.views import CustomLoginRequiredMixin
from expenses.forms import ExpensesForm
from expenses.models import Expense


class ExpenseCreateView(CustomLoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpensesForm
    template_name = 'expenses/income_create.html'

    def get_success_url(self):
        return reverse('expenses:expenses_all')


class ExpenseUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Expense
    template_name = 'expenses/income_update.html'
    form_class = ExpensesForm

    def get_success_url(self):
        return reverse('expenses:expenses_all')


class ExpenseDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Expense
    context_object_name = 'object'

    def get_success_url(self):
        return reverse('spaces:spaces_all')


class ExpenseListView(CustomLoginRequiredMixin, ListView):
    template_name = 'expenses/expenses.html'
    model = Expense
    context_object_name = 'expenses'
