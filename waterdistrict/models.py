from datetime import timedelta
from django.db import models
from django.utils import timezone


class WaterReading(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    water_gallons_used = models.IntegerField(default=0)
    water_tank_level = models.IntegerField(default=0)
    chlorinator_tank_level = models.IntegerField(default=0)
    notes = models.TextField(blank=True)

    def rate(self):
        # Get previous reading
        previous = WaterReading.objects.filter(created_at__lt=self.created_at).first()

        if previous is None:
            return 0

        # Convert timedelta between readings to decimal days
        days = (self.created_at - previous.created_at) / timedelta(days=1)

        rate = (self.water_gallons_used - previous.water_gallons_used) / days

        return round(rate, 2)

    def __str__(self):
        return self.created_at.strftime("%b %d %Y %H:%M:%S")

    class Meta:
        ordering = ['-created_at']
