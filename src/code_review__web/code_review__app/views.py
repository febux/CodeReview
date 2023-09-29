from datetime import datetime
from typing import Any, Dict, Tuple

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from src.code_review__web.code_review__app.forms import CreateFileForm, UpdateFileForm
from src.code_review__web.code_review__app.models import File, FileLog


class FileDetail(LoginRequiredMixin, DetailView):    # type: ignore
    model = File
    template_name = 'details_file.html'
    context_object_name = 'user_file'
    queryset = File.objects.all()

    def get_object(self, **kwargs: Dict[str, Any]) -> File:
        uid = self.kwargs.get('pk')
        return File.objects.get(pk=uid)  # type: ignore

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        file = File.objects.get(pk=self.kwargs.get('pk'))
        context['time_now'] = datetime.utcnow()
        context['user_file_logs'] = FileLog.objects.filter(
            fk_file__fk_user__id=self.request.user.id,
            fk_file__id=file.id,
        ).order_by('-date')
        return context    # type: ignore


class FilesList(LoginRequiredMixin, ListView):    # type: ignore
    model = File
    queryset = File.objects.order_by('-id')
    template_name = 'index.html'
    context_object_name = 'user_files'
    paginate_by = 10

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['user_files'] = File.objects.filter(fk_user__id=self.request.user.id).order_by('-id')
        return context    # type: ignore


class FilesFilter(ListView):    # type: ignore
    model = File
    queryset = File.objects.order_by('-id')
    template_name = 'search.html'
    context_object_name = 'user_files'
    ordering = ['-created_at']
    paginate_by = 10

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context    # type: ignore


class FileAddView(LoginRequiredMixin, CreateView):    # type: ignore
    template_name = 'add_file.html'
    form_class = CreateFileForm
    success_url = '/'

    def post(self, request: Any, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> HttpResponseRedirect:
        file_form = CreateFileForm(request.POST, request.FILES)

        if file_form.is_valid():
            current_user = User.objects.filter(id=request.user.id).first()
            instance = File(file_name=request.POST["file_name"], file_data=request.FILES["file_data"])
            instance.fk_user = current_user
            instance.save()
            return redirect('index')
        return redirect('file_add')


class FileEditView(LoginRequiredMixin, UpdateView):    # type: ignore
    template_name = 'edit_file.html'
    form_class = UpdateFileForm
    success_url = '/'

    def get_object(self, **kwargs: Dict[str, Any]) -> File:
        uid = self.kwargs.get('pk')
        return File.objects.get(pk=uid)  # type: ignore

    def post(self, request: Any, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> HttpResponseRedirect:
        file_form = UpdateFileForm(request.POST, request.FILES)

        if file_form.is_valid():
            uid = self.kwargs.get('pk')
            instance = File.objects.filter(id=uid).first()
            instance.file_name = request.POST["file_name"]
            instance.file_data = request.FILES["file_data"]
            instance.is_reviewed = "not_reviewed_updated"
            instance.save()
            return redirect('file_details')
        return redirect('file_edit')


class FileDeleteView(LoginRequiredMixin, DeleteView):    # type: ignore
    template_name = 'delete_file.html'
    queryset = File.objects.all()
    success_url = '/'

    def get_object(self, **kwargs: Dict[str, Any]) -> File:
        uid = self.kwargs.get('pk')
        return File.objects.get(pk=uid)    # type: ignore
