from django.urls import path

from src.code_review__web.code_review__app.views import FilesList, FileDetail, FileAddView, FileDeleteView, \
    FileEditView, healthcheck

urlpatterns = [
    path('', FilesList.as_view(), name='index'),
    path('files/<uuid:pk>', FileDetail.as_view(), name='file_details'),
    # path('search/', FilesFilter.as_view()),
    path('files/create/', FileAddView.as_view(), name='file_add'),
    path('files/<uuid:pk>/edit/', FileEditView.as_view(), name='file_edit'),
    path('files/<uuid:pk>/delete/', FileDeleteView.as_view(), name='file_delete'),

    path('healthcheck', healthcheck, name='healthcheck'),
]
