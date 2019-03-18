from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from news.models import Articles, Comments


def addLike(request, articles_id):
    try:
        post = Articles.objects.get(id=articles_id)
        post.likes += 1
        post.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/news/')


def articles(request):
    return render_to_response('news/posts.html', {'articles': Articles.objects.all()})


def article(request, article_id):
    return render_to_response('news/post.html', {'article': Articles.objects.get(id=article_id),
                                                 'comments': Comments.objects.filter(comments_articles=article_id)})

# Create your views here.
