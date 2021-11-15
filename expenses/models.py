from django.db import models, transaction


class RegularMonthlyExpenses(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Постоянный месячный расход'
        verbose_name_plural = 'Постоянные месячные расходы'
        ordering = ['name']

    def __str__(self):
        return '{name}'.format(name=self.name)
