from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article, Image, Category
from django.db.models import Q
from functools import reduce
from operator import and_


def home(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'blog/home.html', context)





from . import forms
from django.views.generic import TemplateView

class FormView(TemplateView):

    #初期変数定義
    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                       "form":forms.PostForm(),
                       }

    #GET時の処理を記載
    def get(self,request):
        return render(request, "blog/post.html",context=self.params)

    #POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.PostForm(request.POST, request.FILES)
            
            #フォーム入力が有効な場合
            if self.params["form"].is_valid():
                #入力項目をデータベースに保存
                self.params["form"].save(commit=True)
                self.params["Message"] = "入力情報が送信されました。"

        return redirect("home")


def add_img(request, article_id):
    article2= Article.objects.get(pk= article_id)
    form = forms.ImageForm(request.POST, request.FILES)
    if form.is_valid():
        portfolio_images = request.FILES.getlist('images', False)
        for images in portfolio_images:
            image_instance = Image(
                images=images,
                article= article2
            )
            image_instance.save()

    return redirect("home")

def blog_show(request, article_id):
    article2= Article.objects.get(pk= article_id)
    initial_dict = dict(article=article2)
    context = {
        'article': article2,
        'form': forms.ImageForm(
        initial= initial_dict)
    }
    return render(request, 'blog/show.html', context)


def search(request):
    post_data = Article.objects.all()
    keyword = request.GET.get('keyword')

    if keyword:
        exclusion_list = set([' ', '　'])
        query_list = ''
        for word in keyword:
            if not word in exclusion_list:
                query_list += word
        query = reduce(and_, [Q(title__icontains=q) | Q(body__icontains=q) for q in query_list])
        post_data = post_data.filter(query)

    return render(request, 'blog/home.html', {
        'keyword': keyword,
        'articles' : post_data
    })


def category_choise(request, category):
    category_data = Category.objects.get(name = category)
    articles = Article.objects.all()
    articles = articles.filter(category=category_data)
    return render(request, 'blog/home.html', {'articles': articles})