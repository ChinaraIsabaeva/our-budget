# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

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
