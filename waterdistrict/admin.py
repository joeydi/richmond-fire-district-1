from django.contrib import admin
from django.utils.html import format_html
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


class MemberAdmin(admin.ModelAdmin):
    list_display = [
        'owner',
        '_get_address',
        'phone',
        'email',
    ]

    def _get_address(self, obj):
        return format_html('%s<br />%s' % (obj.address_1, obj.address_2))
    _get_address.short_description = 'Address'

admin.site.register(Member, MemberAdmin)
