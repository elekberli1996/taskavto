from django.shortcuts import render
from .models import Cars

def car_page(request):
    cars=Cars.objects.all()
    return render(request,'cars.html',{'cars':cars})
def my_car_page(request):
    cars=Cars.objects.filter(author=request.user)
    return render(request,'mycar.html',{'cars':cars})

def about_page(request):
    return render(request,"about.html")
# Create your views here.
def contact_page(request):
    return render(request,"contact.html")


