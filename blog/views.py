from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def home(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'blog/home.html', context)

def blog_show(request, article_id):
    article= Article.objects.get(pk= article_id)
    context = {'article': article}
    return render(request, 'blog/show.html', context)