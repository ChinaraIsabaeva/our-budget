# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)
from django.urls import reverse

from core.forms import IncomeForm
from core.models import Income
from spaces.models import Space


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class HomeView(CustomLoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        spaces = Space.objects.exclude(closed=True).order_by('name')
        context['spaces'] = spaces
        return context


class IncomeCreateView(CustomLoginRequiredMixin, CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'incomes/income_create.html'

    def get_success_url(self):
        return reverse('incomes_all')


class IncomeDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Income
    context_object_name = 'object'

    def get_success_url(self):
        return reverse('incomes_all')


class IncomeUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Income
    template_name = 'incomes/income_update.html'
    form_class = IncomeForm

    def get_success_url(self):
        return reverse('incomes_all')


class IncomeListView(CustomLoginRequiredMixin, ListView):
    template_name = 'incomes/incomes.html'
    model = Income
    context_object_name = 'incomes'
