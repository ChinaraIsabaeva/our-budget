from django.db import models
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    EXPENSE_FREQUENCY = [
        ('m', 'monthly'),
        ('d', 'daily'),
        ('w', 'weekly'),
        ('q', 'quarterly'),
        ('ba', 'bi-annual'),
        ('y', 'yearly')
    ]

    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    frequency = models.CharField(
        choices=EXPENSE_FREQUENCY,
        default='m',
        max_length=2
    )

    class Meta:
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)
