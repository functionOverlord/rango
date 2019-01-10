from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    h = " <a href='/rango/about'>About</a>"
    return HttpResponse("Rango says hey there partner!" + h)


def about(request):
    h = " <a href='/rango/'>index</a>"
    return HttpResponse("About" + h)


