from django.shortcuts import render

from articles.models import Article, Scope


def articles_list(request):
    articles = Article.objects.all()
    template = 'articles/news.html'
    context = {'object_list':articles}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
