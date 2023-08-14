from django import forms
from .models import TestDrive


class ApplicationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Введите ваше имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Введите вашу фамилию'}))
    phone = forms.IntegerField(widget=forms.IntegerField())
    date = forms.DateTimeField()

    class Meta:
        model = TestDrive
        fields = []
