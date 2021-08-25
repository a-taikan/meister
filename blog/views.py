from django.shortcuts import render,redirect
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

def post(request):
    return render(request, 'blog/post.html')



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

        return render(request, "blog/post.html",context=self.params)






                