from django import forms
from .models import DataPoint

class DataForm(forms.ModelForm):
    class Meta:
        model = DataPoint
        fields = ['category', 'data'] # removing user. we'll handle that in view