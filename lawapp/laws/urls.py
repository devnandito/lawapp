from django.urls import path
from lawapp.laws.views import show_law, create_law, edit_law, delete_law

app_name = 'lawapp.laws'

urlpatterns = [
    path('dashboard/create/law', create_law, name='create'),
    path('dashboard/edit/<int:pk>/law', edit_law, name='edit'),
    path('dashboard/delete/<int:pk>/law', delete_law, name='delete'),
    path('dashboard/show/law', show_law, name='show'),
]