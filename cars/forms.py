from django import forms
from .models import TestDrive


class TestDriveForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))

    class Meta:
        model = TestDrive
        fields = ['first_name', 'last_name', 'phone']

