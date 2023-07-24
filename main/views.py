from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render (request, 'main/index.html', context)

def portfolio(request):
    context = {}
    return render (request, 'main/portfolio.html', context)

def languages(request):
    context = {}
    return render (request, 'main/lang.html', context)

def projects(request):
    context = {}
    return render(request, 'main/projects.html', context)