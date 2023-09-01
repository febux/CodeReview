from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import FileForm
from .models_managers import get_files_by_user_id


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            user_files = get_files_by_user_id(request.user.id)
            return render(request, 'index.html', {'user_files': user_files})
        return redirect('login')


@login_required     # type: ignore
def files(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form: FileForm = FileForm()
        return render(request, 'add_file.html', {'form': form})
    if request.method == 'POST':
        messages.success(request, 'File was created!')
