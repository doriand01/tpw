from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Tag
# Create your views here.


def home(request):
    latest_articles = Article.objects.all().order_by('-created_at')[:5]
    return render(request, 'news/home.html', {'articles': latest_articles, 'title': 'Latest Articles'})


def articles(request, title):
    formatted_title = title.replace('-', ' ')
    article = Article.objects.get(title__iexact=formatted_title)
    return render(request, 'news/article.html', {'article': article})


def categories(request, category_name):
    cat = get_object_or_404(Category, name=category_name)
    articles = Article.objects.filter(category__name=category_name)
    return render(request, 'news/category.html', {'articles': articles, 'category': cat})


def tags(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    articles = Article.objects.filter(tags__name=tag_name).order_by('-created_at')
    return render(request, 'news/tagpage.html', {'articles': articles, 'tag': tag})
