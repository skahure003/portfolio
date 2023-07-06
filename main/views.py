from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render (request, 'main/index.html', context)

def portfolio(request):
    context = {}
    return render (request, 'main/portfolio.html', context)


