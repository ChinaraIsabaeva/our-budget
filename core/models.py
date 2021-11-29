# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _


class Income(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = _("Income")
        verbose_name_plural = _("Incomes")

    def __str__(self):
        return '{}'.format(self.amount)
