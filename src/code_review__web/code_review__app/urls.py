from django.urls import path

from src.code_review__web.code_review__app.views import FilesList, FileDetail, FileAddView, FileDeleteView

urlpatterns = [
    path('', FilesList.as_view(), name='index'),
    path('<uuid:pk>', FileDetail.as_view(), name='file_details'),
    # path('search/', FilesFilter.as_view()),
    path('create/', FileAddView.as_view(), name='file_add'),
    path('<uuid:pk>/delete/', FileDeleteView.as_view(), name='file_delete'),
]
