
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import CompanyViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'emp', EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]