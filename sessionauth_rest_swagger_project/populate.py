import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","sessionauth_rest_swagger_project.settings")
import django
django.setup()
from sessionauth_rest_swagger_app.models import Employee
import faker
import random
fake=faker.Faker("en_IN")
def populate(n):
    for i in range(n):
        feno=random.randint(11111,99999)
        fename=fake.name()
        fesal=random.uniform(111111.00,999999.99)
        feaddr=fake.address()
        Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)

populate(100)