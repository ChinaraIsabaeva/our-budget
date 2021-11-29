from django.forms import ModelForm, TextInput, Select
from django.utils.translation import gettext_lazy as _

from expenses.models import Expense


class ExpensesForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'frequency']
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Name')
                }
            ),
            'amount': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Amount')
                }
            ),
            'frequency': Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Frequency')
                }
            )
        }
