from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def Home(Request):
    tovs = Article.objects.all()
    return render(Request, 'vis/Home.html', {'tovs': tovs})
