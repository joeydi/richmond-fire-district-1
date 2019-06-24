from django.http import HttpResponse
from django.shortcuts import render
from .models import WaterReading


def index(request):
    context = {
        'title': "Richmond Fire District #1",
        'latest_reading': WaterReading.objects.first(),
        'readings': WaterReading.objects.all()[:10],
    }
    return render(request, 'index.html', context)


def map(request):
    context = {
        'title': "Richmond Fire District #1",
        'latest_reading': WaterReading.objects.first(),
        'readings': WaterReading.objects.all()[:10],
    }
    return render(request, 'map.html', context)
