from django.urls import path,include,re_path
from . import views
from rest_framework import routers
from .views import EmployeeViewSet


router = routers.DefaultRouter()
router.register('empData', EmployeeViewSet)
urlpatterns = [

    path('',include(router.urls))
    # path('', views.EmployeeViewSet, name='app-read'),
    # path('add/', views.add, name='app-add'),




]