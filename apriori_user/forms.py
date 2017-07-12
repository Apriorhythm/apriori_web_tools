from django import forms

from .models import AprioriUser


class LoginForm(forms.ModelForm):
    secure_code = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = AprioriUser

        fields = ['secure_code', 'username', 'password']


