from django.db import models
from django.utils import timezone


class WaterReading(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    water_gallons_used = models.IntegerField(default=0)
    water_tank_level = models.IntegerField(default=0)
    chlorinator_tank_level = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.created_at.strftime("%b %d %Y %H:%M:%S")
