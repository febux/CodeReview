from django.urls import path

from .views import index, files

urlpatterns = [
    path('', index, name='index'),
    path('files/', files, name='files'),
]
