from datetime import datetime
from typing import Any, Dict, Tuple

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from src.code_review__web.code_review__app.forms import CreateFileForm, UpdateFileForm
from src.code_review__web.code_review__app.models import File, FileLog


class FileDetail(LoginRequiredMixin, DetailView[File]):
    model = File
    template_name = 'details_file.html'
    context_object_name = 'user_file'
    queryset = File.objects.all()

    def get_object(self, queryset: QuerySet[Any] | None = None) -> File:
        uid = self.kwargs.get('pk')
        return File.objects.get(pk=uid)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        file: File | None = File.objects.get(pk=self.kwargs.get('pk'))
        context['time_now'] = datetime.utcnow()
        if file:
            context['user_file_logs'] = FileLog.objects.filter(
                fk_file__fk_user__id=self.request.user.id,    # type: ignore
                fk_file__id=file.id,
            ).order_by('-date')
        return context


class FilesList(LoginRequiredMixin, ListView[File]):
    model = File
    queryset = File.objects.order_by('-id')
    template_name = 'index.html'
    context_object_name = 'user_files'
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['user_files'] = File.objects.filter(fk_user__id=self.request.user.id).order_by('-id')    # type: ignore
        return context


# class FilesFilter(ListView):
#     model = File
#     queryset = File.objects.order_by('-id')
#     template_name = 'search.html'
#     context_object_name = 'user_files'
#     ordering = ['-created_at']
#     paginate_by = 10
#
#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         # context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
#         return context


class FileAddView(LoginRequiredMixin, CreateView[File, CreateFileForm]):
    template_name = 'add_file.html'
    form_class = CreateFileForm
    success_url = '/'

    def post(self, request: Any, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> HttpResponseRedirect:
        file_form = CreateFileForm(request.POST, request.FILES)

        if file_form.is_valid():
            current_user: User | None = User.objects.filter(id=request.user.id).first()
            instance: File = File(file_name=request.POST["file_name"], file_data=request.FILES["file_data"])
            instance.fk_user = current_user
            instance.save()
            return redirect('index')
        return redirect('file_add')


class FileEditView(LoginRequiredMixin, UpdateView[File, UpdateFileForm]):
    template_name = 'edit_file.html'
    form_class = UpdateFileForm
    success_url = '/'

    def get_object(self, queryset: QuerySet[Any] | None = None) -> File:
        uid = self.kwargs.get('pk')
        return File.objects.get(pk=uid)

    def post(self, request: Any, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        uid = self.kwargs.get('pk')
        instance: File | None = File.objects.filter(id=uid).first()
        file_form = UpdateFileForm(request.POST, request.FILES, instance=instance)

        if instance:
            if file_form.is_valid():
                instance.file_name = request.POST.get("file_name")
                if file_data := request.FILES.get("file_data"):
                    instance.file_data = file_data
                    instance.is_reviewed = "not_reviewed_updated"
                instance.save()
                messages.success(request, 'The file has been updated successfully.')
                return redirect('file_details', pk=instance.id)
            messages.success(request, 'The file has not been updated.')
            return redirect('file_edit', pk=instance.id)
        messages.success(request, 'The file does not exist.')
        return redirect('index')


class FileDeleteView(LoginRequiredMixin, DeleteView[File]):     # type: ignore
    template_name = 'delete_file.html'
    queryset = File.objects.all()
    context_object_name = 'user_file'
    success_url = '/'

    def get_object(self, queryset: QuerySet[Any] | None = None) -> File:
        uid = self.kwargs.get('pk')
        return File.objects.get(pk=uid)


def healthcheck(request: Any) -> HttpResponse:
    return render(request, 'health-check.html')
