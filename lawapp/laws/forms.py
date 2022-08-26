from django import forms
from lawapp.laws.models import Law

class LawForm(forms.ModelForm):
    class Meta:
        model = Law
        fields = ('title',)