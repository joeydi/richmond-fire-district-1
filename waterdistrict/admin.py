from django.contrib import admin
from .models import *


class WaterReadingAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = [
        'created_at',
        'water_gallons_used',
        'rate',
        'water_tank_level',
        'chlorinator_tank_level',
        'notes',
    ]

admin.site.register(WaterReading, WaterReadingAdmin)
