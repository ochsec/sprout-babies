from django.contrib import admin
from .models import StateTax

@admin.register(StateTax)
class StateTaxAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbr', 'tax_rate']
    list_filter = ['name', 'abbr']
    list_editable = ['tax_rate']

