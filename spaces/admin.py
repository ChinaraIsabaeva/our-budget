from django.contrib import admin

from spaces.models import Space


class EnvelopesAdmin(admin.ModelAdmin):
    list_display = ('name', 'current_amount', 'monthly_replenishment')


admin.site.register(Space, EnvelopesAdmin)
