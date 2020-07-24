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
    Used whenever, user does soemting which will make react forget its state...
    Like refersh or load or reload
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user.
    Post request to this view's url with 
    {
        "usaname" : username, 
        "password": password
    }
    format json works :D
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