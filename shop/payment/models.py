from django.db import models

class StateTax(models.Model):
    name = models.CharField(max_length=25, db_index=True, unique=True)
    abbr = models.CharField(max_length=2, unique=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=3)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name