from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# If you want a custom authentication form:
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username', 'required': 'True'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'required': 'True'}),
        }
