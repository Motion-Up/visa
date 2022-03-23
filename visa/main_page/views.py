from django.shortcuts import render

from .models import Article, Service


def index(request):
    articles = Article.objects.all()
    services = Service.objects.all()
    context = {
        'articles': articles,
        'services': services,
    }
    return render(request, 'main_page/index.html', context=context)
