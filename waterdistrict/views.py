from django.http import HttpResponse
from django.shortcuts import render
from .models import WaterReading, Member


def index(request):
    context = {
        'title': "Richmond Fire District #1",
        'latest_reading': WaterReading.objects.first(),
        'readings': WaterReading.objects.all()[:10],
    }
    return render(request, 'index.html', context)


def map(request):
    return render(request, 'map.html')


def info(request):
    return render(request, 'info.html')


def members(request):
    context = {
        'members': Member.objects.all(),
    }
    return render(request, 'members.html', context)
