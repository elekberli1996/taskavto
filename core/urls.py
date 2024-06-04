"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from cars.views import *

urlpatterns = [
    path('', car_page,name="home"),
    path('updatecar/<int:id>', update_car,name="update"),
    path('deletecar/<int:id>', delete_car,name="delete"),
    path('addcar', add_car,name="add"),
    path('mycar', my_car_page,name="mycar"),
    path('cardetail/<int:id>', car_detail,name="cardetail"),
    path('comment/<int:id>', add_comment,name="comment"),
    path('about', about_page,name="about"),
    path('contact', contact_page,name="contact"),
    path('account/', include("account.urls")),
    path('admin/', admin.site.urls),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)