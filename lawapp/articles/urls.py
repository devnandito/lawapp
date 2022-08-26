from django.urls import path
from lawapp.articles.views import show_article, create_article, edit_article, delete_article, show_article_json, ArticleListView, show_article_json2

app_name = 'lawapp.articles'

urlpatterns = [
    path('dashboard/create/article', create_article, name='create'),
    path('dashboard/edit/<int:pk>/article', edit_article, name='edit'),
    path('dashboard/delete/<int:pk>/article', delete_article, name='delete'),
    path('dashboard/show/article', show_article, name='show'),
    path('dashboard/show/article/api/v1', show_article_json, name='articlejson'),
    path('dashboard/show/article/api/v2', ArticleListView.as_view(), name='articlelist'),
    path('dashboard/show/article/api/v3', show_article_json2, name='articlejson2'),
]