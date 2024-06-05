# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'border: 1px solid black;'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Логин', 'style': 'border: 1px solid black;'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'style': 'border: 1px solid black;'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', 'style': 'border: 1px solid black;'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Логин', 'style': 'border: 1px solid black;'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'style': 'border: 1px solid black;'}))


class ProfileUpdateForm(UserChangeForm):
    password = None  # Не включаем поле пароля
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'border: 1px solid black;'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Логин', 'style': 'border: 1px solid black;'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Старый пароль', 'style': 'border: 1px solid black;'}))
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Новый пароль', 'style': 'border: 1px solid black;'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Подтвердите новый пароль', 'style': 'border: 1px solid black;'}))
