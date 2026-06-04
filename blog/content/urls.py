from django.urls import path
from .views import home

#create your views here
urlpaterns=[
    path('',home, name='home'),
]