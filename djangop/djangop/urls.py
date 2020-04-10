"""djangop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from djangoapp import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('show/',views.show),
    path('hello/',views.display),
    path('sample/',views.sample),
    path('createstudent/',views.createStudent),
    path('createstudent1/',views.createStudent1),
    path('deletestudent/<int:id>/',views.delete),
    path('editstudent/<int:id>/',views.edit),
    path('getcsv',views.getcsv),
    path('getpdf', views.getpdf),
    path('setsession/',views.setsession),
    path('getsession/',views.getsession),
    path('setcookie/',views.setcookie),
    path('getcookie/',views.getcookie),
    path('sendmail/',views.sendmail),
    path('login/',LoginView.as_view()),
    path('customreg/',views.customreg),
    path('check/',views.check),
    path('home/',views.home),
    path('logoutview/',views.logoutview),
    path('about/',views.about),
    path('sample1/',views.sample1),
    path('uploader/',views.uploader),
    path('',views.firstpage)

]
