# -*- coding: utf-8 -*-

from django.forms import ModelForm, TextInput

from expenses.models import RegularMonthlyExpenses


class RegularExpensesForm(ModelForm):
    class Meta:
        model = RegularMonthlyExpenses
        fields = ['name', 'amount']
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Название'
                }
            ),
            'amount': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Сумма'
                }
            )
        }
