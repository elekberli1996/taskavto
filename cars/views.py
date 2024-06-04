from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Cars,Comment
from .form import CarForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def car_page(request):
    cars=Cars.objects.all()
    marka=request.GET.get("marka")
    model=request.GET.get("model")
    if marka or model:
        cars=Cars.objects.filter(model__contains=model ,marka__contains=marka)
        return render(request,'cars.html',{'cars':cars})
    return render(request,'cars.html',{'cars':cars})

@login_required(login_url="account:login")
def my_car_page(request):
    cars=Cars.objects.filter(author=request.user)
    return render(request,'mycar.html',{'cars':cars})

def about_page(request):
    return render(request,"about.html")
# Create your views here.
def contact_page(request):
    return render(request,"contact.html")

@login_required(login_url="account:login")
def add_car(request):
    form=CarForm(request.POST or None,request.FILES or None)

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

@login_required(login_url="account:login")
def update_car(request,id):
    car=get_object_or_404(Cars,id=id)
    form=CarForm(request.POST or None,request.FILES or None,instance=car)

    if form.is_valid():
        car=form.save(commit=False)
        car.author=request.user
        car.save()
        messages.success(request,"islem basarili")
        return redirect("mycar")

    context={
        "form":form
    }
    return render(request,"update.html",context)

@login_required(login_url="account:login")
def delete_car(request,id):
      car=get_object_or_404(Cars,id=id)
      car.delete()
      messages.success(request,"islem basarili")
      return redirect("mycar")



def car_detail(request,id):
    # car=Cars.objects.filter(id=id).first()
    
    car=get_object_or_404(Cars,id=id)
    comments=Comment.objects.filter(car=car)
    context={
        "car":car,
        "comments":comments
    }
    return render(request,"cardetail.html",context)



@login_required(login_url="account:login")
def add_comment(request,id):
    car=get_object_or_404(Cars,id=id)
    if request.method=="POST":
        comment_content=request.POST.get("comment_content")
        newComment= Comment(comment_content=comment_content)
        newComment.car=car
        newComment.author=request.user
        newComment.save()
        messages.success(request,"islem basarili")
    return redirect(reverse("cardetail",kwargs={"id":id}))

