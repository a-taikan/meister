from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    picture = models.ImageField(upload_to='images/')
    posted_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)

    def __str___(self):
        return  self.image.url

class Image(models.Model):
    images = models.ImageField(upload_to='images2/',  null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    