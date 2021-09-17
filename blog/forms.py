from .models import Article, Image
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["picture", "category", "title", "body" ]

        labels = {
            'title':'タイトル',
            'body':'本文',
            'picture':'写真',
            'category' : 'カテゴリー',
        }

        widgets = {
            'body': forms.Textarea(attrs={'rows':40, 'cols':67, 'class': 'body', 'placeholder': '本文を入力'}),
            'title': forms.TextInput(attrs={'size':65, 'class': 'title', 'placeholder': 'タイトル' }),
            'picture': forms.FileInput(attrs={'class': 'image'}),
            'category': forms.Select(attrs={'class': 'category'}),
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