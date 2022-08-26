from django import forms
from lawapp.articles.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('fklaw', 'fkchapter', 'num', 'description',)