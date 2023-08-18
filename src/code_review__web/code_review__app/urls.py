from django.conf.urls import url

from src.code_review__web.code_review__app.views import IndexPageView

urlpatterns = [
    url('', IndexPageView.as_view(), name='index'),
]
