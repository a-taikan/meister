from .models import Article, Image
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body", "picture" ]

        labels = {
            'title':'タイトル',
            'body':'本文',
            'picture': '写真',
        }

class ImageForm(forms.ModelForm):
    images  =  forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    class Meta:
        model = Image
        fields = ["images","article"]

        labels = {
            "images": "画像を追加",
            "article": "記事の番号",
        }