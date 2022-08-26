from django.urls import path
from lawapp.chapters.views import show_chapter, create_chapter, edit_chapter, delete_chapter

app_name = 'lawapp.chapters'

urlpatterns = [
    path('dashboard/create/chapter', create_chapter, name='create'),
    path('dashboard/edit/<int:pk>/chapter', edit_chapter, name='edit'),
    path('dashboard/delete/<int:pk>/chapter', delete_chapter, name='delete'),
    path('dashboard/show/chapter', show_chapter, name='show'),
]