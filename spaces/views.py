# -*- coding: utf-8 -*-

from django.urls import reverse
from django.views.generic import UpdateView, CreateView, ListView, DeleteView

from core.views import CustomLoginRequiredMixin
from spaces.forms import SpacesForm
from spaces.models import Space


class SpaceListView(CustomLoginRequiredMixin, ListView):
    model = Space
    template_name = 'spaces/spaces.html'
    context_object_name = 'spaces'


class SpaceCreateView(CustomLoginRequiredMixin, CreateView):
    model = Space
    template_name = 'spaces/space_create.html'
    form_class = SpacesForm

    def get_success_url(self):
        return reverse('spaces:spaces_all')


class SpaceUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Space
    template_name = 'spaces/space_update.html'
    form_class = SpacesForm

    def get_success_url(self):
        return reverse('spaces:spaces_all')


class SpaceDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Space
    context_object_name = 'object'

    def get_success_url(self):
        return reverse('spaces:spaces_all')
