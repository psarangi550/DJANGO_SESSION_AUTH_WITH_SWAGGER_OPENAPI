from rest_framework.serializers import ModelSerializer
from .models import Employee

class EmpModelSerializer(ModelSerializer):
    model=Employee
    fields="__all__"

    