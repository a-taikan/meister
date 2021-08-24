from .models import Article
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