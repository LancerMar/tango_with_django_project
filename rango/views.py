'''
Author: your name
Date: 2022-01-27 14:25:05
'''
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango say hey guys")