from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from src.code_review__web.code_review__users.forms import LoginForm, RegisterForm


def sign_in(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            messages.success(request, f'Hi {request.user.username}, you are already logged in!')
            return redirect('index')
        form: LoginForm = LoginForm()
        return render(request, 'login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {request.user.username}, welcome back!')
                return redirect('index')

        # form is not valid or user is not authenticated
        messages.error(request, 'Invalid username or password')
        return render(request, 'login.html', {'form': form})

    messages.error(request, 'Invalid request')
    return redirect('index')


def sign_out(request: HttpRequest) -> HttpResponse:
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')


def sign_up(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'sign_up.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'sign_up.html', {'form': form})
    messages.error(request, 'Invalid request')
    return redirect('index')
