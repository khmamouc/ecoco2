from django.db import models


class Rates(models.Model):
    datetime = models.DateTimeField(help_text="Datetime")
    co2_rate = models.IntegerField(help_text="CO2 rate")
