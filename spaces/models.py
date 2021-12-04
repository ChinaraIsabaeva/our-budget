from django.db import models
from django.utils.translation import gettext_lazy as _


class Space(models.Model):
    name = models.CharField(max_length=255)
    current_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )
    monthly_replenishment = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    closed = models.BooleanField(default=False)
    max_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('Space')
        verbose_name_plural = _('Spaces')
        ordering = ('name', )

    def __str__(self):
        return f"{self.name}"

    @property
    def get_absolute_url(self):
        return f"/{self.name}/"
