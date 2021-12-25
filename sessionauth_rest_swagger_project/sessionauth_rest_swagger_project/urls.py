"""sessionauth_rest_swagger_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from sessionauth_rest_swagger_app import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter(trailing_slash=True)
router.register("api",views.EmployeeAPIView,basename="api")
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="Employee API Testing With Faker using Session Authentication",
        default_version="v1",
        description="Testing API Functionality of Employee Model Using Swagger by drf_yasg_package",
        terms_of_service="API Functionality Testing with Faker MOdule",
        contact=openapi.Contact("psarangi50@gmail.com"),
        license = openapi.License("BT Certificied MIT Licence")),public=True,permission_classes=[permissions.IsAuthenticated])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include("rest_framework.urls",namespace="api")),
    path("",include(router.urls)),
    path("swagger/",schema_view.with_ui("swagger",cache_timeout=0),name="swagger"),
    path("redoc/",schema_view.with_ui("redoc",cache_timeout=0),name="redoc"),

]
