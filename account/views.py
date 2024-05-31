from django.shortcuts import render,redirect
from  .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.
def register_page(request):

 
    form=RegisterForm(request.POST or None)

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()

        login(request,newUser)
        messages.success(request,"ugurla qeydiyatdan kecdiniz")

        return redirect("home")


    context={
        "form":form
    }


    return render(request,"register.html",context)


def login_page(request):
    form=LoginForm(request.POST or None )
    context={
        "form":form
    }

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        user =authenticate(username=username,password=password)
        if user is None:
            render(request,"login.html")

        login(request,user)
        messages.success(request,"ugurla qeydiyatdan kecdiniz")
        return redirect("home")
    

    return render(request,"login.html",context)


def logout_page(request):
    logout(request)
    messages.warning(request,"cixis etdiniz")
    return redirect("home")
