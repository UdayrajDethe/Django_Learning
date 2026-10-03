"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from . import views

#todo URL file was geting the requests and guide them where or which views function to respone / invoke 
#! Url Patterns
#? path is a django function which one creates a one mapping
#? It will take/required two things 1. URL Path , 2. view function
urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.home, name="home"), #? /home/ this a path , and function was in views.home, third optional name argument is just a nickname used for reusable label 
    path("contact/", views.contactus, name= "contact"),
    path("about/", views.about, name= "about"),
]
