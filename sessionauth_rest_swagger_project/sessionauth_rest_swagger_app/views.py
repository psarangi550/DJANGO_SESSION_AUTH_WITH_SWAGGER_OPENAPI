from django.shortcuts import render
# from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmpModelSerializer
# from rest_framework.permissions import IsAuthenticated
from .paginations import EmployeePagination

# Create your views here.

class EmployeeAPIView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class=EmpModelSerializer
    pagination_class=EmployeePagination