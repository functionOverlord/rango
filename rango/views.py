from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    h = " <a href='/rango/about'>About</a>"

    context = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context)


def about(request):
    h = " <a href='/rango/'>index</a>"

    context = {}
    return render(request, 'rango/about.html', context=context)


