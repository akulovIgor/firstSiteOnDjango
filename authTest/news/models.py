# -*- coding: utf-8 -*-
from django.db import models


class Articles(models.Model):
    class Meta:
        db_table = 'article'

    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comments(models.Model):
    class Meta:
        db_table = 'comments'

    comments_text = models.TextField(verbose_name="Текст комментария")
    comments_articles = models.ForeignKey(Articles, on_delete= models.CASCADE)
