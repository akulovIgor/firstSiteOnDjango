from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import render, redirect, render_to_response
from news.models import Articles, Comments
from news.forms import CommentForm
from django.template.context_processors import csrf


def addLike(request, articles_id):
    try:
        post = Articles.objects.get(id=articles_id)
        post.likes += 1
        post.save()
    except ObjectDoesNotExist:
        raise Http404
    if (request.path != '/news/'):
        return redirect('/news/' + str(articles_id) + '/')
    else:
        return redirect('/news/')


def articles(request):
    return render_to_response('news/posts.html', {'articles': Articles.objects.all()})


def article(request, article_id):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Articles.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_articles=article_id)
    args['form'] = comment_form
    return render_to_response('news/post.html', args)
    # return render_to_response('news/post.html', {'article': Articles.objects.get(id=article_id),
    #                                            'comments': Comments.objects.filter(comments_articles=article_id)})


# Create your views here.
def addСomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_articles = Articles.objects.get(id=article_id)
            form.save()
    return redirect('/news/' + str(article_id) + '/')
