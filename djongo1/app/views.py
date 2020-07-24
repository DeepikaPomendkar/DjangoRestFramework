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



from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


from rest_framework import viewsets
from .models import employees
from .serializers import EmployeeSerializer


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = EmployeeSerializer