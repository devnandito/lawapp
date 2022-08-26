from django import forms
from lawapp.chapters.models import Chapter

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ('description',)