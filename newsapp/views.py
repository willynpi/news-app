from django.shortcuts import render
from newsapp.models import NewsUnit

def index(request):
    news = NewsUnit.objects.filter(enabled=True).order_by('-pubtime')
    return render(request, 'newsapp/index.html', {"news":news})

def read(request, id):
    news = NewsUnit.objects.get(id=id)
    return render(request, 'newsapp/read.html', {"news":news})