from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from src.code_review__web.code_review__users.forms import LoginForm

from .models_managers import get_user_files_by_user_id


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            user_files = get_user_files_by_user_id(request.user.id)
            return render(request, 'index.html', {'user_files': user_files})
        form: LoginForm = LoginForm()
        return render(request, 'login.html', {'form': form})
