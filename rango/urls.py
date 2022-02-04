'''
Author: your name
Date: 2022-01-27 15:11:48
'''

from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about,name='about'),
    path('category/<slug:category_name_slug>/',
        views.show_category, name='show_category'),
]