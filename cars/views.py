from django.shortcuts import render,redirect
from .models import Cars
from .form import CarForm
from django.contrib import messages

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

def add_car(request):
    form=CarForm(request.POST or None)

    if form.is_valid():
        car=form.save(commit=False)
        car.author=request.user
        car.save()
        messages.success(request,"islem basarili")
        return redirect("mycar")

    context={
        "form":form
    }
    return render(request,"addcar.html",context)

def car_detail(request,id):
    car=Cars.objects.filter(id=id).first()
    context={
        "car":car
    }
    return render(request,"cardetail.html",context)