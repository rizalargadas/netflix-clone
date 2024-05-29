from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class EmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'mt-2 bg-black/50 w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))


class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Full Name',
        'class': 'mt-4 bg-black/50 w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'mt-4 bg-black/50 w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password.',
        'class': 'mt-4 bg-black/50 w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password.',
        'class': 'mt-4 bg-black/50 w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'mt-4 bg-black/50 w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password.',
        'class': 'mt-4 bg-black/50 w-[400px] px-4 py-4 border-2 border-gray-500 rounded-lg'
    }))
