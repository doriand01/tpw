from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/<str:title>/', views.articles, name='articles'),
    path('categories/<str:category_name>/', views.categories, name='category'),
    path('tags/<str:tag_name>/', views.tags, name='tag')
    ]