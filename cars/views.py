from django.shortcuts import render
from .models import Cars

def car_page(request):
    cars=Cars.objects.all()
    return render(request,'cars.html',{'cars':cars})

# Create your views here.
