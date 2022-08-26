from django.urls import path
from lawapp.pages.views import show_home, login_user, logout_user, newsletter_user

app_name = 'lawapp.pages'

urlpatterns = [
    # path('', show_home, name='show'),
    path('', login_user, name='login'),
    path('logout/', logout_user, name="logout"),
    path('register/', newsletter_user, name="register"),
]