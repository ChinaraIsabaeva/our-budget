from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import (
    ModelForm,
    TextInput,
    PasswordInput,
    CharField
)
from django.utils.translation import gettext_lazy as _

from core.models import Income


class LoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'placeholder': 'username'
            }
        ),
    )
    password = CharField(
        strip=False,
        widget=PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }
        ),
    )


class IncomeForm(ModelForm):
    class Meta:
        model = Income
        fields = ['name', 'amount']
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
            )
        }
