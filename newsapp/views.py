from django.shortcuts import render
from newsapp.models import NewsUnit

def index(request):
    news = NewsUnit.objects.filter(enabled=True).order_by('-pubtime')
    return render('newsapp/index.html', {"news":news})
