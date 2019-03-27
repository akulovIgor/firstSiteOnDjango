"""authTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.views.generic import ListView, DetailView
from news.models import Articles, Comments

urlpatterns = [
    #path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:10],
     #                         template_name="news/posts.html")),
    path('', views.articles, name='articles'),
    re_path(r'^(?P<article_id>\d+)/$', views.article, name='article'),
    re_path(r'^(?P<articles_id>\d+)/addLike/$', views.addLike, name='addLike'),
    re_path(r'^(?P<article_id>\d+)/addComment/$', views.addСomment, name='addComment'),
    re_path(r'^page/(\d+)/$', views.articles, name='articles'),
]
