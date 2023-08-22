from django.urls import path

from src.code_review__web.code_review__app.views import IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
]
