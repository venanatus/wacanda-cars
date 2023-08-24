from django import forms
from .models import TestDrive


class TestDriveForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label="Введите ваше имя")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label="Введите фамилию")
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label="введите номер телефона")
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'input'}), label="Введите дату тест драйва")

    class Meta:
        model = TestDrive
        fields = ['first_name', 'last_name', 'phone', 'date']
