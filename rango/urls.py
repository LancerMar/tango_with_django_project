'''
Author: your name
Date: 2022-01-27 15:11:48
'''

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
]