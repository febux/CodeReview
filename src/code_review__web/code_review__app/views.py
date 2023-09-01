from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import FileForm
from .models import File
from .models_managers import get_files_by_user_id


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            user_files = get_files_by_user_id(request.user.id)
            return render(request, 'index.html', {'user_files': user_files})
        return redirect('login')


@login_required     # type: ignore
def files(request: HttpRequest) -> HttpResponse:
    form: FileForm = FileForm()
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = User.objects.filter(id=request.user.id).first()
            instance = File(file_name=request.POST["file_name"], file_data=request.FILES["file_data"])
            instance.fk_user = current_user
            instance.save()
            messages.success(request, 'File was created!')
            return redirect("index")
        messages.error(request, 'File was not created! Try again.')
    return render(request, 'add_file.html', {'form': form})
