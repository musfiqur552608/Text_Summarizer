from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('analyze', views.analyze, name='analyze'),
]