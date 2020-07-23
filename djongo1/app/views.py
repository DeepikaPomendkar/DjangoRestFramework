# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import employees
# # Create your views here.
# def read(request):
#     x=0
#
# def add(request):
#
#     firstName = "John"
#     lastName = "Doe"
#     id = 2
#     emp = employees(firstName=firstName,lastName=lastName,emp_id = id)
#     emp.save()
#     return HttpResponse('Inserted')
#
# def read(request):
#     id = 1
#     emp = employees.objects.get(emp_id =id)
#
#     val = emp.firstName + emp.lastName




#
#     return HttpResponse(val)






from rest_framework import viewsets
from .models import employees
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = EmployeeSerializer