from django import forms

from .models import TempFile


class TempFileForm(forms.ModelForm):
    class Meta:
        model = TempFile

        fields = ['file', 'life_time']
