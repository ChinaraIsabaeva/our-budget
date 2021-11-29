# -*- coding: utf-8 -*-

from django.forms import (
    Form,
    ModelForm,
    TextInput,
    ModelChoiceField,
    CheckboxInput,
    Select
)
from django.utils.translation import gettext_lazy as _

from spaces.models import Space


class SpacesForm(ModelForm):
    class Meta:
        model = Space
        fields = [
            'name',
            'monthly_replenishment',
            'closed',
            'max_amount'
        ]
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Name')
                }
            ),
            'monthly_replenishment': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Monthly payment')
                }
            ),
            'max_amount': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Max space amount')
                }
            ),
            'closed': CheckboxInput(attrs={'class': 'checkbox'})
        }

        labels = {
            'closed': _('Closed'),
        }

    def __init__(self, *args, **kwargs):
        super(SpacesForm, self).__init__(*args, **kwargs)
        message = _('Missed required field')
        for field in self.fields:
            self.fields[field].error_messages['required'] = message
