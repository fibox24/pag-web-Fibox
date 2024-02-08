from django.shortcuts import render
from .models import Plan

# Create your views here.
def Inicio(request):
    return render(request, 'core/index.html')

def Planes(request):
    planes = Plan.objects.all()
    return render(request, 'core/planes.html', {'planes':planes})

def Quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

