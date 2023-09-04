from django import forms
from .models import TestDrive


class TestDriveForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label="введите номер телефона")
    # date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'input'}), label="Введите дату тест драйва")
    date = forms.DateTimeField(widget=forms.DateTimeField())

    class Meta:
        model = TestDrive
        fields = ['phone', 'date']
