# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from games.models import CartModel
from .forms import UserRegisterForm, UserLoginForm, ProfileUpdateForm, CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout


def login_register_view(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = UserLoginForm(data=request.POST)
            register_form = UserRegisterForm()
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        elif 'register' in request.POST:
            register_form = UserRegisterForm(request.POST)
            login_form = UserLoginForm()
            if register_form.is_valid():
                register_form.save()
                username = register_form.cleaned_data.get('username')
                password = register_form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('profile')
    else:
        login_form = UserLoginForm()
        register_form = UserRegisterForm()
        cart_items = CartModel.objects.filter(user=request.user)

    return render(request, 'login-register.html', {
        'login_form': login_form,
        'register_form': register_form,
        'cart_items': cart_items
    })


@login_required
def profile_view(request):
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            profile_form = ProfileUpdateForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Ваш профиль был успешно обновлен.')
                return redirect('profile')
        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Обновление хеша сессии для предотвращения выхода пользователя
                messages.success(request, 'Ваш пароль был успешно изменен.')
                return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)
        cart_items = CartModel.objects.filter(user=request.user)

    context = {
        'profile_form': profile_form,
        'password_form': password_form,
        'cart_items': cart_items
    }
    return render(request, 'my-account.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
